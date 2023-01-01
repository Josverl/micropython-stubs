# Parkinglot

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
