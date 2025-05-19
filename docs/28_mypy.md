(mypy_config)=
# Type Checking with MyPy

Mypy is an optional static type checker for Python that aims to combine the benefits of dynamic (or "duck") typing and static typing. Mypy combines the expressive power and convenience of Python with a powerful type system and compile-time type checking.


## MyPy and stub-only packages installed in a `typings` folder

MyPy can be configured to use stubs located in a folder, usually a folder named `typings`
for details see: https://mypy.readthedocs.io/en/stable/stubs.html

As of version *v1.24.1.post2*, the stubs have been adjusted to be compatible with MyPy and can be installed in a `typings` folder.

There are several configuration options required to make this work, I prefer to add them all in a pyproject.toml file, but they can likely also be added in a `mypy.ini` file or though command line options or environment settings.

### mypy configuration using pyproject.toml

Using pyproject.toml for configuration is the preferred way, as it can also be used for the configuration of other tools in the Python ecosystem, such as for configuration of multiple tools and the installation of the stubs.
See <project:#pyproject-config> for an example.

### MyPy and stub-only packages installed in a virtual environment

If MyPy is installed in a virtual environment, it can detect and use MicroPython packages installed in that environment.
I found that I still need to specify the paths to get mypy to work in this configuration

*`pyproject.toml` with stub installed in a virtual environment `.venv`:*
```
[tool.mypy]
platform = "linux"
mypy_path = ".venv/Lib/site-packages"
custom_typeshed_dir = ".venv/Lib/site-packages" # allow mypy to use micropython-stdlib
files = "src/*.py"
follow_imports = "silent"
```
