#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from vswitch import (
    __version__ as version,
    __package_name__ as package_name
)

setup_params = dict(
    version=version,
    name=package_name
)
