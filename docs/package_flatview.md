(flatview)=
# Overview of all modules

A simple way to discover if stubs for a specific module have been published is to check the .
This offers a searchable and exportable view of the all_modules.json file that is automatically updated when new stubs are published.

:::{figure} img/flatgithub.png
[view of all modules](https://flatgithub.com/Josverl/micropython-stubs?filename=all_modules.json)

View the list of all modules that are currently available as stubs.
This view is created using the [Flat Viewer](https://githubnext.com/projects/flat-data) project.
:::

:::{note}

This list does not precisely reflect which modules are available on what firmware, as a few modules are omitted from the distribution packages to avoid conflicts with CPython.

For instance the documentation on the `re` module is included in the micropython, but the documentation is not detailed enough to generate a working stub for it.
 <!--TODO: add list of excluded modules  -->
:::


<!-- 
TODO: 

- currently not yet automatically updated
- add links to PyPi 
 -->
