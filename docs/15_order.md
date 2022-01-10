# Order of the stub folders

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

## Stub Types

 1. **Source code:**  
   example: `['src', 'src/lib'] `  
   This should include the path to your source files and any libraries used.  
   This should be the fist location any tool should check. Also this allows you to override any library if needed.

 2. **Cpython stubs:**  
   `['all-stubs/cpython_core-pycopy', 'all-stubs/cpython_core-micropython'] `  
   These are Python files that are intended to allow Micropython files to be run. with some limitations, on CPython. They also help resolve most MicroPython stdlib uses.
   There are currenly two different sources for these stubs : 
    - the micropython-lib version :  'all-stubs/cpython_core-micropython'
    - the **pycopy-lib** version :  'all-stubs/cpython_core-pycopy'
    The recommended cpython core is based off the pycopy libs as, in my opinion, they offer most functionality. 

 3. **Frozen stubs - Micropython - [Version] - frozen / [Port] / [Board]:**  
    `['all-stubs/micropython-{Version}-Frozen/{Port}/{Board}']`  
    MicroPython for most boards has a number of Python modulesFrozen (included) as part of the firmware.
    For common firmwares and ports, these modules have been collected, and stubs have been generated for these modules.
    If you select the correct **Port** and **Board** you should getresults that exactly match your firmware. 

 4. **Doc stubs - Micropython - [Version] -docstubs:**  
    `['all-stubs/micropython-{Version}-docstubs']`  
    These stubs are generated based on the Micropython formal documentation.
    This type of stub is very rich in parameter and class descriptions, but as they are generic by definition, they may/will not follow the nuances of your firmware.
    
 5. **Board stubs - Micropython - [Version] - [Port]:**  
   ` 'all-stubs/micropython-{Version}-{Port}-Frozen' `  
   This type of stubs that is generated on the micropython board with the specific firmware, and therefore **very closely matches** the capabilities of your board and firmware.
   While they have they have a low level of detail, they do contain a comprehensive overview of the modules, classes and functions available even on custom and one-off firmwares.

In most cases using ths order provides a good mix between richness and coverage of the functionality provided by your board.
As an example : 
```
    "python.autoComplete.extraPaths": [
        "board/lib",
        "all-stubs/cpython_core",
        "all-stubs/micropython-1_17-frozen/esp32/GENERIC",
        "all-stubs/micropython-esp32-1_17"
    ],

```

 1. **Your own source files**, including any libraries you add to your project.
 This can be a single libs folder or multiple directories

 2. **The CPython common stubs**. These stubs are handcrafted to mimic MicroPython modules on a CPython system.
 there are only a limited number of these stubs. ALso for some modules this approach does not appear to work. (such as the `cg` and `sys` modules)

 3. **Firmware specific frozen stubs**. Most micropython firmwares include a number of python modules that have been included in the firmware as frozen modules in order to take up less memory.
 these modules have been extracted from the source code. where possible this is done per port and board,  or if not possible the common configuration for has been included.

 4. **Micropython-stubber Stubs**. For all other modules that are included on the board, [micropython-stubber](https://github.com/Josverl/micropython-stubber) or [micropy-cli](https://github.com/BradenM/micropy-cli) has been used to extract as much information as available, and provide that as stubs. While there is a lot of relevant and useful information for code completion, it does unfortunately not provide all details regarding parameters that the earlier  options may provide.


When using a different code editor, a similar configuration may be used. 

 _**Note:**_ While it is possible for you to configure different processing orders, this will probably lead to confusing or contradicting feedback in the code editor that you are using.

