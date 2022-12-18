# VSCode 

VSCode  uses Pylance, and optionally a linter such as pylint or mypy.

### Option 1) Install the stubs from PyPi :

you need to know which port you want the stubs for `stm32`, `esp32`, `rp2`, `esp8622`

### `pip install -U micropython-<port>-stubs` 

or install the stubs for a specific version of micropython unsing  
`pip install -U micropython-stm32-stubs==1.17.*`


### Option 2) Clone the stubs repo 

this is the 'olde way' of installing the stubs.
only sefull if you are activly developing / updating the stubs

## Configure VSCode & Pylance to use the selected stub folders  
This instructs the VSCode Pylance extension to consider your libs folder and the stubs for code completion and static type-checking.

VSCode allows this configuration to be set on **_workspace_** , folder or _user_ level. I prefer setting it per workspace or folder as that allows different settings for different projects, but you could do either.
     
The below configuration is [Pylance][] specific  
     
- use the {download}`samples/.VSCode/settings.json`  located in the sample folder
- you can open this file in VSCode itself, or use the settings menu 
- add the folders to the `python.analysis.extraPaths` section. 
- it can be on a single line or split across lines. 
    - make sure it is a valid json array 

Example from `.vscode/settings.json`
```json
    "python.languageServer": "Pylance",
    "python.analysis.autoSearchPaths": true,
    "python.analysis.extraPaths": [
        "src/lib", 
        "all-stubs/cpython_core-pycopy", 
        "all-stubs/micropyton-1_17-frozen/esp32/GENERIC", 
        "all-stubs/micropyton-1_17-esp32",
    ],
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

