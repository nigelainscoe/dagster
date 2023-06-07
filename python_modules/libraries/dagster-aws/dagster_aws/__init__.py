from __future__ import annotations

from dagster._core.libraries import DagsterLibraryRegistry

from .version import __version__

DagsterLibraryRegistry.register("dagster-aws", __version__)
