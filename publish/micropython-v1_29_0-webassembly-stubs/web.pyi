"""Pythonic DOM API documented by PyScript 2026.7.3."""

# Copyright (c) 2020-2025 Jos Verlinde
# MIT Licensed

from __future__ import annotations

from typing import Any, Iterable, Iterator, Mapping, overload

from _typeshed import Incomplete
from pyscript import Event, document
from pyscript.ffi import create_proxy

page: Page = ...
CONTAINER_TAGS: list[str]
VOID_TAGS: list[str]

class Element:
    element_classes_by_tag_name: dict[str, type[Element]]
    @classmethod
    def get_tag_name(cls) -> str:
        """Return the HTML tag name for the class.

        For classes that have a trailing underscore (because they clash with a Python
        keyword or built-in), we remove it to get the tag name. e.g. for the `input_`
        class, the tag name is `input`.

        """
        ...

    @classmethod
    def register_element_classes(cls, element_classes: Iterable[type[Element]]) -> None:
        """Register an iterable of element classes."""
        ...

    @classmethod
    def unregister_element_classes(cls, element_classes: Iterable[type[Element]]) -> None:
        """Unregister an iterable of element classes."""
        ...

    @classmethod
    def wrap_dom_element(cls, dom_element: Any) -> Element:
        """Wrap an existing DOM element in an instance of a subclass of `Element`.

        We look up the `Element` subclass by the DOM element's tag name. For any unknown
        elements (custom tags etc.) use *this* class (`Element`).
        """
        ...

    def __init__(
        self,
        dom_element: Any = None,
        classes: str | Iterable[str] | None = None,
        style: Mapping[str, object] | None = None,
        **kwargs: Any,
    ) -> None:
        """Create a new, or wrap an existing DOM element.

        If `dom_element` is None we are being called to *create* a new element.
        Otherwise, we are being called to *wrap* an existing DOM element.
        """
        ...

    def __eq__(self, obj: object) -> bool:
        """Check for equality by comparing the underlying DOM element."""
        ...

    @overload
    def __getitem__(self, key: int) -> Element: ...
    @overload
    def __getitem__(self, key: slice) -> ElementCollection: ...
    @overload
    def __getitem__(self, key: str) -> Element | None:
        """Get an item within the element's children.

        If `key` is an integer or a slice we use it to index/slice the element's
        children. Otherwise, we use `key` as a query selector.
        """
        ...

    def __getattr__(self, name: str) -> Any:
        """
        Get an attribute from the element.

        If the attribute is an event (e.g. "on_click"), we wrap it in an `Event`
        instance and return that. Otherwise, we return the attribute from the
        underlying DOM element.
        """
        ...

    def __setattr__(self, name: str, value: object) -> None: ...
    def get_event(self, name: str) -> Event:
        """
        Get an `Event` instance for the specified event name.
        """
        ...

    @property
    def children(self) -> ElementCollection:
        """Return the element's children as an `ElementCollection`."""
        ...

    @property
    def classes(self) -> Classes:
        """Return the element's `classList` as a `Classes` instance."""
        ...

    @property
    def parent(self) -> Element | None:
        """Return the element's `parent `Element`."""
        ...

    @property
    def style(self) -> Style:
        """Return the element's `style` attribute as a `Style` instance."""
        ...

    def append(self, *items: Any) -> None:
        """Append the specified items to the element."""
        ...

    def clone(self, clone_id: str | None = None) -> Element:
        """Make a clone of the element (clones the underlying DOM object too)."""
        ...

    def find(self, selector: str) -> ElementCollection:
        """Find all elements that match the specified selector.

        Return the results as a (possibly empty) `ElementCollection`.
        """
        ...

    def show_me(self) -> None:
        """Convenience method for 'element.scrollIntoView()'."""
        ...

    def update(
        self,
        classes: str | Iterable[str] | None = None,
        style: Mapping[str, object] | None = None,
        **kwargs: Any,
    ) -> None:
        """Update the element with the specified classes, styles, and DOM properties."""
        ...

class Classes(set[str]):
    """A set-like interface to an element's `classList`."""

    def __init__(self, element: Element) -> None: ...
    def add(self, class_name: str) -> None:
        """Add one or more space-separated classes to the element."""
        ...

    def remove(self, class_name: str) -> None:
        """Remove one or more space-separated classes from the element."""
        ...

    def discard(self, class_name: str) -> None:
        """Discard one or more space-separated classes from the element."""
        ...

    def clear(self) -> None: ...

