from __future__ import annotations

import os
from tempfile import TemporaryDirectory

import pytest
from dagster._check import CheckError
from dagster._core.test_utils import instance_for_test
from dagster._core.workspace.load import load_workspace_process_context_from_yaml_paths
from dagster._utils import touch_file


def test_bad_workspace_yaml_load():
    with instance_for_test() as instance:
        with TemporaryDirectory() as temp_dir:
            touch_file(os.path.join(temp_dir, "foo.yaml"))

            with pytest.raises(
                CheckError,
                match=(
                    "Invariant failed. Description: Could not parse a workspace config from the "
                    "yaml file at"
                ),
            ):
                with load_workspace_process_context_from_yaml_paths(
                    instance, [os.path.join(temp_dir, "foo.yaml")]
                ):
                    pass
