(using-the-stubs)=
# Using the MicroPython stubs

in order to get the most out of the MicroPython stubs, you should follow these steps:

- determine which Micropython **version** and **port**  you are using.


To install the latest stubs: `pip install  micropython-<port>-stubs`   
where port is the port of the MicroPython firmware. ( stm32, eps32,rp2...) 

To install the stubs for an older version, such as MicroPython 1.17: `pip install micropython-stm32-stubs==1.17.*` 

Note that not all ports are published as I do not have access to hardware to run all ports.
Please let me know if you would like to see a port added, and are willing to help. [Discussions][]
## What do you get

 * `micropython-<port>[-<board>]-stubs`  
    The stubs for a specific version port and board of the MicroPython firmware.
    These are built by combining:
     * The 'Firmware stubs' generated on a generic board for the port 
     * The 'Frozen stubs' from the Micropython repository for that specific version and that port & board combination
     * The 'Core Stubs' to provide a common interface for the Micropython firmware and the CPython core.
    
    Note: board is omitted if it is `GENERIC`  

    Examples:
      - micropython-stm32-stubs
      - micropython-esp32-stubs
      - micropython-rp2-stubs
      - micropython-esp8266-stubs

You can search for [Micropython stub packages on PyPI][PYPI]

## Clone or download a copy of the Micropython-Stubs repo
While it is also possible to clone the Micropython-Stubs repo directly from GH, but this is no longer needed in morst cases.

However there are still a number of stubs that are in the repo and that are not published on PyPI. For these cases please follow the below instructions, and if you would like to see them on PyPI as well, please let me know in the [Discussions][].


 1.  Download a copy of this repo , either via `git clone` or by download a zip file with it's contents
     - store this in a folder, for example 'next to' your software projects such as in `c:\develop\micropython-stubs`  
     this contains a `stubs` folder that contains all stubs
        ```
        git clone https://github.com/Josverl/micropython-stubs.git
        ```

 2. Over time you may want to periodically update this folder using
    ```
    git fetch && git pull
    ```

## Project configuration 
For each project where you want to use the stubs you need to configure vscode and any linters that you use to use the correct stubs.
This is not as complex as it seems initially, and once you have configured your first project, you can copy /paste that structure for other projects. 

## Create a symlink to the stubs folder  
Create a symlink to the `c:\develop\micropython-stubs\stubs` from inside your project.
This will allow you to reference the same stub files from multiple projects, and limit the space
needed. This a recommendation, and things work equally well if you copy or clone the `stubs` folder into your project.  
For details on how to create a symlink, please see : {ref}`create-symbolic-link`

## Quick start: 
Copy the [samples][] folder to your project  
This contains the template files you need to improve syntax highlighting with Pylance and linting with pylint.

## Select which stub folders you need to reference
- The order will influence results. place the 'higher quality' folders first.
- Use forward slashes `/` rather than backslashes, also on Windows.
- for example for micropython 1.17 on an ESP32 select:
    1. "./src/lib",
    2. "all-stubs/cpython_core-pycopy",
    3. "all-stubs/micropython-v1_17-frozen/esp32/GENERIC", 
    4. "all-stubs/micropython-v1_17-esp32",


[samples]: https://github.com/josverl/micropython-stubs/tree/main/docs/samples
[Discussions]: https://github.com/Josverl/micropython-stubs/discussions/categories/ideas
[PYPI]: https://pypi.org/search/?q=-stubs&o=&c=Programming+Language+%3A%3A+Python+%3A%3A+Implementation+%3A%3A+MicroPython