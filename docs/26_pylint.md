(pylint_config)=
# Pylint Configuration


Unfortunately Pylint does not (yet) support the use of stubs int the `.pyi` format.
Please refer to [Being able to use stub pyi files in pylint](https://github.com/PyCQA/pylint/issues/4987) for more information.


::: {admonition} Untested Update
There appears to be updates to allow the use of stubs in the `.pyi` format.
```
    --prefer-stubs
    Resolve imports to .pyi stubs if available. May reduce no-member messages and increase not-an-iterable messages.

```

See: https://github.com/pylint-dev/astroid/pull/2182

Partial test results are: 
1) init_hook should be updated to include the stubs folder.
    `init-hook='import sys;sys.path[1:1] = ["./typings",];`
2) all modules must be stored in `modulename/__init__.pyi` format, which is not the current format (`modulename.pyi`).
 
:::

## Pylint:Legacy configuration.

:::{note}
 The below configuration for pylint will only work if the stub folders you are using contain `.py` files.
For this you will need to manually rename  the `.pyi` files to `.py` files, 
or copy them directly from the repository.
:::
- Configure pylint to use the selected stub folders

This instructs pylint to insert the list of paths into `sys.path` before performing linting, thus allowing it to find the stubs and use them to better validate your code. 

- use the {download}`.pylintrc sample file <samples/.pylintrc>`.

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