class HasOptions:
    """Mix-in for elements that have an options attribute.

    The elements that support options are: <datalist>, <optgroup>, and <select>.
    """

    @property
    def options(self) -> Options:
        """Return the element's options as an `Options"""
        ...

class Options:
    """This class represents the <option>s of a <datalist>, <optgroup> or <select>.

    It allows access to add and remove <option>s by using the `add`, `remove` and
    `clear` methods.
    """

    def __init__(self, element: Element) -> None: ...
    def __getitem__(self, key: int) -> Element: ...
    def __iter__(self) -> Iterator[Element]: ...
    def __len__(self) -> int: ...
    def __repr__(self) -> str: ...
    @property
    def options(self) -> list[Element]:
        """Return the list of options."""
        ...

    @property
    def selected(self) -> Element:
        """Return the selected option."""
        ...

    def add(
        self,
        value: object = None,
        html: str | None = None,
        text: str | None = None,
        before: Element | int | None = None,
        **kwargs: Any,
    ) -> None:
        """Add a new option to the element"""
        ...

    def clear(self) -> None:
        """Remove all options."""
        ...

    def remove(self, index: int) -> None:
        """Remove the option at the specified index."""
        ...

class Style(dict[str, object]):
    """A dict-like interface to an element's `style` attribute."""

    def __init__(self, element: Element) -> None: ...
    def __setitem__(self, key: str, value: object) -> None: ...
    def __delitem__(self, key: str) -> None: ...

class ContainerElement(Element):
    """Base class for elements that can contain other elements."""

    def __init__(
        self,
        *args: Any,
        children: Iterable[Any] | None = None,
        dom_element: Any = None,
        style: Mapping[str, object] | None = None,
        classes: str | Iterable[str] | None = None,
        **kwargs: Any,
    ) -> None: ...
    def __iter__(self) -> Iterator[Element]: ...

class ElementCollection:
    @classmethod
    def wrap_dom_elements(cls, dom_elements: Iterable[Any]) -> ElementCollection:
        """Wrap an iterable of dom_elements in an `ElementCollection`."""
        ...

    def __init__(self, elements: list[Element]) -> None: ...
    def __eq__(self, obj: object) -> bool:
        """Check for equality by comparing the underlying DOM elements."""
        ...

    @overload
    def __getitem__(self, key: int) -> Element: ...
    @overload
    def __getitem__(self, key: slice) -> ElementCollection: ...
    @overload
    def __getitem__(self, key: str) -> Element | None:
        """Get an item in the collection.

        If `key` is an integer or a slice we use it to index/slice the collection.
        Otherwise, we use `key` as a query selector.
        """
        ...

    def __iter__(self) -> Iterator[Element]: ...
    def __len__(self) -> int: ...
    def __repr__(self) -> str: ...
    @property
    def elements(self) -> list[Element]:
        """Return the elements in the collection as a list."""
        ...

    def find(self, selector: str) -> ElementCollection:
        """Find all elements that match the specified selector.

        Return the results as a (possibly empty) `ElementCollection`.
        """
        ...

    def update_all(
        self,
        classes: str | Iterable[str] | None = None,
        style: Mapping[str, object] | None = None,
        **kwargs: Any,
    ) -> None: ...

