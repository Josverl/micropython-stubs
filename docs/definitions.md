# Terms and Definitions

*MicroPython Specific Terms*

(micropython_port)=
MicroPython *port*
:   A "port" in MicroPython refers to an adaptation of the MicroPython interpreter to a specific microcontroller family or architecture. 
    Each port is tailored to run on a particular type of hardware. The MicroPython project contains several ports, each residing in a subdirectory within the project repository. 
    Examples of ports are `esp32`, `stm32`, `rp2`, and `unix`.
    Port names are commonly written in lowercase.

(micropython_board)=    
MicroPython *board*
:   A "board" represents a specific piece of hardware that a port can run on. Boards can be development kits or devices. 
    For example, if you're working with the `rp2` port, you might use the `RPI-PICO` board, which is based on the Raspberry Pi Pico microcontroller.
    Board names are commonly written in ALL_CAPS with spaces replaced by hyphens or underscores.


(micropython_variant)=
MicroPython *variant*
:   Some boards support "variants," which allow for small variations of an otherwise similar board. Variants might differ in flash sizes or other features. For instance, the "spiram" variant is used for boards based on WROVER modules or those with SPIRAM (PSRAM). 
    The "d2wd" variant is specific to ESP32-D2WD chips with 2MiB flash, while "unicore" is for single-core ESP32 chips. Additionally, the "ota" variant sets up the partition table for Over-the-Air updates.

*Static Type Checkers and tooling* 

(pyright)=
Pyright
:   Pyright is a static type checker for Python that is developed by Microsoft. It is designed to be fast and efficient, providing real-time feedback as you write code. Pyright supports type hinting and type checking for Python 3.6 and later. 
    Pyright is often used in conjunction with Visual Studio Code, where it provides IntelliSense features and type checking for Python code. (Also see Pylance below.) 

    For configuring Pyright see <project:#pyright_config>

(pylance)=
Pylance
:   Pylance is a Visual Studio Code extension that provides advanced language support for Python. It is built on the Pyright static type checker and offers features like IntelliSense, type checking, and code navigation. Pylance is designed to improve the Python development experience in Visual Studio Code.

    For configuring Pylance see <project:#pylance_config>

(mypy)=
Mypy
:  Mypy is a static type checker for Python that is designed to help developers find type-related errors in their code. Mypy supports type hinting and type checking for Python 3.5 and later. It is often used in conjunction with a code editor or IDE to provide static type checking for Python code.

    For configuring Mypy see <project:#mypy_config>

(stubgen)=
stubgen
:  A tool that generates type stubs for Python modules. Type stubs are files that contain type hints but no implementation code. They are used by static type checkers like Mypy to analyze code for type-related errors. Stubgen is part of the Mypy project and is used to generate stubs for Python modules that do not already have type hints.

(typeshed)=
typeshed
:  A repository of type stubs for the Python standard library and other common Python packages. Typeshed provides type hints for functions, classes, and modules that do not have type annotations in their source code. It is used by static type checkers like Mypy to analyze code and provide type-related feedback.

(stdlib)=
stdlib
:  The "standard library" of a programming language is a collection of modules and packages that provide core functionality for the language. In MicroPython, the standard library includes modules like `os`, `sys`, and `math`, which provide functions for interacting with the operating system, system-specific parameters, and mathematical operations, respectively.The MicroPython modules are similar, but not exactly the  same as the Python libraries.

*Linters*

(pylint)=
pylint
:   Pylint is a linting tool for Python that checks for errors, enforces coding standards, and looks for code smells in Python code. It analyzes code for potential bugs, style issues, and other problems, providing feedback to help developers write cleaner, more maintainable code.

    For configuring Pylint see <project:#pylint_config>

<!-- 
FYI: 
Board name and variant changes · micropython - GitHub. https://github.com/orgs/micropython/discussions/12294. -->
