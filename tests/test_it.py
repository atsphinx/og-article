"""Standard tests."""
import datetime
from io import StringIO

import pytest
from dateutil.tz import UTC
from sphinx.testing.util import SphinxTestApp

from atsphinx import og_article


@pytest.mark.sphinx("html")
def test__it(app: SphinxTestApp, status: StringIO, warning: StringIO):
    """Test to pass."""
    app.builder.read()
    doctree = app.env.get_doctree("index")
    assert doctree is not None
    target_nodes = list(doctree.findall(og_article.og_article))
    assert len(target_nodes) == 1
    target = target_nodes[0]
    assert isinstance(target["published_time"], datetime.datetime)
    assert target["published_time"].tzinfo == UTC


@pytest.mark.sphinx("html")
def test__key_patterns(app: SphinxTestApp, status: StringIO, warning: StringIO):
    """Test to pass."""
    app.builder.read()
    doctree = app.env.get_doctree("case-times-complete")
    for target in doctree.findall(og_article.og_article):
        assert target["published_time"]
        assert target["modified_time"]
