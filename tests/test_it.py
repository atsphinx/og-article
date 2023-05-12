"""Standard tests."""
from io import StringIO

import pytest
from sphinx.testing.util import SphinxTestApp

from atsphinx.og_article import models


@pytest.mark.sphinx("html")
def test__it(app: SphinxTestApp, status: StringIO, warning: StringIO):
    """Test to pass."""
    app.builder.read()
    doctree = app.env.get_doctree("index")
    assert doctree is not None
    target_nodes = list(doctree.findall(models.og_article))
    assert len(target_nodes) == 1
