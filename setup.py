#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="zeus-api",
    version="0.1.0",
    author="osbd-systems",
    author_email="osbd-systems@cisco.com",
    packages=[
        "zeus_api",
    ],
    include_package_data=True,
    install_requires=[
        "Django==1.7.6",
    ],
    zip_safe=False,
    scripts=["zeus_api/manage.py"],
)
