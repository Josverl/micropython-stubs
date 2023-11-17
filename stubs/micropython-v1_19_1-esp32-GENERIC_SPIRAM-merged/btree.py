"""
Module: 'btree' on micropython-v1.19.1-esp32
"""
# MCU: {'ver': 'v1.19.1', 'build': '', 'platform': 'esp32', 'port': 'esp32', 'machine': 'ESP32 module (spiram) with ESP32', 'release': '1.19.1', 'nodename': 'esp32', 'name': 'micropython', 'family': 'micropython', 'sysname': 'esp32', 'version': '1.19.1'}
# Stubber: 1.9.11
from typing import Dict, Optional, Any
from _typeshed import Incomplete as Incomplete

DESC = 2  # type: int
INCL = 1  # type: int


def open(stream, *, flags: int = ..., pagesize: int = ..., cachesize: int = ..., minkeypage: int = ...) -> Dict:
    """
    Open a database from a random-access `stream` (like an open file). All
    other parameters are optional and keyword-only, and allow to tweak advanced
    parameters of the database operation (most users will not need them):

    * *flags* - Currently unused.
    * *pagesize* - Page size used for the nodes in BTree. Acceptable range
      is 512-65536. If 0, a port-specific default will be used, optimized for
      port's memory usage and/or performance.
    * *cachesize* - Suggested memory cache size in bytes. For a
      board with enough memory using larger values may improve performance.
      Cache policy is as follows: entire cache is not allocated at once;
      instead, accessing a new page in database will allocate a memory buffer
      for it, until value specified by *cachesize* is reached. Then, these
      buffers will be managed using LRU (least recently used) policy. More
      buffers may still be allocated if needed (e.g., if a database contains
      big keys and/or values). Allocated cache buffers aren't reclaimed.
    * *minkeypage* - Minimum number of keys to store per page. Default value
      of 0 equivalent to 2.

    Returns a BTree object, which implements a dictionary protocol (set
    of methods), and some additional methods described below.
    """
    ...
