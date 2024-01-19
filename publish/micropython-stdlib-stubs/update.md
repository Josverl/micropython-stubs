This is a short description of the steps taken to create or update the stubs for the micropython-stdlib-stubs distribution.
There may be some steps and details missing as I have not documented the process as I went along.

1. copy typeshed/stdlib (from python/typeshed pyright fallback)
    ( I used a different version than listed here, but the process should be the same )
    - ...\.vscode\extensions\ms-python.vscode-pylance-2023.12.1\dist\typeshed-fallback\stdlib
    - to ...\micropython-stdlib-stubs\stdlib

2. Keep only the following packages 
    - [ ] `_typeshed`,
    - [ ] `asyncio`,
    - [ ] `collections`,
    - [ ] `sys`,
    - [ ] `os`,
    - [ ] `__future__`,
    - [ ] `_ast`,
    - [ ] `_codecs`,
    - [ ] `_collections_abc`,
    - [ ] `_decimal`,
    - [ ] `abc`,
    - [ ] `builtins`,
    - [ ] `io`,
    - [ ] `re`,
    - [ ] `socket`,
    - [ ] `sys`,
    - [ ] `types`,
    - [ ] `typing_extensions`,
    - [ ] `typing`,
    - [ ] `ssl`,
    - [ ] `enum`,
    - [ ] `functools`,
    - [ ] `queue`,
    - [ ] `selectors`,
    - [ ] `sre_compile`,
    - [ ] `sre_constants`,
    - [ ] `sre_parse`,

    - remove all other folders (27-ish folders)

3. Merge the docstubs into the stdlib stubs 
    
    * Use `enrich_folder` to add the docstrings to the stubs, without overwriting the parameter names and types. This may need to be repeated for modules that are sperated into multiple files.
    * opdate the exported names ( `__all__` ) to include the newly added names


    Note that this may lead to some differences between the stubs and the actual implementation.


4.  may need some manual / automated editing of the stubs
    - remove CPython specific attributes that are not supported by micropython



4.  format the stubs with black and autoflake






