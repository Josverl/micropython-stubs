# PyScript 2026.7.3: root window proxy contract.

from pyscript import window


def handle_click(event):
    """
    Simply log the click event to the browser's console.
    """
    window.console.log(event)
