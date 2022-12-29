# Parkinglot



``` {mermaid}
%%{ init: { 'flowchart': { 'curve': 'bump' } } }%%
graph TB

    %% Get frozen
    MPY --> |fa:fa-list port/board/manifest.py| GFS
    LIB -->GFS -->FR
    
    %% create Board stubs
    MCU --> CS --> FW
    %% create docstubs
    DOCS --> GDS --> DS --> Merge
    %% merge fw and docstubs 
    FW --> Merge --> MS

    %% Build 
    FR --> Build
    MS --> Build
    Core --> Build
    Package --> Stubs
    Build <--> DB    
    Build --> Package 
    %% Publish 
    Stubs --> Publish
    Publish --> PyPi --> MPS
    DB <--> Publish

    %% Text labels and Styling 
    MPY{{fab:fa-github MicroPython}}:::repo
    LIB{{fab:fa-github MicroPython-lib}}:::repo
    DOCS{{fab:fa-github MicroPython Docs}}:::repo
    Stubs{{fab:fa-github MicroPython-stubs/publish}}:::repo
    PyPi{{fas:fa-th-list PyPi}}:::pkg
    MPS[fa:fa-suitcase MicroPython-***-stubs]:::pkg
    
    FR[/fas:fa-folder-tree Frozen stubs/]:::stubs 
    FW[/fas:fa-folder-tree Firmware-stubs/]:::stubs
    MS[/fa:fa-folder-tree Merged-stubs/]:::stubs
    DS[/fa:fa-folder-tree Doc-stubs/]:::stubs
    Core[/fa:fa-folder-tree Core-stubs/]:::stubs
    
    Package[/fa:fa-suitcase Package/]:::pkg
    DB[(fa:fa-database jsondb)]

    MCU[fa:fa-microchip MCU]
    CS[[fa:fa-microchip createstubs.py]]:::stubber

    Merge[[Merge]]:::stubber
    GFS[[get-frozenstubs]]:::stubber
    GDS[[get-docstubs]]:::stubber
    Build[[Build]]:::stubber
    Publish[[Publish]]:::stubber

%%    classDef repo fill:lightblue,stroke-width:4px
%%    classDef stubber fill:lightgreen
%%    classDef stubs fill:cyan,stroke-width:4px
%%    classDef pkg fill:cyan,stroke-width:4px

%% update
```


## Stubber Prosessing order

``` {mermaid}
%%{ init: { 'flowchart': { 'curve': 'bump' } } }%%
graph TB

    %% Get frozen
    MPY --> |fa:fa-list port/board/manifest.py| GFS
    LIB -->GFS -->FR
    
    %% create Board stubs
    MCU --> CS --> FW
    %% create docstubs
    DOCS --> GDS --> DS --> Merge
    %% merge fw and docstubs 
    FW --> Merge --> MS

    %% Build 
    FR --> Build
    MS --> Build
    Core --> Build
    Package --> Stubs
    Build <--> DB    
    Build --> Package 
    %% Publish 
    Stubs --> Publish
    Publish --> PyPi --> MPS
    DB <--> Publish

    %% Text labels and Styling 
    MPY{{fab:fa-github MicroPython}}:::repo
    LIB{{fab:fa-github MicroPython-lib}}:::repo
    DOCS{{fab:fa-github MicroPython Docs}}:::repo
    Stubs{{fab:fa-github MicroPython-stubs/publish}}:::repo
    PyPi{{fas:fa-th-list PyPi}}:::pkg
    MPS[fa:fa-suitcase MicroPython-***-stubs]:::pkg
    
    FR[/fas:fa-folder-tree Frozen stubs/]:::stubs 
    FW[/fas:fa-folder-tree Firmware-stubs/]:::stubs
    MS[/fa:fa-folder-tree Merged-stubs/]:::stubs
    DS[/fa:fa-folder-tree Doc-stubs/]:::stubs
    Core[/fa:fa-folder-tree Core-stubs/]:::stubs
    
    Package[/fa:fa-suitcase Package/]:::pkg
    DB[(fa:fa-database jsondb)]

    MCU[fa:fa-microchip MCU]
    CS[[fa:fa-microchip createstubs.py]]:::stubber

    Merge[[Merge]]:::stubber
    GFS[[get-frozenstubs]]:::stubber
    GDS[[get-docstubs]]:::stubber
    Build[[Build]]:::stubber
    Publish[[Publish]]:::stubber

%%    classDef repo fill:lightblue,stroke-width:4px
%%    classDef stubber fill:lightgreen
%%    classDef stubs fill:cyan,stroke-width:4px
%%    classDef pkg fill:cyan,stroke-width:4px

%% update
```



## Resolve stdlib modules

``` {mermaid}
sequenceDiagram
    participant P as Pylance/Pyright
    participant Source as Source code
    participant venv as micropython.pyi stubs in typings or venv
    participant stdlib as micropython stdlib .pyi stubs in typings/stdlib or venv/.../stdlib
    participant typeshed as typeshed stdlib stubs
    autonumber

    note right of P: lookup micropython module
    P --x Source: check 
    
        rect rgba(0, 0, 255, .3)
            P ->>+ venv: check
            venv -->>- P: resolved MicroPython stubs
        end
    opt recommended configuration
        rect rgba(0, 128, 128, .3)
            note over P,stdlib: requires { "python.analysis.typeshedPaths": ["typings",".venv/Lib/site-packages"] }
            P ->>+ stdlib: check
            stdlib -->>-P: resolved MicroPython stdlib stubs
        end
    end
    rect rgba(128, 28, 128, .3)
        %% note over P,typeshed: requires configuration of path
        P ->>+ typeshed: check
        typeshed -->>-P: resolved stdlib stubs
    end
```




## legacy resolving order 

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


## Published 
The list of the current included firmwares, ports and boards includes stubs from the following micropython families: 


 - **MicroPython**
 - Pycopy 
 - Loboris port (ESP32)

 - LVGL
 - EV3 / Lego
 - M5Stack

## What do you get


Then in VSCode press : `F1` and select `Python: Restart language server`  
(only needed once)


# Legacy 

## Clone or download a copy of the Micropython-Stubs repo
While it is also possible to clone the Micropython-Stubs repo directly from GH, but this is no longer needed in morst cases.

However there are still a number of stubs that are in the repo and that are not published on PyPI. For these cases please follow the below instructions, and if you would like to see them on PyPI as well, please let me know in the [Discussions][].


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
