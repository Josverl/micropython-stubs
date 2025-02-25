# samples from: https://docs.pyscript.net/2025.2.3/user-guide/dom/#pyscriptweb
# pyscript.web

# pyscript.web.page

from pyscript.web import page

# Print all the child elements of the document's head.
print(page.head.children)
# Find all the paragraphs in the DOM.
paragraphs = page.find("p")
# Or use square brackets.
paragraphs = page["p"]


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
            style={"background-color": "red"}
        ),
        div(
            children=[
                button(
                    children=[
                        span("Hello! "),
                        span("Again!")
                    ],
                    id="another-button"
                ),
                br(),
                button("b"),
            ],
            classes=["css-class1", "css-class2"]
        )
    )
)


from pyscript.web import page, div, p 


my_div = div()
my_div.style["background-color"] = "red"
my_div.classes.add("a-css-class")

my_p = p()
my_p.content = "This is a paragraph."

my_div.append(my_p)

