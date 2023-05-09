===================
atsphinx-og-article
===================

.. image:: https://img.shields.io/pypi/v/atsphinx-og-article.svg
   :target: https://pypi.org/project/atsphinx-og-article/
   :alt: Stable version on PyPI

.. image:: https://github.com/atsphinx/og-article/actions/workflows/main.yml/badge.svg
   :target: https://github.com/atsphinx/og-article/actions
   :alt: "Continuous Integration" status for main branch

.. image:: https://readthedocs.org/projects/atsphinx-og-article/badge/?version=latest
   :target: https://atsphinx-og-article.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation status

Support article tpye's properties of Open Graph for Sphinx.

Overview
========

This is Sphinx extension to handle properties of article typeof Open Graph.

You can add ``og-article`` directive with some options.

.. code:: rst

   .. og-article::
      :published_time: 2023-05-07
      :modified_time: 2023-05-07 12:00:00

When it runs builder with this directive,
your html file is generated included `<meta property="article:published_time">` and more properties.

Getting started
===============

Install from PyPI.

.. code: console

   pip install atsphinx-og-article

Configure your ``conf.py``.

.. code: python

   extensions = [
       # After other extensions.
       "atsphinx.og_article",
   ]

Append ``og-article`` directive into your document.

Important note
==============

This extension renders only ``article:*`` properties, and does not render ``og:*`` properties.

I recommend to install ``sphinxext-opengraph`` too.

Ref
===

- `Globally defined properties on OGP site. <https://ogp.me/#type_article>`_
- `sphinxext-opengraph <https://pypi.org/project/sphinxext-opengraph/>`_
