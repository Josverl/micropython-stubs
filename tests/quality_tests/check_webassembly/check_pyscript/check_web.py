# PyScript 2026.7.3: current web element, collection, class, style, and options contracts.

from pyscript.web import page

# Print all the child elements of the document's head.
print(page.head.children)
# Find all the paragraphs in the DOM.
paragraphs = page.find("p")
# Square brackets look up an element by id.
paragraph = page["paragraph-id"]
if paragraph is not None:
    print(paragraph.children)

# PyScript 2026.3.1: update_all delegates classes and style to Element.update.
paragraphs.update_all(classes="checked", style={"color": "green"})


from pyscript.web import page, div, select, option, button, span, br


page.append(
    div(
        div("Hello!", classes="a-css-class", id="hello"),
        select(
            option("apple", value=1),
            option("pear", value=2),
            option("orange", value=3),
        ),
        div(
            button(span("Hello! "), span("World!"), id="my-button"),
            br(),
            button("Click me!"),
            classes=["css-class1", "css-class2"],
            style={"background-color": "red"},
        ),
        div(
            children=[
                button(children=[span("Hello! "), span("Again!")], id="another-button"),
                br(),
                button("b"),
            ],
            classes=["css-class1", "css-class2"],
        ),
    )
)


from pyscript.web import page, div, p


my_div = div()
my_div.style["background-color"] = "red"
del my_div.style["background-color"]
my_div.classes.add("a-css-class")
my_div.classes.discard("optional-class")

my_p = p()
my_p.content = "This is a paragraph."

my_div.append(my_p)

first_child = my_div[0]
child_slice = my_div[:1]
found_child = my_div["paragraph-id"]

choices = select()
choices.options.add(value="mpy", text="MicroPython")
selected_option = choices.options.selected
print(first_child, child_slice, found_child, selected_option)
