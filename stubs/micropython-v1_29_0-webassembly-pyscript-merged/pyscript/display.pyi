"""Display API documented by PyScript 2026.7.3."""
# Copyright (c) 2020-2025 Jos Verlinde
# MIT Licensed

class HTML:
    """
    Wrap a string so that display() can render it as plain HTML
    """
    def __init__(self, html: object) -> None: ...
    def _repr_html_(self) -> object: ...

def display(*values: object, target: object = None, append: bool = True) -> None:
    """Display values in a target element, appending by default."""
    ...
