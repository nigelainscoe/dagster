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
from dagster._core.definitions.decorators.op_decorator import CODE_ORIGIN_ENABLED


@pytest.fixture
def ignore_code_origin():
    CODE_ORIGIN_ENABLED[0] = False

    yield

    CODE_ORIGIN_ENABLED[0] = True
