#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import find_packages
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="robin",
    version="0.1.0",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Savio Fernandes",
    author_email="savio@saviof.com",
    license="MIT",
    url="https://github.com/artbycrunk/robin",
    download_url='https://github.com/artbycrunk/robin/archive/0.1.0.tar.gz',
    keywords=[],
    packages=find_packages("src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    install_requires=[
        "click",
    ],
    entry_points={
        "console_scripts": [
            "robin = robin.cli:main"
        ]
    }
)