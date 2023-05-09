"""Standard tests."""
from io import StringIO

import pytest
from dateutil.tz import gettz
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


@pytest.mark.sphinx()
@pytest.mark.parametrize(
    "case, published_has_tzinfo, modified_has_tzinfo, is_same",
    [
        ("none-none", False, False, True),
        ("none-local", False, False, True),
        ("none-tzinfo", True, True, True),
        ("local-none", False, False, True),
        ("local-local", False, False, False),
        ("local-tzinfo", False, True, False),
        ("tzinfo-none", True, True, True),
        ("tzinfo-local", True, False, False),
        ("tzinfo-tzinfo", True, True, False),
    ],
)
def test__time_values(
    app: SphinxTestApp,
    status: StringIO,
    warning: StringIO,
    case: str,
    published_has_tzinfo: bool,
    modified_has_tzinfo: bool,
    is_same: bool,
):
    """Test case for time complements."""
    app.build()
    doctree = app.env.get_doctree(f"cases-for-times/{case}")
    target = list(doctree.findall(og_article.og_article))[0]
    assert (target["published_time"].tzinfo is not None) is published_has_tzinfo
    assert (target["modified_time"].tzinfo is not None) is modified_has_tzinfo
    if is_same:
        assert target["published_time"] == target["modified_time"]
    else:
        assert target["published_time"] != target["modified_time"]


@pytest.mark.sphinx(confoverrides={"og_article_timezone": "UTC"})
@pytest.mark.parametrize(
    "case, is_same",
    [
        ("none-none", True),
        ("none-local", True),
        ("none-tzinfo", True),
        ("local-none", True),
        ("local-local", False),
        ("local-tzinfo", False),
        ("tzinfo-none", True),
        ("tzinfo-local", False),
        ("tzinfo-tzinfo", False),
    ],
)
def test__time_values_with_conf(
    app: SphinxTestApp, status: StringIO, warning: StringIO, case: str, is_same: bool
):
    """Test case for time complements with ``og_article_timezone``."""
    app.build()
    doctree = app.env.get_doctree(f"cases-for-times/{case}")
    target = list(doctree.findall(og_article.og_article))[0]
    assert target["published_time"].tzinfo is not None
    assert target["modified_time"].tzinfo is not None
    if "tzinfo" not in case:
        assert target["published_time"].tzinfo == gettz("UTC")
        assert target["modified_time"].tzinfo == gettz("UTC")
    if is_same:
        assert target["published_time"] == target["modified_time"]
    else:
        assert target["published_time"] != target["modified_time"]
