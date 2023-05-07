"""Support article tpye's properties of Open Graph for Sphinx."""

from docutils import nodes
from docutils.parsers.rst import Directive, directives
from sphinx.application import Sphinx

__version__ = "0.0.0"


class og_article(nodes.General, nodes.Element):
    """Node class to manage article metadata."""

    pass


def skip_node(self, node: og_article):
    """Minimum function to skip when builder visit it."""
    raise nodes.SkipNode()


class OgArticleDirective(Directive):
    """Definition of directive to declare article metadata."""

    has_content = True

    option_spec = {
        "published_time": directives.unchanged,
        "modified_time": directives.unchanged,
    }

    def run(self):  # noqa: D102
        node = og_article()
        node.attributes = self.options
        return [
            node,
        ]


def setup(app: Sphinx):  # noqa: D103
    app.add_directive("og-article", OgArticleDirective)
    app.add_node(
        og_article,
        html=(skip_node, None),
        latex=(skip_node, None),
        text=(skip_node, None),
        man=(skip_node, None),
        texinfo=(skip_node, None),
    )
    return {
        "version": __version__,
        "env_version": 1,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
