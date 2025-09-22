import pytest
from sybil import Sybil
from sybil.parsers.rest import DocTestParser, PythonCodeBlockParser

@pytest.fixture(scope='session')
def keep_seed():
    import myproj
    seed = myproj.SEED
    yield
    myproj.SEED = seed

pytest_collect_file = Sybil(
    parsers=[
        DocTestParser(),
        PythonCodeBlockParser(),
    ],
    patterns=['*.rst', '*.py'],
    fixtures=['keep_seed']
).pytest()

