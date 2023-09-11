#!/usr/bin/env python
"""
Installs Badger CLI.
| Copyright 2017-2023, Voxel51, Inc.
| `voxel51.com <https://voxel51.com/>`_
|
"""

from setuptools import setup, find_packages

setup(
    name="badger",
    version="0.1",
    packages=find_packages(),
    install_requires=["argparse", "pyperclip", "xml"],
    extras_require={
        "web": ["bs4", "requests"],
        "wild": ["openai"],
    },
    entry_points={"console_scripts": ["badger = src.badger:main"]},
    author="Voxel51, Inc.",
    author_email="info@voxel51.com",
    description="A CLI tool for generating custom badges",
    url="https://github.com/voxel51/badger",
    license="Apache",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
    ],
)
