Sample Documentation
====================

Let's put something in the Sybil document's namespace:

.. invisible-code-block: python

  remember_me = b'see how namespaces work?'

Suppose we define a function, convoluted and pointless but shows stuff nicely:

.. code-block:: python

  import sys

  def prefix_and_print(message):
      print('prefix:', message.decode('ascii'))

Now we can use a doctest REPL to show it in action:

>>> prefix_and_print(remember_me)
prefix: see how namespaces work?

The namespace carries across from example to example, no matter what parser:

>>> remember_me
b'see how namespaces work?'
