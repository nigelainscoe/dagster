from __future__ import annotations

from typing import TYPE_CHECKING

from dagster import asset

if TYPE_CHECKING:
    from pandas import DataFrame


@asset
def activity_forecast(activity_daily_stats: DataFrame) -> DataFrame:
    return activity_daily_stats.head(100)
