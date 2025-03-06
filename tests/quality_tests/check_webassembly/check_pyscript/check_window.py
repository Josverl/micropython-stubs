# https://docs.pyscript.net/2025.2.3/api/#html-attributes
# This classic pattern of coding (inline event handlers) is no longer considered good practice in web development circles.

from pyscript import window 


def handle_click(event):
    """
    Simply log the click event to the browser's console.
    """
    window.console.log(event)    
