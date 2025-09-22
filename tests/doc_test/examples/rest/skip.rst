.. skip: next

This would be wrong but is skipped:

>>> 1 == 2
True

This is pseudo-code:

.. skip: start

>>> foo = ...
>>> foo(..)

.. skip: end

>>> import sys

This will only work on Python 3:

.. skip: next if(__import__('sys').version_info < (4, 0), reason="python 3 only")

>>> repr(b'foo')
"b'foo'"

This will test MicroPython-specific condition:

.. skip: next if(__import__('sys').implementation.name != 'micropython', reason="MicroPython only")

>>> import micropython
>>> micropython.const(42)
42

This example is not yet working, but I wanted to be reminded:

.. skip: next "not yet working"

>>> 1.1 == 1.11
True

And here we can see some pseudo-code that will work in a future release:

.. skip: start "Fix in v5"

>>> helper = Framework().make_helper()
>>> helper.describe(...)

.. skip: end

