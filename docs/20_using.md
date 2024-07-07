## Using MicroPython Stubs

MicroPython stubs are incredibly useful for both beginners and advanced developers. They help you write code more efficiently, reduce errors, and enhance your overall development experience. Here’s a step-by-step guide on how to work with MicroPython stubs:

### Determine the MicroPython Version, Port, and Board

Before installing the stubs, you’ll need to know the specific MicroPython version, port, and board you’re working with. If you’re unsure, you can find this information by running mpflash:

```bash
pipx install mpflash
mpflash list
```

This should give you an output similar to:

```
                                Connected boards                                 
┏━━━━━━━┳━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━┓
┃Serial ┃Family     ┃Port   ┃Board                          ┃CPU        ┃Version┃
┡━━━━━━━╇━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━┩
│ttyACM1│micropython│stm32  │PYBV11                         │STM32F405RG│v1.21.0│
│       │           │       │PYBv1.1 with STM32F405RG       │           │       │
│ttyACM2│micropython│rp2    │RPI_PICO_W                     │RP2040     │v1.23.0│
│       │           │       │Raspberry Pi Pico W with RP2040│           │       │
│ttyUSB0│micropython│esp8266│ESP8266_GENERIC                │ESP8266    │v1.23.0│
│       │           │       │ESP module with ESP8266        │           │       │
│ttyUSB1│micropython│esp32  │ESP32_GENERIC_C3               │ESP32C3    │v1.21.0│
│       │           │       │ESP32C3 module with ESP32C3    │           │       │
│ttyUSB2│micropython│esp32  │ESP32_GENERIC                  │ESP32      │v1.21.0│
│       │           │       │Generic ESP32 module with ESP32│           │       │
└───────┴───────────┴───────┴───────────────────────────────┴───────────┴───────┘
```

Use the **port**  from the respective column.

For **board** use the BOARD_ID  in ALL_CAPS

### Install Stubs for a specific port

If you only know the port then that is sufficient. 
This will install the stubs for a generic board for that port of micropython.

```bash
pip install -U micropython-<port>-stubs --target typing --no-user
pip install -U micropython-esp32-stubs  --target typing --no-user
```

#### Install Stubs for a Specific Version

To install stubs for an older version (e.g., MicroPython 1.18), specify the version followed by  `.*` :

> [Note]
> 
> The stub packages are published as post-releases using the same M.M.M version numbering, allowing the stubs to be updated while keeping a clear reference to the MicroPython version.

```bash
pip install -U micropython-<port>-stubs==1.18.* --target typing --no-user
pip install -U micropython-esp32-stubs==1.18.* --target typing --no-user
```

#### Install Stubs for a Specific Board

For a specific board (e.g., ESP32 UM-TinyPico), install both the port and board stubs:

```bash
pip install -U micropython-<port>-<board>-stubs  --target typing --no-user
pip install -U micropython-esp32-um-tinypico-stubs  --target typing --no-user
```

**Notes:**

- The BOARD_NAMES are commonly in ALL_CAPS with all spaces replaced by _ 
- They should be the same as the name of the board folder in the micropython repo.
- PyPi converts port and board names to lowercase with kebab-case (not snake_case).
- Not all possible ports/boards are published, as creating board-stubs requires access to hardware.
- Some boards have been renamed between versions such as the rp2 PICO to RPI_PICO and several boards have switched from lowercase to all_caps
- Check PyPi directly for newly published stubs.

#### 

And that’s it! 

You’re all set to write MicroPython code with the help of these powerful stubs.

For more details, check out the [MicroPython Stubs documentation](https://micropython-stubs.readthedocs.io/). You can also explore the [full overview of all stubs](https://micropython-stubs.readthedocs.io/). 😊