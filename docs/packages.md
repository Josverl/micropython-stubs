(mp_packages)=
# List of available packages

## Packages on PyPi

Overview of the published ports and boards.

```{include} modules_pypi_body.md
```

:::{note}

- PyPi transforms all names of the ports and boards to small-caps and kebab-case, (not snake_case).
- Not all possible ports/boards are published as I do not have access to hardware to create board-stubs for all ports and boards.
- Newly published stubs may show as 'not found', please [check PyPi directly](https://pypi.org/search/?q=micropython+-stubs&o=&c=Programming+Language+%3A%3A+Python+%3A%3A+Implementation+%3A%3A+MicroPython)
:::


## Packages on GitHub

The stubs for the preview version of the firmware are available on GitHub.
Note that installation from git can be a little slower than from PyPi as the entire repository is cloned by pip in order to install the package.

Apologies that the urls are long and complex due to the requirements by pip , and the folder naming conventions used in the repo.

```{include} modules_git_body.md
```


## List of current firmwares and all partial stubs

This includes stubs from the following MicroPython families: 

- [MicroPython](micropython-stubs)

- [Pycopy](pycopy-stubs)

- M5Stack

- EV3/Lego

- Loboris port (ESP32) - Available but no longer maintained
  
  and Micropython Modules: 

- All frozen MicroPython modules

- the [LVGL GUI libraries](https://github.com/lvgl/lv_binding_micropython)

- [ulab native modules](ulab-stubs)

An up-to-date list of all current Firmwares, ports and boards is listed on the [**Firmwares page**](all-stubs) 
