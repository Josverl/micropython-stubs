(mypy_config)=
# Type Checking with MyPy

Mypy is an optional static type checker for Python that aims to combine the benefits of dynamic (or "duck") typing and static typing. Mypy combines the expressive power and convenience of Python with a powerful type system and compile-time type checking.



## MyPy and stub-only packages installed in a `typings` folder

MyPy can be configured to use stubs located in a folder, usually a folder named `typings`
for details see: https://mypy.readthedocs.io/en/stable/stubs.html

Although the documentation also states that stub-only packages [cannot be located though a provided path](https://mypy.readthedocs.io/en/stable/installed_packages.html#installed-packages) this seems to work on initial testing, with a few workarounds needed.
(possibly the MyPy detection or definition of a stub-only package does not flag the MicroPython-stub packages as stub-only packages)

Therefore after installing the stubs into a `typings` folder, MyPy can be configured to use the stubs by setting the `MYPYPATH` environment variable to the path of the `typings` folder.

Linux/MacOS:

```bash
export MYPYPATH=./typings
```

Windows:

```pwsh
$env:MYPYPATH="./typings"
```

### Workarounds for some MyPy warnings and errors

```
mypy: "typings\sys.pyi" shadows library module "sys"
note: A user-defined top-level module with name "sys" is not supported
```

Partial workaround:

```bash
del typings/os.pyi
del typings/sys.pyi
```



### MyPy and stub-only packages installed in a virtual environment

MyPy should automatically detect and use all MicroPython packages installed in a virtual environment as they follow the PEP-561 standard for stub-only packages.
However MyPy fails to detect the stubs installed in a `venv` :-(

This will need to be investigated in more detail, and possibly the packaging format needs to be adjusted.
