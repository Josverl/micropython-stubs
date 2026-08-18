# Stub QA testing (Validation Snippets)

<!-- Origin: tests/quality_tests/readme.md -->
This folder contains a collection of code snippets to help validate the quality of the stubs by providing some code to validate.
Think of this as 'End to End' tests or integration tests for the stubs.


Please read : https://typing.readthedocs.io/en/latest/source/quality.html#testing-using-assert-type-and-warn-unused-ignores

## Usage

Note: In order to get the correct typechecking for each of the folders/mcu architectures,  
you should open/add this folder to a VSCode workspace workspace or open it in a seperate VSCode window

You can update / install the type-stubs in the various `typings` folders using the [`just`](https://just.systems) recipes from the repo root (these run on both Windows and Ubuntu):

```console
# build all stubs (doc + frozen + merge + build, all ports) + stdlib for one version
just update_stubs v1.28.0

# or build stubs for a single port only (default port is rp2)
just port rp2 v1.28.0

# repeat for each version you want available in the typings folders
just update_stubs v1.27.0
just update_stubs v1.26.1
```

> Note: when running the snippet tests with pytest, the required stubs are installed
> automatically (see [Test with pytest](#test-with-pytest) below), so you normally
> don't need to build them by hand.

## Test with pytest

There is a custom pytest configuration in `conftest.py` that will automatically download and copy the relevant stubs to the `typings` folder in the various `check_xxxx` and  `feat_yyyy` folders.

The tests themselves live in `test_snippets.py` (pyright, mypy, ruff, and pyrefly/ty as `xfail` since they are experimental), with `test_mypy.py`, `test_ruff.py` and `test_pyrefly.py` covering their dedicated feature folders. All snippet tests are marked with the `snippets` marker.

### Using `just`

The most common test runs are available as [`just`](https://just.systems) recipes (see the `justfile` in the repo root). Each recipe accepts extra pytest arguments (e.g. `--cache-clear`, `-x`, `-k ...`):

| Recipe | Runs |
| --- | --- |
| `just test` | all snippet tests (default versions) |
| `just test-stable` | current stable release only (`--stable-only`) |
| `just test-preview` | most recent preview build (`--preview-only`) |
| `just test-recent` | last 3 stable `major.minor` releases (`--recent-majors`) |
| `just test-linter [pyright\|mypy\|ruff\|pyrefly\|ty]` | a single linter on the stable release (default: `pyright`) |
| `just test-version [v1.28.0]` | a specific version (default: `v1.28.0`) |

```powershell
# examples
just test --cache-clear
just test-stable -k mypy
just test-linter mypy -x
just test-version v1.27.0

# run a single test file with all its linters, stable release only
# (the file path is passed straight through to pytest)
just test-stable tests/quality_tests/test_stdlib_only.py
```

The sections below document the underlying pytest options in case you need finer control.

### Running with pytest directly

Example of running the tests:
- run all snippet tests (using any cached stubs - Max lifetime = 24 Hr) :  
  `pytest -m snippets`

- run all snippet tests - but clear the cache first :  
  `pytest -m snippets --cache-clear`

- run a single test (node id format is `test_typecheck[<stub_source>-<version>-<portboard>-<feature>-<linter>]`) :  
  `pytest "test_snippets.py::test_typecheck[local-v1.28.0-stm32-stdlib-pyright]"`

- run a single test but clear the cache first :  
  `pytest --cache-clear "test_snippets.py::test_typecheck[local-v1.28.0-stm32-stdlib-pyright]"`

## Command-line options

The suite adds a few custom options (see `conftest.py`):

| Option | Description |
| --- | --- |
| `--no-cache` | Disable the 24-hour stub-installation cache and always reinstall the stubs. |
| `--stable-only` | Only run tests for the current **stable** MicroPython release. |
| `--preview-only` | Only run tests for the most recent **preview** MicroPython version. |
| `--recent-majors` | Only run tests for the last 3 stable `major.minor` releases (excludes preview). |

## Version selection

By default the tests run against the last 3 stable `major.minor` releases. The resolved
version list is cached for 24h in `.versions_cache.json` so that all `pytest-xdist`
workers agree on the same parametrization matrix. Use the options above to narrow the set:

```powershell
# only the current stable release (fastest)
pytest -m snippets --stable-only

# only the most recent preview build
pytest -m snippets --preview-only

# the last 3 stable major.minor releases (default behaviour, made explicit)
pytest -m snippets --recent-majors
```

To target one specific version, filter the parametrized version id with `-k`:

```powershell
# run every linter, but only for v1.28.0
pytest -m snippets -k "v1.28.0"
```

## Running specific linter(s)

Each snippet is checked by `pyright`, `mypy` and `ruff`, plus `pyrefly` and `ty` marked as `xfail`
since they are experimental. `pyrefly` also runs against its own dedicated feature folder (see
`test_pyrefly.py`). Because the linter name is part of the test node id, you can select linters
with `-k` or by running the dedicated test files:

```powershell
# only pyright
pytest -m snippets -k "pyright"

# only mypy and ruff
pytest -m snippets -k "mypy or ruff"

# a specific version with a single linter
pytest -m snippets --stable-only -k "pyright"
pytest -m snippets -k "v1.28.0 and mypy"

# run the dedicated mypy / ruff / pyrefly feature suites
pytest tests/quality_tests/test_mypy.py -m snippets
pytest tests/quality_tests/test_ruff.py -m snippets
pytest tests/quality_tests/test_pyrefly.py -m snippets
```

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

Finally, some tests make use of :
 - `# type: ignore`         both pyright and mypy ignore errors on this line
 - `# pyright: ignore`      pyright ignores errors on this line
 
  comments (in combination withmypy's
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

In order to reduce the time needed to run the tests of the snippets, we cache the packages in the `.pytest_cache` folder.
this makes use of the `pytest_cache` plugin : https://pypi.org/project/pytest-cache/

The cache lifetime for each package is 24 hours, after which it will be re-downloaded.
The cache can be cleared by:
 -  running the following command: `pytest --clearcache`
 - deleting the `.pytest_cache` folder

