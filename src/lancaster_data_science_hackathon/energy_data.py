"""Utilities for loading energy data from four Lancaster University buildings.

This module is interfaced with using one function :meth:`load_energy_data()`
which returns ``pandas`` dataframes for each of the four buildings.
"""

from pathlib import Path

import pandas as pd

from lancaster_data_science_hackathon.utils import DEFAULT_DATA_DIR


def load_energy_data(data_path: str | None = None) -> dict:
    """Loads all five CSV files as pandas dataframes.

    :param data_path: Directory containing the building ``.csv`` files.
        Defaults to ``<repo>/data/'Energy Usage'/Data``.
    :returns: Mapping from building name (the CSV stem, e.g. ``"Library"``)
        to its DataFrame, indexed by ``time`` with columns ``series``,
        ``unit``, ``cumval`` and ``value``.
    :raises FileNotFoundError: If ``data_path`` does not exist or contains
        no ``.csv`` files.
    """
    directory = (
        DEFAULT_DATA_DIR / "Energy Usage" / "Data"
        if data_path is None
        else Path(data_path)
    )
    if not directory.is_dir():
        raise FileNotFoundError(
            f"Energy data folder not found: {directory!s}. Pass an explicit "
            f"`data_path` or run from a checkout that contains "
            f"data/Energy Usage/Data."
        )

    csv_files = sorted(p for p in directory.iterdir() if p.suffix == ".csv")
    if not csv_files:
        raise FileNotFoundError(f"No .csv files found in {directory!s}")

    return {
        path.stem: pd.read_csv(
            path,
            usecols=["series", "unit", "time", "cumval", "value"],
            dtype={
                "series": "string",
                "unit": "string",
                "cumval": "float64",
                "value": "float64",
            },
            parse_dates=["time"],
            index_col="time",
        )
        for path in csv_files
    }
