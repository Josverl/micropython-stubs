A fairly pointless function:

.. code-block:: python

  import sys

  def write_message(filename, message):
      with open(filename, 'w') as target:
          target.write(message)

Now we can use a doctest REPL to show it in action:

>>> write_message('test.txt', 'is this thing on?')
>>> with open('test.txt') as source:
...     print(source.read())
is this thing on?
