# Formatting

We'll set up Visual Studio Code so Python code is automatically formatted on file save.

As of 2022, most modern Python projects settled on the following tools.

- [Black, the uncompromising code formatter](https://black.readthedocs.io/en/stable/)
- [isort your imports, so you don't have to](https://pycqa.github.io/isort/)

Those tools need to be installed in the working Python environment, see [here](environment.md).

Then add the following settings.

In the user `settings.json`:

```json
    "editor.formatOnSave": true,
    "python.formatting.provider": "black",
    "python.formatting.blackArgs": ["--line-length=99"],
    "python.sortImports.args": [
        "--profile", "black",
        "--line-length", "99"
    ],
    "[python]": {
        "editor.codeActionsOnSave": {
            "source.organizeImports": true
        }
    },
```

I'd repeat the following settings in `.vscode/settings.json` for each project:

```json
    "python.formatting.provider": "black",
    "python.formatting.blackArgs": ["--line-length=99"],
    "python.sortImports.args": [
        "--profile", "black",
        "--line-length", "99"
    ],
```

## Extra stuff

I don't need this, but maybe you do:
- Remove unused imports with [autoflake](https://pypi.org/project/autoflake/), corresponding [VS Code extension](https://marketplace.visualstudio.com/items?itemName=TrungNgo.autoflake)
