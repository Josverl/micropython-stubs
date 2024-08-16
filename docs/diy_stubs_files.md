# DIY Stub file creation for MicroPython



To create stubs for your MicroPython board, you can use the `micropython-stubber` package. This package will connect to your board and create a set of stub files that you can use in your IDE to get code completion and type checking.

The recommendation is:

- To create a folder from which to run the tool and store the various repos and files
- Create a .venv virtual environment to run the tool in.
  `python -m venv .venv`



## Install micropython-stubber



`pip install micropython-stubber`

## Create a folder and a `pyproject.toml` file

This folder is where stubber will store the various files and repos 

Check the configuration with `stubber show-config`

```
14:12:36 | INFO     | cli                - micropython-stubber 1.19.0
14:12:36 | INFO     | config_cmd         - config file                D:\test\pyproject.toml
14:12:36 | INFO     | config_cmd         - CONFIG.repo_path           repos
14:12:36 | INFO     | config_cmd         - CONFIG.mpy_path            repos\micropython
14:12:36 | INFO     | config_cmd         - CONFIG.mpy_lib_path        repos\micropython-lib
14:12:36 | INFO     | config_cmd         - CONFIG.mpy_stubs_path      repos\micropython-stubs
14:12:36 | INFO     | config_cmd         - CONFIG.stub_path           repos\micropython-stubs\stubs
14:12:36 | INFO     | config_cmd         - CONFIG.publish_path        repos\micropython-stubs\publish
14:12:36 | INFO     | config_cmd         - CONFIG.template_path       repos\micropython-stubs\publish\template
```

## Clone the micropython source repos and the micropython-stubs repos

In order to create and merge the mcu-stub to a complete stub package, the stubber needs the micropython source code and the micropython-stubs repo.

Run: `stubber clone --add-stubs`

# Run the mcu stubber

Note that this will attempt to stub all connected boards.  
TODO: Currently there is no option to specify a single board/serial port , but that would be useful

```shell
# switch to the appropriate version of micropython
stubber switch preview
# optionally also check out a specific branch in ./repos/micropython

# run the mcu stubber on all or a specific boards
# stubber get-mcu-stubs 
stubber get-mcu-stubs --serial /dev/ttyUSB1
```



This will : 

- run the mcu stubber on the attached board

- copy the mcu-stubs to `repos/micropython/stubs/micropython/stubs/....`

- merge the mcu stubs with the docstubs, and frozen stubs for that board

- create a publication package in `repos/micropython/stubs/micropython/publish/....`

## check results

You should then find the prepared stubs package under the `micropython-stubs/publish` folder 



for example: `repos/micropython-stubs/publish/micropython-v1_22_2-samd-seeed_wio_terminal-stubs`

The folder naming convention is `micropython-<flat_version>-<port>-<BOARD_ID>-stubs`

## Install the stubs to a typing folder to use in your IDE

`pip install repos/micropython-stubs/publish/micropython-v1_22_2-samd-seeed_wio_terminal-stubs --target ./typings --no-user`

## Create a PR to the micropython-stubs repo

If you have added stubs for a board or version that is not yet in the micropython-stubs repo, please create a PR to the repo.




