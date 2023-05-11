"""Standard tests."""
from io import StringIO
from pathlib import Path

import pytest
from bs4 import BeautifulSoup
from sphinx.testing.util import SphinxTestApp

from atsphinx.og_article import models


@pytest.mark.sphinx()
@pytest.mark.parametrize(
    "case, expected",
    [
        ("no-data", 0),
        ("single", 1),
        ("multiple", 2),
    ],
)
def test__tags_len(
    app: SphinxTestApp,
    status: StringIO,
    warning: StringIO,
    case: str,
    expected: int,
):
    """Test case for time complements."""
    app.build()
    doctree = app.env.get_doctree(f"cases-for-tags/{case}")
    target = list(doctree.findall(models.og_article))[0]
    assert len(target["tags"]) == expected
    soup = BeautifulSoup(
        Path(f"{app.outdir}/cases-for-tags/{case}.html").read_text(), "html.parser"
    )
    assert len(soup.find_all("meta", {"property": "article:tag"})) == expected
