My Project
==========

Here is a function:

.. code-block: python

    def a_function(text: str) -> str:
        return f'a function called with {text}'

Let's see this function in use:

    >>> a_function('baz')
    'a function called with baz'


TODO: the Doctest fails because the code-block is executed on the MCU
      and the Doctest is executed on the host Python.

# The Doctest should be executed on the MCU as well.