class a(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a"""

    ...

class abbr(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/abbr"""

    ...

class address(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/address"""

    ...

class area(Element):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/area"""

    ...

class article(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/article"""

    ...

class aside(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/aside"""

    ...

class audio(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/audio"""

    ...

class b(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/b"""

    ...

class base(Element):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/base"""

    ...

class blockquote(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/blockquote"""

    ...

class body(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/body"""

    ...

class br(Element):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/br"""

    ...

class button(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/button"""

    ...

class canvas(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/canvas"""

    def download(self, filename: str = ...) -> None:
        """Download the current element with the filename provided in input.

        Inputs:
            * filename (str): name of the file being downloaded

        Output:
            None
        """
        ...

    def draw(self, what, width=..., height=...) -> None:
        """Draw `what` on the current element

        Inputs:

            * what (canvas image source): An element to draw into the context. The
                specification permits any canvas image source, specifically, an
                HTMLImageElement, an SVGImageElement, an HTMLVideoElement,
                an HTMLCanvasElement, an ImageBitmap, an OffscreenCanvas, or a
                VideoFrame.
        """
        ...

class caption(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/caption"""

    ...

class cite(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/cite"""

    ...

class code(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/code"""

    ...

class col(Element):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/col"""

    ...

class colgroup(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/colgroup"""

    ...

class data(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/data"""

    ...

class datalist(ContainerElement, HasOptions):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/datalist"""

    ...

class dd(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dd"""

    ...

class del_(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/del"""

    ...

class details(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/details"""

    ...

class dialog(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dialog"""

    ...

class div(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/div"""

    ...

class dl(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dl"""

    ...

class dt(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dt"""

    ...

class em(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/em"""

    ...

class embed(Element):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/embed"""

    ...

class fieldset(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/fieldset"""

    ...

class figcaption(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/figcaption"""

    ...

class figure(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/figure"""

    ...

class footer(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/footer"""

    ...

class form(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form"""

    ...

class h1(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/h1"""

    ...

class h2(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/h2"""

    ...

class h3(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/h3"""

    ...

class h4(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/h4"""

    ...

class h5(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/h5"""

    ...

class h6(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/h6"""

    ...

class head(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/head"""

    ...

class header(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/header"""

    ...

class hgroup(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/hgroup"""

    ...

class hr(Element):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/hr"""

    ...

class html(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/html"""

    ...

class i(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/i"""

    ...

class iframe(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe"""

    ...

class img(Element):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img"""

    ...

class input_(Element):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input"""

    ...

class ins(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ins"""

    ...

class kbd(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/kbd"""

    ...

class label(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/label"""

    ...

class legend(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/legend"""

    ...

class li(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/li"""

    ...

class link(Element):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/link"""

    ...

class main(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/main"""

    ...

class map_(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/map"""

    ...

class mark(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/mark"""

    ...

class menu(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/menu"""

    ...

class meta(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meta"""

    ...

class meter(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meter"""

    ...

class nav(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/nav"""

    ...

class object_(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/object"""

    ...

class ol(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ol"""

    ...

class optgroup(ContainerElement, HasOptions):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/optgroup"""

    ...

class option(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/option"""

    ...

class output(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/output"""

    ...

class p(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/p"""

    ...

class param(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/param"""

    ...

class picture(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/picture"""

    ...

class pre(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/pre"""

    ...

class progress(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/progress"""

    ...

class q(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/q"""

    ...

class s(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/s"""

    ...

class script(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script"""

    ...

class section(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/section"""

    ...

class select(ContainerElement, HasOptions):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/select"""

    ...

class small(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/small"""

    ...

class source(Element):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/source"""

    ...

class span(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/span"""

    ...

class strong(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/strong"""

    ...

class style(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/style"""

    ...

class sub(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/sub"""

    ...

class summary(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/summary"""

    ...

class sup(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/sup"""

    ...

class table(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/table"""

    ...

class tbody(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/tbody"""

    ...

class td(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/td"""

    ...

class template(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/template"""

    ...

class textarea(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/textarea"""

    ...

class tfoot(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/tfoot"""

    ...

class th(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/th"""

    ...

class thead(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/thead"""

    ...

class time(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/time"""

    ...

class title(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/title"""

    ...

class tr(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/tr"""

    ...

class track(Element):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/track"""

    ...

class u(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/u"""

    ...

class ul(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ul"""

    ...

class var(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/var"""

    ...

class video(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video"""

    def snap(self, to: Element | str = ..., width: int | None = ..., height: int | None = ...) -> canvas | Element:
        """
        Capture a snapshot (i.e. a single frame) of a video to a canvas.

        Inputs:

            * to: the canvas to save the video frame to (if None, one is created).
            * width: width of the snapshot (defaults to the video width).
            * height: height of the snapshot (defaults to the video height).

        Output:
            (Element) canvas element where the video frame snapshot was drawn into
        """
        ...

class wbr(ContainerElement):
    """Ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/wbr"""

    ...

class Page:
    """Represents the whole page."""

    def __init__(self) -> None: ...
    @property
    def html(self) -> Element: ...
    @property
    def head(self) -> Element: ...
    @property
    def body(self) -> Element: ...
    def __getitem__(self, key: str) -> Element | None:
        """Get an item on the page.

        We don't index/slice the page like we do with `Element` and `ElementCollection`
        as it is a bit muddier what the ideal behavior should be. Instead, we simply
        use this as a convenience method to `find` elements on the page.
        """
        ...

    @property
    def title(self) -> str:
        """Return the page title."""
        ...

    @title.setter
    def title(self, value) -> None:
        """Set the page title."""
        ...

    def append(self, *items) -> None:
        """Shortcut for `page.body.append`."""
        ...

    def find(self, selector) -> ElementCollection:
        """Find all elements that match the specified selector.

        Return the results as a (possibly empty) `ElementCollection`.
        """
        ...
