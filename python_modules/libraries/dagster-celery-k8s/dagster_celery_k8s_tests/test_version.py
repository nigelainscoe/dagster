from __future__ import annotations

from dagster_celery_k8s.version import __version__


def test_version():
    assert __version__
