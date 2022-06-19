## Naming conventions

Initially `<family>` is `micropython`, but this may be extended to other firmware families

 * `<family>-<port>[-<board>]-stubs`  
    The stubs for a specific version port and board of the MicroPython firmware.
    These is built by combining:
     * The 'Firmware stubs' generated on a generic board for the port 
     * The 'Frozen stubs' from the Micropython repository for that specific version and that port & board combination
     * The 'Core Stubs' to provide a common interface for the Micropython firmware and the CPython core.
    
    Note: board is omitted if it is `GENERIC`  

    Examples:
      - micropython-stm32-stubs
      - micropython-esp32-stubs
      - micropython-rp2-stubs
      - micropython-esp8266-stubs

 * `<family>-doc-stubs`  
    Only for MicroPython version 1.17 and later 
    The documentation stubs for a specific version of micropython.
    These stubs are generated based on the documentation of the MicroPython firmware and contain rich type information.
    however they will contain references to features that are not available in other ports that may not be avaialble on your board.

    The intent is for these stubs to be merged into 
    Example:
      - micropython-doc-stubs

**Note:** that the different stubs packages have significant overlaps in the types they provide.
If you install multiple stubs packages, the last installed package may/will overwrite some of the types by another package.


## Use

To install the latest stubs:
`pip install -I  micropython-<port>-stubs` where port is the port of the MicroPython firmware.

To install the stubs for an older version, such as MicroPython 1.17:
`pip install micropython-stm32-stubs==1.17.*` which will install the last post release of the stubs for MicroPython 1.17.


## Versioning 


## Version Specifiers and Semantic Versioning

https://peps.python.org/pep-0440/#version-specifiers

Post-releases and final releases receive no special treatment in version specifiers - they are always included unless explicitly excluded.

Examples
 - ~=3.1: version 3.1 or later, but not version 4.0 or later.
 - ~=3.1.2: version 3.1.2 or later, but not version 3.2.0 or later.
 - ~=3.1a1: version 3.1a1 or later, but not version 4.0 or later.
 - == 3.1: specifically version 3.1 (or 3.1.0), excludes all pre-releases, post releases, developmental releases and any 3.1.x maintenance releases.
 - == 3.1.*: any version that starts with 3.1. Equivalent to the ~=3.1.0 compatible release clause.
 - ~=3.1.0, != 3.1.3: version 3.1.0 or later, but not version 3.1.3 and not version 3.2.0 or later.
