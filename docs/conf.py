# noqa: D100
from atsphinx.og_article import __version__

# -- Project information
project = "atsphinx-og-article"
copyright = "2023, Kazuya Takei"
author = "Kazuya Takei"
release = __version__

# -- General configuration
extensions = [
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
]
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output
html_theme = "alabaster"
html_static_path = ["_static"]

# -- Options for extensions
# sphinx.ext.intersphinx
intersphinx_mapping = {
    "sphinx": ("https://www.sphinx-doc.org/en/master", None),
}
# sphinx.ext.todo
todo_include_todos = True


def setup(app):  # noqa: D103
    app.add_object_type(
        "confval",
        "confval",
        objname="configuration value",
        indextemplate="pair: %s; configuration value",
    )
