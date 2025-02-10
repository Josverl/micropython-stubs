(pycharm_config)=
# PyCharm Configuration

## Configure PyCharm to use the selected stub folders

PyCharm supports Python stub files, so the simplest option to enable it to 'understand' MicroPython is to install the micropython-stubs for your port/board from PyPi.  

```{figure} img/pycharm-completion-2.png

Example of code completion in Pycharm
```
<!-- TODO : Add GIF with some additional samples -->
## Install the stubs from PyPi.

Install the stubs as documented in [](project:#install-stubs)

Example: `pip install -U micropython-stm32-stubs==1.19.1.*`

If you have a `requirements-dev.txt` file you can add the stubs to it, and PyCharm will offer to install them automatically into the project's environment

```text
# requirements-dev.txt
micropython-stm32-stubs==1.19.1.*
```

After this Pycharm will use the stubs it finds in the (virtual) environment to help validate your code and provide hints.

## Check library imports

To check if the correct types are used for your imports you can 'hover' the mouse over the module of an import statement. 
Pycharm will show the module's docstring that will allow you to identify which stub is being used.

```{figure} img/pycharm-import.png
Hover over the import statement to see the module's docstring.
```

:::{note}
Although Pycharm's rendering of the docstrings is somewhat limited compared to VSCode, it  is still quite useful.
<!-- todo: explain what the limitations are -->
:::



### Verify the paths

You can verify the paths used in your project by 

File > Settings > Project Settings 

> Project Structure 

This should list the selected folders with stubs as Source Folders  

```{figure} img/pycharm-settings.png
PyCharm Settings
```	
