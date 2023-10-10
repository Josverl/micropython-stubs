(using-the-stubs)=
# Using the MicroPython stubs
There are a few different options in which you can install the stubs, 

The logical steps are:
1. Determine the MicroPython version, port and board you will be using the stubs for.
2. Create and activate a virtual environment
3. Install or copy the stubs to your system
4. Configure your IDE (or other tools) where the stubs are located
5. Add configuration to suppress false positives and unneeded warnings

At minimum you will need to specify the **port** of the stubs.
If you do not specify a version, the stubs for the last published version will be used. (Note that this is different from the **_latest version_** )

##  Determine the version and port
If you do not know the exact version and port,  run the below command in MicroPython
`import sys; print( "version:", sys.version, "port:", sys.platform)`
In the documentation these will be referred to as **version**, **port** and **board** 

## Create and activate a .venv
A Python virtual environment is a tool that helps to keep dependencies required by different projects separate by creating isolated python virtual environments for them. This is one of the most important tools that most of the Python developers use.
To create and activate a virtual environment in your project directory 
    ```bash
    # linux / mac
    python3 -m venv .venv
    source .venv/bin/activate
    ```
    ```bash
    # windows
    python -m venv .venv
    .venv\Scripts\Activate.ps1
    ```
_While it is possible to install the MicroPython stubs in your global environment it is better to use virtual environments or to a `typings` folder._
If you install the MicroPython stubs in your general or global python environment, then please note that this may/will cause regular Python code to also be validated against the MicroPython stubs, and this will almost certainly result in false-positive errors being flagged in your CPython code.

## Install the stub packages to your system
- Install a stub-package into a virtual environment
- Install a stub package into a `typings` folder
- Legacy method using a copy or clone 

### Install into a `venv`
#### Last published version
The package naming convention is: `micropython-<port>[-<board>]-stubs`
where port is the port of the MicroPython firmware. ( stm32, eps32,rp2, samd, ...) 

To install the stubs for the last published version of MicroPython: 
``` bash
pip install -U  micropython-<port>-stubs
pip install -U  micropython-stm32-stubs
```
#### Install stubs for a specific version.
To install the stubs for an older version, such as MicroPython 1.18:  
specify the version as follows ** `micropython-<port>-stubs==<version>.*` **
``` bash
pip install -U  micropython-<port>-stubs==<version>.*
pip install -U  micropython-esp32-stubs==1.18.*
```
#### Install stubs for a specific board.
To install the stubs for a specific board, such as the `ESP32 UM-TinyPico`:   
specify both the port and the board
``` bash
pip install -U micropython-<port>-<board>-stubs
pip install -U micropython-esp32-um-tinypico-stubs
```
**Notes:** 
 - PyPi transforms all names of the ports and boards to small-caps and kebab-case, (not snake_case).
 - Not all possible ports/boards are published as I do not have access to hardware to create board-stubs for all ports and boards.
 - Newly published stubs may show as 'not found', please [check PyPi directly](https://pypi.org/search/?q=micropython+-stubs&o=&c=Programming+Language+%3A%3A+Python+%3A%3A+Implementation+%3A%3A+MicroPython)

### Install into a `typings` folder.
In some cases a single project my need to make use of stubs for different ports or boards at the same time. In a venv it is possible to install only **one** stub package.

Some tools such as Pylance and Pyright can also make use of stubs that are located in a folder, usually a folder named `typings`
Another advantage of  using a typings folder is that it can be checked in to a source code repo 

In order to install the stubs into a typings folder append `--target <folder> --no-user` to the pip install commands listed in the above sections.
`--target` specifies the destination folder 
`--no-user` is only needed to avoid conflicts with an active venv

To install the stubs for the last published version of MicroPython: 
``` bash
pip install -U  micropython-<port>-stubs --target <folder> --no-user
pip install -U  micropython-stm32-stubs --target ./typings --no-user
```
or 
``` bash
pip install -U  micropython-esp32-stubs==1.18.* --target ./typings --no-user
```


## Configure your IDE (or other tools) where the stubs are located
the configuration for your IDE or tool set is specific to that IDE or tool,
however there will be some commonalities.
Most tools will :
- Be able to use the stubs if they are located in the active virtual environment
- If not using a `venv` you will need to configure the tool with the location, unless it uses `typings` as the default location.
- can be configured with a python language version. MicroPython is based on Python 3.5 with some features from later versions. 



[samples]: https://github.com/josverl/micropython-stubs/tree/main/docs/samples
[Discussions]: https://github.com/Josverl/micropython-stubs/discussions/categories/ideas
[PYPI]: https://pypi.org/search/?q=-stubs&o=&c=Programming+Language+%3A%3A+Python+%3A%3A+Implementation+%3A%3A+MicroPython