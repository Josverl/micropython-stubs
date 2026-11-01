# Type checker test report

    This is a report of the MicroPython type stubs using different type checkers.

    It organizes the test results by version of the micropython stubs and type checker, 
    and includes links to more detailed failure information for failed tests.
    

## stdlib / no version

| Test | mypy | pyrefly | pyright | ruff | ty | zuban |
| --- | --- | --- | --- | --- | --- | --- |
| stdlib stdlib_only | <span style="color: #1a7f37; font-weight: 600">PASS</span> | <span style="color: #1a7f37; font-weight: 600">PASS</span> | <span style="color: #1a7f37; font-weight: 600">PASS</span> | <span style="color: #1a7f37; font-weight: 600">PASS</span> | <span style="color: #16ef71; font-weight: 600">XPASS</span> | <a href="typecheck_report_zuban.md#typecheck-detail-zuban-c3a186f04ce3"><span style="color: #9a6700; font-weight: 600">XFAIL</span></a> |

## NotSetType.token

| Test | mypy | pyrefly | pyright | ruff | ty | zuban |
| --- | --- | --- | --- | --- | --- | --- |
| NotSetType.token NotSetType.token | <span style="color: #6e7781; font-weight: 600">SKIP</span> | <span style="color: #6e7781; font-weight: 600">SKIP</span> | <span style="color: #6e7781; font-weight: 600">SKIP</span> | <span style="color: #6e7781; font-weight: 600">SKIP</span> | <span style="color: #6e7781; font-weight: 600">SKIP</span> | <span style="color: #6e7781; font-weight: 600">SKIP</span> |
