# Configure VSCode & Pylance to use the selected stub folders  
# VSCode 
VSCode uses Pylance, and optionally a linter suchc as pylint or mypy.

## Configure VSCode & Pylance to use the selected stub folders  
This instructs the VSCode Pylance to consider your libs folder and the stubs for static code evaluation.
VSCode allows this configuration to be set on **_workspace_** or _user_ level. I prefer setting it per workspace as that allows different settings for different projects, but you could do either.
     
The below configuration is [Pylance][] specific  
     
- use the {download}`samples/.VSCode/settings.json`  located in the sample folder
- you can open this file in VSCode itself, or use the settings menu 
- add the folders to the `python.autoComplete.extraPaths` section. 
- it can be on a single line or split across lines. 
    - make sure it is a valid json array 

Example from `.vscode/settings.json`
```json
    "python.languageServer": "Pylance",
    "python.analysis.autoSearchPath": true,
    "python.autoComplete.extraPaths": [
        "src/lib", 
        "all-stubs/cpython_core", 
        "all-stubs/micropyton-1_17-frozen/esp32/GENERIC", 
        "all-stubs/micropyton-1_17-esp32",
    ]
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
```

## Restart VSCode  
VSCode must be restated for so that Pylance and linters such as Pylint to read the updated configuration.

You can use: 
- the `Developer: Reload Window` command.
- or stop / start the editor


```{note} Pymakr: Update pymakr.conf 
 
Depending on the tools and configuration you are using it may be needed to exclude the 
To avoid the "all-stubs" folder to be uploaded to your Micropython MCU

```
 - add "all-stubs" to the "py_ignore" section

 ``` json 
{
    "address": "192.168.4.1",
    "username": "micro",
    "password": "python",
    "sync_folder": "",
    "open_on_start": true,
    "safe_boot_on_upload": false,
    "py_ignore": [
        "all-stubs",
        "pymakr.conf",
        ".vscode",
        ".gitignore",
        ".git",
        "project.pymakr",
        "env",
        "venv",
        ".venv"
    ],
    "fast_upload": false
}
```



[Pylance]: https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance

