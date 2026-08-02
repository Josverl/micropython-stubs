# Vendored MicroPython libraries

These modules are copied into the container's `/usr/lib/micropython` folder by the
`copy_mpy_typings_fx` fixture in `tests/quality_tests/test_typings.py`, alongside the
`mip/typing*.py|.mpy` and `mip/abc.py|.mpy` modules under test.

| module     | source                                                                              |
| ---------- | ----------------------------------------------------------------------------------- |
| `unittest` | micropython-lib `python-stdlib/unittest`, branch `unittest_expectedfailure_direct`    |
| `__future__` | micropython-lib `python-stdlib/__future__` - declared as a dependency in `mip/typing.json` |

The vendored `unittest` is used instead of the released micropython-lib package because
the ported runtime tests rely on `@unittest.expectedFailure`, which is not in a release yet.
