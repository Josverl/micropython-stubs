"""Execution-context API documented by PyScript 2026.7.3."""

from _typeshed import Incomplete

RUNNING_IN_WORKER: bool
"""Whether PyScript is running in a web worker."""

config: dict[str, object]
"""The normalized PyScript configuration, including ``type`` (``py`` or ``mpy``)."""

js_modules: Incomplete
window: Incomplete
document: Incomplete
sync: Incomplete

def js_import(*urls: str) -> Incomplete:
    """Dynamically import one or more JavaScript modules."""
    ...

def PyWorker(url: str, **options: object) -> Incomplete:
    """Create a Python web worker from the main browser thread."""
    ...

def current_target() -> Incomplete:
    """Return the current output target."""
    ...
