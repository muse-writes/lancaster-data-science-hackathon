# Lancaster Data Science Hackathon Project

A template repository for the data science hackathon. Good luck and have fun!

## Environment

The Python environment is managed through [Pixi](https://pixi.prefix.dev/latest/), please ensure it is installed.

To install the environment, navigate to the repository's directory and run

```bash
pixi install
```

To add a dependency, run

```bash
pixi add [package-name[=version]]
```

To use your environment to run the main function, run

```bash
pixi run main
```

You can freely edit the source code or include new modules, and are particularly encouraged to do so in `src/lancaster_data_science_hackathon/main.py` for convenience.

## Hackathon Goals

The main goal is to perform some exploratory data analysis on one of the three datasets provided.

To use any of the datasets, download them and place them in a `./data/` folder (which you will need to create). This will let the provided scripts for locating and loading the data find it.


### Radar Data

Download the `RadarData` folder and place it in `./data/`. The source file, `radar_data.py` contains a public function `load_radar_data()` which loads the relevant data files as a dictionary of `numpy` arrays, and `ACTIVITIES` which is a dictionary of integer-assigned human activities.

### Energy Data

Download the `'Energy Usage'` folder and place it in `./data/`. The source file, `energy_data.py` contains `load_energy_data()` which loads the energy CSV files as a dictionary of `pandas` dataframes.

### Mouse Brain Data

Download the `'Mouse Brain'` folder and palce it in `./data/`. The source file, `mouse_brain_data.py` contains `load_mouse_brain_data()`, which loads the sparse matrices as `AnnData` objects.

### Usage Notes

All data loading functions have been exposed at the package level, and can be imported through:

```Python
from lancaster_data_science_hackathon import (
    load_radar_data,
    load_energy_data,
    load_mouse_brain_data
)
```

## Extras

- This repository is missing a `./tests/` directory. Try and add your own if you have time. A common unit testing framework is `pytest`.
- It is often desirable to document your code, for reproducibility's sake. Try editing this README with usage instructions, or create a `./docs/` folder containing Markdown files.
- Finding yourself writing one-off Python scripts to automate some command line process? You don't have to just store them in your `./src/` folder. You can make a `./scripts` directory, and include them as tasks by running
  ```bash
  pixi task add mytask "python scripts/myscript.py"
  ```
