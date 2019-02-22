# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 Mirek Simek.
#
# oarepo-links is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Module tests."""

from __future__ import absolute_import, print_function

from flask import Flask

from oarepo_links import oarepolinks


def test_version():
    """Test version import."""
    from oarepo_links import __version__
    assert __version__


def test_init():
    """Test extension initialization."""
    app = Flask('testapp')
    ext = oarepolinks(app)
    assert 'oarepo-links' in app.extensions

    app = Flask('testapp')
    ext = oarepolinks()
    assert 'oarepo-links' not in app.extensions
    ext.init_app(app)
    assert 'oarepo-links' in app.extensions


def test_view(base_client):
    """Test view."""
    res = base_client.get("/")
    assert res.status_code == 200
    assert 'Welcome to oarepo-links' in str(res.data)
