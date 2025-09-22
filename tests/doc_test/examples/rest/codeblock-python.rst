Here's a function:

.. code-block:: python

  import sys

  def prefix(message):
      return 'prefix:'+message

This won't show up but will verify it works:

.. invisible-code-block: python

  assert prefix('foo') == 'prefix:foo'
