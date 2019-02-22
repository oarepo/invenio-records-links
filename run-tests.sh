#!/usr/bin/env sh
# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 Mirek Simek.
#
# oarepo-links is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

pydocstyle oarepo_links tests docs && \
isort -rc -c -df && \
check-manifest --ignore ".travis-*" && \
sphinx-build -qnNW docs docs/_build/html && \
python setup.py test
