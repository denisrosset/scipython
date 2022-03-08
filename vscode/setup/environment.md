# Python environment

The code you work on will run on a Python environment. By default, Python uses the system environment. It is recommended to create virtual environments for different projects to avoid library conflicts.

There are several ways to create/deal with Python environments:

- Instantiate them manually using [venv](https://docs.python.org/3/library/venv.html). In that case, VS Code won't be able to find them automatically.

- Manage Python interpreters and environments using [Conda](https://docs.conda.io/en/latest/), in which case VS Code *will* find Conda environments automatically.

- Use [Poetry](https://python-poetry.org/) to manage a Python project. This option is fantastic for more mature projects that will later be released on PyPI. Poetry manages the project dependencies in a `.venv/` subfolder; the dependencies are listed in the main `pyproject.toml` file.

The Python environment you select will be used for new terminal windows, running and debugging code.

## If Python/Conda is not detected automatically

If required by your Python/Conda installation, update the following settings in the user `settings.json`, or through the UI:

```json
    "python.defaultInterpreterPath": "/path/to/python",
    "python.condaPath": "/path/to/conda",
```

## Selecting a Python environment in VS Code

CTRL+SHIFT+P `Python: Select interpreter` should show a list of autodetected environments. One can always select a `venv` that is not in the list.

This is the only VS Code setting that:

- won't be stored in the user `settings.json` file: indeed, the Python environment changes project by project

- won't be stored in the project `.vscode/settings.json` file: indeed, paths to Python environments change from computer to computer

## Installing development dependencies

Below we list the tools that are required *during development*. Those tools are not required to use the Python packages you'll develop.

### Installation in a regular `venv` or in Conda

In a standard Python `venv` or one managed by Conda, use the commands:

```bash
pip install isort
pip install black
pip install mypy
```

(even though some/all these packages are available in Conda, the PyPI versions tend to be more up to date)


### Installation using Poetry

If using Poetry, use the `--dev` argument to flag those dependencies as not required for simple use of the package you may publish later.
```bash
poetry add --dev black
poetry add --dev isort
poetry add --dev mypy
```

## Installing Jupyter notebooks support

The Python VS Code extension installs support for Jupyter notebooks by default, see [our explanation](../extensions.md).

However, one needs to install the `jupyterlab` PyPI package to use that support.

```bash
pip install jupyterlab
```

or 

```
poetry add --dev jupyterlab
```


## Extra reading

https://code.visualstudio.com/docs/python/environments
