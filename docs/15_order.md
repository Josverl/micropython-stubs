# Order of the stub folders

The stubs can be used by different components in your development environment.
 1. the VSCode Pylance Language Server
 2. the VSCode Python add-in
 3. and optionally by an additional [Python linter](https://code.visualstudio.com/docs/python/linting#_specific-linters) such as pylint or mypy.
 
These  tools work together to provide code completion/prediction, type checking and all the other good things.
For this the order in which these tools use  the stub folders is significant, and best results are when they use the same order. 
( Note that the different tools will not always agree, MyPy might show a warning where PyLance understands the intent of your code, and vice-versa )

In most cases the best results are achieved by the below setup:
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
