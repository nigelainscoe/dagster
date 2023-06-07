# Used to set the priority for a particular step execution
from __future__ import annotations

DAGSTER_CELERY_STEP_PRIORITY_TAG = "dagster-celery/priority"

# Used to set the priority for an overall job run
DAGSTER_CELERY_RUN_PRIORITY_TAG = "dagster-celery/run_priority"

# Used to select a Celery queue
DAGSTER_CELERY_QUEUE_TAG = "dagster-celery/queue"
