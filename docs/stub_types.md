# Micropython-Stubs

The installable stub packages are created by merging and assembling different types of stubs that are generated using different means.
Each method of generation has its own advantages, and by combining and merging these in an automated manner allows the creation of accurate and up-to-date stub packages for many of the different ports and board supported by MicroPython.
As the recent versions MicroPython has over 150 different boards, maintaining the stubs manually is not really an option.

The goal is to publish and maintain stub packages for all ports of the last 4 published MicroPython versions on PyPi, and provide packages for the pre-release version (MicroPython master branch) as a pre-release.
Currently the pre-release packages are not (yet) published to PyPi

See the list of [packages](project:#mp_packages) for an overview of the available packages.


The below stub types are referenced in the documentation and can be considered half-products that are used to generate the stub packages.

(mcu_stubs)=
## MCU stubs:
   This type of stubs that is generated on a MicroPython board with a specific firmware, and therefore *closely matches* the capabilities of your board and firmware.
   However MCU stubs do no provide information on the expected parameters or the types returned by functions and methods.
   While they have they have a low level of detail, they do contain a comprehensive overview of the modules, classes and functions available even on custom and one-off firmwares.  
   _Location:_`'stubs/micropython-{Version}-{Port}[-{Board}]'`

(frozen_stubs)=
## Frozen stubs: 
   The firmware for most boards have a number of Python modules Frozen (included) as part of the firmware. For each port and board there is a [manifest file](https://docs.micropython.org/en/latest/reference/manifest.html) that specified which modules should be included in the firmware. These modules have been collected, and stubs have been generated for these modules using [mypy stubgen](https://mypy.readthedocs.io/en/stable/stubgen.html).
   Frozen stubs provider better information regarding the expected parameters, but
   If you select the correct **Port** and **Board** you should get results that exactly match your firmware.  
   _Location:_`'stubs/micropython-{Version}-Frozen/{Port}/{Board}'`

(doc_stubs)=
## Doc stubs:  
   Documentation stubs are generated based on the MicroPython formal documentation `.rst` source files. The `.rst` files are parsed and used to build stubs that match the documentation for that specific version.
   This type of stub is very rich in parameter and class descriptions, but as they are generic by definition, they may/will not follow the specifics of a port or board firmware.  
   _Location:_`'stubs/micropython-{Version}-docstubs'`

(merged_stubs)=
## Merged stubs:
   In order to combine the precision of the MCU stubs with the richness of the docstubs, the two are merged. The merge process add the 'doc strings' parameters and return types to functions, classes and methods.
   The resulting stubs are both precise and rich, however may still lack some details, or contain errors due to lacking or incorrect documentation.  
   _Location:_`'stubs/micropython-{Version}-{Port}[-{Board}]-merged'`

(core_stubs)=
## MicroPython core stubs:
   In only a few cases it is needed to provide an override for classes and functions that cannot yet be automatically generated reliably from the documentation, and need to be augmented manually.
   Currently this contains a single module stub `micropython.pyi`  
   _Location:_`'stubs/micropython[-{Version}]-core'`

(stdlib_stubs)=
## MicroPython stdlib packages
   MicroPython implements a number of stdlib packages with different functionality and functions.
   Examples of this are:
   
   - `gc` has additional functions such as `gc.mem_free()`
   - `time` has additional functions such as `time.sleep_ms()`

    While on one hand these are just modules, tools and linters often use a different logic to
    locate stubs for these stdlib modules, or have a built-in copy of the typeshed stdlib stubs that they use by default.
    
    in order to allow such tools to locate these, a copy of these 'MicroPython stdlib' modules is included in the stub packages in the 'stdlib' module/folder.

    
