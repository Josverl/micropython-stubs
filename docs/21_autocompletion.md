# Use Auto completion and documentation popups

These are first things that you can benefit from,

**If you:**

- Use a modern Editor or IDE that supports Python static type checking

- Install the MicroPython stubs on you computer (not on the MCU)

- Add some basic configuration to your Editor

**You will get:**

- MicroPython specific auto completion, of arguments and things like board specific Pin names

- Tooltips with documentation of the MicroPython stdlib and included modules , specific to you port and board

- Direct feedback or errors if you provide incorrect parameters to functions or methods

TODO: Add code sampled / gifs of unannotated code 

# Static Type checking with MicroPython

Static Type checking builds on the auto completion,

**If you also: **

- Add typing annotations to your micropython code

- Add the typing libraries to your MCU by either:
  
  - add them to your src folder
  
  - `mip install typing.py/.mpy to your MCU`

- Run a Python type checker such a pylance, pyright or mypy

You will can also benefit from

- Find and correct errors before they occur

- < add common STC benefits>....
