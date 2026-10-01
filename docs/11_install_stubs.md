(install-stubs)=
# Install the micropython-stubs

There are two main ways to install the stubs into your environment:

## Quick setup script (`uv run`)

Use the repository setup script to create a `pyproject.toml` using the test template and install stubs into `typings`:

```bash
uv run https://raw.githubusercontent.com/Josverl/micropython-stubs/refs/heads/main/setup_micropython_stubs.py
```


## 1: Install to `typings` folder

Store the stubs in a folder in your repo or somewhere else on a disk, the default for this is a `typings` folder in the root of your project.
   The advantage is that this method works without even needing Python (the full CPython) on your computer.
   Also if you have multiple projects using the same version of the same stubs , you can use symlinks to save a few cents on hard drive space.
   Removing the stubs is simple - you can just delete the typings folder.

### Install the stubs in a `typings` folder within your project:
   
   ```bash
   pip install -U micropython-<port>[-<board>]stubs --no-user --target ./typings
   ```

### Enjoy enhanced code completion and type checking!

## Migrating to the canonical `stdlib/` layout

Recent board and port packages install MicroPython modules that shadow CPython
standard-library modules once, under `stdlib/`. They are no longer duplicated at
the root of the install target.

When upgrading from a package that used the flat layout, remove the existing
target before reinstalling. `pip --target` and `uv pip --target` overwrite files
but do not remove obsolete flat stubs:

```bash
# Remove only the dedicated stub target, then recreate it.
rm -rf typings
python -m pip install -U micropython-<port>[-<board>]-stubs --no-user --target typings
```

On Windows PowerShell, replace the removal command with:

```powershell
Remove-Item -LiteralPath .\typings -Recurse -Force
```

Configure each checker with the install-target root, not with a copied set of
flat compatibility files:

```toml
[tool.pyright]
stubPath = "typings"
typeshedPath = "typings"

[tool.mypy]
mypy_path = "typings"
custom_typeshed_dir = "typings"

[tool.zuban]
mypy_path = ["typings", "typings/stdlib"]

[tool.ty.environment]
extra-paths = ["typings"]
typeshed = "typings"
```

For Pylance, use the equivalent workspace settings:

```json
{
    "python.analysis.stubPath": "typings",
    "python.analysis.typeshedPaths": ["typings"]
}
```

The package layout intentionally has no flat-plus-`stdlib/` compatibility mode.
If an older tool cannot read the configured stdlib location, keep using the
previous package release until that tool can be configured, rather than copying
the shadow modules and creating two competing definitions.

## 2: Install in a Virtual Environment

Install the stubs into your active python virtual environment (venv) 
If you use Python on your host computer and use venv (or virtualenv) you can install the stubs into that same venv.
most IDEs and tools will use the stubs in that environment when they detect it. 
Removing the stubs is done using `pip uninstall ...` 


A Python virtual environment keeps dependencies separate for different projects.
To create and activate a virtual environment in your project directory, follow these steps:

(activate_venv)=
### Activate your virtual environment.

### For Linux/Mac:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### For Windows:

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### Install the stubs in the virtual environment:

```bash

1. ```bash
   pip install -U micropython-<port>[-<board>]stubs --no-user
   ```

```bash
pip install -U micropython-stm32-stubs --target typings --no-user

# Install stubs for a specific version.
pip install -U micropython-esp32-stubs==1.20.0.* --target typings --no-user

# Install stubs for a specific board.
pip install -U micropython-rp2-pico_w-stubs --target typings --no-user
```
See [](project:#install-stubs) for more details and examples.

<!-- :::{admonition} **Requirements File** -->
:::{tip} 
**Requirements File**

Consider adding a `requirements-dev.txt` file to your project with the specified stubs. It’ll help keep your development environment consistent.


```
#requirements-dev.txt
micropython-esp32-stubs~=1.23.0
```

Then install the stubs with `pip install -r requirements-dev.txt --target typings`.	

:::
