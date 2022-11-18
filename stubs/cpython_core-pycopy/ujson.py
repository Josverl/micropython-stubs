import micropython
import json
from json import dump, dumps
import io
import sys


# Before CPython3.6. only str input was acceptet by json module
_json_only_str = sys.version_info < (3, 6)


def load(stream):
    if _json_only_str:
        # io.TextIOWrapper doesn't support text streams as input,
        # so we should pass only binary streams to it.
        if not isinstance(stream, (io.TextIOWrapper, io.StringIO)):
            stream = io.TextIOWrapper(stream)
    return json.load(stream)


def loads(s):
    if _json_only_str and not isinstance(s, str):
        s = s.decode()
    return json.loads(s)
