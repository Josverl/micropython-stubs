from _typeshed import Incomplete as Incomplete
from typing import Any, Dict, Optional

INCL: Incomplete
DESC: Incomplete

class btree:
    """ """

    def close(self) -> None:
        """
        Close the database. It's mandatory to close the database at the end of
        processing, as some unwritten data may be still in the cache. Note that
        this does not close underlying stream with which the database was opened,
        it should be closed separately (which is also mandatory to make sure that
        data flushed from buffer to the underlying storage).
        """
    def flush(self) -> Incomplete:
        """
        Flush any data in cache to the underlying stream.
        """
    def __getitem__(self, key) -> Incomplete:
        """
        Standard dictionary methods.
        """
    def get(self, key, default: Incomplete | None = ...) -> Incomplete:
        """
        Standard dictionary methods.
        """
    def __setitem__(self, key, val) -> Incomplete:
        """
        Standard dictionary methods.
        """
    def __delitem__(self, key) -> Incomplete:
        """
        Standard dictionary methods.
        """
    def __contains__(self, key) -> Incomplete:
        """
        Standard dictionary methods.
        """
    def __iter__(self) -> Incomplete:
        """
        A BTree object can be iterated over directly (similar to a dictionary)
        to get access to all keys in order.
        """
    def keys(self, start_key, end_key, flags: Optional[Any] = ...) -> Incomplete:
        """
        These methods are similar to standard dictionary methods, but also can
        take optional parameters to iterate over a key sub-range, instead of
        the entire database. Note that for all 3 methods, *start_key* and
        *end_key* arguments represent key values. For example, `values()`
        method will iterate over values corresponding to they key range
        given. None values for *start_key* means "from the first key", no
        *end_key* or its value of None means "until the end of database".
        By default, range is inclusive of *start_key* and exclusive of
        *end_key*, you can include *end_key* in iteration by passing *flags*
        of `btree.INCL`. You can iterate in descending key direction
        by passing *flags* of `btree.DESC`. The flags values can be ORed
        together.
        """
    def values(self, start_key, end_key, flags: Optional[Any] = ...) -> Incomplete:
        """
        These methods are similar to standard dictionary methods, but also can
        take optional parameters to iterate over a key sub-range, instead of
        the entire database. Note that for all 3 methods, *start_key* and
        *end_key* arguments represent key values. For example, `values()`
        method will iterate over values corresponding to they key range
        given. None values for *start_key* means "from the first key", no
        *end_key* or its value of None means "until the end of database".
        By default, range is inclusive of *start_key* and exclusive of
        *end_key*, you can include *end_key* in iteration by passing *flags*
        of `btree.INCL`. You can iterate in descending key direction
        by passing *flags* of `btree.DESC`. The flags values can be ORed
        together.
        """
    def items(self, start_key, end_key, flags: Optional[Any] = ...) -> Incomplete:
        """
        These methods are similar to standard dictionary methods, but also can
        take optional parameters to iterate over a key sub-range, instead of
        the entire database. Note that for all 3 methods, *start_key* and
        *end_key* arguments represent key values. For example, `values()`
        method will iterate over values corresponding to they key range
        given. None values for *start_key* means "from the first key", no
        *end_key* or its value of None means "until the end of database".
        By default, range is inclusive of *start_key* and exclusive of
        *end_key*, you can include *end_key* in iteration by passing *flags*
        of `btree.INCL`. You can iterate in descending key direction
        by passing *flags* of `btree.DESC`. The flags values can be ORed
        together.
        """

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
