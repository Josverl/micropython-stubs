# Parkinglot

## Stubber Prosessing order

``` {mermaid}
%%{ init: {'theme': 'light','flowchart': { 'curve': 'bump' } }%%
graph TB

    %% Get frozen
    MPY --> |"fas:fa-folder-tree ports/.../boards/.../manifest.py"| GFS
    LIB -->GFS -->FR
    
    %% create MCU stubs
    MCU --> CS --> FW
    %% create docstubs
    DOCS --> GDS --> DS --> Merge
    %% merge fw and docstubs 
    FW --> Merge --> MS

    %% Build 
    FR --> Build
    MS --> Build
    Stdlib --> Build
    Build <--> DB    
    Build --> PUB
    %% Publish 
    PUB --> Publish
    Publish --> PyPi --> PKG
    DB <--> Publish

    %% Styling 
    MPY{{fab:fa-github MicroPython}}:::repo
    LIB{{fab:fa-github MicroPython-lib}}:::repo
    DOCS{{fab:fa-github MicroPython Docs}}:::repo
    PyPi{{fas:fa-th-list PyPi}}:::pkg

    PKG[fa:fa-suitcase MicroPython-***-stubs]:::pkg

    PUB[/fa:fa-suitcase Packages\nfas:fa-folder-tree /publish/...//]:::stubs
    FR[/fas:fa-pencil Frozen stubs\nfas:fa-folder-tree stubs/... -frozen/]:::stubs 
    FW[/fas:fa-pencil Firmware-stubs\nfas:fa-folder-tree stubs/.../]:::stubs
    MS[/fa:fa-pencil Merged-stubs\nfas:fa-folder-tree stubs/... -merged/]:::stubs
    DS[/fa:fa-pencil Doc-stubs\nfas:fa-folder-tree stubs/... -docstub/]:::stubs
    Stdlib[/fa:fa-pencil Stdlib-stubs\nfas:fa-folder-tree stubs/-stdlib/]:::stubs
    
    DB[(fa:fa-database jsondb)]

    MCU[<img src='https://micropython.org/static/img/Mlogo_138wh.png'> MCU]:::device
    CS[[fa:fa-microchip createstubs.py]]:::stubber

    Merge[[Merge]]:::stubber
    GFS[[get-frozenstubs]]:::stubber
    GDS[[get-docstubs]]:::stubber
    Build[[Build]]:::stubber
    Publish[[Publish]]:::stubber

    classDef repo fill:lightblue,stroke-width:4px
    classDef stubber fill:lightgreen
    classDef stubs fill:cyan,stroke-width:4px
    classDef pkg fill:cyan,stroke-width:4px
    classDef device fill:black,stroke-width:4px,color:white,stroke:white

%% update
```
