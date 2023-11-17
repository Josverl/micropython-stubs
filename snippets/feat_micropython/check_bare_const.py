"""Check const() without importing it from micropython."""
# # ref https://github.dev/microsoft/pyright/blob/3cc4e6ccdde06315f5682d9cf61c51ce6fac2753/docs/builtins.md#L7
# OK:  pyright 1.1.218 can handle this

FOO = const(11) 
# false test outcome : https://github.com/Josverl/micropython-stubber/issues/429
