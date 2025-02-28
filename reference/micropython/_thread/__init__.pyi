""" 
Manual typestub for _thread module.

multithreading support. See: https://docs.micropython.org/en/v1.24.0/library/_thread.html

|see_cpython_module| :mod:`python:_thread` https://docs.python.org/3/library/_thread.html .

This module implements multithreading support.

This module is highly experimental and its API is not yet fully settled
and not yet described in this documentation.
"""

from typing import Callable, NoReturn, Optional, Tuple

def get_ident() -> int:
    """\
    Return the ‘thread identifier’ of the current thread. This is a nonzero integer. 
    Its value has no direct meaning; it is intended as a magic cookie to be used e.g. to index a dictionary of thread-specific data. 
    Thread identifiers may be recycled when a thread exits and another thread is created
    """
    ...

def start_new_thread(function: Callable, args: Tuple) -> None:
    """
    Start a new thread. The thread executes the function function with the argument list args (which must be a tuple). The optional kwargs argument specifies a dictionary of keyword arguments.
    When the function returns, the thread silently exits.

    - rp2040 : only one additional thread is supported, so this function will raise an exception if called more than once unless the first thread has already exited.

    """
    ...

def stack_size(size: Optional[int] = 0) -> int:
    """\
    Return the thread stack size used when creating new threads. 
    The optional size argument specifies the stack size to be used for subsequently created threads, and must be 0 (use platform or configured default) 
    or a positive integer value of at least 32,768 (32 KiB). If size is not specified, 0 is used. 
    """
    ...

def exit() -> NoReturn:
    """\
    Raise the SystemExit exception. When not caught, this will cause the thread to exit silently
    """
    ...

def allocate_lock() -> lock:  # Lock object
    """
    Return a new lock object. The lock is initially unlocked.
    """
    ...

class lock:
    def __init__(self) -> None:
        """
        Locks should be allocated via `allocate_lock()`.
        Initially, it is unlocked.
        """
        ...

    def acquire(self, blocking: bool = True, timeout: int = -1) -> bool:
        """
        Without any optional argument, this method acquires the lock unconditionally, if necessary waiting until it is released by another thread (only one thread at a time can acquire a lock — that’s their reason for existence).
        If the blocking argument is present, the action depends on its value: if it is False, the lock is only acquired if it can be acquired immediately without waiting, while if it is True, the lock is acquired unconditionally as above.
        The return value is True if the lock is acquired successfully, False if not.
        """
        ...

    def release(self) -> None:
        """Releases the lock. The lock must have been acquired earlier, but not necessarily by the same thread."""
        ...

    def locked(self) -> bool:
        """
        Return the status of the lock: True if it has been acquired by some thread, False if not.
        """
        ...
