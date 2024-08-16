(install-stubs)=
# Install the micropython-stubs

There are two main ways to install the stubs into your environment:


## 1: Install to `typings` folder

Store the stubs in a folder in your repo or somewhere else on a disk, the default for this is a `typings` folder in the root of your project.
   The advantage is that this method works without even needing Python (the full CPython) on your computer.
   Also if you have multiple projects using the same version of the same stubs , you can use symlinks to save a few cents on hard drive space.
   Removing the stubs is simple - you can just delete the typings folder.

### Install the stubs in a `typings` folder within your project:
   
   ```bash
   pip install -U micropython-<port>[-<board>]stubs --no-user --target ./typings
   ```

### Enjoy enhanced code completion and type checking!

## 2: Install in a Virtual Environment

Install the stubs into your active python virtual environment (venv) 
If you use Python on your host computer and use venv (or virtualenv) you can install the stubs into that same venv.
most IDEs and tools will use the stubs in that environment when they detect it. 
Removing the stubs is done using `pip uninstall ...` 


A Python virtual environment keeps dependencies separate for different projects.
To create and activate a virtual environment in your project directory, follow these steps:

(activate_venv)=
### Activate your virtual environment.

### For Linux/Mac:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### For Windows:

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### Install the stubs in the virtual environment:

```bash

1. ```bash
   pip install -U micropython-<port>[-<board>]stubs --no-user
   ```

```bash
pip install -U micropython-stm32-stubs --target typings --no-user

# Install stubs for a specific version.
pip install -U micropython-esp32-stubs==1.20.0.* --target typings --no-user

# Install stubs for a specific board.
pip install -U micropython-rp2-pico_w-stubs --target typings --no-user
```
See [](project:#install-stubs) for more details and examples.

<!-- :::{admonition} **Requirements File** -->
:::{tip} 
**Requirements File**

Consider adding a `requirements-dev.txt` file to your project with the specified stubs. It’ll help keep your development environment consistent.


```
#requirements-dev.txt
micropython-esp32-stubs~=1.23.0
```

Then install the stubs with `pip install -r requirements-dev.txt --target typings`.	

:::


