"""
Pyscript 2025.2.3 type-stub.
see: https://docs.pyscript.net/2025.2.3/api/
"""

_MIME_METHODS = ...
_MIME_RENDERERS = ...

class HTML:
    """
    Wrap a string so that display() can render it as plain HTML
    """

    def __init__(self, html) -> None: ...

def display(*values, target=..., append=...) -> None:
    """
    A function used to display content. The function is intelligent enough to introspect the object[s] it is passed and work out how to correctly
    display the object[s] in the web page based on the following mime types::
        - text/plain to show the content as text
        - text/html to show the content as HTML
        - image/png to show the content as <img>
        - image/jpeg to show the content as <img>
        - image/svg+xml to show the content as <svg>
        - application/json to show the content as JSON
        - application/javascript to put the content in <script> (discouraged)


    The display function takes a list of *values as its first argument, and has two optional named arguments::
        - target=None - the DOM element into which the content should be placed. If not specified, the target will use the current_script() returned id and populate the related dedicated node to show the content.
        - append=True - a flag to indicate if the output is going to be appended to the target.
    """
    ...
