"""Check const() without importing it from micropython."""
# # ref https://github.dev/microsoft/pyright/blob/3cc4e6ccdde06315f5682d9cf61c51ce6fac2753/docs/builtins.md#L7
# pyright 1.1.218+ can handle this
# TODO: mypy: cannot add builtins AFAIK

FOO = const(11) #stubs-ignore : linter=="mypy"
# false test outcome : https://github.com/Josverl/micropython-stubber/issues/429
