# Micropython v1.26.1 frozen stubs
# This module provides a backwards-compatble import for `urequests`.
# It lazy-loads from `requests` without duplicating its globals dict.


def __getattr__(attr):
    import requests

    return getattr(requests, attr)
