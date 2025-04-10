# Static Type Checking of MicroPython code

Static type checking in Python strikes a balance between early error detection and code readability. While it has some downsides, its benefits often outweigh the drawbacks, especially in larger projects or .
When MicroPython code is compiled to .mpy or frozen into a firmware, the microcode size does *not* increase with type hints, so there is no adverse effect on the memory footprint of the code.

## What is Static Type Checking?
   Static type checking involves specifying the types of variables and function parameters at compile time or during development. Unlike dynamic typing, where types are determined at runtime, static type checking helps catch errors early by ensuring that variables adhere to their declared types.

### Advantages:
   - Early Error Detection: Static type checking catches type-related issues before running the code, reducing runtime errors.
   - Performance Optimization: Compiled code with known types can be optimized for speed and memory usage⁵.
   - Enhanced Code Readability: Type hints improve code documentation and make it easier for developers to understand and maintain the codebase.
   - Tool Support: Tools like [Mypy](mypy) and [Pyright](pyright) provide static type checking for Python, aiding developers in identifying type inconsistencies¹.
   - Refactoring: Static type checking helps identify type-related issues during refactoring, making code changes safer and more predictable.
   - API Documentation: Type hints serve as documentation for function signatures, making it easier to understand how to use them¹.

### Disadvantages:
   - Verbose Syntax: Adding type hints can make code more verbose, especially for complex data structures.
   - Learning Curve: Developers need to learn type hinting syntax and conventions.
   - Flexibility Trade-off: Static typing restricts flexibility, as it requires specifying types explicitly.
   - False Positives: Some type checkers may produce false positives, flagging valid code as erroneous².

### When to Use Static Type Checking?
   - Large Projects: For large and complex projects, static type checking significantly reduces maintenance overhead.
   - Collaboration: When working in teams, type hints enhance collaboration and reduce misunderstandings.
   - Critical Code Paths: Use static type checking for critical parts of your application to prevent subtle bugs.

## Alternative Method: Static Type Checking without a Typing Module

In some cases, you may want to perform static type checking without using a typing module. This can be achieved using the `TYPE_CHECKING` constant and conditional imports. This method allows you to include type hints and imports only when performing static type checking, without affecting the runtime behavior of your code.

### Example

```python
from machine import I2C

TYPE_CHECKING = False
if TYPE_CHECKING:
    from enum import IntEnum
    from typing import Optional
else:
    IntEnum = object
    Optional = object

class AW210xxRegisters(IntEnum):
    """
    Enum for all registers on a AW210xx. Any _BASE registers represent the
    0th register with that name, the number of additional registers
    is dependent on model
    """
    # Example register definitions
    REG1 = 0x00
    REG2 = 0x01

def get_register_name(register: int) -> Optional[str]:
    if register == AW210xxRegisters.REG1:
        return "Register 1"
    elif register == AW210xxRegisters.REG2:
        return "Register 2"
    else:
        return None
```

In this example, the `TYPE_CHECKING` constant is set to `False` by default. When performing static type checking, you can set `TYPE_CHECKING` to `True` to include the type hints and imports. This allows you to use type hints and perform static type checking without requiring the `typing` module at runtime.


## Positional and keyword parameter types 

Based on [PEP-570](https://peps.python.org/pep-0570/)


While MicroPython does not support the full range of Python's function parameter types at runtime ,
it does make sense to support some of them in static type checking.

In type stubs the following function signature is used to indicate the types of parameters:

```python

def name(positional_only_parameters, /, positional_or_keyword_parameters,
         *, keyword_only_parameters):
    ...

```

The following would apply:

- All parameters left of the `/` are treated as positional-only.
- If `/` is not specified in the function definition, that function does not accept any positional-only arguments.
- The logic around optional values for positional-only parameters remains the same as for positional-or-keyword parameters.
- Once a positional-only parameter is specified with a default, the following positional-only and positional-or-keyword parameters need to have defaults as well.
- Positional-only parameters which do not have default values are required positional-only parameters.

As guidance:

Use positional-only if names do not matter or have no meaning, and there are only a few arguments which will always be passed in the same order.
Use keyword-only when names have meaning and the function definition is more understandable by being explicit with names.
