# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import fancastic_17
version = fancastic_17.__version__

setup(
    name='fancastic_17',
    version=version,
    author='',
    author_email='vivyly9@gmail.com',
    packages=[
        'fancastic_17',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.5',
    ],
    zip_safe=False,
    scripts=['fancastic_17/manage.py'],
)