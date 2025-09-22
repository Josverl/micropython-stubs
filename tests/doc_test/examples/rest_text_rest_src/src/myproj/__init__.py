"""
This package foo's stuff so it bars.

:data:`SEED` is normally random, but if you like you
can set it as follows:

.. code-block:: python

    import myproj
    myproj.SEED = 0.2
"""
import random

SEED: float = random.random()


def foo(text: str):
    """
    Put some ``bar`` on your ``foo``!
    >>> foo('stuff')
    'stuff bar bar'

    """
    return text+int(SEED*10)*' bar'
