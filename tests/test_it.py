"""Standard tests."""
from io import StringIO
from pathlib import Path

import pytest
from bs4 import BeautifulSoup
from sphinx.testing.util import SphinxTestApp

from atsphinx.og_article import models


@pytest.mark.sphinx("html")
def test__it(app: SphinxTestApp, status: StringIO, warning: StringIO):
    """Test to pass."""
    app.build()
    doctree = app.env.get_doctree("index")
    assert doctree is not None
    target_nodes = list(doctree.findall(models.og_article))
    assert len(target_nodes) == 1
    soup = BeautifulSoup(Path(f"{app.outdir}/index.html").read_text(), "html.parser")
    assert soup.find("meta", {"property": "article:published_time"})
    assert soup.find("meta", {"property": "article:modified_time"})
    assert "b'" not in str(soup)
