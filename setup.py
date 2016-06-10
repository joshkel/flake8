"""Packaging logic for Flake8."""
# -*- coding: utf-8 -*-
from __future__ import with_statement

import functools
import sys

import setuptools

import flake8  # noqa

try:
    # Work around a traceback with Nose on Python 2.6
    # http://bugs.python.org/issue15881#msg170215
    __import__('multiprocessing')
except ImportError:
    pass

try:
    # Use https://docs.python.org/3/library/unittest.mock.html
    from unittest import mock
except ImportError:
    # < Python 3.3
    mock = None


tests_require = ['pytest']
if mock is None:
    tests_require.append('mock')


requires = [
    "pyflakes >= 0.8.1, != 1.2.0, != 1.2.1, != 1.2.2",
    "pep8 >= 1.5.7, != 1.6.0, != 1.6.1, != 1.6.2",
    "mccabe >= 0.5.0",
]

if sys.version_info < (3, 4):
    requires.append("enum34")

if sys.version_info < (3, 2):
    requires.append("configparser")


def get_long_description():
    """Generate a long description from the README and CHANGES files."""
    descr = []
    for fname in ('README.rst', 'CHANGES.rst'):
        with open(fname) as f:
            descr.append(f.read())
    return '\n\n'.join(descr)

PEP8 = 'pep8'
_FORMAT = '{0}.{1} = {0}:{1}'
PEP8_PLUGIN = functools.partial(_FORMAT.format, PEP8)


setuptools.setup(
    name="flake8",
    license="MIT",
    version=flake8.__version__,
    description="the modular source code checker: pep8, pyflakes and co",
    # long_description=get_long_description(),
    author="Tarek Ziade",
    author_email="tarek@ziade.org",
    maintainer="Ian Cordasco",
    maintainer_email="graffatcolmingov@gmail.com",
    url="https://gitlab.com/pycqa/flake8",
    packages=[
        "flake8",
        "flake8.formatting",
        "flake8.main",
        "flake8.options",
        "flake8.plugins",
    ],
    install_requires=requires,
    entry_points={
        'distutils.commands': ['flake8 = flake8.main:Flake8Command'],
        'console_scripts': ['flake8 = flake8.main.cli:main'],
        'flake8.extension': [
            'F = flake8.plugins.pyflakes:FlakesChecker',
            # PEP-0008 checks provied by PyCQA/pycodestyle
            PEP8_PLUGIN('tabs_or_spaces'),
            PEP8_PLUGIN('tabs_obsolete'),
            PEP8_PLUGIN('trailing_whitespace'),
            PEP8_PLUGIN('trailing_blank_lines'),
            PEP8_PLUGIN('maximum_line_length'),
            PEP8_PLUGIN('blank_lines'),
            PEP8_PLUGIN('extraneous_whitespace'),
            PEP8_PLUGIN('whitespace_around_keywords'),
            PEP8_PLUGIN('missing_whitespace'),
            PEP8_PLUGIN('indentation'),
            PEP8_PLUGIN('continued_indentation'),
            PEP8_PLUGIN('whitespace_before_parameters'),
            PEP8_PLUGIN('whitespace_around_operator'),
            PEP8_PLUGIN('missing_whitespace_around_operator'),
            PEP8_PLUGIN('whitespace_around_comma'),
            PEP8_PLUGIN('whitespace_around_named_parameter_equals'),
            PEP8_PLUGIN('whitespace_before_comment'),
            PEP8_PLUGIN('imports_on_separate_lines'),
            PEP8_PLUGIN('module_imports_on_top_of_file'),
            PEP8_PLUGIN('compound_statements'),
            PEP8_PLUGIN('explicit_line_join'),
            PEP8_PLUGIN('break_around_binary_operator'),
            PEP8_PLUGIN('comparison_to_singleton'),
            PEP8_PLUGIN('comparison_negative'),
            PEP8_PLUGIN('comparison_type'),
            PEP8_PLUGIN('python_3000_has_key'),
            PEP8_PLUGIN('python_3000_raise_comma'),
            PEP8_PLUGIN('python_3000_not_equal'),
            PEP8_PLUGIN('python_3000_backticks'),
        ],
        'flake8.report': [
            'default = flake8.formatting.default:Default',
            'pylint = flake8.formatting.default:Pylint',
        ],
    },
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
    ],
    tests_require=tests_require,
    setup_requires=['pytest-runner'],
)
