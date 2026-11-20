"""Load radar micro-Doppler spectrograms from the Glasgow radar dataset.

Data source: https://researchdata.gla.ac.uk/848/

Each ``.mat`` file in ``data/RadarData/Data`` contains a single MATLAB
variable ``Data_spec_MTI2``: a complex-valued spectrogram (a micro-Doppler
signature).  The spectrogram is obtained by cutting the radar signal into
short, overlapping time windows and taking an FFT of each window.  The result
is a matrix where:

* each **column** is one time window -> left to right shows how the activity
  unfolds over time;
* each **row** is one Doppler frequency bin -> Doppler frequency is
  proportional to the radial velocity of the reflecting body part (positive /
  negative = moving towards / away from the radar);
* each **cell** is the complex amplitude at that velocity and time.

The leading digit of a file name is the activity class::

    1 = walking, 2 = sitting down, 3 = standing up,
    4 = picking up an object, 5 = drinking, 6 = falling.

Power is stored in dB, computed as ``20 * log10(|Data_spec_MTI2|)``
matching the R reference script ``data/RadarData/LoadData.R``.  Cells equal to
0 become ``-inf`` after the log, exactly as in R; clip the dynamic range (e.g.
to 40 dB) before visualising.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import scipy.io

from lancaster_data_science_hackathon.utils import DEFAULT_DATA_DIR

# Leading digit of the file name -> human-readable activity name.
ACTIVITIES: dict[int, str] = {
    1: "Walking",
    2: "Sitting down",
    3: "Standing up",
    4: "Picking up object",
    5: "Drinking",
    6: "Falling",
}

# The single MATLAB variable held in every .mat file in this dataset.
_MAT_VARIABLE = "Data_spec_MTI2"

# Default location of the .mat files, resolved relative to the repo root.
_DEFAULT_ENERGY_DATA_DIR = DEFAULT_DATA_DIR / "RadarData" / "Data"


def _to_db(complex_spec: np.ndarray) -> np.ndarray:
    """Convert a complex spectrogram to power in dB.

    Computes ``20 * log10(|complex_spec|)``.  Cells equal to 0 become
    ``-inf`` (matching the R reference script); clip the dynamic range before
    visualising.

    :param complex_spec: Complex-valued spectrogram array.
    :returns: Real-valued spectrogram with power in dB.
    """
    with np.errstate(divide="ignore"):
        return 20.0 * np.log10(np.abs(complex_spec))


def _read_spectrogram(path: Path) -> np.ndarray:
    """Read one ``.mat`` file and return its spectrogram in dB.

    :param path: Path to a ``.mat`` file containing the ``Data_spec_MTI2``
        variable.
    :returns: Real-valued 2-D spectrogram in dB (rows = Doppler bins,
        columns = time bins).
    :raises KeyError: If the file does not contain ``Data_spec_MTI2``.
    """
    mat = scipy.io.loadmat(str(path))
    try:
        raw = mat[_MAT_VARIABLE]
    except KeyError as exc:  # pragma: no cover - defensive, dataset is fixed
        raise KeyError(
            f"{path.name} does not contain the expected variable "
            f"{_MAT_VARIABLE!r}; found {list(mat)!r}"
        ) from exc
    return _to_db(np.asarray(raw))


def load_radar_data(
    data_dir: str | Path | None = None,
) -> dict[int, np.ndarray]:
    """Load radar micro-Doppler spectrograms from ``.mat`` files.

    Reproduces ``RadarData/LoadData.R``: for each activity class (leading
    digit of the file name) it loads the first ``.mat`` file (alphabetically)
    and returns its spectrogram in dB.

    :param data_dir: Directory containing the ``.mat`` files.  Defaults to
        ``<repo>/data/RadarData/Data``.
    :returns: Mapping from activity class (``int``, see :data:`ACTIVITIES`)
        to that class's dB spectrogram, a 2-D :class:`numpy.ndarray` with
        rows = Doppler bins and columns = time bins.
    :raises FileNotFoundError: If ``data_dir`` does not exist or contains no
        ``.mat`` files.
    """
    directory = (
        Path(data_dir) if data_dir is not None else _DEFAULT_ENERGY_DATA_DIR
    )
    if not directory.is_dir():
        raise FileNotFoundError(
            f"Radar data folder not found: {directory!s}. Pass an explicit "
            f"`data_dir` or run from a checkout that contains "
            f"data/RadarData/Data."
        )

    mat_files = sorted(p for p in directory.iterdir() if p.suffix == ".mat")
    if not mat_files:
        raise FileNotFoundError(
            f"No .mat files found in {directory!s}"
        )

    # First file (alphabetically) whose name starts with each class digit,
    # mirroring LoadData.R's sel_files.
    selected: dict[int, np.ndarray] = {}
    for path in mat_files:
        cls = int(path.name[0])
        if cls not in selected:
            selected[cls] = _read_spectrogram(path)
    return dict(sorted(selected.items()))
