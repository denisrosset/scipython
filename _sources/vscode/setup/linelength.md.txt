# Line length

While many Python packages have now settled on the use of Black as a code formatter (which does not
have many tweaks! and thus saves time on style discussion), line length recommendations vary 
widely.

In 2001, [PEP8](https://www.python.org/dev/peps/pep-0008/) prescribed 79 characters per line.
Twenty years later, modern Python code tends to use more descriptive, longer identifiers.
The introduction of [type hints](https://www.python.org/dev/peps/pep-0484/) also widens function/method declarations.

Black's default is 88 characters.

I personally tend to use 99 characters on OOP code with type hints.

See https://jakevdp.github.io/blog/2017/11/09/exploring-line-lengths-in-python-packages/ for 
additional analysis.

Whatever choice you'll made, I suggest you set the line length options in the user JSON settings,
and also per-project in `.vscode/settings.json` folder
(as to document the style choice to other contributors to the project).

There are several settings to set.

## Ruler in the editor

To indicate the column where the line is supposed to end, add this in the JSON settings:

```json
    "editor.rulers": [99],
```

## Black formatting, setting in VS Code

If you [set up Black properly](formatting), the formatting will be done on each save.
VS Code can apply additional parameters when running Black at that point.

Simply add the following line to the user/project JSON settings:

```json
    "python.formatting.blackArgs": ["--line-length=99"],
```

The line length also affects import sorting, so add:
```json
    "python.sortImports.args": [
        "...",
        "--line-length", "99"
        "...",
    ],
```

## Black formatting, setting in `pyproject.toml`

There is a standard place to put Black parameters in Python projects, so that the settings will
apply when using other IDEs, or when running Black from the command line.

Modern Python tooling (poetry) uses a `pyproject.toml` file in the root project folder.

Add sections:

```
[tool.black]
...
line-length = 99
...

[tool.isort]
...
line_length = 99
...
```

See [formatting](formatting) for full details.
