# pyscript referene stubs 
 - Version : 2025.2.3

## Steps to create detailed pyright stubs 

- clone the pyscript/pyscript repo
- create a pyproject.toml file in `core/src/stdlib/pyproject.toml`
- open command prompt in the `core/src/stdlib` folder
- run `pyright --verbose --createstub pyscript`
- type-stubs will be created in `core/src/stdlib/typings/pyscript`

- apply manual edits as needed 
    - better return types are generated as comments, in most cased these can be used 
        - replace ` : # -> ` with ` -> `
        - add missing type imports 
- Add / Update module level docstrings 

- copy the resulting stubs 
  - from the pyscript repo : `core/src/stdlib/typings/pyscript`
  - to the micropython-stubs repo `reference/pyscript` 

- check with pylance/pyright, mypy, ruff

## Create MCU/Firmware stubs on pyscript.com
Steps to run createstubs on pyscript.com 
- https://pyscript.com/@jos_verlinde/createstubs-pyscript/

- create a project in pyscript.com
    - set script type to mpy 
    - use pyscript 2025.2.3 or newer to be able to use [`pyscript.fs`](https://docs.pyscript.net/2025.10.1/api/#pyscriptfs)
- copy the createstubs.py script to the project
- add the script to mount , sync and dismount a local filesystem

- run the script
    - a popup should allow yuo to select a local (empty) folder
      it may be needed to pop-out the preview window to a tab or seperate window to be able to [✅Authorize] access to the local file-system.
    - the createstubs.py script will crerate MCU stubs as usual
    - these will sync back to the local folder 
- [optionally] copy from he temp folder to the micropython-stubs repo to the `stubs folder`
- rename the `stubs/micropython-v1_24_1-webassembly` folder to `stubs/micropython-v1_24_1-webassembly-GENERIC` 

*Postprocessing:*
 - *Manual merge/copy:* # TODO: integrate this in the automatic merge process 
    - copy the 'pyright' stubs
        - from: `reference/pyright`
        - into `stubs/micropython-v1_24_1-webassembly-GENERIC/pyright` 
        (overwriting the existing files)
- `stubber merge --port webassembly --version v1.24.1`
- `stubber build --port webassembly --version v1.24.1`
