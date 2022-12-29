# Order of the stub folders

The stubs can be used by different components in your development environment.
 1. the VSCode Pylance Language Server
 2. the VSCode Python add-in
 3. and optionally by an additional [Python linter](https://code.visualstudio.com/docs/python/linting#_specific-linters) such as pylint or mypy.
 
These  tools work together to provide code completion/prediction, type checking and all the other good things.
For this the order in which these tools use  the stub folders is significant, and best results are when they use the same order. 
( Note that the different tools will not always agree, MyPy might show a warning where PyLance understands the intent of your code, and vice-versa )

In most cases the best results are achieved by the below setup:

```{mermaid}
sequenceDiagram
    participant Pylance
    autonumber
    Pylance --x Source code: check 
    rect rgba(0, 0, 255, .3)
    Pylance --x CPython stubs: check 
    Pylance --x Frozen stubs: check 
    Pylance --x Doc Stubs: check 
    Pylance ->>+Board Stubs: check
    Board Stubs ->>-Pylance: return info 
    end
```
