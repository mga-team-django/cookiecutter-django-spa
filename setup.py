#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open("README.rst") as readme_file:
    long_description = readme_file.read()

setup(
    name="cookiecutter-django-spa",
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    description="A Cookiecutter template for creating SPA apps with Django.",
    long_description=long_description,
    author="Christophe CHAUVET",
    author_email="christophe.chauvet@@gmail.com",
    url="https://github.com/mga-team-django/cookiecutter-django-spa",
    packages=[],
    license="BSD",
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Framework :: Django :: 2.2",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development",
    ],
    keywords=(
        "cookiecutter, django, projects, project templates "
    ),
)