"""Support article tpye's properties of Open Graph for Sphinx."""

from docutils import nodes
from sphinx.application import Sphinx

from . import models, processors

__version__ = "0.1.1"


def skip_node(self, node: models.og_article):
    """Minimum function to skip when builder visit it."""
    raise nodes.SkipNode()


def setup(app: Sphinx):  # noqa: D103
    app.add_config_value("og_article_timezone", None, "env", [str])
    app.add_directive("og-article", models.OgArticleDirective)
    app.add_node(
        models.og_article,
        html=(skip_node, None),
        latex=(skip_node, None),
        text=(skip_node, None),
        man=(skip_node, None),
        texinfo=(skip_node, None),
    )
    app.connect("html-page-context", processors.add_metatags)
    return {
        "version": __version__,
        "env_version": 1,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
