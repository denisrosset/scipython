project = "scipython"
copyright = "2022, Denis Rosset"
author = "Denis Rosset"

html_title = "Modern scientific Python"

extensions = [
    "myst_nb",
]

templates_path = ["_templates"]

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", ".venv", ".vscode", ".history"]

html_theme = "sphinx_book_theme"
html_static_path = ["_static"]

html_theme_options = {"show_prev_next": False}

myst_enable_extensions = ["linkify"]
