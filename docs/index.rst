===================
atsphinx-og-article
===================

Overview
========

.. todo:: Write it

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

Configuration
=============

.. todo:: I plan to declare configurations.
