from __future__ import annotations

from dagster_dask.version import __version__


def test_version():
    assert __version__
