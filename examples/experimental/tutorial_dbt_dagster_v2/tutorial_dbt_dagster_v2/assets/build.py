from __future__ import annotations

from typing import TYPE_CHECKING

from dagster_dbt.asset_decorator import dbt_assets
from dagster_dbt.cli import DbtCli, DbtManifest

from . import MANIFEST_PATH

if TYPE_CHECKING:
    from dagster import OpExecutionContext

manifest = DbtManifest.read(path=MANIFEST_PATH)


@dbt_assets(manifest=manifest)
def my_dbt_assets(context: OpExecutionContext, dbt: DbtCli):
    yield from dbt.cli(["build"], manifest=manifest, context=context).stream()
