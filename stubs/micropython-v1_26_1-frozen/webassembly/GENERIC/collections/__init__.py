# Micropython v1.26.1 frozen stubs
# Replace built-in collections module.
from ucollections import *

# Provide optional dependencies (which may be installed separately).
try:
    from .defaultdict import defaultdict
except ImportError:
    pass


class MutableMapping:
    pass
