# micropython-esp32-um_tinypico-stubs


This is a stub-only package for MicroPython.
It is intended to be installed in a projects virtual environment to allow static type checkers and intellisense features to be used while writing Micropython code.

The version of this package is alligned the the version of the MicroPython firmware.
 - Major, Minor and Patch levels are alligned to the same version as the firmware.  
 - The post release level is used to publish new releases of the stubs.

For `Micropython 1.17` the stubs are published as `1.17.post1` ... `1.17.post2`  
for `Micropython 1.18` the stubs are published as `1.18.post1` ... `1.18.post2`  

To install the latest stubs:  
`pip install -I  micropython-<port>-stubs` where port is the port of the MicroPython firmware.

To install the stubs for an older version, such as MicroPython 1.17:  
`pip install micropython-stm32-stubs==1.17.*` which will install the last post release of the stubs for MicroPython 1.17.


As the creation of the stubs, and merging of the different types is still going though improvements, the stub packages are marked as Beta.
To upgrade stubs to the latest stubs for a specific version use `pip install micropython-stm32-stubs==1.17.* --upgrade`

If you have suggestions or find any issues with the stubs, please report them in the [MicroPython-stubs Discussions](https://github.com/Josverl/micropython-stubs/discussions)

For an overview of  Micropython Stubs please see: https://micropython-stubs.readthedocs.io/en/main/ 
 * List of all stubs : https://micropython-stubs.readthedocs.io/en/main/firmware_grp.html

Included stubs:
* Merged stubs from `stubs/micropython-v1_19_1-esp32-merged`
* Frozen stubs from `stubs/micropython-v1_19_1-frozen/esp32/um_tinypico`
* Core stubs from `stubs/cpython_core-pycopy`


origin | Family | Port | Board | Version
-------|--------|------|-------|--------
Firmware | micropython | esp32 | ESP32 module (spiram) with ESP32 | v1.19.1 
Documentation | micropython | - | - | v1.19.1 
