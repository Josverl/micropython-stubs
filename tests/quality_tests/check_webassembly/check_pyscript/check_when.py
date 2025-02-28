# samples from: https://docs.pyscript.net/2025.2.3/api/#pyscriptwhen

# pyscript.when 

from pyscript import when
from pyscript.web import page 


btn = page["#my-button"]

@when("click", btn)
def my_button_click_handler(event):
    print("The button has been clicked!")


from pyscript import when, display


@when("click", "#my_button")
def click_handler(event):
    """
    Event handlers get an event object representing the activity that raised
    them.
    """
    display("I've been clicked!")

### Or manually setting handler without a decorator
when("click", "#my-button", handler=click_handler)
