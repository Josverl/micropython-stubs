# Stub folder Naming Conventions.
<!-- Origin: publish/readme.md -->

Initially `<family>` is `micropython`, but this may be extended to other firmware families.

 * `<family>-<version>-<port>[-<board>]-stubs`  
    The stubs for a specific version port and board of the MicroPython firmware.
    These are built by combining:
     * The 'Board stubs' generated on a generic board for the port 
     * The 'Frozen stubs' from the Micropython repository for that specific version and that port & board combination
     * The 'Core Stubs' to provide a common interface for the Micropython firmware and the CPython core.
    
    As most of the boards for a port share the same firmware, the stubs for a port are usually the same for all boards of that port. So the board is optional in the name, but there may be modules missing or different if they are specific to a that board.  

    Examples:
      - micropython-stm32-stubs
      - micropython-esp32-stubs
      - micropython-rp2-stubs
      - micropython-esp8266-stubs

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


# Installing directy from the repository

The below installs 2 stub packages 
 - from the branch : reference/rp2
    - from the folder : publish/micropython-stdlib-stubs
    - from the folder : publish/micropython-v1_24_1-rp2-rpi_pico_w-stubs
 - to the folder : typings

```bash
pip install "git+https://github.com/Josverl/micropython-stubs@reference/rp2#subdirectory=publish/micropython-stdlib-stubs" --target typings
pip install "git+https://github.com/Josverl/micropython-stubs@reference/rp2#subdirectory=publish/micropython-v1_24_1-rp2-rpi_pico_w-stubs" --target typings
```

*Note:* This is quite a long command, so it is best to copy and paste it into the terminal.
it is also quite slow to install, as it needs to download all the files from the repository, 
but it works well to test out a preview of the stubs.
