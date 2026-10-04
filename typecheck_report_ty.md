# ty failures and expected failures

[Back to type checker test report](typecheck_report.md)

<a id="typecheck-detail-ty-9e9dc80bf0e3"></a>
## v1.28.0 webassembly webassembly - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.28.0-webassembly-webassembly-ty]

```text
ty found 9 errors and 0 warnings in 5 files.
assert 8 == 0

"check_pyscript/check_config.py"(3,5): unresolved-import: Cannot resolve imported module `pyscript.context`
"check_pyscript/check_ffi_storage.py"(22,31): invalid-assignment: Object of type `Storage` is not assignable to `Preferences`
"check_pyscript/check_ffi_storage.py"(22,60): invalid-argument-type: Argument to function `storage` is incorrect: Expected `type[Storage]`, found `<class 'Preferences'>`
"check_pyscript/check_ffi_storage.py"(23,4): invalid-assignment: Cannot assign to a subscript on an object of type `Preferences`
"check_pyscript/check_modules.py"(16,22): too-many-positional-arguments: Too many positional arguments to bound method `Event.remove_listener`: expected 1, got 2
"check_pyscript/check_modules.py"(18,58): unknown-argument: Argument `indent` does not match any known parameter of function `stringify`
"check_pyscript/check_web.py"(53,4): not-subscriptable: Cannot delete subscript on object of type `Style` with no `__delitem__` method
"check_pyscript/check_web.py"(55,0): unresolved-attribute: Object of type `Classes` has no attribute `discard`
```
