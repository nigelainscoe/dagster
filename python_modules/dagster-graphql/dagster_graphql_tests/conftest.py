import os

import pytest


@pytest.fixture(scope="session", autouse=True)
def unset_dagster_home():
    old_env = os.getenv("DAGSTER_HOME")
    if old_env is not None:
        del os.environ["DAGSTER_HOME"]
    yield
    if old_env is not None:
        os.environ["DAGSTER_HOME"] = old_env


import pytest
from dagster._core.definitions.decorators.op_decorator import do_not_attach_code_origin


@pytest.fixture
def ignore_code_origin():
    # avoid attaching code origin metadata to ops/assets, because this can change from environment
    # to environment and break snapshot tests
    with do_not_attach_code_origin():
        yield
