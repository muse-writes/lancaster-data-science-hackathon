"""Load mouse-brain spatial transcriptomics pucks from ``data/Mouse Brain``.

Each ``Puck_Num_*.h5ad`` file is one spatial "puck" stored as an
:class:`anndata.AnnData` object: ``.X`` is a sparse matrix of UMI counts
(squares × genes), ``.obs`` holds per-square metadata (counts, brain-region
annotations such as ``TopStruct``/``CCF_acronym``, coordinates) and ``.var``
holds the gene names.

This module is interfaced with using one function :meth:`load_mouse_brain_data()`
which returns an :class:`anndata.AnnData` for each puck, keyed by puck number.
"""

from __future__ import annotations

import re
from pathlib import Path

import anndata as ad

from lancaster_data_science_hackathon.utils import DEFAULT_DATA_DIR

# Default location of the puck .h5ad files, relative to the repo root.
_DEFAULT_MOUSE_BRAIN_DATA_DIR = DEFAULT_DATA_DIR / "Mouse Brain" / "MouseBrainPucks"

# Leading number in a ``Puck_Num_<NN>.h5ad`` file name.
_PUCK_RE = re.compile(r"Puck_Num_(\d+)")


def load_mouse_brain_data(
    data_path: str | Path | None = None,
) -> dict[int, ad.AnnData]:
    """Load all ``Puck_Num_*.h5ad`` files as :class:`anndata.AnnData` objects.

    :param data_path: Directory containing the ``.h5ad`` files.  Defaults to
        ``<repo>/data/Mouse Brain/MouseBrainPucks``.
    :returns: Mapping from puck number (``int``, e.g. ``51``) to its
        :class:`anndata.AnnData`.
    :raises FileNotFoundError: If ``data_path`` does not exist or contains no
        ``.h5ad`` files.
    """
    directory = (
        Path(data_path) if data_path is not None else _DEFAULT_MOUSE_BRAIN_DATA_DIR
    )
    if not directory.is_dir():
        raise FileNotFoundError(
            f"Mouse Brain data folder not found: {directory!s}. Pass an "
            f"explicit `data_path` or run from a checkout that contains "
            f"data/Mouse Brain/MouseBrainPucks."
        )

    def _puck_number(path: Path) -> int:
        match = _PUCK_RE.search(path.name)
        if match is None:
            raise ValueError(f"Unexpected file name (no puck number): {path.name!r}")
        return int(match.group(1))

    h5ad_files = sorted(
        (p for p in directory.iterdir() if p.suffix == ".h5ad"),
        key=_puck_number,
    )
    if not h5ad_files:
        raise FileNotFoundError(f"No .h5ad files found in {directory!s}")

    return {_puck_number(path): ad.read_h5ad(path) for path in h5ad_files}
