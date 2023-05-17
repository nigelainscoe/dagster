import pytest
from dagster import job, op
from dagster._core.errors import DagsterInvariantViolationError
from dagster._core.events import DagsterEvent, DagsterEventType
from dagster._core.execution.api import create_execution_plan
from dagster._core.execution.plan.global_concurrency_context import GlobalConcurrencyContext
from dagster._core.execution.plan.objects import StepSuccessData
from dagster._core.execution.plan.outputs import StepOutputData, StepOutputHandle
from dagster._core.execution.retries import RetryMode
from dagster._core.storage.tags import GLOBAL_CONCURRENCY_TAG
from dagster._core.test_utils import instance_for_test
from dagster._core.utils import make_new_run_id


def define_foo_job():
    @op
    def foo_op():
        pass

    @job
    def foo_job():
        foo_op()

    return foo_job


def test_recover_with_step_in_flight():
    foo_job = define_foo_job()

    with instance_for_test():
        with pytest.raises(
            DagsterInvariantViolationError,
            match="Execution finished without completing the execution plan",
        ):
            with create_execution_plan(foo_job).start(RetryMode.DISABLED) as active_execution:
                steps = active_execution.get_steps_to_execute()
                assert len(steps) == 1
                step_1 = steps[0]
                assert step_1.key == "foo_op"

                active_execution.handle_event(
                    DagsterEvent(
                        DagsterEventType.STEP_START.value,
                        job_name=foo_job.name,
                        step_key=step_1.key,
                    )
                )

        # CRASH!- we've closed the active execution. Now we recover, spinning up a new one

        with create_execution_plan(foo_job).start(RetryMode.DISABLED) as active_execution:
            possibly_in_flight_steps = active_execution.rebuild_from_events(
                [
                    DagsterEvent(
                        DagsterEventType.STEP_START.value,
                        job_name=foo_job.name,
                        step_key=step_1.key,
                    )
                ]
            )
            assert possibly_in_flight_steps == [step_1]

            assert not active_execution.get_steps_to_execute()

            active_execution.handle_event(
                DagsterEvent(
                    DagsterEventType.STEP_SUCCESS.value,
                    job_name=foo_job.name,
                    event_specific_data=StepSuccessData(duration_ms=10.0),
                    step_key=step_1.key,
                )
            )


def define_two_op_job():
    @op
    def foo_op():
        pass

    @op
    def bar_op(_data):
        pass

    @job
    def two_op_job():
        bar_op(foo_op())

    return two_op_job


def test_recover_in_between_steps():
    two_op_job = define_two_op_job()

    events = [
        DagsterEvent(
            DagsterEventType.STEP_START.value,
            job_name=two_op_job.name,
            step_key="foo_op",
        ),
        DagsterEvent(
            DagsterEventType.STEP_OUTPUT.value,
            job_name=two_op_job.name,
            event_specific_data=StepOutputData(
                StepOutputHandle(step_key="foo_op", output_name="result")
            ),
            step_key="foo_op",
        ),
        DagsterEvent(
            DagsterEventType.STEP_SUCCESS.value,
            job_name=two_op_job.name,
            event_specific_data=StepSuccessData(duration_ms=10.0),
            step_key="foo_op",
        ),
    ]

    with instance_for_test():
        with pytest.raises(
            DagsterInvariantViolationError,
            match="Execution finished without completing the execution plan",
        ):
            with create_execution_plan(two_op_job).start(RetryMode.DISABLED) as active_execution:
                steps = active_execution.get_steps_to_execute()
                assert len(steps) == 1
                step_1 = steps[0]
                assert step_1.key == "foo_op"

                active_execution.handle_event(events[0])
                active_execution.handle_event(events[1])
                active_execution.handle_event(events[2])

        # CRASH!- we've closed the active execution. Now we recover, spinning up a new one

        with create_execution_plan(two_op_job).start(RetryMode.DISABLED) as active_execution:
            possibly_in_flight_steps = active_execution.rebuild_from_events(events)
            assert len(possibly_in_flight_steps) == 1
            step_2 = possibly_in_flight_steps[0]
            assert step_2.key == "bar_op"

            assert not active_execution.get_steps_to_execute()

            active_execution.handle_event(
                DagsterEvent(
                    DagsterEventType.STEP_START.value,
                    job_name=two_op_job.name,
                    step_key="bar_op",
                )
            )
            active_execution.handle_event(
                DagsterEvent(
                    DagsterEventType.STEP_SUCCESS.value,
                    job_name=two_op_job.name,
                    event_specific_data=StepSuccessData(duration_ms=10.0),
                    step_key="bar_op",
                )
            )


def define_concurrency_job():
    @op(tags={GLOBAL_CONCURRENCY_TAG: "foo"})
    def foo_op():
        pass

    @op(tags={GLOBAL_CONCURRENCY_TAG: "foo"})
    def bar_op():
        pass

    @job
    def foo_job():
        foo_op()
        bar_op()

    return foo_job


def test_active_concurrency():
    foo_job = define_concurrency_job()
    run_id = make_new_run_id()

    with instance_for_test() as instance:
        instance.event_log_storage.set_concurrency_slots("foo", 1)

        with pytest.raises(
            DagsterInvariantViolationError,
            match="Execution finished without completing the execution plan",
        ):
            with GlobalConcurrencyContext(instance, run_id) as global_concurrency_context:
                with create_execution_plan(foo_job).start(
                    RetryMode.DISABLED,
                    global_concurrency_context=global_concurrency_context,
                ) as active_execution:
                    steps = active_execution.get_steps_to_execute()
                    assert len(steps) == 1
                    step_1 = steps[0]

                    foo_info = instance.event_log_storage.get_concurrency_info("foo")
                    assert foo_info.active_slot_count == 1
                    assert foo_info.active_run_ids == {run_id}
                    assert foo_info.pending_step_count == 1
                    assert foo_info.assigned_step_count == 1

                    active_execution.handle_event(
                        DagsterEvent(
                            DagsterEventType.STEP_START.value,
                            job_name=foo_job.name,
                            step_key=step_1.key,
                        )
                    )

        foo_info = instance.event_log_storage.get_concurrency_info("foo")
        assert foo_info.active_slot_count == 1
        assert foo_info.active_run_ids == {run_id}
        assert foo_info.pending_step_count == 0
        assert foo_info.assigned_step_count == 1
