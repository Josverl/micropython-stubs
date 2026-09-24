# pyright failures and expected failures

[Back to type checker test report](typecheck_report.md)

<a id="typecheck-detail-pyright-1fa048b7f28a"></a>
## v1.29.0 webassembly webassembly - FAIL

**Test specification:**
> pytest tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-webassembly-webassembly-pyright]

```text
pyright found 15 errors and 0 warnings in 15 files.
assert 15 == 0

"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w0/check_pyscript/check_config.py"(8,20): No parameter named "target"
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w0/check_pyscript/check_config.py"(8,36): No parameter named "append"
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w0/check_pyscript/check_ffi_storage.py"(23,4): "__setitem__" method not defined on type "Preferences"
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w0/check_pyscript/check_html.py"(11,37): No parameter named "target"
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w0/check_pyscript/check_html.py"(29,3): Cannot assign to attribute "onopen" for class "WebSocket"
  Attribute "onopen" is unknown
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w0/check_pyscript/check_html.py"(30,3): Cannot assign to attribute "onmessage" for class "WebSocket"
  Attribute "onmessage" is unknown
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w0/check_pyscript/check_html.py"(31,3): Cannot assign to attribute "onclose" for class "WebSocket"
  Attribute "onclose" is unknown
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w0/check_pyscript/check_modules.py"(16,22): Expected 0 positional arguments
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w0/check_pyscript/check_pyworker.py"(5,23): No parameter named "target"
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w0/check_pyscript/check_pyworker.py"(5,40): No parameter named "append"
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w0/check_pyscript/check_when.py"(10,15): Expected 1 positional argument
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w0/check_pyscript/check_when.py"(18,15): Expected 1 positional argument
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w0/check_pyscript/check_when.py"(28,14): Expected 1 positional argument
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w0/check_pyscript/check_workers.py"(6,19): Arguments missing for parameters "x2", "x3"
"/tmp/pytest-of-vscode/pytest-15/popen-gw0/test_typecheck_local_v1_29_0_w0/check_pyscript/check_workers.py"(6,68): No parameter named "type"
```
