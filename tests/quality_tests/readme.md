# Validation Snippets

This folder contains a collection of code snippets to help validate the quality of the stubs by providing some code to validate.
Think of this as 'End to End' tests or integration tests for the stubs.


Please read : https://typing.readthedocs.io/en/latest/source/quality.html#testing-using-assert-type-and-warn-unused-ignores

## Usage

Note: In order to get the correct typechecking for each of the folders/mcu architectures,  
you should open/add this folder to a VSCode workspace workspace or open it in a seperate VSCode window

You can update / install the type-stubs in the various typings folders by running the following command:

```powershell
# Update the type stubs
# , "v1.18.0", "v1.17.0"
foreach ($version in @( "latest","v1.21.0", "v1.20.0", "v1.19.1" )) {
    stubber get-docstubs --version $version
    stubber get-frozen --version $version
    stubber merge --version $version --port auto --board auto
    stubber build --version $version --port auto --board auto
}


```	

stubber switch latest
stubber get-docstubs 
stubber merge --version latest
stubber build --version latest

.\snippets\install-stubs.ps1
```
## Test with pytest

There is a custom pytest configuration in `conftests.py` that will automatically download and copy the relevant stubs to the `typings` folder in the various `check_xxxx` and  `feat_yyyy` folders.

The configuration of these test is part of the `test_snippets.py` file in the `snippets` folder.

Example of running the tests:
- run all tests (using any cached stubs - Max lifetime = 24 Hr) :  
  `pytest ./snippets`

- run all tests - but clear the cache first : :  
  `pytest ./snippets --cache-clear`

- run a single test :  
  `pytest snippets\test_snippets.py::test_pyright[local-v1.20.0-stm32-stdlib]`

- run a single test but clear the cache first : :  
  `pytest --cache-clear snippets\test_snippets.py::test_pyright[local-v1.20.0-stm32-stdlib]`

## Test with pyright (used by the Pylance VSCode extension)

```powershell	
.\snippets\check-stubs.ps1
```


### Naming convention

Use the same top-level name for the module / package you would like to test.
Use the `check_${thing}.py` naming pattern for individual test files.

By default, test cases go into a file with the same name as the stub file, prefixed with `check_`.
For example: `stdlib/check_contextlib.py`.

If that file becomes too big, we instead create a directory with files named after individual objects being tested.
For example: `stdlib/builtins/check_dict.py`.


### How the tests work
Below is a relevant section from pypy's testing readme.md

The code in this directory is not intended to be directly executed. Instead,
type checkers are run on the code, to check that typing errors are
emitted at the correct places.

Some files in this directory simply contain samples of idiomatic Python, which
should not (if the stubs are correct) cause a type checker to emit any errors.

Many test cases also make use of
[`assert_type`](https://docs.python.org/3.11/library/typing.html#typing.assert_type),
a function which allows us to test whether a type checker's inferred type of an
expression is what we'd like it be.

Finally, some tests make use of `# type: ignore` comments (in combination with
mypy's
[`--warn-unused-ignores`](https://mypy.readthedocs.io/en/stable/command_line.html#cmdoption-mypy-warn-unused-ignores)
setting and pyright's
[`reportUnnecessaryTypeIgnoreComment`](https://github.com/microsoft/pyright/blob/main/docs/configuration.md#type-check-diagnostics-settings)
setting) to test instances where a type checker *should* emit some kind of
error, if the stubs are correct. Both settings are enabled by default for the entire
subdirectory.

For more information on using `assert_type` and
`--warn-unused-ignores`/`reportUnnecessaryTypeIgnoreComment` to test type
annotations,
[this page](https://typing.readthedocs.io/en/latest/source/quality.html#testing-using-assert-type-and-warn-unused-ignores)
provides a useful guide.

## Caching of packages

In order to reducte the time needed to run the tests of the snippets, we cache the packages in the `.pytest_cache` folder.
this makes use of the `pytest_cache` plugin : https://pypi.org/project/pytest-cache/

The cache lifetime for each package is 24 hours, after which it will be re-downloaded.
The cache can be cleared by:
 -  running the following command: `pytest --clearcache`
 - deleting the `.pytest_cache` folder
 - By pressing the 'refresh-test' 🔄️ button in the test explorer. 
   Note:  This is a side-effect/bug of the current version (v2023.18.0) of the python explorer extension.

