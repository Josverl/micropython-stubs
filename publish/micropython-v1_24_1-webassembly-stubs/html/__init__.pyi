from _typeshed import Incomplete

_escape_map: Incomplete
_escape_map_full: Incomplete

def escape(s, quote: bool = True):
    """
    Replace special characters "&", "<" and ">" to HTML-safe sequences.
    If the optional flag quote is true (the default), the quotation mark
    characters, both double quote (") and single quote (\') characters are also
    translated.
    """
