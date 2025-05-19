(pyproject-config)=
# Configuration using pyproject.toml


## Configuration using pyproject.toml with stubs in a `typings` folder

File: `pyproject.toml`
```toml
[project]
name = "my-micropython-project"
version = "0.1.0"

[project.optional-dependencies]
# install to folder typings
# uv pip install -r pyproject.toml --extra stubs --target typings 
stubs = [
  "micropython-esp32-stubs"
]


# ###################################################################
# pyright and pylance options:
# ###################################################################

[tool.pyright]
include = ["src"]
ignore = ["**/typings"]
exclude = [".*", "__*", "**/typings"]

typeCheckingMode = "basic"
stubPath = "typings"
typeshedPath = "typings"
pythonPlatform = "Linux"
pythonVersion = "3.8"

reportMissingModuleSource = "none"
reportUnnecessaryTypeIgnoreComment = "information"

# ###################################################################
# # mypy global options:
# ###################################################################
[tool.mypy]
platform = "linux"
python_version = "3.8"

mypy_path = "typings"
custom_typeshed_dir = "typings"
files = "*.py"
exclude = [
    "typings[\\/].*", # TOML basic string 
]

follow_imports = "silent"
follow_imports_for_stubs = true
no_site_packages = true
check_untyped_defs = true

```
