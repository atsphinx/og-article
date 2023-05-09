"""Object models in doctree domain."""

from datetime import datetime

from dateutil.parser import parse
from dateutil.tz import gettz
from docutils import nodes
from sphinx.config import Config
from sphinx.util.docutils import SphinxDirective


class og_article(nodes.General, nodes.Element):
    """Node class to manage article metadata."""

    pass


def complement_time_options(options: dict, config: Config) -> dict:
    """Convert datetime object flexibly.

    :returns: datetime object with tzinfo.
    """
    # Define vars
    published_time = options.get("published_time", None)
    modified_time = options.get("modified_time", None)
    # Append timezone if need
    if config.og_article_timezone:
        tzinfo = gettz(config.og_article_timezone)
        if published_time and not published_time.tzinfo:
            published_time = published_time.replace(tzinfo=tzinfo)
        if modified_time and not modified_time.tzinfo:
            modified_time = modified_time.replace(tzinfo=tzinfo)
    # Complete times
    if published_time is None and modified_time is not None:
        published_time = modified_time
    elif published_time is not None and modified_time is None:
        modified_time = published_time
    elif published_time is None and modified_time is None:
        now = datetime.now()
        if config.og_article_timezone:
            now = now.replace(tzinfo=gettz(config.og_article_timezone))
        published_time = now
        modified_time = now
    # Return
    options["published_time"] = published_time
    options["modified_time"] = modified_time
    return options


class OgArticleDirective(SphinxDirective):
    """Definition of directive to declare article metadata."""

    has_content = True

    option_spec = {
        "published_time": parse,
        "modified_time": parse,
    }

    def run(self):  # noqa: D102
        node = og_article()
        node.attributes = complement_time_options(self.options, self.env.config)
        return [
            node,
        ]
