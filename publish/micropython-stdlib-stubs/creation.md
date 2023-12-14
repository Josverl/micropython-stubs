This is a short description of the steps taken to create the stubs for the micropython-stdlib-stubs distribution.
There may be some steps and details missing as I have not documented the process as I went along.

1. copy typeshed/stdlib (from pyright fallback)
    ( I used a different version than listed here, but the process should be the same )
    - ...\.vscode\extensions\ms-python.vscode-pylance-2023.12.1\dist\typeshed-fallback\stdlib
    - to ...\micropython-stdlib-stubs\stdlib

2. Keep only the following **sub folders** / packages 
    - [ ] `_typeshed`
    - [ ] `asyncio`
    - [ ] `collections`
    - [ ] `os`

    - remove all other folders (28-ish folders)

3. Rename the stubs that are used internally, but are not part of micropython
    with two leading underscores ( __ ) 
    NOTE: rename them in vscode to that the files that reference them get automagically refactored 
    - [ ] `codecs.pyi`         --> `__codecs.pyi`
    - [ ] `contextlib.pyi`     --> `__contextlib.pyi`
    - [ ] `contextvars.pyi`    --> `__contextvars.pyi`
    - [ ] `dataclasses.pyi`    --> `__dataclasses.pyi`
    - [ ] `decimal.pyi`        --> `__decimal.pyi`
    - [ ] `enum.pyi`           --> `__enum.pyi`
    - [ ] `fractions.pyi`      --> `__fractions.pyi`
    - [ ] `functools.pyi`      --> `__functools.pyi`
    - [ ] `numbers.pyi`        --> `__numbers.pyi`
    - [ ] `queue.pyi`          --> `__queue.pyi`
    - [ ] `selectors.pyi`      --> `__selectors.pyi`
    - [ ] `sre_compile.pyi`    --> `__sre_compile.pyi`
    - [ ] `sre_constants.pyi`  --> `__sre_constants.pyi`
    - [ ] `sre_parse.pyi`      --> `__sre_parse.pyi`

4. Remove all stubs and stub-only packages that are not in micropython
    Keep only the following: 
    - [ ] All `__<package>.pyi` from step 3 
    - [ ] `__future__.pyi`
    - [ ] `_ast.pyi`
    - [ ] `_codecs.pyi`
    - [ ] `_collections_abc.pyi`
    - [ ] `_decimal.pyi`
    - [ ] `abc.pyi`
    - [ ] `builtins.pyi`
    - [ ] `io.pyi`
    - [ ] `re.pyi`
    - [ ] `socket.pyi`
    - [ ] `sys.pyi`
    - [ ] `types.pyi`
    - [ ] `typing_extensions.pyi`
    - [ ] `typing.pyi`







