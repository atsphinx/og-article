"""Context processrors for Sphinx."""

from typing import Optional
from xml.etree import ElementTree as ET

from sphinx import addnodes
from sphinx.application import Sphinx

from . import models


def add_metatags(
    app: Sphinx,
    pathname: str,
    templatename: str,
    context: dict,
    doctree: Optional[addnodes.document] = None,
):
    """Pick og attributes from document and inject into metatags."""
    if not doctree:
        return
    targets = list(doctree.findall(models.og_article))
    if not targets:
        return
    if "metatags" not in context:
        context["metatags"] = ""
    node: models.og_article = targets[0]
    # Append time properties
    metatags = [
        ET.Element(
            "meta",
            {
                "property": "article:published_time",
                "content": node["published_time"].isoformat(timespec="seconds"),
            },
        ),
        ET.Element(
            "meta",
            {
                "property": "article:modified_time",
                "content": node["modified_time"].isoformat(timespec="seconds"),
            },
        ),
    ]
    metatags = b"\n".join([ET.tostring(e) for e in metatags])
    context["metatags"] += f"\n{metatags}"
