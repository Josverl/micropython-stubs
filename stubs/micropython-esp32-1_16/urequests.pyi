from typing import Any

Node = Any

class Response:
    def close() -> None: ...
    def json() -> None: ...

def delete() -> None: ...
def get() -> None: ...
def head() -> None: ...
def patch() -> None: ...
def post() -> None: ...
def put() -> None: ...
def request() -> None: ...
