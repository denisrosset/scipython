# Managing dependencies

## Packages 

[conda-forge](conda-forge.org)  vs. [PyPI](pypi.org)

We want

- to specify the package versions we depend on (is it a `==` requirement? or a `>=` requirement?)

- to solve version conflicts automatically (and know beforehand of incompatibilities)

- to distribute our code so that people can install compatible versions of libraries, or even *install exactly the same package versions that worked on our computer*

Example: https://github.com/openlawlibrary/pygls/pull/148

   pydantic seems to make breaking changes at minor releases; however 1.8 works just fine so I've allowed 1.7.x and 1.8.x


We will use [Poetry](python-poetry.org)

### Options for virtual environments:

- If you are happy with the system Python version:

```
mkdir testproj
python -m venv .venv
```

- If you are not happy with the system Python version, use [pyenv](https://github.com/pyenv/pyenv)
  (I haven't tried those)

for these two last options, and you do not need to do anything special to use Poetry.

- If you want to use Conda:

  Use Conda to set non-Python-package things, such as the Python interpreter

```
conda create -n testproj_env python==3.10
conda activate testproj_env
```

.. but you'll need to activate the Conda environment before using Poetry on the command line.

Note: the only weak spot of Poetry is publishing packages with C/C++/Fortran/Cython code. The workaround I'd recommend is this: put the C/C++/Fortran/Cython parts in a separate package managed by an old-style `setup.py` script, where you can use wonderful legacy tools such a `f2py` etc. Then add this separate package as a requirement in your main project.

## Starting a project with Poetry

### Setup Poetry and the environments

* [Install Poetry](https://python-poetry.org/docs/#installation)

* Optional: use Conda to create a Conda environment with the Python version you want to use (and potentially external tools required for the project, but avoid if possible)

```
$ mkdir testproj
$ cd testproj
$ conda activate testproj_env
```

or

```
$ mkdir testproj
$ cd testproj
$ python -m venv .venv
```

Now it's time to generate the `pyproject.toml` info file.

```
(testproj_env) $ poetry init

This command will guide you through creating your pyproject.toml config.

Package name [testproj]:  
Version [0.1.0]:  
Description []:  
Author [Denis Rosset <physics@denisrosset.com>, n to skip]:  
License []:  
Compatible Python versions [^3.10]:  

Would you like to define your main dependencies interactively? (yes/no) [yes] no
Would you like to define your development dependencies interactively? (yes/no) [yes] no 
Generated file

[tool.poetry]
name = "testproj"
version = "0.1.0"
description = ""
authors = ["Denis Rosset <physics@denisrosset.com>"]

[tool.poetry.dependencies]
python = "^3.10"

[tool.poetry.dev-dependencies]

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"


Do you confirm generation? (yes/no) [yes] yes
(testproj_env) $ 
```

This generated a `pyproject.toml` file.

### Add the development dependencies:

```
(testproj_env) $ poetry add --dev black mypy pytest isort
Using version ^22.1.0 for black
Using version ^0.941 for mypy
Using version ^7.1.1 for pytest
Using version ^5.10.1 for isort

Updating dependencies
Resolving dependencies... (1.1s)

Writing lock file

Package operations: 16 installs, 0 updates, 0 removals

  • Installing pyparsing (3.0.7)
  • Installing attrs (21.4.0)
  • Installing click (8.0.4)
  • Installing iniconfig (1.1.1)
  • Installing mypy-extensions (0.4.3)
  • Installing packaging (21.3)
  • Installing pathspec (0.9.0)
  • Installing platformdirs (2.5.1)
  • Installing pluggy (1.0.0)
  • Installing py (1.11.0)
  • Installing tomli (2.0.1)
  • Installing typing-extensions (4.1.1)
  • Installing black (22.1.0)
  • Installing isort (5.10.1)
  • Installing mypy (0.941)
  • Installing pytest (7.1.1)
```

### Open the project in VS Code

Now you can open the `testproj` folder in VS Code.

### Formatting

Add to `pyproject.toml` the defaults for the formatting tools:

```toml
[tool.black]
line-length = 99
target_version = ['py310'] # replace by your Python version

[tool.doc8]
max-line-length = 99

[tool.isort]
line_length = 99
profile = "black"
py_version = 310
```

### .gitignore

Create a minimal `.gitignore` file:

```
.venv/
__pycache__/
.mypy_cache/
.pytest_cache/
build/
dist/
.pytest_cache/
```

### VS code

Create a `testproj/.vscode` folder and add the following bare-bones `settings.json` file:

```
{
    "python.testing.unittestEnabled": false,
    "python.testing.pytestEnabled": true,
    "python.linting.mypyEnabled": true,
    "editor.formatOnSave": true,
    "python.formatting.provider": "black",
    "editor.rulers": [
        99
    ],
    "[python]": {
        "editor.codeActionsOnSave": {
            "source.organizeImports": true
        }
    },
    "files.exclude": {
        ".venv/": true,
        "**/__pycache__": true,
        "**/.mypy_cache": true,
        "**/.pytest_cache": true,
        "**/build": true,
        "**/dist": true,
    },
}
```

### Test the stuff

Create a `adder.py` file with the following:

```python
def addition(x: float, y: float) -> float:
   return x + y
```

Verify that Black reformats the code on save.

Now let's write a test script `test_addition.py`:

```python
from adder import addition
def test_addition() -> None:
   assert addition(2, 2) == 4
```
## A few words about `poetry run`

## A few words about `poetry.lock`

