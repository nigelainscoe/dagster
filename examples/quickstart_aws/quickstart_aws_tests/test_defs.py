from __future__ import annotations

from quickstart_aws import defs


def test_def_can_load():
    assert defs.get_job_def("all_assets_job")
