"""Support article tpye's properties of Open Graph for Sphinx."""

from datetime import datetime

from dateutil.parser import parse
from dateutil.tz import UTC
from docutils import nodes
from docutils.parsers.rst import Directive
from sphinx.application import Sphinx

__version__ = "0.0.0"


class og_article(nodes.General, nodes.Element):
    """Node class to manage article metadata."""

    pass


def skip_node(self, node: og_article):
    """Minimum function to skip when builder visit it."""
    raise nodes.SkipNode()


def parse_datetime(src: str) -> datetime:
    """Convert datetime object flexibly.

    :returns: datetime object with tzinfo.
    """
    dt = parse(src)
    if dt.tzinfo is None:
        dt = dt.astimezone(UTC)
    return dt


class OgArticleDirective(Directive):
    """Definition of directive to declare article metadata."""

    has_content = True

    option_spec = {
        "published_time": parse_datetime,
        "modified_time": parse_datetime,
    }

    @classmethod
    def complement_options(cls, options: dict) -> dict:
        """Inject values of options for other options."""
        if "published_time" in options and "modified_time" not in options:
            options["modified_time"] = options["published_time"]
        elif "published_time" not in options and "modified_time" in options:
            options["published_time"] = options["modified_time"]
        elif "published_time" not in options and "modified_time" not in options:
            dt = datetime.now().astimezone(UTC)
            options["published_time"] = dt
            options["modified_time"] = dt
        return options

    def run(self):  # noqa: D102
        node = og_article()
        node.attributes = self.complement_options(self.options)
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
