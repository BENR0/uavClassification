# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    "description": "Very high resolution orthoimage classification.",
    "author": "Benjamin Roesner",
    "url": "https://github.com/BENR0/uavClassification",
    "download_url": "https://github.com/BENR0/uavClassification",
    "author_email": ".",
    "version": "0.0",
    "install_requires": ["tqdm"],
    "packages": ["uavClassification"],
    # "scripts": ["scripts/mod35_l2.py"],
    "name": "uavClassification"
}

setup(**config)
