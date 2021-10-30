# Order of the stub folders

The stubs are used by 2 or 3 components.
 1. the VSCode Pylance Language Server
 2. the VSCode Python add-in
 3. and optionally by an additional [Python linter](https://code.visualstudio.com/docs/python/linting#_specific-linters) such as **pylint** or **mypy**
 
These  tools work together to provide code completion/prediction, type checking and all the other good things.
For this the order in which these tools use  the stub folders is significant, and best results are when they use the same order. 
( Note that the different tools will not always agree, MyPy might show a warning where PyLance understands the intent of your code, and vice-versa )

In most cases the best results are achieved by the below setup:

```{mermaid}
sequenceDiagram
    participant Pylance
    autonumber
    Pylance --x Source code: check 
    Pylance --x CPython stubs: check 
    Pylance --x Frozen stubs: check 
    Pylance --x RST Stubs: check 
    rect rgba(0, 0, 255, .3)
    Pylance ->>+Board Stubs: check
    Board Stubs ->>-Pylance: return info 
    end
```
 1. **Source code:**  
   example: `['src', 'src/lib'] `  
   This should include the path to your source files and any libraries used.  

 2. **Cpython stubs:**  
   `['all-stubs/cpython-core'] `  
   These are Python files that are intended to allow Micropython files to be run. with some limitations, on CPython. They also help resolve most MicroPython stdlib uses.

 3. **Frozen stubs - Micropython - [Version] - [Port]-frozen:**  
    `['all-stubs/micropython-{Version}-{Port}-Frozen']`  
    MicroPython for most boards has a number of Python modulesFrozen (included) as part of the firmware.
    For common firmwares and ports, these modules have been collected, and stubs have been generated for these modules.

 4. **Board stubs - Micropython - [Version] - [Port]:**  
   ` 'all-stubs/micropython-{Version}-{Port}-Frozen' `  
   This are the stubs that are generated on the board.
   While they have they have a low level of detail, they do contain a comprehensive overview of the modules, classes and functions available even on custom and one-off firmwares.

in most cases using ths order provides a good mix between richness and coverage of the functionality provided by your board.


 1. **Your own source files**, including any libraries you add to your project.
 This can be a single libs folder or multiple directories

 2. **The CPython common stubs**. These stubs are handcrafted to mimic MicroPython modules on a CPython system.
 there are only a limited number of these stubs. ALso for some modules this approach does not appear to work. (such as the `cg` and `sys` modules)

 3. **Firmware specific frozen stubs**. Most micropython firmwares include a number of python modules that have been included in the firmware as frozen modules in order to take up less memory.
 these modules have been extracted from the source code. where possible this is done per port and board,  or if not possible the common configuration for has been included.

 4. **Micropython-stubber Stubs**. For all other modules that are included on the board, [micropython-stubber](https://github.com/Josverl/micropython-stubber) or [micropy-cli](https://github.com/BradenM/micropy-cli) has been used to extract as much information as available, and provide that as stubs. While there is a lot of relevant and useful information for code completion, it does unfortunately not provide all details regarding parameters that the earlier  options may provide.


When using a different code editor, a similar configuration may be used. 

 _**Note:**_ While it is possible for you to configure different processing orders, this will probably lead to confusing or contradicting feedback in the code editor that you are using.

