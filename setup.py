#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

setup(name='pyramid_tenjin',
      version='0.1',
      packages=find_packages(),
      include_package_data=True,
      install_requires=['pyramid', 'Tenjin'],
      )
