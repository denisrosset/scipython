project = 'scipython'
copyright = '2022, Denis Rosset'
author = 'Denis Rosset'


extensions = [
    "myst_nb",
]

templates_path = ['_templates']

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.venv', '.vscode', '.history']

html_theme = "sphinx_book_theme"
html_static_path = ['_static']
