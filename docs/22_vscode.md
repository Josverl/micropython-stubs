# VSCode and Pylance or Pyright

VSCode  uses Pylance, and optionally a linter such as pylint or mypy.

## Install the stubs from PyPi.

`pip install -U micropython-<port>-stubs` 
For details see [Using stubs](20_using.md)

## 

## Configure VSCode & Pylance.



### Install the Python and Pylance extensions.

1. Install the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) from the marketplace.
   The Python extension will automatically install the following extensions by default to provide the best Python development experience in VS Code:
   - [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance "https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance") - to provide performant Python language support
   - [Python Debugger](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy "https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy") - to provide a seamless debug experience with debugpy
   
   

### Set Pylance as the language Server.

Note: If you've previously set a language server and want to try Pylance, make sure you've set `"python.languageServer": "Default" or "Pylance"` in your settings.json file using the text editor, or using the Settings Editor UI. 

Example from `.vscode/settings.json`

```json
{
    "python.languageServer": "Pylance",
    "python.analysis.typeCheckingMode": "basic",
} 
```

> [Note]
> 
> Note that the same options from the .toml configuration can also be set in the VSCode configuration for Python/Pylance.

### Select the correct Python environment.

If you have created a `venv` make sure to also select it in VSCode using 
`F1, >Python: select interpreter` or the UX 

![](https://raw.githubusercontent.com/microsoft/vscode-python/main/images/InterpreterSelectionZoom.gif)



## Using pyproject.toml

One of the simplest ways to configure the VSCode Python add-ins is to create a pyproject.toml file and add the relevant configuration to that.



`./pyproject.toml`

```toml
[tool.pyright]
include = ["src"]
ignore = ["**/typings"]
exclude = [
    ".*",
    "__*",
    "**/typings",
]

typeCheckingMode = "basic"
stubPath = "typings"
typeshedPath = "typings"
pythonPlatform = "Linux"

reportMissingModuleSource = "none"
reportUnnecessaryTypeIgnoreComment = "error"
```

This has the added advantage that the same configuration ca be used by the pyright command line tool if you choose to use it.



### 

## Add configuration to suppress unneeded warnings.

After installing the stubs you may see some warnings that the source code to referenced modules is not found. 

```
Import "machine" could not be resolved from source
Import "time" could not be resolved from source
Import "urequests" could not be resolved from source
```

This is because the packages do not include the source code, as it are stub-only packages. 

To supress these warnings add the following to your VSCode configuration.

`.vscode/settings.json`

```json
    "python.analysis.diagnosticSeverityOverrides": {
        "reportMissingModuleSource": "none"
    },
```

## Configure Pylance to read MicroPython stdlib stubs.

Pylance and Pyright do not by default allow you to override the stdlib stubs.
This is possible but needs to be configured explicitly in the settings.

the VSCode configuration for this is shown below.

`.vscode/settings.json`

```json
{
    "python.analysis.typeshedPaths": [
        ".venv/Lib/site-packages",
        "typings"
    ],
}
```

The diagram below shows the sequence of checks that Pylance/Pyright does to resolve the stubs for a module.
with the above configuration it will first check the `venv` or the `typings` folder and then look for the stdlib stubs in these folders.
Without the configuration it will only look for the stdlib stubs in the typeshed stubs that are shipped with Pyright.

## Sample VSCode configuration file.



VSCode allows the configuration to be set on ***workspace*** , folder or *user* level. I prefer setting it per workspace or folder as that allows different settings for different projects, but you could do either.





The below configuration combines the above settings.

* Enable Pylance and set basic checking
* Suppress warnings about missing source code
* Configure Pylance to read MicroPython stdlib stubs

`.vscode/settings.json`

```json
{
    "python.languageServer": "Pylance",
    "python.analysis.typeCheckingMode": "basic",
    "python.analysis.diagnosticSeverityOverrides": {
        "reportMissingModuleSource": "none"
    },
    "python.analysis.typeshedPaths": [
        ".venv/Lib/site-packages"
    ],
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
}
```

[Pylance]: https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance
