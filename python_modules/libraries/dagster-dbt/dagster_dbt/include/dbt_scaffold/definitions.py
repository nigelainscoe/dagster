from pathlib import Path

from dagster import Definitions

from dagster_dbt import DbtCli, DbtManifest, dbt_assets

DBT_PROJECT_DIR = Path(__file__).parent.joinpath("../jaffle_shop")
DBT_MANIFEST_PATH = DBT_PROJECT_DIR.joinpath("target/manifest.json")
DBT_MANIFEST = DbtManifest.read(path=DBT_MANIFEST_PATH)


@dbt_assets(manifest=DBT_MANIFEST)
def my_dbt_assets(dbt: DbtCli):
    yield from dbt.cli(["build"], manifest=DBT_MANIFEST).stream()


schedules = [
    DBT_MANIFEST.build_schedule(
        job_name="materialize_dbt_models",
        cron_schedule="0 0 0 * *",
    )
]

defs = Definitions(
    assets=[my_dbt_assets],
    schedules=schedules,
    resources={
        "dbt": DbtCli(
            project_dir=DBT_PROJECT_DIR.as_posix(),
        ),
    },
)
