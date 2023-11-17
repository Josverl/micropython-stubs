"""
Module: 'btree' on micropython-v1.20.0-esp32-GENERIC_S3
"""
# MCU: OrderedDict({'version': '1.20.0', 'mpy': 'v6.1', 'port': 'esp32', 'board': 'GENERIC_S3', 'family': 'micropython', 'build': '', 'arch': 'xtensawin', 'ver': 'v1.20.0', 'cpu': 'ESP32S3'})
# Stubber: v1.13.7
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
