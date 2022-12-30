# Pylint

# Pylint does not work with stub-only packages.
Unfortunatly pylint does not (yet) support the use of stubs int the `.pyi` format.
Please refer to [Being able to use stub pyi files in pylint](https://github.com/PyCQA/pylint/issues/4987) for more information.


## Pylint:Legacy configuration.

**Note:** The below configuration for pylint will only work if the stub folders you are using contain `.py` files.

- Configure pylint to use the selected stub folders

This instructs pylint to insert the list of paths into `sys.path` before performing linting, thus allowing it to find the stubs and use them to better validate your code. 

- use the {download}`.pylintcr sample file <samples/.pylintrc>`.

- edit the line that starts with `init-hook=`  
        ```
        init-hook='import sys;sys.path[1:1] = ["src/lib", "folder1","folder2", "folder3",];'
        ```
- replace the folders with your selection of stub folders.  
**Note that in `.pylintrc` the list of folders MUST be on a single line**
- the result should look like:  
        ```
        init-hook='import sys;sys.path[1:1] = ["src/lib", "all-stubs/cpython_core-pycopy","all-stubs/micropython-v1_17-frozen/esp32/GENERIC", "all-stubs/micropython-v1_17-esp32",];'
        ```
