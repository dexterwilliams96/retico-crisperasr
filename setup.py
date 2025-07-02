#!/usr/bin/env python3

"""
Setup script.

Use this script to install CrisperWhisper ASR module for retico. Usage:
    $ python3 setup.py install

Author: Dexter Williams (dexterwilliams4355@gmail.com)
"""

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

exec(open("retico_crisperasr/version.py").read())

import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")

config = {
    "description": "ASR for retico using CrisperWhisper",
    "long_description": long_description,
    "long_description_content_type": "text/markdown",
    "author": "Dexter Williams",
    "author_email": "dexterwilliams4355@gmail.com",
    "url": "https://github.com/dexterwilliams96/retico-crisperasr",
    "download_url": "https://github.com/dexterwilliams96/retico-crisperasr",
    "version": __version__,
    "python_requires": ">=3.10, <4",
    "keywords": "retico, framework, incremental, dialogue, dialog",
    "install_requires": [
        "retico-core>=0.2.10,<0.3.0",
        "transformers>=4.53.0,<5.0.0",
        "torch>=2.0,<3.0.0",
        "torchaudio>=2.7.1,<3.0.0",
        "pydub>=0.25.1,<0.26.0",
        "webrtcvad>=2.0.10,<3.0.0"
        ],
    "packages": find_packages(),
    "name": "retico-crisperasr",
    "classifiers": [
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
    ],
}

setup(**config)
