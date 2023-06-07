from __future__ import annotations

from dagster._core.libraries import DagsterLibraryRegistry

from .docker_executor import docker_executor as docker_executor
from .docker_run_launcher import DockerRunLauncher as DockerRunLauncher
from .ops import (
    docker_container_op as docker_container_op,
    execute_docker_container as execute_docker_container,
)
from .version import __version__

DagsterLibraryRegistry.register("dagster-docker", __version__)
