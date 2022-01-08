(using-the-stubs)=
# Using the MicroPython stubs

In order to use the stubs you need to do a few things:  
## Clone or download a copy of the Micropython-Stubs repo
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
