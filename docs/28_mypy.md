# MyPy - limited functionality
This section is preliminary and needs to be expanded.
While MyPy used to work quite well with the .PY stubs, it is now not working anymore now that the stubs are type-only stubs.

## MyPy and stub-only packages installed in a virtual environment

MyPy should automatically detect and use all Micropython packages installed in a virtual environment as they follow the PEP-561 standard for stub-only packages.
However MyPy fails to detect the stubs installed in a `venv` :-( 

This will need to be investigated in more detail, and possibly an issue to be raised with MyPy.
In addition it has  not been tested if MyPy is able to detect and allow an override by the MicroPython stdlib packages.

## MyPy and stub-only packages installed in a `typings` folder
MyPy can be configured to use stubs located in a folder, usually a folder named `typings`
for details see: https://mypy.readthedocs.io/en/stable/stubs.html

Although the documentation also states that stub-only packages [cannot be located though a provided path](https://mypy.readthedocs.io/en/stable/installed_packages.html#installed-packages) this seems to work on intitial testing, with a few workarounds neede.
(possibly the MyPy detecttion or definiton of a stub-only package does not flag the microspython-stub packages as stub-only packages)

Therefore after installing the stubs into a `typings` folder, MyPy can be configured to use the stubs by setting the `MYPYPATH` environment variable to the path of the `typings` folder.

Linux/MacOS:
``` bash
export MYPYPATH=./typings
```
Windows:
```pwsh
$env:MYPYPATH="./typings"
```

### Workarounds for some mypy warnings and errors 

```
mypy: "typings\sys.pyi" shadows library module "sys"
note: A user-defined top-level module with name "sys" is not supported
```

Partial workaround:
``` bash
del typings/os.pyi
del typings/sys.pyi
```
