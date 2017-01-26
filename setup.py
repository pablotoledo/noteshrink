#!/usr/bin/env python
//TEXTO DE MASTER
//TEXTO DE MASTER
//TEXTO DE MASTER
//TEXTO DE MASTER
//TEXTO DE MASTER
//TEXTO DE MASTER
//TEXTO DE MASTER
from __future__ import print_function

import os
import sys
from setuptools import setup


if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    os.system("python setup.py bdist_wheel upload")
    print("You probably want to also tag the version now:")
    print("  git tag -a VERSION -m 'version VERSION'")
    print("  git push --tags")
    sys.exit()
    ///Comentario 3
    ///Comentario 3
    ///Comentario 3
    ///Comentario 3

    ///Comentario 1
    /////Comentario 1
    ///Comentario 1
    ///Comentario 1

setup(
    name="noteshrink",
    version="0.1.1",
    author="Matt Zucker",
    description="Convert scans of handwritten notes to beautiful, compact PDFs",
    url="https://github.com/mzucker/noteshrink",
    py_modules=["noteshrink"],
    install_requires=[
        "numpy>=1.1.0",
        "scipy",
        "pillow",
    ],
    entry_points="""
        [console_scripts]
        noteshrink=noteshrink:main
    """,
)
