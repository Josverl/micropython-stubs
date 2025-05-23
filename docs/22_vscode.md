(vscode_config)=
(pylance_config)=
(pyright_config)=
# Configuring VSCode, Pylance or Pyright

VSCode `can use multiple static type checkers and linters such as : 
 - Pylance,
 - mypy
 - pylint

This page will focus on configuring Pylance and Pyright to use the MicroPython stubs.

Vscode has a flexible configuration system with settings that can be set at the user, workspace or folder level.
The settings can be stored in a `settings.json` file in the `.vscode` folder of the workspace or at a user level where they are shared across projects, but can be overridden if needed.
Most settings can be entered though the VSCode UX, a few need to directly entered into the `settings.json` file.
In this document I show the .json file configuration, but the same settings can (often) be entered in the UX.  

In addition Pyright can be configured using a `pyrightconfig.json` or `pyproject.toml` file in the root of the workspace folders.
Most, if not all, settings described below can be set via either method or combination of methods. You may need to look for the tool specific documentation to find the preferences in case of overlapping configurations though.

## Pyright configuration using pyproject.toml

Using pyproject.toml for configuration is the preferred way, as it can also be used for the configuration of other tools in the Python ecosystem, such as for configuration of multiple tools and the installation of the stubs.
See <project:#pyproject-config> for a sample.

## Install the stubs from PyPi.

You should install the micropython type-stubs locally into a `typings` folder or into the `.venv` folder of your project.
Both locations will work, but some paths need to be adjusted to your chosen install location.  

For details see <project:#install-stubs>

## vscode Configuration for Pylance.

### vscode: Install the Python and Pylance extensions.

1. Install the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) from the marketplace.
   The Python extension will automatically install the following extensions by default to provide the best Python development experience in VS Code:
   - [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance "https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance") - to provide performant Python language support
   - [Python Debugger](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy "https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy") - to provide a seamless debug experience with debugpy
   

### vscode: Set Pylance as the language Server.

Note: If you've previously set a language server and want to try Pylance, make sure you've set `"python.languageServer": "Default" or "Pylance"` in your settings.json file using the text editor, or using the Settings Editor UI. 

Example from `.vscode/settings.json`

```json
{
    "python.languageServer": "Pylance",
    "python.analysis.typeCheckingMode": "basic",
} 
```

### vscode: Select the correct Python environment.

If you have created a `.venv` make sure to also select it in VSCode using 
`F1, >Python: select interpreter` or the UX 
```{figure} https://raw.githubusercontent.com/microsoft/vscode-python/main/images/InterpreterSelectionZoom.gif
Select the Python interpreter in VSCode.
```

## vscode: Ignore 'could not be resolved from source'.

After installing the stubs you may see some warnings that the source code for some of the commonly used modules are not found: 

```
Import "machine" could not be resolved from source
Import "time" could not be resolved from source
Import "urequests" could not be resolved from source
```

This is because the packages do not include the source code, as it are stub-only packages. The stubs are still used , but the expectation is that the source files for the modules are also available. With MicroPython these are part of the firmware image, and not directly available as source files. Therefore it makes sense to ignore these warnings. 
To suppress these warnings add the following to your VSCode configuration.

File: `.vscode/settings.json`
```json
    "python.analysis.diagnosticSeverityOverrides": {
        "reportMissingModuleSource": "none"
    },
```

## vscode: Configure Pylance to read MicroPython stdlib stubs.

Pylance (and Pyright) do not by default allow you to override the stdlib stubs.
This is possible but needs to be configured explicitly in the settings.

The VSCode configuration for this is shown below.

File: `.vscode/settings.json`
```json
{
    "python.analysis.typeshedPaths": [
        ".venv/Lib/site-packages",
        "typings"
    ],
}
```

The `python.analysis.typeshedPaths` setting is a list of paths to search for typeshed stubs. *Only the first path* in the list is used to resolve the stubs for a module. If the stubs are not found in the first path, the included stdlib is used. 
The default value is `["typings"]`.

:::{note}

If you right-click on a MicroPython stdlib module name in VScode, there are a few options to navigate to the (type) definition of the module.

* *Go to **Type** Definition*, will take you to the stub file in the `typings` folder, that should be a MicroPython stub.
* *Go to Definition*, will take you to a `.py` source file , which is a CPython stdlib module. ( not what you may expect)

:::

## VSCode: Sample workspace configuration file.

VSCode allows the configuration to be set on ***workspace*** , folder or *user* level. I prefer setting it per workspace or folder as that allows different settings for different projects, but you could do either.

The below configuration combines the settings described in the above sections: 
* Enable Pylance and set basic checking
* Suppress warnings about missing source code
* Configure Pylance to read MicroPython stdlib stubs

File: `.vscode/settings.json`
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
}
```

## pylance/pyright: Using pyproject.toml

One of the simplest ways to configure the VSCode Python add-ins is to create a pyproject.toml file and add the relevant configuration to that.


The use of a pyproject.toml file has the advantage that the same configuration can be used by the pyright command line tool, for instance as part of a CI/CD pipeline.

## Most Relevant settings

A short list of the most relevant settings for Pylance and Pyright and recommended values for each.
All settings for both Pylance and Pyright are documented in [Pyright Configuration](https://github.com/microsoft/pyright/blob/main/docs/configuration.md)
Most of these settings are also documented as part of the vscode documentation for the Python extension, but the Pyright documentation is more complete.

| Setting | Description | Recommended value | Info |
| ---| --- | --- | --- |
| `typeCheckingMode` | The level of type checking to perform. | `basic` | Use`basic` or `standard`.|
| `stubPath` | Path to the MicroPython stubs. | `"typings"` | Default is `typings`, only needed if you have a different path. | 
| `extraPaths` | Additional stubs. | `[]` | used by [MicroPico](project:#micropico) 
| `pythonVersion` | The version of Python syntax to use. | - | [](pythonVersion) |
| `typeshedPaths` | (List of) Path to the MicroPython stdlib stubs. (Only the first path is used) | `[".venv/Lib/site-packages"]` or `["typings"]` | Needed to override the stdlib stubs. |
| `diagnosticSeverityOverrides` | Ignore missing source warnings. | `{"reportMissingModuleSource": "none"}` | [Diag settings](https://github.com/microsoft/pyright/blob/main/docs/configuration.md#type-check-diagnostics-settings)


(pythonVersion)=
#### pythonVersion
MicroPython is based on Python 3.4, but also has [some features from newer Python versions](https://docs.micropython.org/en/latest/genrst/index.html). I have found little benefit in changing the `pythonVersion` setting from the default. If you do, please let me know.




[Pylance]: https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance
