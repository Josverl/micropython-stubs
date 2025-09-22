from os import chdir, getcwd
from shutil import rmtree
from tempfile import mkdtemp

import pytest
from sybil import Sybil
from sybil.parsers.codeblock import PythonCodeBlockParser
from sybil.parsers.doctest import DocTestParser

# @pytest.fixture(scope="module")
# def tempdir():
#     # there are better ways to do temp directories, but it's a simple example:
#     path = mkdtemp()
#     cwd = getcwd()
#     try:
#         chdir(path)
#         yield path
#     finally:
#         chdir(cwd)
#         rmtree(path)

# pytest_collect_file = Sybil(
#     parsers=[
#         DocTestParser(),
#         PythonCodeBlockParser(future_imports=['print_function']),
#     ],
#     pattern='*.rst',
#     # fixtures=['tempdir']
# ).pytest()
