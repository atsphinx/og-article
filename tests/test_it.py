"""Standard tests."""
from io import StringIO

import pytest
from sphinx.testing.util import SphinxTestApp

from atsphinx import og_article


@pytest.mark.sphinx("html")
def test__it(app: SphinxTestApp, status: StringIO, warning: StringIO):
    """Test to pass."""
    app.builder.read()
    doctree = app.env.get_doctree("index")
    assert doctree is not None
    assert len(list(doctree.findall(og_article.og_article))) == 1
