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

## Hackathon Goals

The main goal is to perform some exploratory data analysis on one of the three datasets provided.

## Extras

- This repository is missing a `./tests/` directory. Try and add your own if you have time. A common unit testing framework is `pytest`.
- It is often desirable to document your code, for reproducibility's sake. Try editing this README with usage instructions, or create a `./docs/` folder containing Markdown files.
- Finding yourself writing one-off Python scripts to automate some command line process? You don't have to just store them in your `./src/` folder. You can make a `./scripts` directory, and include them as tasks by running
  ```bash
  pixi task add mytask "python scripts/myscript.py"
  ```
