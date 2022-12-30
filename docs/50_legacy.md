# Legacy installation

Prior to publish the stub packes to PyPi, the only option was to copy or clone the entire repository to a local drive and reference the different stub types from there.
that method has been depricated, but I wanted to keep the documentation just in case that is still useful for someone.

However there are still a number of stubs that are in the repo and that are not published on PyPI. For these cases please follow the below instructions, and if you would like to see them on PyPI as well, please let me know in the [Discussions][].

Note however that I will not be activly maintaining these pages.

## Clone or download a copy of the Micropython-Stubs repo



 1.  Download a copy of this repo , either via `git clone` or by download a zip file with it's contents
     - store this in a folder, for example 'next to' your software projects such as in `c:\develop\micropython-stubs`  
     this contains a `stubs` folder that contains all stubs
        ```
        git clone https://github.com/Josverl/micropython-stubs.git
        ```

 2. Over time you may want to periodically update this folder using
    ```
    git fetch && git pull
    ```

## Project configuration 
For each project where you want to use the stubs you need to configure vscode and any linters that you use to use the correct stubs.
This is not as complex as it seems initially, and once you have configured your first project, you can copy /paste that structure for other projects. 

## Create a symlink to the stubs folder  
Create a symlink to the `c:\develop\micropython-stubs\stubs` from inside your project.
This will allow you to reference the same stub files from multiple projects, and limit the space
needed. This a recommendation, and things work equally well if you copy or clone the `stubs` folder into your project.  
For details on how to create a symlink, please see : {ref}`create-symbolic-link`

## Quick start: 
Copy the [samples][] folder to your project  
This contains the template files you need to improve syntax highlighting with Pylance and linting with pylint.

## Select which stub folders you need to reference
- The order will influence results. place the 'higher quality' folders first.
- Use forward slashes `/` rather than backslashes, also on Windows.
- for example for micropython 1.17 on an ESP32 select:
    1. "./src/lib",
    2. "all-stubs/cpython_core-pycopy",
    3. "all-stubs/micropython-v1_17-frozen/esp32/GENERIC", 
    4. "all-stubs/micropython-v1_17-esp32",

### Option 2) Clone the stubs repo 

this is the 'olde way' of installing the stubs.
only usefull if you are activly developing / updating the stubs

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

## Order of the stub folders

The stubs can be used by different components in your development environment.
 1. the VSCode Pylance Language Server
 2. the VSCode Python add-in
 3. and optionally by an additional [Python linter](https://code.visualstudio.com/docs/python/linting#_specific-linters) such as pylint or mypy.
 
These  tools work together to provide code completion/prediction, type checking and all the other good things.
For this the order in which these tools use  the stub folders is significant, and best results are when they use the same order. 
( Note that the different tools will not always agree, MyPy might show a warning where PyLance understands the intent of your code, and vice-versa )

In most cases the best results are achieved by the below setup:

```{mermaid}
sequenceDiagram
    participant Pylance
    autonumber
    Pylance --x Source code: check 
    rect rgba(0, 0, 255, .3)
    Pylance --x CPython stubs: check 
    Pylance --x Frozen stubs: check 
    Pylance --x Doc Stubs: check 
    Pylance ->>+Board Stubs: check
    Board Stubs ->>-Pylance: return info 
    end
```
