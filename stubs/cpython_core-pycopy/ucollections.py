import collections
from collections import OrderedDict, namedtuple


class deque:

    def __init__(self, iterable, maxlen, flags=0):
        assert iterable == ()
        self.maxlen = maxlen
        self.flags = flags
        self.d = collections.deque(iterable, maxlen)

    def __len__(self):
        return len(self.d)

    def append(self, x):
        if self.flags & 1:
            if len(self.d) == self.maxlen:
                raise IndexError
        self.d.append(x)

    def popleft(self):
        return self.d.popleft()
