===================
atsphinx-og-article
===================

Overview
========

This is Sphinx extension to handle properties of article typeof Open Graph.

You can add ``og-article`` directive with some options.
This appends extra properties into meta tags from ``og-article`` directive.

NOTE: Use with sphinxext-opengraph
----------------------------------

This renders only ``article:**`` meta tags.
For full functional as OpenGraph, install :pypi:`sphinxext-opengraph` too.

Installation
============

.. todo:: This is scheduled method.

This is registered on PyPI.
You can install ``pip`` command.

.. code-block:: console

   pip install atsphinx-og-article

Edit your ``conf.py`` to add extension.

.. code-block:: python

   extensions = [
       "atsphinx.og_article",
   ]

Usage
=====

Standard usage is adding ``og-article`` directive into your document.
You may add directive into document that you want to consider as "article".

.. code-block:: rst

   .. og-article::
      :published_time: 2023-05-07

When you run html-like builders,
generated files include ``<meta property="article:PROP" >`` elements
from documents added directive.

.. rst:directive:: og-article

   .. rst:directive:option:: published_time
      :type: string

   .. rst:directive:option:: modified_time
      :type: string

   ``published_time`` and ``modified_time`` accept any format that dateutil can parse.
   When it is parsing attribute, datetime object has timezone always.

   These are complement by mutually. If one is not set, use another value automately.
   If neither not set, these are set build datetime.

Configuration
=============

.. confval:: og_article_timezone

   :Type: ``str | None``
   :Default: ``None``
   :Example: ``Asia/Tokyo``

   If this is not ``None``, replace timezone of ``published_time`` and ``modified_time`` that do not have timezone text.
