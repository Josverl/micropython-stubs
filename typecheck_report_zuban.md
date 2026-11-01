# zuban failures and expected failures

[Back to type checker test report](typecheck_report.md)

<a id="typecheck-detail-zuban-c3a186f04ce3"></a>
## - stdlib stdlib_only - XFAIL

**Test specification:**
> pytest tests/quality_tests/test_stdlib_only.py::test_typecheck_stdlib_only[zuban-local-stdlib_only---stdlib]

```text
zuban found 1364 errors and 0 warnings in 52 files.
assert 1364 == 0

"_mpy_shed/IRQs.pyi"(39,6): Invalid type comment or annotation
"_mpy_shed/__init__.pyi"(49,16): Invalid type comment or annotation
"_mpy_shed/__init__.pyi"(53,10): Invalid type comment or annotation
"_mpy_shed/__init__.pyi"(54,14): Invalid type comment or annotation
"_mpy_shed/__init__.pyi"(58,11): Invalid type comment or annotation
"_mpy_shed/_mp_available.pyi"(36,4): An implementation for an overloaded function is not allowed in a stub file
"_mpy_shed/_mpy_builtins.pyi"(13,6): Invalid type comment or annotation
"_mpy_shed/_mpy_builtins.pyi"(27,56): Invalid type comment or annotation
"_mpy_shed/blockdevice.pyi"(28,30): Invalid type comment or annotation
"_mpy_shed/blockdevice.pyi"(29,22): Invalid type comment or annotation
"_mpy_shed/buffer_mp.pyi"(7,16): Invalid type comment or annotation
"_mpy_shed/buffer_mp.pyi"(8,16): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(104,22): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(105,26): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(118,72): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(124,73): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(131,8): Signatures of "__ior__" and "__or__" are incompatible
"_mpy_shed/collections/__init__.pyi"(131,70): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(133,8): Signatures of "__ior__" and "__or__" are incompatible
"_mpy_shed/collections/__init__.pyi"(133,63): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(156,39): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(162,46): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(163,47): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(164,47): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(165,33): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(166,34): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(167,34): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(172,22): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(173,26): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(192,26): Name "UserString" is not defined
"_mpy_shed/collections/__init__.pyi"(207,59): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(208,35): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(209,39): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(210,40): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(211,41): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(212,33): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(213,34): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(214,36): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(215,44): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(216,28): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(217,26): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(218,48): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(226,46): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(244,47): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(245,23): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(246,50): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(250,63): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(251,63): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(255,9): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(258,47): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(260,50): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(267,49): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(268,26): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(269,23): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(270,39): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(271,23): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(272,35): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(281,22): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(291,26): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(298,39): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(299,50): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(300,29): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(300,41): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(301,40): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(302,41): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(309,52): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(320,22): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(356,57): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(357,57): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(358,57): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(359,56): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(397,22): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(429,8): Signature of "__or__" incompatible with supertype "builtins.dict"
"_mpy_shed/collections/__init__.pyi"(430,54): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(434,55): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(481,26): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(482,22): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(484,8): Signature of "__or__" incompatible with supertype "builtins.dict"
"_mpy_shed/collections/__init__.pyi"(485,54): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(489,55): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(496,70): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(498,25): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(524,22): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(540,54): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(544,55): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(549,8): Signatures of "__ior__" and "__or__" are incompatible
"_mpy_shed/collections/__init__.pyi"(549,70): Invalid type comment or annotation
"_mpy_shed/collections/__init__.pyi"(551,8): Signatures of "__ior__" and "__or__" are incompatible
"_mpy_shed/collections/__init__.pyi"(551,63): Invalid type comment or annotation
"_mpy_shed/io_modes.pyi"(17,23): Invalid type comment or annotation
"_mpy_shed/io_modes.pyi"(51,22): Invalid type comment or annotation
"_mpy_shed/io_modes.pyi"(52,22): Invalid type comment or annotation
"_mpy_shed/io_modes.pyi"(55,15): Invalid type comment or annotation
"_mpy_shed/io_modes.pyi"(57,25): Invalid type comment or annotation
"_mpy_shed/io_modes.pyi"(83,24): Invalid type comment or annotation
"_mpy_shed/io_modes.pyi"(84,24): Invalid type comment or annotation
"_mpy_shed/io_modes.pyi"(85,17): Invalid type comment or annotation
"_mpy_shed/os_vfs.pyi"(6,15): Invalid type comment or annotation
"_mpy_shed/os_vfs.pyi"(23,18): Invalid type comment or annotation
"_mpy_shed/pathlike.pyi"(15,15): Name "ABC" is not defined
"_mpy_shed/time_mp.pyi"(13,13): Invalid type comment or annotation
"_mpy_shed/time_mp.pyi"(14,13): Invalid type comment or annotation
"_mpy_shed/time_mp.pyi"(15,12): Invalid type comment or annotation
"stubs/mypy-extensions/mypy_extensions.pyi"(19,0): Class stubs.mypy-extensions.mypy_extensions._TypedDict has abstract attributes "__getitem__", "__iter__", "__len__"
"stubs/mypy-extensions/mypy_extensions.pyi"(19,17): Metaclass conflict: the metaclass of a derived class must be a (non-strict) subclass of the metaclasses of all its bases
"stubs/mypy-extensions/mypy_extensions.pyi"(26,28): Invalid type comment or annotation
"stubs/mypy-extensions/mypy_extensions.pyi"(28,21): Invalid type comment or annotation
"stubs/mypy-extensions/mypy_extensions.pyi"(33,29): Invalid type comment or annotation
"stdlib/__future__.pyi"(3,14): Invalid type comment or annotation
"stdlib/_asyncio.pyi"(27,34): Can only assign concrete classes to a variable of type "type[Coroutine]"
"stdlib/_asyncio.pyi"(27,45): Can only assign concrete classes to a variable of type "type[Generator]"
"stdlib/_codecs.pyi"(13,10): Invalid type comment or annotation
"stdlib/_codecs.pyi"(14,10): Invalid type comment or annotation
"stdlib/_codecs.pyi"(15,17): Invalid type comment or annotation
"stdlib/_codecs.pyi"(27,23): Invalid type comment or annotation
"stdlib/_codecs.pyi"(46,19): Invalid type comment or annotation
"stdlib/_codecs.pyi"(51,0): Overloaded function signature 2 will never be matched: signature 1's parameter type(s) are the same or broader
"stdlib/_codecs.pyi"(57,0): Overloaded function signature 2 will never be matched: signature 1's parameter type(s) are the same or broader
"stdlib/_codecs.pyi"(61,0): Overloaded function signature 3 will never be matched: signature 1's parameter type(s) are the same or broader
"stdlib/_codecs.pyi"(61,0): Overloaded function signature 3 will never be matched: signature 2's parameter type(s) are the same or broader
"stdlib/_codecs.pyi"(69,0): Overloaded function signature 4 will never be matched: signature 1's parameter type(s) are the same or broader
"stdlib/_codecs.pyi"(69,0): Overloaded function signature 4 will never be matched: signature 2's parameter type(s) are the same or broader
"stdlib/_decimal.pyi"(58,11): Invalid type comment or annotation
"stdlib/_typeshed/__init__.pyi"(50,12): Invalid type comment or annotation
"stdlib/_typeshed/__init__.pyi"(53,8): Invalid type comment or annotation
"stdlib/_typeshed/__init__.pyi"(58,11): Invalid type comment or annotation
"stdlib/_typeshed/__init__.pyi"(101,24): Invalid type comment or annotation
"stdlib/_typeshed/__init__.pyi"(171,9): Invalid type comment or annotation
"stdlib/_typeshed/__init__.pyi"(172,11): Invalid type comment or annotation
"stdlib/_typeshed/__init__.pyi"(173,13): Invalid type comment or annotation
"stdlib/_typeshed/__init__.pyi"(173,43): Type variable "typing.AnyStr" is unbound
"stdlib/_typeshed/__init__.pyi"(174,16): Invalid type comment or annotation
"stdlib/_typeshed/__init__.pyi"(176,22): Invalid type comment or annotation
"stdlib/_typeshed/__init__.pyi"(210,21): Invalid type comment or annotation
"stdlib/_typeshed/__init__.pyi"(211,21): Invalid type comment or annotation
"stdlib/_typeshed/__init__.pyi"(212,14): Invalid type comment or annotation
"stdlib/_typeshed/__init__.pyi"(213,24): Invalid type comment or annotation
"stdlib/_typeshed/__init__.pyi"(239,23): Invalid type comment or annotation
"stdlib/_typeshed/__init__.pyi"(240,23): Invalid type comment or annotation
"stdlib/_typeshed/__init__.pyi"(241,16): Invalid type comment or annotation
"stdlib/_typeshed/__init__.pyi"(247,16): Invalid type comment or annotation
"stdlib/_typeshed/__init__.pyi"(248,20): Invalid type comment or annotation
"stdlib/_typeshed/__init__.pyi"(249,22): Invalid type comment or annotation
"stdlib/_typeshed/__init__.pyi"(275,16): Invalid type comment or annotation
"stdlib/_typeshed/__init__.pyi"(277,17): Invalid type comment or annotation
"stdlib/_typeshed/__init__.pyi"(279,16): Invalid type comment or annotation
"stdlib/_typeshed/__init__.pyi"(281,21): All bases of a protocol must be protocols
"stdlib/_typeshed/__init__.pyi"(284,21): All bases of a protocol must be protocols
"stdlib/_typeshed/__init__.pyi"(294,17): All bases of a protocol must be protocols
"stdlib/_typeshed/__init__.pyi"(297,16): Invalid type comment or annotation
"stdlib/_typeshed/__init__.pyi"(299,9): Invalid type comment or annotation
"stdlib/_typeshed/__init__.pyi"(300,12): Invalid type comment or annotation
"stdlib/_typeshed/__init__.pyi"(331,57): Type expected
"stdlib/_typeshed/__init__.pyi"(335,45): Type expected
"stdlib/_typeshed/__init__.pyi"(338,17): Invalid type comment or annotation
"stdlib/_typeshed/__init__.pyi"(341,15): Invalid type comment or annotation
"stdlib/_typeshed/__init__.pyi"(351,18): Invalid type comment or annotation
"stdlib/_typeshed/__init__.pyi"(352,20): Invalid type comment or annotation
"stdlib/_typeshed/dbapi.pyi"(9,15): Invalid type comment or annotation
"stdlib/_typeshed/dbapi.pyi"(9,27): Unsupported left operand type for | ("object")
"stdlib/_typeshed/dbapi.pyi"(12,24): Invalid type comment or annotation
"stdlib/abc.pyi"(33,42): Can only replace ParamSpec with a parameter types list or another ParamSpec, got "_P"
"stdlib/abc.pyi"(35,42): The first argument to Callable must be a list of types, parameter specification, or "..."
"stdlib/abc.pyi"(38,40): Can only replace ParamSpec with a parameter types list or another ParamSpec, got "_P"
"stdlib/abc.pyi"(40,42): The first argument to Callable must be a list of types, parameter specification, or "..."
"stdlib/array.pyi"(27,14): Invalid type comment or annotation
"stdlib/array.pyi"(28,16): Invalid type comment or annotation
"stdlib/array.pyi"(29,18): Invalid type comment or annotation
"stdlib/array.pyi"(30,11): Invalid type comment or annotation
"stdlib/array.pyi"(94,21): Argument 1 of "extend" is incompatible with supertype "typing.MutableSequence"; supertype defines the argument type as "Iterable[_T]"
"stdlib/array.pyi"(193,23): Argument 1 of "__iadd__" is incompatible with supertype "typing.MutableSequence"; supertype defines the argument type as "Iterable[_T]"
"stdlib/array.pyi"(193,44): Invalid type comment or annotation
"stdlib/array.pyi"(202,41): Invalid type comment or annotation
"stdlib/asyncio/__init__.pyi"(11,6): Cannot find implementation or library stub for module named "asyncio.futures"
"stdlib/asyncio/__init__.pyi"(37,10): Cannot find implementation or library stub for module named "asyncio.unix_events"
"stdlib/asyncio/__init__.pyi"(46,20): Invalid type comment or annotation
"stdlib/asyncio/__init__.pyi"(46,53): Type variable "asyncio._T_co" is unbound
"stdlib/asyncio/__init__.pyi"(46,72): Type variable "asyncio._T_co" is unbound
"stdlib/asyncio/__init__.pyi"(47,20): Invalid type comment or annotation
"stdlib/asyncio/__init__.pyi"(47,53): Type variable "asyncio._T_co" is unbound
"stdlib/asyncio/__init__.pyi"(47,82): Type variable "asyncio._T_co" is unbound
"stdlib/asyncio/base_events.pyi"(5,13): Cannot find implementation or library stub for module named "asyncio.futures"
"stdlib/asyncio/base_events.pyi"(25,10): Invalid type comment or annotation
"stdlib/asyncio/base_events.pyi"(26,19): Invalid type comment or annotation
"stdlib/asyncio/base_events.pyi"(27,18): Invalid type comment or annotation
"stdlib/asyncio/base_events.pyi"(28,13): Invalid type comment or annotation
"stdlib/asyncio/base_events.pyi"(68,64): A function returning TypeVar should receive at least one argument containing the same Typevar
"stdlib/asyncio/base_events.pyi"(79,28): Invalid type comment or annotation
"stdlib/asyncio/base_events.pyi"(80,15): Invalid type comment or annotation
"stdlib/asyncio/base_events.pyi"(86,28): Invalid type comment or annotation
"stdlib/asyncio/base_events.pyi"(87,15): Invalid type comment or annotation
"stdlib/asyncio/base_events.pyi"(104,28): Invalid type comment or annotation
"stdlib/asyncio/base_events.pyi"(105,15): Invalid type comment or annotation
"stdlib/asyncio/base_events.pyi"(108,61): Invalid type comment or annotation
"stdlib/asyncio/base_events.pyi"(108,87): Invalid type comment or annotation
"stdlib/asyncio/base_events.pyi"(463,69): Invalid type comment or annotation
"stdlib/asyncio/base_events.pyi"(463,96): Invalid type comment or annotation
"stdlib/asyncio/base_events.pyi"(465,69): Invalid type comment or annotation
"stdlib/asyncio/base_events.pyi"(465,96): Invalid type comment or annotation
"stdlib/asyncio/base_events.pyi"(479,63): Invalid type comment or annotation
"stdlib/asyncio/base_events.pyi"(479,90): Invalid type comment or annotation
"stdlib/asyncio/base_futures.pyi"(12,6): Cannot find implementation or library stub for module named "asyncio.futures"
"stdlib/asyncio/coroutines.pyi"(22,39): The first argument to Callable must be a list of types, parameter specification, or "..."
"stdlib/asyncio/coroutines.pyi"(22,62): Invalid type comment or annotation
"stdlib/asyncio/coroutines.pyi"(24,39): The first argument to Callable must be a list of types, parameter specification, or "..."
"stdlib/asyncio/coroutines.pyi"(24,55): Invalid type comment or annotation
"stdlib/asyncio/coroutines.pyi"(26,41): Invalid type comment or annotation
"stdlib/asyncio/coroutines.pyi"(27,32): Invalid type comment or annotation
"stdlib/asyncio/events.pyi"(14,6): Cannot find implementation or library stub for module named "asyncio.futures"
"stdlib/asyncio/events.pyi"(18,6): Cannot find implementation or library stub for module named "asyncio.unix_events"
"stdlib/asyncio/events.pyi"(52,10): Invalid type comment or annotation
"stdlib/asyncio/events.pyi"(53,19): Invalid type comment or annotation
"stdlib/asyncio/events.pyi"(54,18): Invalid type comment or annotation
"stdlib/asyncio/events.pyi"(55,13): Invalid type comment or annotation
"stdlib/asyncio/events.pyi"(102,34): Invalid type comment or annotation
"stdlib/asyncio/events.pyi"(120,64): A function returning TypeVar should receive at least one argument containing the same Typevar
"stdlib/asyncio/events.pyi"(139,32): Invalid type comment or annotation
"stdlib/asyncio/events.pyi"(140,19): Invalid type comment or annotation
"stdlib/asyncio/events.pyi"(147,32): Invalid type comment or annotation
"stdlib/asyncio/events.pyi"(148,19): Invalid type comment or annotation
"stdlib/asyncio/events.pyi"(181,32): Invalid type comment or annotation
"stdlib/asyncio/events.pyi"(182,19): Invalid type comment or annotation
"stdlib/asyncio/events.pyi"(190,61): Invalid type comment or annotation
"stdlib/asyncio/events.pyi"(190,87): Invalid type comment or annotation
"stdlib/asyncio/events.pyi"(561,69): Invalid type comment or annotation
"stdlib/asyncio/events.pyi"(561,96): Invalid type comment or annotation
"stdlib/asyncio/events.pyi"(565,69): Invalid type comment or annotation
"stdlib/asyncio/events.pyi"(565,96): Invalid type comment or annotation
"stdlib/asyncio/events.pyi"(587,63): Invalid type comment or annotation
"stdlib/asyncio/events.pyi"(587,93): Invalid type comment or annotation
"stdlib/asyncio/events.pyi"(630,0): Class asyncio.events.BaseDefaultEventLoopPolicy has abstract attributes "get_child_watcher", "set_child_watcher"
"stdlib/asyncio/format_helpers.pyi"(13,11): Invalid type comment or annotation
"stdlib/asyncio/format_helpers.pyi"(18,0): Overloaded function signature 2 will never be matched: signature 1's parameter type(s) are the same or broader
"stdlib/asyncio/locks.pyi"(12,6): Cannot find implementation or library stub for module named "asyncio.futures"
"stdlib/asyncio/micropython.pyi"(30,28): Name "Generator" is not defined
"stdlib/asyncio/mixins.pyi"(10,36): Invalid type comment or annotation
"stdlib/asyncio/sslproto.pyi"(93,22): Invalid type comment or annotation
"stdlib/asyncio/streams.pyi"(32,26): Invalid type comment or annotation
"stdlib/asyncio/streams.pyi"(199,27): Invalid type comment or annotation
"stdlib/asyncio/tasks.pyi"(11,6): Cannot find implementation or library stub for module named "asyncio.futures"
"stdlib/asyncio/tasks.pyi"(71,17): Invalid type comment or annotation
"stdlib/asyncio/tasks.pyi"(71,63): Type variable "asyncio.tasks._T" is unbound
"stdlib/asyncio/tasks.pyi"(71,79): Type variable "asyncio.tasks._T" is unbound
"stdlib/asyncio/tasks.pyi"(72,16): Invalid type comment or annotation
"stdlib/asyncio/tasks.pyi"(97,0): Overloaded function signature 2 will never be matched: signature 1's parameter type(s) are the same or broader
"stdlib/asyncio/tasks.pyi"(397,10): Overloaded function signature 2 will never be matched: signature 1's parameter type(s) are the same or broader
"stdlib/asyncio/tasks.pyi"(432,10): Overloaded function signature 2 will never be matched: signature 1's parameter type(s) are the same or broader
"stdlib/asyncio/tasks.pyi"(443,25): Invalid type comment or annotation
"stdlib/asyncio/tasks.pyi"(443,69): Type variable "asyncio.tasks._T_co" is unbound
"stdlib/asyncio/tasks.pyi"(443,98): Type variable "asyncio.tasks._T_co" is unbound
"stdlib/asyncio/threads.pyi"(10,35): The first argument to Callable must be a list of types, parameter specification, or "..."
"stdlib/asyncio/threads.pyi"(10,54): Variable "asyncio.threads._P" is not valid as a type
"stdlib/asyncio/threads.pyi"(10,73): Variable "asyncio.threads._P" is not valid as a type
"stdlib/asyncio/timeouts.pyi"(14,34): Invalid type comment or annotation
"stdlib/asyncio/trsock.pyi"(12,10): Invalid type comment or annotation
"stdlib/asyncio/trsock.pyi"(13,13): Invalid type comment or annotation
"stdlib/asyncio/trsock.pyi"(14,14): Invalid type comment or annotation
"stdlib/asyncio/trsock.pyi"(15,7): Invalid type comment or annotation
"stdlib/asyncio/trsock.pyi"(93,37): "type" expects no type arguments, but 1 given
"stdlib/builtins.pyi"(109,6): Invalid type comment or annotation
"stdlib/builtins.pyi"(123,56): Invalid type comment or annotation
"stdlib/builtins.pyi"(176,27): "type" expects no type arguments, but 1 given
"stdlib/builtins.pyi"(176,32): Invalid type comment or annotation
"stdlib/builtins.pyi"(178,30): "type" expects no type arguments, but 1 given
"stdlib/builtins.pyi"(180,24): Invalid type comment or annotation
"stdlib/builtins.pyi"(183,26): Argument 1 of "__setattr__" is incompatible with supertype "builtins.object"; supertype defines the argument type as "str"
"stdlib/builtins.pyi"(184,26): Argument 1 of "__delattr__" is incompatible with supertype "builtins.object"; supertype defines the argument type as "str"
"stdlib/builtins.pyi"(185,4): Return type "bool" of "__eq__" incompatible with return type "bool" in supertype "builtins.object"
"stdlib/builtins.pyi"(185,21): Argument 1 of "__eq__" is incompatible with supertype "builtins.object"; supertype defines the argument type as "object"
"stdlib/builtins.pyi"(186,4): Return type "bool" of "__ne__" incompatible with return type "bool" in supertype "builtins.object"
"stdlib/builtins.pyi"(186,21): Argument 1 of "__ne__" is incompatible with supertype "builtins.object"; supertype defines the argument type as "object"
"stdlib/builtins.pyi"(187,4): Return type "str" of "__str__" incompatible with return type "str" in supertype "builtins.object"
"stdlib/builtins.pyi"(188,4): Return type "str" of "__repr__" incompatible with return type "str" in supertype "builtins.object"
"stdlib/builtins.pyi"(189,4): Return type "int" of "__hash__" incompatible with return type "int" in supertype "builtins.object"
"stdlib/builtins.pyi"(190,4): Return type "str" of "__format__" incompatible with return type "str" in supertype "builtins.object"
"stdlib/builtins.pyi"(190,25): Argument 1 of "__format__" is incompatible with supertype "builtins.object"; supertype defines the argument type as "str"
"stdlib/builtins.pyi"(191,31): Argument 1 of "__getattribute__" is incompatible with supertype "builtins.object"; supertype defines the argument type as "str"
"stdlib/builtins.pyi"(192,4): Return type "int" of "__sizeof__" incompatible with return type "int" in supertype "builtins.object"
"stdlib/builtins.pyi"(195,4): Return type "str | tuple[Any]" of "__reduce__" incompatible with return type "str | tuple[Any, ...]" in supertype "builtins.object"
"stdlib/builtins.pyi"(195,34): "tuple" expects 1 type argument, but 2 given
"stdlib/builtins.pyi"(195,45): Unexpected "..."
"stdlib/builtins.pyi"(196,4): Return type "str | tuple[Any]" of "__reduce_ex__" incompatible with return type "str | tuple[Any, ...]" in supertype "builtins.object"
"stdlib/builtins.pyi"(196,65): "tuple" expects 1 type argument, but 2 given
"stdlib/builtins.pyi"(196,76): Unexpected "..."
"stdlib/builtins.pyi"(200,4): Return type "Iterable[str]" of "__dir__" incompatible with return type "Iterable[str]" in supertype "builtins.object"
"stdlib/builtins.pyi"(205,27): Free type variable expected in Generic[...]
"stdlib/builtins.pyi"(205,31): Duplicate type variables in Generic[...] or Protocol[...]
"stdlib/builtins.pyi"(207,35): The first argument to Callable must be a list of types, parameter specification, or "..."
"stdlib/builtins.pyi"(210,35): The first argument to Callable must be a list of types, parameter specification, or "..."
"stdlib/builtins.pyi"(212,66): The first argument to Callable must be a list of types, parameter specification, or "..."
"stdlib/builtins.pyi"(222,30): Free type variable expected in Generic[...]
"stdlib/builtins.pyi"(222,34): Duplicate type variables in Generic[...] or Protocol[...]
"stdlib/builtins.pyi"(224,35): The first argument to Callable must be a list of types, parameter specification, or "..."
"stdlib/builtins.pyi"(227,35): The first argument to Callable must be a list of types, parameter specification, or "..."
"stdlib/builtins.pyi"(231,45): "type" expects no type arguments, but 1 given
"stdlib/builtins.pyi"(231,70): The first argument to Callable must be a list of types, parameter specification, or "..."
"stdlib/builtins.pyi"(242,15): "tuple" expects 1 type argument, but 2 given
"stdlib/builtins.pyi"(242,27): Unexpected "..."
"stdlib/builtins.pyi"(255,25): "tuple" expects 1 type argument, but 2 given
"stdlib/builtins.pyi"(255,37): Unexpected "..."
"stdlib/builtins.pyi"(265,41): "tuple" expects 1 type argument, but 2 given
"stdlib/builtins.pyi"(265,53): Unexpected "..."
"stdlib/builtins.pyi"(270,11): The erased type of self "builtins.type" is not a supertype of its class "type[builtins.type]"
"stdlib/builtins.pyi"(270,13): "type" expects no type arguments, but 1 given
"stdlib/builtins.pyi"(270,53): "tuple" expects 1 type argument, but 2 given
"stdlib/builtins.pyi"(270,65): Unexpected "..."
"stdlib/builtins.pyi"(280,47): "tuple" expects 1 type argument, but 2 given
"stdlib/builtins.pyi"(280,59): Unexpected "..."
"stdlib/builtins.pyi"(295,18): Invalid type comment or annotation
"stdlib/builtins.pyi"(296,18): Invalid type comment or annotation
"stdlib/builtins.pyi"(301,54): Invalid type comment or annotation
"stdlib/builtins.pyi"(303,76): Invalid type comment or annotation
"stdlib/builtins.pyi"(304,34): "tuple" expects 1 type argument, but 2 given
"stdlib/builtins.pyi"(304,45): Invalid type comment or annotation
"stdlib/builtins.pyi"(308,22): Invalid type comment or annotation
"stdlib/builtins.pyi"(312,29): Invalid type comment or annotation
"stdlib/builtins.pyi"(334,23): Invalid type comment or annotation
"stdlib/builtins.pyi"(337,13): Invalid type comment or annotation
"stdlib/builtins.pyi"(348,43): "tuple" expects 1 type argument, but 2 given
"stdlib/builtins.pyi"(355,44): "tuple" expects 1 type argument, but 2 given
"stdlib/builtins.pyi"(357,25): Invalid type comment or annotation
"stdlib/builtins.pyi"(357,43): Invalid type comment or annotation
"stdlib/builtins.pyi"(359,29): Invalid type comment or annotation
"stdlib/builtins.pyi"(359,58): Invalid type comment or annotation
"stdlib/builtins.pyi"(363,4): Overloaded function signature 4 will never be matched: signature 3's parameter type(s) are the same or broader
"stdlib/builtins.pyi"(367,4): Overloaded function signature 5 will never be matched: signature 3's parameter type(s) are the same or broader
"stdlib/builtins.pyi"(367,4): Overloaded function signature 5 will never be matched: signature 4's parameter type(s) are the same or broader
"stdlib/builtins.pyi"(389,4): Return type "bool" of "__eq__" incompatible with return type "bool" in supertype "builtins.object"
"stdlib/builtins.pyi"(389,21): Argument 1 of "__eq__" is incompatible with supertype "builtins.object"; supertype defines the argument type as "object"
"stdlib/builtins.pyi"(390,4): Return type "bool" of "__ne__" incompatible with return type "bool" in supertype "builtins.object"
"stdlib/builtins.pyi"(390,21): Argument 1 of "__ne__" is incompatible with supertype "builtins.object"; supertype defines the argument type as "object"
"stdlib/builtins.pyi"(398,4): Return type "int" of "__hash__" incompatible with return type "int" in supertype "builtins.object"
"stdlib/builtins.pyi"(403,56): Invalid type comment or annotation
"stdlib/builtins.pyi"(404,34): "tuple" expects 1 type argument, but 2 given
"stdlib/builtins.pyi"(408,40): Invalid type comment or annotation
"stdlib/builtins.pyi"(420,45): "tuple" expects 1 type argument, but 2 given
"stdlib/builtins.pyi"(433,46): "tuple" expects 1 type argument, but 2 given
"stdlib/builtins.pyi"(437,4): Overloaded function signature 2 will never be matched: signature 1's parameter type(s) are the same or broader
"stdlib/builtins.pyi"(440,4): Overloaded function signature 3 will never be matched: signature 1's parameter type(s) are the same or broader
"stdlib/builtins.pyi"(440,4): Overloaded function signature 3 will never be matched: signature 2's parameter type(s) are the same or broader
"stdlib/builtins.pyi"(451,4): Return type "bool" of "__eq__" incompatible with return type "bool" in supertype "builtins.object"
"stdlib/builtins.pyi"(451,21): Argument 1 of "__eq__" is incompatible with supertype "builtins.object"; supertype defines the argument type as "object"
"stdlib/builtins.pyi"(452,4): Return type "bool" of "__ne__" incompatible with return type "bool" in supertype "builtins.object"
"stdlib/builtins.pyi"(452,21): Argument 1 of "__ne__" is incompatible with supertype "builtins.object"; supertype defines the argument type as "object"
"stdlib/builtins.pyi"(462,4): Return type "int" of "__hash__" incompatible with return type "int" in supertype "builtins.object"
"stdlib/builtins.pyi"(472,9): Invalid type comment or annotation
"stdlib/builtins.pyi"(474,95): Invalid type comment or annotation
"stdlib/builtins.pyi"(490,4): Return type "bool" of "__eq__" incompatible with return type "bool" in supertype "builtins.object"
"stdlib/builtins.pyi"(490,21): Argument 1 of "__eq__" is incompatible with supertype "builtins.object"; supertype defines the argument type as "object"
"stdlib/builtins.pyi"(491,4): Return type "bool" of "__ne__" incompatible with return type "bool" in supertype "builtins.object"
"stdlib/builtins.pyi"(491,21): Argument 1 of "__ne__" is incompatible with supertype "builtins.object"; supertype defines the argument type as "object"
"stdlib/builtins.pyi"(495,4): Return type "int" of "__hash__" incompatible with return type "int" in supertype "builtins.object"
"stdlib/builtins.pyi"(508,46): Invalid type comment or annotation
"stdlib/builtins.pyi"(510,88): Invalid type comment or annotation
"stdlib/builtins.pyi"(512,25): Invalid type comment or annotation
"stdlib/builtins.pyi"(512,43): Invalid type comment or annotation
"stdlib/builtins.pyi"(516,23): Invalid type comment or annotation
"stdlib/builtins.pyi"(516,41): Invalid type comment or annotation
"stdlib/builtins.pyi"(520,21): Invalid type comment or annotation
"stdlib/builtins.pyi"(520,68): Invalid type comment or annotation
"stdlib/builtins.pyi"(520,95): Invalid type comment or annotation
"stdlib/builtins.pyi"(523,4): Signature of "count" incompatible with supertype "typing.Sequence"
"stdlib/builtins.pyi"(525,37): "tuple" expects 1 type argument, but 2 given
"stdlib/builtins.pyi"(525,48): Unexpected "..."
"stdlib/builtins.pyi"(527,25): Invalid type comment or annotation
"stdlib/builtins.pyi"(527,71): Invalid type comment or annotation
"stdlib/builtins.pyi"(532,21): Invalid type comment or annotation
"stdlib/builtins.pyi"(532,43): Invalid type comment or annotation
"stdlib/builtins.pyi"(532,68): Invalid type comment or annotation
"stdlib/builtins.pyi"(532,86): Invalid type comment or annotation
"stdlib/builtins.pyi"(534,4): Overloaded function signature 2 will never be matched: signature 1's parameter type(s) are the same or broader
"stdlib/builtins.pyi"(536,4): Return type "int" of "index" incompatible with return type "int" in supertype "typing.Sequence"
"stdlib/builtins.pyi"(550,19): Invalid type comment or annotation
"stdlib/builtins.pyi"(550,53): Invalid type comment or annotation
"stdlib/builtins.pyi"(550,75): Invalid type comment or annotation
"stdlib/builtins.pyi"(554,20): Invalid type comment or annotation
"stdlib/builtins.pyi"(554,67): Invalid type comment or annotation
"stdlib/builtins.pyi"(554,94): Invalid type comment or annotation
"stdlib/builtins.pyi"(558,20): Invalid type comment or annotation
"stdlib/builtins.pyi"(558,38): Invalid type comment or annotation
"stdlib/builtins.pyi"(566,24): Invalid type comment or annotation
"stdlib/builtins.pyi"(566,44): Invalid type comment or annotation
"stdlib/builtins.pyi"(566,65): "tuple" expects 1 type argument, but 3 given
"stdlib/builtins.pyi"(566,71): Invalid type comment or annotation
"stdlib/builtins.pyi"(566,86): Invalid type comment or annotation
"stdlib/builtins.pyi"(566,101): Invalid type comment or annotation
"stdlib/builtins.pyi"(568,40): "tuple" expects 1 type argument, but 3 given
"stdlib/builtins.pyi"(576,26): Invalid type comment or annotation
"stdlib/builtins.pyi"(576,46): Invalid type comment or annotation
"stdlib/builtins.pyi"(576,66): Invalid type comment or annotation
"stdlib/builtins.pyi"(576,114): Invalid type comment or annotation
"stdlib/builtins.pyi"(581,31): Invalid type comment or annotation
"stdlib/builtins.pyi"(581,54): Invalid type comment or annotation
"stdlib/builtins.pyi"(581,75): Invalid type comment or annotation
"stdlib/builtins.pyi"(585,31): Invalid type comment or annotation
"stdlib/builtins.pyi"(585,54): Invalid type comment or annotation
"stdlib/builtins.pyi"(585,75): Invalid type comment or annotation
"stdlib/builtins.pyi"(592,20): Invalid type comment or annotation
"stdlib/builtins.pyi"(592,67): Invalid type comment or annotation
"stdlib/builtins.pyi"(592,94): Invalid type comment or annotation
"stdlib/builtins.pyi"(596,25): Invalid type comment or annotation
"stdlib/builtins.pyi"(596,45): Invalid type comment or annotation
"stdlib/builtins.pyi"(596,66): "tuple" expects 1 type argument, but 3 given
"stdlib/builtins.pyi"(596,72): Invalid type comment or annotation
"stdlib/builtins.pyi"(596,87): Invalid type comment or annotation
"stdlib/builtins.pyi"(596,102): Invalid type comment or annotation
"stdlib/builtins.pyi"(598,41): "tuple" expects 1 type argument, but 3 given
"stdlib/builtins.pyi"(615,39): "tuple" expects 1 type argument, but 2 given
"stdlib/builtins.pyi"(615,50): Unexpected "..."
"stdlib/builtins.pyi"(621,23): Invalid type comment or annotation
"stdlib/builtins.pyi"(621,41): Invalid type comment or annotation
"stdlib/builtins.pyi"(625,20): Invalid type comment or annotation
"stdlib/builtins.pyi"(625,38): Invalid type comment or annotation
"stdlib/builtins.pyi"(630,20): Invalid type comment or annotation
"stdlib/builtins.pyi"(630,38): Invalid type comment or annotation
"stdlib/builtins.pyi"(634,20): Invalid type comment or annotation
"stdlib/builtins.pyi"(634,63): Invalid type comment or annotation
"stdlib/builtins.pyi"(637,4): "staticmethod[dict[int, Any]]" not callable
"stdlib/builtins.pyi"(639,19): "self" parameter missing for a non-static method (or an invalid type for self)
"stdlib/builtins.pyi"(640,4): "staticmethod[dict[int, int]]" not callable
"stdlib/builtins.pyi"(643,4): "staticmethod[dict[int, int | None]]" not callable
"stdlib/builtins.pyi"(647,22): Invalid type comment or annotation
"stdlib/builtins.pyi"(647,44): Invalid type comment or annotation
"stdlib/builtins.pyi"(647,65): Invalid type comment or annotation
"stdlib/builtins.pyi"(652,4): Return type "bool" of "__eq__" incompatible with return type "bool" in supertype "builtins.object"
"stdlib/builtins.pyi"(652,21): Argument 1 of "__eq__" is incompatible with supertype "builtins.object"; supertype defines the argument type as "object"
"stdlib/builtins.pyi"(654,4): Signature of "__getitem__" incompatible with supertype "typing.Sequence"
"stdlib/builtins.pyi"(655,26): Invalid type comment or annotation
"stdlib/builtins.pyi"(655,75): Invalid type comment or annotation
"stdlib/builtins.pyi"(659,4): Return type "int" of "__hash__" incompatible with return type "int" in supertype "builtins.object"
"stdlib/builtins.pyi"(661,23): Invalid type comment or annotation
"stdlib/builtins.pyi"(661,50): Invalid type comment or annotation
"stdlib/builtins.pyi"(665,4): Return type "int" of "__len__" incompatible with return type "int" in supertype "typing.Collection"
"stdlib/builtins.pyi"(668,22): Invalid type comment or annotation
"stdlib/builtins.pyi"(668,44): Invalid type comment or annotation
"stdlib/builtins.pyi"(668,60): "tuple" expects 1 type argument, but 2 given
"stdlib/builtins.pyi"(668,66): Invalid type comment or annotation
"stdlib/builtins.pyi"(668,81): Unexpected "..."
"stdlib/builtins.pyi"(668,93): Invalid type comment or annotation
"stdlib/builtins.pyi"(672,22): Invalid type comment or annotation
"stdlib/builtins.pyi"(672,65): Invalid type comment or annotation
"stdlib/builtins.pyi"(675,4): Return type "bool" of "__ne__" incompatible with return type "bool" in supertype "builtins.object"
"stdlib/builtins.pyi"(675,21): Argument 1 of "__ne__" is incompatible with supertype "builtins.object"; supertype defines the argument type as "object"
"stdlib/builtins.pyi"(677,23): Invalid type comment or annotation
"stdlib/builtins.pyi"(677,66): Invalid type comment or annotation
"stdlib/builtins.pyi"(684,104): Invalid type comment or annotation
"stdlib/builtins.pyi"(686,74): Invalid type comment or annotation
"stdlib/builtins.pyi"(688,24): Invalid type comment or annotation
"stdlib/builtins.pyi"(691,4): Signature of "count" incompatible with supertype "typing.Sequence"
"stdlib/builtins.pyi"(695,33): "tuple" expects 1 type argument, but 2 given
"stdlib/builtins.pyi"(695,55): Unexpected "..."
"stdlib/builtins.pyi"(703,4): Return type "int" of "index" incompatible with return type "int" in supertype "typing.Sequence"
"stdlib/builtins.pyi"(716,51): "tuple" expects 1 type argument, but 3 given
"stdlib/builtins.pyi"(725,52): "tuple" expects 1 type argument, but 3 given
"stdlib/builtins.pyi"(732,33): "tuple" expects 1 type argument, but 2 given
"stdlib/builtins.pyi"(732,55): Unexpected "..."
"stdlib/builtins.pyi"(744,40): Invalid type comment or annotation
"stdlib/builtins.pyi"(747,4): Return type "int" of "__len__" incompatible with return type "int" in supertype "typing.Collection"
"stdlib/builtins.pyi"(749,4): Return type "int" of "__hash__" incompatible with return type "int" in supertype "builtins.object"
"stdlib/builtins.pyi"(750,4): Signature of "__getitem__" incompatible with supertype "typing.Sequence"
"stdlib/builtins.pyi"(760,4): Return type "bool" of "__eq__" incompatible with return type "bool" in supertype "builtins.object"
"stdlib/builtins.pyi"(760,21): Argument 1 of "__eq__" is incompatible with supertype "builtins.object"; supertype defines the argument type as "object"
"stdlib/builtins.pyi"(761,4): Return type "bool" of "__ne__" incompatible with return type "bool" in supertype "builtins.object"
"stdlib/builtins.pyi"(761,21): Argument 1 of "__ne__" is incompatible with supertype "builtins.object"; supertype defines the argument type as "object"
"stdlib/builtins.pyi"(779,21): Argument 1 of "append" is incompatible with supertype "typing.MutableSequence"; supertype defines the argument type as "int"
"stdlib/builtins.pyi"(782,4): Signature of "count" incompatible with supertype "typing.Sequence"
"stdlib/builtins.pyi"(787,33): "tuple" expects 1 type argument, but 2 given
"stdlib/builtins.pyi"(787,55): Unexpected "..."
"stdlib/builtins.pyi"(793,21): Argument 1 of "extend" is incompatible with supertype "typing.MutableSequence"; supertype defines the argument type as "Iterable[int]"
"stdlib/builtins.pyi"(796,4): Return type "int" of "index" incompatible with return type "int" in supertype "typing.Sequence"
"stdlib/builtins.pyi"(797,43): Argument 2 of "insert" is incompatible with supertype "typing.MutableSequence"; supertype defines the argument type as "int"
"stdlib/builtins.pyi"(810,51): "tuple" expects 1 type argument, but 3 given
"stdlib/builtins.pyi"(821,52): "tuple" expects 1 type argument, but 3 given
"stdlib/builtins.pyi"(828,33): "tuple" expects 1 type argument, but 2 given
"stdlib/builtins.pyi"(828,55): Unexpected "..."
"stdlib/builtins.pyi"(840,40): Invalid type comment or annotation
"stdlib/builtins.pyi"(843,4): Return type "int" of "__len__" incompatible with return type "int" in supertype "typing.Collection"
"stdlib/builtins.pyi"(846,4): Signature of "__getitem__" incompatible with supertype "typing.MutableSequence"
"stdlib/builtins.pyi"(846,4): Signature of "__getitem__" incompatible with supertype "typing.Sequence"
"stdlib/builtins.pyi"(850,4): Signature of "__setitem__" incompatible with supertype "typing.MutableSequence"
"stdlib/builtins.pyi"(854,4): Signature of "__delitem__" incompatible with supertype "typing.MutableSequence"
"stdlib/builtins.pyi"(857,52): Invalid type comment or annotation
"stdlib/builtins.pyi"(860,51): Invalid type comment or annotation
"stdlib/builtins.pyi"(864,4): Return type "bool" of "__eq__" incompatible with return type "bool" in supertype "builtins.object"
"stdlib/builtins.pyi"(864,21): Argument 1 of "__eq__" is incompatible with supertype "builtins.object"; supertype defines the argument type as "object"
"stdlib/builtins.pyi"(865,4): Return type "bool" of "__ne__" incompatible with return type "bool" in supertype "builtins.object"
"stdlib/builtins.pyi"(865,21): Argument 1 of "__ne__" is incompatible with supertype "builtins.object"; supertype defines the argument type as "object"
"stdlib/builtins.pyi"(874,17): Invalid type comment or annotation
"stdlib/builtins.pyi"(885,23): "tuple" expects 1 type argument, but 2 given
"stdlib/builtins.pyi"(885,34): Unexpected "..."
"stdlib/builtins.pyi"(887,25): "tuple" expects 1 type argument, but 2 given
"stdlib/builtins.pyi"(887,36): Unexpected "..."
"stdlib/builtins.pyi"(889,28): "tuple" expects 1 type argument, but 2 given
"stdlib/builtins.pyi"(889,39): Unexpected "..."
"stdlib/builtins.pyi"(904,45): Invalid type comment or annotation
"stdlib/builtins.pyi"(905,27): Invalid type comment or annotation
"stdlib/builtins.pyi"(906,33): "type" expects no type arguments, but 1 given
"stdlib/builtins.pyi"(908,27): Invalid type comment or annotation
"stdlib/builtins.pyi"(908,66): "tuple" expects 1 type argument, but 2 given
"stdlib/builtins.pyi"(908,77): Unexpected "..."
"stdlib/builtins.pyi"(910,4): Overloaded function signature 2 will never be matched: signature 1's parameter type(s) are the same or broader
"stdlib/builtins.pyi"(910,27): Invalid type comment or annotation
"stdlib/builtins.pyi"(910,77): "tuple" expects 1 type argument, but 2 given
"stdlib/builtins.pyi"(910,88): Unexpected "..."
"stdlib/builtins.pyi"(912,4): Overloaded function signature 3 will never be matched: signature 1's parameter type(s) are the same or broader
"stdlib/builtins.pyi"(912,4): Overloaded function signature 3 will never be matched: signature 2's parameter type(s) are the same or broader
"stdlib/builtins.pyi"(912,27): Invalid type comment or annotation
"stdlib/builtins.pyi"(912,60): "tuple" expects 1 type argument, but 2 given
"stdlib/builtins.pyi"(912,71): Unexpected "..."
"stdlib/builtins.pyi"(914,4): Overloaded function signature 4 will never be matched: signature 1's parameter type(s) are the same or broader
"stdlib/builtins.pyi"(914,4): Overloaded function signature 4 will never be matched: signature 2's parameter type(s) are the same or broader
"stdlib/builtins.pyi"(914,4): Overloaded function signature 4 will never be matched: signature 3's parameter type(s) are the same or broader
"stdlib/builtins.pyi"(914,63): "tuple" expects 1 type argument, but 2 given
"stdlib/builtins.pyi"(914,74): Unexpected "..."
"stdlib/builtins.pyi"(915,4): Signature of "__getitem__" incompatible with supertype "typing.Sequence"
"stdlib/builtins.pyi"(916,47): "tuple" expects 1 type argument, but 2 given
"stdlib/builtins.pyi"(916,68): Unexpected "..."
"stdlib/builtins.pyi"(919,4): Return type "bool" of "__contains__" incompatible with return type "bool" in supertype "typing.Sequence"
"stdlib/builtins.pyi"(919,4): Return type "bool" of "__contains__" incompatible with return type "bool" in supertype "typing.Container"
"stdlib/builtins.pyi"(919,27): Argument 1 of "__contains__" is incompatible with supertype "typing.Sequence"; supertype defines the argument type as "object"
"stdlib/builtins.pyi"(921,4): Return type "int" of "__len__" incompatible with return type "int" in supertype "typing.Collection"
"stdlib/builtins.pyi"(922,4): Return type "bool" of "__eq__" incompatible with return type "bool" in supertype "builtins.object"
"stdlib/builtins.pyi"(922,21): Argument 1 of "__eq__" is incompatible with supertype "builtins.object"; supertype defines the argument type as "object"
"stdlib/builtins.pyi"(923,4): Return type "int" of "__hash__" incompatible with return type "int" in supertype "builtins.object"
"stdlib/builtins.pyi"(927,47): "tuple" expects 1 type argument, but 2 given
"stdlib/builtins.pyi"(927,68): Unexpected "..."
"stdlib/builtins.pyi"(947,44): Invalid type comment or annotation
"stdlib/builtins.pyi"(1002,4): Return type "bool" of "__eq__" incompatible with return type "bool" in supertype "builtins.object"
"stdlib/builtins.pyi"(1002,21): Argument 1 of "__eq__" is incompatible with supertype "builtins.object"; supertype defines the argument type as "object"
"stdlib/builtins.pyi"(1008,48): "tuple" expects 1 type argument, but 3 given
"stdlib/builtins.pyi"(1011,60): Invalid type comment or annotation
"stdlib/builtins.pyi"(1012,4): Return type "int" of "__len__" incompatible with return type "int" in supertype "typing.Collection"
"stdlib/builtins.pyi"(1013,4): Return type "bool" of "__contains__" incompatible with return type "bool" in supertype "typing.Sequence"
"stdlib/builtins.pyi"(1013,4): Return type "bool" of "__contains__" incompatible with return type "bool" in supertype "typing.Container"
"stdlib/builtins.pyi"(1013,27): Argument 1 of "__contains__" is incompatible with supertype "typing.Sequence"; supertype defines the argument type as "object"
"stdlib/builtins.pyi"(1014,4): Signature of "__getitem__" incompatible with supertype "typing.Sequence"
"stdlib/builtins.pyi"(1017,44): "tuple" expects 1 type argument, but 2 given
"stdlib/builtins.pyi"(1017,57): Unexpected "..."
"stdlib/builtins.pyi"(1019,28): "tuple" expects 1 type argument, but 2 given
"stdlib/builtins.pyi"(1019,41): Unexpected "..."
"stdlib/builtins.pyi"(1020,28): "tuple" expects 1 type argument, but 2 given
"stdlib/builtins.pyi"(1020,41): Unexpected "..."
"stdlib/builtins.pyi"(1021,28): "tuple" expects 1 type argument, but 2 given
"stdlib/builtins.pyi"(1021,41): Unexpected "..."
"stdlib/builtins.pyi"(1022,28): "tuple" expects 1 type argument, but 2 given
"stdlib/builtins.pyi"(1022,41): Unexpected "..."
"stdlib/builtins.pyi"(1023,4): Return type "bool" of "__eq__" incompatible with return type "bool" in supertype "builtins.object"
"stdlib/builtins.pyi"(1023,21): Argument 1 of "__eq__" is incompatible with supertype "builtins.object"; supertype defines the argument type as "object"
"stdlib/builtins.pyi"(1024,4): Return type "int" of "__hash__" incompatible with return type "int" in supertype "builtins.object"
"stdlib/builtins.pyi"(1026,29): "tuple" expects 1 type argument, but 2 given
"stdlib/builtins.pyi"(1026,42): Unexpected "..."
"stdlib/builtins.pyi"(1026,54): "tuple" expects 1 type argument, but 2 given
"stdlib/builtins.pyi"(1026,67): Unexpected "..."
"stdlib/builtins.pyi"(1028,4): Overloaded function signature 2 will never be matched: signature 1's parameter type(s) are the same or broader
"stdlib/builtins.pyi"(1028,29): "tuple" expects 1 type argument, but 2 given
"stdlib/builtins.pyi"(1028,39): Unexpected "..."
"stdlib/builtins.pyi"(1028,51): "tuple" expects 1 type argument, but 2 given
"stdlib/builtins.pyi"(1028,69): Unexpected "..."
"stdlib/builtins.pyi"(1029,50): "tuple" expects 1 type argument, but 2 given
"stdlib/builtins.pyi"(1029,63): Unexpected "..."
"stdlib/builtins.pyi"(1030,51): "tuple" expects 1 type argument, but 2 given
"stdlib/builtins.pyi"(1030,64): Unexpected "..."
"stdlib/builtins.pyi"(1031,4): Return type "int" of "count" incompatible with return type "int" in supertype "typing.Sequence"
"stdlib/builtins.pyi"(1032,4): Return type "int" of "index" incompatible with return type "int" in supertype "typing.Sequence"
"stdlib/builtins.pyi"(1044,29): "tuple" expects 1 type argument, but 2 given
"stdlib/builtins.pyi"(1044,45): Unexpected "..."
"stdlib/builtins.pyi"(1046,18): "tuple" expects 1 type argument, but 2 given
"stdlib/builtins.pyi"(1046,29): Unexpected "..."
"stdlib/builtins.pyi"(1075,4): Return type "int" of "index" incompatible with return type "int" in supertype "typing.Sequence"
"stdlib/builtins.pyi"(1076,4): Return type "int" of "count" incompatible with return type "int" in supertype "typing.Sequence"
"stdlib/builtins.pyi"(1088,4): Return type "int" of "__len__" incompatible with return type "int" in supertype "typing.Collection"
"stdlib/builtins.pyi"(1091,4): Signature of "__getitem__" incompatible with supertype "typing.MutableSequence"
"stdlib/builtins.pyi"(1091,4): Signature of "__getitem__" incompatible with supertype "typing.Sequence"
"stdlib/builtins.pyi"(1095,4): Signature of "__setitem__" incompatible with supertype "typing.MutableSequence"
"stdlib/builtins.pyi"(1099,4): Signature of "__delitem__" incompatible with supertype "typing.MutableSequence"
"stdlib/builtins.pyi"(1105,50): Invalid type comment or annotation
"stdlib/builtins.pyi"(1108,51): Invalid type comment or annotation
"stdlib/builtins.pyi"(1109,4): Return type "bool" of "__contains__" incompatible with return type "bool" in supertype "typing.Sequence"
"stdlib/builtins.pyi"(1109,4): Return type "bool" of "__contains__" incompatible with return type "bool" in supertype "typing.Container"
"stdlib/builtins.pyi"(1109,27): Argument 1 of "__contains__" is incompatible with supertype "typing.Sequence"; supertype defines the argument type as "object"
"stdlib/builtins.pyi"(1115,4): Return type "bool" of "__eq__" incompatible with return type "bool" in supertype "builtins.object"
"stdlib/builtins.pyi"(1115,21): Argument 1 of "__eq__" is incompatible with supertype "builtins.object"; supertype defines the argument type as "object"
"stdlib/builtins.pyi"(1136,42): "tuple" expects 1 type argument, but 2 given
"stdlib/builtins.pyi"(1140,27): "tuple" expects 1 type argument, but 2 given
"stdlib/builtins.pyi"(1150,51): Invalid type comment or annotation
"stdlib/builtins.pyi"(1159,4): "classmethod[Any, dict[Any, Any | None]]" not callable
"stdlib/builtins.pyi"(1162,4): "classmethod[Any, dict[Any, Any]]" not callable
"stdlib/builtins.pyi"(1178,4): Return type "int" of "__len__" incompatible with return type "int" in supertype "typing.Collection"
"stdlib/builtins.pyi"(1183,4): Return type "bool" of "__eq__" incompatible with return type "bool" in supertype "typing.Mapping"
"stdlib/builtins.pyi"(1183,4): Return type "bool" of "__eq__" incompatible with return type "bool" in supertype "builtins.object"
"stdlib/builtins.pyi"(1183,21): Argument 1 of "__eq__" is incompatible with supertype "typing.Mapping"; supertype defines the argument type as "object"
"stdlib/builtins.pyi"(1183,21): Argument 1 of "__eq__" is incompatible with supertype "builtins.object"; supertype defines the argument type as "object"
"stdlib/builtins.pyi"(1198,8): Signatures of "__ior__" and "__or__" are incompatible
"stdlib/builtins.pyi"(1198,73): Invalid type comment or annotation
"stdlib/builtins.pyi"(1200,8): Signatures of "__ior__" and "__or__" are incompatible
"stdlib/builtins.pyi"(1200,42): "tuple" expects 1 type argument, but 2 given
"stdlib/builtins.pyi"(1200,66): Invalid type comment or annotation
"stdlib/builtins.pyi"(1214,4): Return type "bool" of "isdisjoint" incompatible with return type "bool" in supertype "typing.AbstractSet"
"stdlib/builtins.pyi"(1222,4): Return type "int" of "__len__" incompatible with return type "int" in supertype "typing.Collection"
"stdlib/builtins.pyi"(1223,4): Return type "bool" of "__contains__" incompatible with return type "bool" in supertype "typing.AbstractSet"
"stdlib/builtins.pyi"(1223,4): Return type "bool" of "__contains__" incompatible with return type "bool" in supertype "typing.Container"
"stdlib/builtins.pyi"(1223,27): Argument 1 of "__contains__" is incompatible with supertype "typing.AbstractSet"; supertype defines the argument type as "object"
"stdlib/builtins.pyi"(1226,57): Invalid type comment or annotation
"stdlib/builtins.pyi"(1228,52): Invalid type comment or annotation
"stdlib/builtins.pyi"(1230,4): Signatures of "__isub__" and "__sub__" are incompatible
"stdlib/builtins.pyi"(1230,57): Invalid type comment or annotation
"stdlib/builtins.pyi"(1232,53): Invalid type comment or annotation
"stdlib/builtins.pyi"(1233,4): Signatures of "__le__" of "set[_T]" and "__ge__" of "AbstractSet[object]" are unsafely overlapping
"stdlib/builtins.pyi"(1233,4): Return type "bool" of "__le__" incompatible with return type "bool" in supertype "typing.AbstractSet"
"stdlib/builtins.pyi"(1234,4): Signatures of "__lt__" of "set[_T]" and "__gt__" of "AbstractSet[object]" are unsafely overlapping
"stdlib/builtins.pyi"(1234,4): Return type "bool" of "__lt__" incompatible with return type "bool" in supertype "typing.AbstractSet"
"stdlib/builtins.pyi"(1235,4): Signatures of "__ge__" of "set[_T]" and "__le__" of "AbstractSet[object]" are unsafely overlapping
"stdlib/builtins.pyi"(1235,4): Return type "bool" of "__ge__" incompatible with return type "bool" in supertype "typing.AbstractSet"
"stdlib/builtins.pyi"(1236,4): Signatures of "__gt__" of "set[_T]" and "__lt__" of "AbstractSet[object]" are unsafely overlapping
"stdlib/builtins.pyi"(1236,4): Return type "bool" of "__gt__" incompatible with return type "bool" in supertype "typing.AbstractSet"
"stdlib/builtins.pyi"(1237,4): Return type "bool" of "__eq__" incompatible with return type "bool" in supertype "typing.AbstractSet"
"stdlib/builtins.pyi"(1237,4): Return type "bool" of "__eq__" incompatible with return type "bool" in supertype "builtins.object"
"stdlib/builtins.pyi"(1237,21): Argument 1 of "__eq__" is incompatible with supertype "typing.AbstractSet"; supertype defines the argument type as "object"
"stdlib/builtins.pyi"(1237,21): Argument 1 of "__eq__" is incompatible with supertype "builtins.object"; supertype defines the argument type as "object"
"stdlib/builtins.pyi"(1244,24): Invalid type comment or annotation
"stdlib/builtins.pyi"(1246,54): Invalid type comment or annotation
"stdlib/builtins.pyi"(1250,4): Return type "bool" of "isdisjoint" incompatible with return type "bool" in supertype "typing.AbstractSet"
"stdlib/builtins.pyi"(1255,4): Return type "int" of "__len__" incompatible with return type "int" in supertype "typing.Collection"
"stdlib/builtins.pyi"(1256,4): Return type "bool" of "__contains__" incompatible with return type "bool" in supertype "typing.AbstractSet"
"stdlib/builtins.pyi"(1256,4): Return type "bool" of "__contains__" incompatible with return type "bool" in supertype "typing.Container"
"stdlib/builtins.pyi"(1256,27): Argument 1 of "__contains__" is incompatible with supertype "typing.AbstractSet"; supertype defines the argument type as "object"
"stdlib/builtins.pyi"(1262,4): Signatures of "__le__" of "frozenset[_T_co]" and "__ge__" of "AbstractSet[object]" are unsafely overlapping
"stdlib/builtins.pyi"(1262,4): Return type "bool" of "__le__" incompatible with return type "bool" in supertype "typing.AbstractSet"
"stdlib/builtins.pyi"(1263,4): Signatures of "__lt__" of "frozenset[_T_co]" and "__gt__" of "AbstractSet[object]" are unsafely overlapping
"stdlib/builtins.pyi"(1263,4): Return type "bool" of "__lt__" incompatible with return type "bool" in supertype "typing.AbstractSet"
"stdlib/builtins.pyi"(1264,4): Signatures of "__ge__" of "frozenset[_T_co]" and "__le__" of "AbstractSet[object]" are unsafely overlapping
"stdlib/builtins.pyi"(1264,4): Return type "bool" of "__ge__" incompatible with return type "bool" in supertype "typing.AbstractSet"
"stdlib/builtins.pyi"(1265,4): Signatures of "__gt__" of "frozenset[_T_co]" and "__lt__" of "AbstractSet[object]" are unsafely overlapping
"stdlib/builtins.pyi"(1265,4): Return type "bool" of "__gt__" incompatible with return type "bool" in supertype "typing.AbstractSet"
"stdlib/builtins.pyi"(1266,4): Return type "bool" of "__eq__" incompatible with return type "bool" in supertype "typing.AbstractSet"
"stdlib/builtins.pyi"(1266,4): Return type "bool" of "__eq__" incompatible with return type "bool" in supertype "builtins.object"
"stdlib/builtins.pyi"(1266,21): Argument 1 of "__eq__" is incompatible with supertype "typing.AbstractSet"; supertype defines the argument type as "object"
"stdlib/builtins.pyi"(1266,21): Argument 1 of "__eq__" is incompatible with supertype "builtins.object"; supertype defines the argument type as "object"
"stdlib/builtins.pyi"(1267,4): Return type "int" of "__hash__" incompatible with return type "int" in supertype "builtins.object"
"stdlib/builtins.pyi"(1273,26): Invalid type comment or annotation
"stdlib/builtins.pyi"(1274,26): "tuple" expects 1 type argument, but 2 given
"stdlib/builtins.pyi"(1287,48): Invalid type comment or annotation
"stdlib/builtins.pyi"(1289,97): Invalid type comment or annotation
"stdlib/builtins.pyi"(1290,4): Return type "int" of "count" incompatible with return type "int" in supertype "typing.Sequence"
"stdlib/builtins.pyi"(1292,4): Return type "int" of "__len__" incompatible with return type "int" in supertype "typing.Collection"
"stdlib/builtins.pyi"(1293,4): Return type "bool" of "__eq__" incompatible with return type "bool" in supertype "builtins.object"
"stdlib/builtins.pyi"(1293,21): Argument 1 of "__eq__" is incompatible with supertype "builtins.object"; supertype defines the argument type as "object"
"stdlib/builtins.pyi"(1294,4): Return type "int" of "__hash__" incompatible with return type "int" in supertype "builtins.object"
"stdlib/builtins.pyi"(1295,4): Return type "bool" of "__contains__" incompatible with return type "bool" in supertype "typing.Sequence"
"stdlib/builtins.pyi"(1295,4): Return type "bool" of "__contains__" incompatible with return type "bool" in supertype "typing.Container"
"stdlib/builtins.pyi"(1295,27): Argument 1 of "__contains__" is incompatible with supertype "typing.Sequence"; supertype defines the argument type as "object"
"stdlib/builtins.pyi"(1297,4): Signature of "__getitem__" incompatible with supertype "typing.Sequence"
"stdlib/builtins.pyi"(1339,32): Invalid type comment or annotation
"stdlib/builtins.pyi"(1369,11): Invalid type comment or annotation
"stdlib/builtins.pyi"(1390,11): Invalid type comment or annotation
"stdlib/builtins.pyi"(1467,74): Invalid type comment or annotation
"stdlib/builtins.pyi"(1469,46): Invalid type comment or annotation
"stdlib/builtins.pyi"(1469,92): Invalid type comment or annotation
"stdlib/builtins.pyi"(1471,4): Overloaded function signature 3 will never be matched: signature 2's parameter type(s) are the same or broader
"stdlib/builtins.pyi"(1471,46): Invalid type comment or annotation
"stdlib/builtins.pyi"(1471,89): Invalid type comment or annotation
"stdlib/builtins.pyi"(1473,4): Overloaded function signature 4 will never be matched: signature 2's parameter type(s) are the same or broader
"stdlib/builtins.pyi"(1473,4): Overloaded function signature 4 will never be matched: signature 3's parameter type(s) are the same or broader
"stdlib/builtins.pyi"(1473,82): Invalid type comment or annotation
"stdlib/builtins.pyi"(1474,26): Invalid type comment or annotation
"stdlib/builtins.pyi"(1518,16): Invalid type comment or annotation
"stdlib/builtins.pyi"(1518,35): "tuple" expects 1 type argument, but 2 given
"stdlib/builtins.pyi"(1518,53): Unexpected "..."
"stdlib/builtins.pyi"(1528,76): Invalid type comment or annotation
"stdlib/builtins.pyi"(1530,103): Invalid type comment or annotation
"stdlib/builtins.pyi"(1532,130): Invalid type comment or annotation
"stdlib/builtins.pyi"(1542,9): Invalid type comment or annotation
"stdlib/builtins.pyi"(1553,9): Invalid type comment or annotation
"stdlib/builtins.pyi"(1566,9): Invalid type comment or annotation
"stdlib/builtins.pyi"(1567,26): Invalid type comment or annotation
"stdlib/builtins.pyi"(1604,9): Invalid type comment or annotation
"stdlib/builtins.pyi"(1624,15): Invalid type comment or annotation
"stdlib/builtins.pyi"(1637,15): Invalid type comment or annotation
"stdlib/builtins.pyi"(1648,15): Invalid type comment or annotation
"stdlib/builtins.pyi"(1659,15): Invalid type comment or annotation
"stdlib/builtins.pyi"(1702,11): Invalid type comment or annotation
"stdlib/builtins.pyi"(1734,24): Invalid type comment or annotation
"stdlib/builtins.pyi"(1734,57): Invalid type comment or annotation
"stdlib/builtins.pyi"(1736,0): Overloaded function signature 3 will never be matched: signature 2's parameter type(s) are the same or broader
"stdlib/builtins.pyi"(1738,0): Overloaded function signature 4 will never be matched: signature 2's parameter type(s) are the same or broader
"stdlib/builtins.pyi"(1738,0): Overloaded function signature 4 will never be matched: signature 3's parameter type(s) are the same or broader
"stdlib/builtins.pyi"(1743,0): Overloaded function signature 5 will never be matched: signature 2's parameter type(s) are the same or broader
"stdlib/builtins.pyi"(1743,0): Overloaded function signature 5 will never be matched: signature 3's parameter type(s) are the same or broader
"stdlib/builtins.pyi"(1743,0): Overloaded function signature 5 will never be matched: signature 4's parameter type(s) are the same or broader
"stdlib/builtins.pyi"(1747,0): Overloaded function signature 7 will never be matched: signature 6's parameter type(s) are the same or broader
"stdlib/builtins.pyi"(1761,0): Overloaded function signature 12 will never be matched: signature 11's parameter type(s) are the same or broader
"stdlib/builtins.pyi"(1765,0): Overloaded function signature 14 will never be matched: signature 6's parameter type(s) are the same or broader
"stdlib/builtins.pyi"(1765,0): Overloaded function signature 14 will never be matched: signature 7's parameter type(s) are the same or broader
"stdlib/builtins.pyi"(1775,26): Invalid type comment or annotation
"stdlib/builtins.pyi"(1818,0): Overloaded function signature 2 will never be matched: signature 1's parameter type(s) are the same or broader
"stdlib/builtins.pyi"(1818,83): Invalid type comment or annotation
"stdlib/builtins.pyi"(1876,79): "tuple" expects 1 type argument, but 2 given
"stdlib/builtins.pyi"(1878,101): "tuple" expects 1 type argument, but 3 given
"stdlib/builtins.pyi"(1882,17): "tuple" expects 1 type argument, but 4 given
"stdlib/builtins.pyi"(1886,17): "tuple" expects 1 type argument, but 5 given
"stdlib/builtins.pyi"(1898,17): "tuple" expects 1 type argument, but 2 given
"stdlib/builtins.pyi"(1898,28): Unexpected "..."
"stdlib/builtins.pyi"(1900,26): Invalid type comment or annotation
"stdlib/builtins.pyi"(1933,10): "tuple" expects 1 type argument, but 2 given
"stdlib/builtins.pyi"(1933,21): Unexpected "..."
"stdlib/builtins.pyi"(1939,49): Invalid type comment or annotation
"stdlib/builtins.pyi"(1941,61): Invalid type comment or annotation
"stdlib/collections/__init__.pyi"(111,22): Invalid type comment or annotation
"stdlib/collections/__init__.pyi"(112,26): Invalid type comment or annotation
"stdlib/collections/__init__.pyi"(159,39): Invalid type comment or annotation
"stdlib/collections/__init__.pyi"(165,46): Invalid type comment or annotation
"stdlib/collections/__init__.pyi"(166,47): Invalid type comment or annotation
"stdlib/collections/__init__.pyi"(167,47): Invalid type comment or annotation
"stdlib/collections/__init__.pyi"(168,33): Invalid type comment or annotation
"stdlib/collections/__init__.pyi"(169,34): Invalid type comment or annotation
"stdlib/collections/__init__.pyi"(170,34): Invalid type comment or annotation
"stdlib/collections/__init__.pyi"(175,22): Invalid type comment or annotation
"stdlib/collections/__init__.pyi"(176,26): Invalid type comment or annotation
"stdlib/collections/__init__.pyi"(189,26): Name "UserString" is not defined
"stdlib/collections/__init__.pyi"(204,59): Invalid type comment or annotation
"stdlib/collections/__init__.pyi"(205,35): Invalid type comment or annotation
"stdlib/collections/__init__.pyi"(206,39): Invalid type comment or annotation
"stdlib/collections/__init__.pyi"(207,40): Invalid type comment or annotation
"stdlib/collections/__init__.pyi"(208,41): Invalid type comment or annotation
"stdlib/collections/__init__.pyi"(209,33): Invalid type comment or annotation
"stdlib/collections/__init__.pyi"(210,34): Invalid type comment or annotation
"stdlib/collections/__init__.pyi"(211,36): Invalid type comment or annotation
"stdlib/collections/__init__.pyi"(212,44): Invalid type comment or annotation
"stdlib/collections/__init__.pyi"(213,28): Invalid type comment or annotation
"stdlib/collections/__init__.pyi"(214,26): Invalid type comment or annotation
"stdlib/collections/__init__.pyi"(215,48): Invalid type comment or annotation
"stdlib/collections/__init__.pyi"(219,46): Invalid type comment or annotation
"stdlib/collections/__init__.pyi"(237,47): Invalid type comment or annotation
"stdlib/collections/__init__.pyi"(238,23): Invalid type comment or annotation
"stdlib/collections/__init__.pyi"(239,50): Invalid type comment or annotation
"stdlib/collections/__init__.pyi"(243,63): Invalid type comment or annotation
"stdlib/collections/__init__.pyi"(244,63): Invalid type comment or annotation
"stdlib/collections/__init__.pyi"(246,91): Invalid type comment or annotation
"stdlib/collections/__init__.pyi"(249,47): Invalid type comment or annotation
"stdlib/collections/__init__.pyi"(251,50): Invalid type comment or annotation
"stdlib/collections/__init__.pyi"(256,49): Invalid type comment or annotation
"stdlib/collections/__init__.pyi"(257,26): Invalid type comment or annotation
"stdlib/collections/__init__.pyi"(258,23): Invalid type comment or annotation
"stdlib/collections/__init__.pyi"(259,39): Invalid type comment or annotation
"stdlib/collections/__init__.pyi"(260,23): Invalid type comment or annotation
"stdlib/collections/__init__.pyi"(261,35): Invalid type comment or annotation
"stdlib/collections/__init__.pyi"(287,22): Invalid type comment or annotation
"stdlib/collections/__init__.pyi"(314,26): Invalid type comment or annotation
"stdlib/collections/__init__.pyi"(322,50): Invalid type comment or annotation
"stdlib/collections/__init__.pyi"(323,29): Invalid type comment or annotation
"stdlib/collections/__init__.pyi"(323,41): Invalid type comment or annotation
"stdlib/collections/__init__.pyi"(324,40): Invalid type comment or annotation
"stdlib/collections/__init__.pyi"(325,41): Invalid type comment or annotation
"stdlib/collections/__init__.pyi"(343,22): Invalid type comment or annotation
"stdlib/collections/__init__.pyi"(379,57): Invalid type comment or annotation
"stdlib/collections/__init__.pyi"(380,57): Invalid type comment or annotation
"stdlib/collections/__init__.pyi"(381,57): Invalid type comment or annotation
"stdlib/collections/__init__.pyi"(382,56): Invalid type comment or annotation
"stdlib/collections/__init__.pyi"(459,22): Invalid type comment or annotation
"stdlib/collections/__init__.pyi"(532,26): Invalid type comment or annotation
"stdlib/collections/__init__.pyi"(533,22): Invalid type comment or annotation
"stdlib/collections/__init__.pyi"(549,25): Invalid type comment or annotation
"stdlib/collections/__init__.pyi"(573,22): Invalid type comment or annotation
"stdlib/enum.pyi"(56,12): Invalid type comment or annotation
"stdlib/enum.pyi"(211,39): Invalid type comment or annotation
"stdlib/enum.pyi"(235,36): Invalid type comment or annotation
"stdlib/enum.pyi"(248,34): Invalid type comment or annotation
"stdlib/enum.pyi"(250,28): Invalid type comment or annotation
"stdlib/enum.pyi"(250,37): Invalid type comment or annotation
"stdlib/enum.pyi"(251,29): Invalid type comment or annotation
"stdlib/enum.pyi"(251,38): Invalid type comment or annotation
"stdlib/enum.pyi"(252,29): Invalid type comment or annotation
"stdlib/enum.pyi"(252,38): Invalid type comment or annotation
"stdlib/enum.pyi"(253,28): Invalid type comment or annotation
"stdlib/enum.pyi"(312,40): Invalid type comment or annotation
"stdlib/enum.pyi"(313,40): Invalid type comment or annotation
"stdlib/enum.pyi"(314,41): Invalid type comment or annotation
"stdlib/enum.pyi"(315,41): Invalid type comment or annotation
"stdlib/enum.pyi"(324,24): Invalid type comment or annotation
"stdlib/enum.pyi"(331,34): Invalid type comment or annotation
"stdlib/enum.pyi"(331,43): Invalid type comment or annotation
"stdlib/enum.pyi"(332,35): Invalid type comment or annotation
"stdlib/enum.pyi"(332,44): Invalid type comment or annotation
"stdlib/enum.pyi"(333,35): Invalid type comment or annotation
"stdlib/enum.pyi"(333,44): Invalid type comment or annotation
"stdlib/io.pyi"(174,15): Cannot override writeable attribute "read" in base "IOBase" with read-only property in base "_RawIOBase"
"stdlib/io.pyi"(174,15): Cannot override writeable attribute "write" in base "IOBase" with read-only property in base "_RawIOBase"
"stdlib/io.pyi"(175,20): Cannot override writeable attribute "read" in base "IOBase" with read-only property in base "_BufferedIOBase"
"stdlib/io.pyi"(175,20): Cannot override writeable attribute "write" in base "IOBase" with read-only property in base "_BufferedIOBase"
"stdlib/io.pyi"(176,16): Definition of "__next__" in base class "_TextIOBase" is incompatible with definition in base class "IOBase"
"stdlib/io.pyi"(176,16): Definition of "readline" in base class "_TextIOBase" is incompatible with definition in base class "IOBase"
"stdlib/io.pyi"(176,16): Definition of "__iter__" in base class "_TextIOBase" is incompatible with definition in base class "IOBase"
"stdlib/io.pyi"(176,16): Cannot override writeable attribute "read" in base "IOBase" with read-only property in base "_TextIOBase"
"stdlib/io.pyi"(176,16): Cannot override writeable attribute "write" in base "IOBase" with read-only property in base "_TextIOBase"
"stdlib/io.pyi"(176,16): Definition of "readlines" in base class "_TextIOBase" is incompatible with definition in base class "IOBase"
"stdlib/io.pyi"(277,15): Variable "io._OpenFile" is not valid as a type
"stdlib/io.pyi"(285,15): Variable "io._OpenFile" is not valid as a type
"stdlib/io.pyi"(293,0): Overloaded function signature 3 will never be matched: signature 2's parameter type(s) are the same or broader
"stdlib/io.pyi"(293,15): Variable "io._OpenFile" is not valid as a type
"stdlib/json/__init__.pyi"(16,6): Cannot find implementation or library stub for module named "json.decoder"
"stdlib/json/__init__.pyi"(17,6): Cannot find implementation or library stub for module named "json.encoder"
"stdlib/os/__init__.pyi"(44,4): Can only assign concrete classes to a variable of type "type[Iterator]"
"stdlib/os/__init__.pyi"(256,18): Invalid type comment or annotation
"stdlib/os/__init__.pyi"(300,8): Signatures of "__ior__" and "__or__" are incompatible
"stdlib/os/__init__.pyi"(300,61): Invalid type comment or annotation
"stdlib/os/__init__.pyi"(302,8): Signatures of "__ior__" and "__or__" are incompatible
"stdlib/os/__init__.pyi"(302,69): Invalid type comment or annotation
"stdlib/os/__init__.pyi"(446,0): Overloaded function signature 3 will never be matched: signature 1's parameter type(s) are the same or broader
"stdlib/os/__init__.pyi"(446,0): Overloaded function signature 3 will never be matched: signature 2's parameter type(s) are the same or broader
"stdlib/os/__init__.pyi"(447,0): Overloaded function implementation does not accept all possible parameters of signature 1
"stdlib/os/__init__.pyi"(447,0): Overloaded function implementation does not accept all possible parameters of signature 2
"stdlib/os/__init__.pyi"(447,0): Overloaded function implementation does not accept all possible parameters of signature 3
"stdlib/os/__init__.pyi"(448,4): An implementation for an overloaded function is not allowed in a stub file
"stdlib/os/__init__.pyi"(608,9): Invalid type comment or annotation
"stdlib/os/__init__.pyi"(840,73): A function returning TypeVar should receive at least one argument containing the same Typevar
"stdlib/os/__init__.pyi"(930,10): Invalid type comment or annotation
"stdlib/os/__init__.pyi"(971,39): Invalid type comment or annotation
"stdlib/os/__init__.pyi"(972,40): Invalid type comment or annotation
"stdlib/os/__init__.pyi"(975,40): Invalid type comment or annotation
"stdlib/os/__init__.pyi"(976,41): Invalid type comment or annotation
"stdlib/os/__init__.pyi"(983,12): Invalid type comment or annotation
"stdlib/os/__init__.pyi"(997,10): Invalid type comment or annotation
"stdlib/os/__init__.pyi"(1019,27): Invalid type comment or annotation
"stdlib/os/__init__.pyi"(1154,49): Invalid type comment or annotation
"stdlib/re.pyi"(203,8): Module has no attribute "SRE_FLAG_ASCII"
"stdlib/re.pyi"(205,12): Module has no attribute "SRE_FLAG_DEBUG"
"stdlib/re.pyi"(206,8): Module has no attribute "SRE_FLAG_IGNORECASE"
"stdlib/re.pyi"(208,8): Module has no attribute "SRE_FLAG_LOCALE"
"stdlib/re.pyi"(210,8): Module has no attribute "SRE_FLAG_MULTILINE"
"stdlib/re.pyi"(212,8): Module has no attribute "SRE_FLAG_DOTALL"
"stdlib/re.pyi"(214,8): Module has no attribute "SRE_FLAG_VERBOSE"
"stdlib/re.pyi"(216,8): Module has no attribute "SRE_FLAG_UNICODE"
"stdlib/re.pyi"(219,12): Module has no attribute "SRE_FLAG_TEMPLATE"
"stdlib/re.pyi"(244,12): Invalid type comment or annotation
"stdlib/sre_constants.pyi"(12,47): Invalid type comment or annotation
"stdlib/sre_parse.pyi"(6,26): Module "sre_constants" has no attribute "error"
"stdlib/sre_parse.pyi"(30,19): Invalid type comment or annotation
"stdlib/sre_parse.pyi"(31,23): Invalid type comment or annotation
"stdlib/sre_parse.pyi"(32,11): Invalid type comment or annotation
"stdlib/sre_parse.pyi"(33,15): Invalid type comment or annotation
"stdlib/sre_parse.pyi"(34,9): Invalid type comment or annotation
"stdlib/sre_parse.pyi"(35,11): Invalid type comment or annotation
"stdlib/sre_parse.pyi"(88,15): Invalid type comment or annotation
"stdlib/sre_parse.pyi"(89,19): Invalid type comment or annotation
"stdlib/ssl.pyi"(89,5): Cannot find implementation or library stub for module named "tls"
"stdlib/ssl.pyi"(99,21): Module "_ssl" has no attribute "RAND_egd"
"stdlib/ssl.pyi"(105,9): Invalid type comment or annotation
"stdlib/ssl.pyi"(106,10): Invalid type comment or annotation
"stdlib/ssl.pyi"(107,22): Invalid type comment or annotation
"stdlib/ssl.pyi"(108,18): Invalid type comment or annotation
"stdlib/ssl.pyi"(109,15): Invalid type comment or annotation
"stdlib/ssl.pyi"(414,34): Invalid type comment or annotation
"stdlib/ssl.pyi"(416,34): Invalid type comment or annotation
"stdlib/ssl.pyi"(418,36): Invalid type comment or annotation
"stdlib/ssl.pyi"(467,8): An implementation for an overloaded function is not allowed in a stub file
"stdlib/ssl.pyi"(482,29): Invalid type comment or annotation
"stdlib/ssl.pyi"(482,46): Invalid type comment or annotation
"stdlib/ssl.pyi"(482,56): Invalid type comment or annotation
"stdlib/ssl.pyi"(483,34): Invalid type comment or annotation
"stdlib/ssl.pyi"(483,51): Invalid type comment or annotation
"stdlib/ssl.pyi"(483,61): Invalid type comment or annotation
"stdlib/ssl.pyi"(484,29): Invalid type comment or annotation
"stdlib/ssl.pyi"(484,46): Invalid type comment or annotation
"stdlib/ssl.pyi"(484,56): Invalid type comment or annotation
"stdlib/ssl.pyi"(541,76): Invalid type comment or annotation
"stdlib/sys/__init__.pyi"(24,11): Invalid type comment or annotation
"stdlib/sys/__init__.pyi"(25,13): Invalid type comment or annotation
"stdlib/sys/__init__.pyi"(161,26): Invalid type comment or annotation
"stdlib/sys/__init__.pyi"(168,16): Invalid type comment or annotation
"stdlib/sys/__init__.pyi"(332,17): Invalid type comment or annotation
"stdlib/sys/__init__.pyi"(333,17): Invalid type comment or annotation
"stdlib/sys/__init__.pyi"(345,15): Invalid type comment or annotation
"stdlib/sys/__init__.pyi"(484,15): Invalid type comment or annotation
"stdlib/sys/__init__.pyi"(484,27): Unsupported left operand type for | ("object")
"stdlib/types.pyi"(100,9): Invalid type comment or annotation
"stdlib/types.pyi"(226,13): Invalid type comment or annotation
"stdlib/types.pyi"(291,13): Invalid type comment or annotation
"stdlib/types.pyi"(299,70): Invalid type comment or annotation
"stdlib/types.pyi"(356,51): Invalid type comment or annotation
"stdlib/types.pyi"(373,26): Invalid type comment or annotation
"stdlib/types.pyi"(393,27): Invalid type comment or annotation
"stdlib/types.pyi"(442,66): Invalid type comment or annotation
"stdlib/types.pyi"(511,107): Invalid type comment or annotation
"stdlib/types.pyi"(592,29): The first argument to Callable must be a list of types, parameter specification, or "..."
"stdlib/types.pyi"(592,71): The first argument to Callable must be a list of types, parameter specification, or "..."
"stdlib/types.pyi"(604,53): Invalid type comment or annotation
"stdlib/typing.pyi"(1,0): Module shadows the typeshed module "typing"
"stdlib/typing.pyi"(140,13): Variable "typing._T" is not valid as a type
"stdlib/typing.pyi"(140,20): Variable "typing._T" is not valid as a type
"stdlib/typing.pyi"(146,27): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(148,39): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(182,43): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(182,55): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(199,38): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(331,31): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(331,39): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(346,19): Variable "typing._F" is not valid as a type
"stdlib/typing.pyi"(346,26): Variable "typing._F" is not valid as a type
"stdlib/typing.pyi"(347,23): Variable "typing._F" is not valid as a type
"stdlib/typing.pyi"(347,30): Variable "typing._F" is not valid as a type
"stdlib/typing.pyi"(348,39): Invalid type comment or annotation
"stdlib/typing.pyi"(348,60): Invalid type comment or annotation
"stdlib/typing.pyi"(351,33): Variable "typing._F" is not valid as a type
"stdlib/typing.pyi"(351,40): Variable "typing._F" is not valid as a type
"stdlib/typing.pyi"(357,36): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(357,44): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(382,27): Variable "typing._TC" is not valid as a type
"stdlib/typing.pyi"(382,35): Variable "typing._TC" is not valid as a type
"stdlib/typing.pyi"(384,18): Invalid base class "Protocol"
"stdlib/typing.pyi"(389,20): Invalid base class "Protocol"
"stdlib/typing.pyi"(394,22): Invalid base class "Protocol"
"stdlib/typing.pyi"(399,20): Invalid base class "Protocol"
"stdlib/typing.pyi"(404,20): Invalid base class "Protocol"
"stdlib/typing.pyi"(409,18): Invalid base class "Protocol[_T_co]"
"stdlib/typing.pyi"(411,25): Variable "typing._T_co" is not valid as a type
"stdlib/typing.pyi"(414,20): Invalid base class "Protocol[_T_co]"
"stdlib/typing.pyi"(420,44): Variable "typing._T_co" is not valid as a type
"stdlib/typing.pyi"(423,12): Invalid base class "Protocol"
"stdlib/typing.pyi"(428,15): Invalid base class "Protocol"
"stdlib/typing.pyi"(436,15): Invalid base class "Protocol[_T_co]"
"stdlib/typing.pyi"(438,26): "Iterator" expects no type arguments, but 1 given
"stdlib/typing.pyi"(438,35): Variable "typing._T_co" is not valid as a type
"stdlib/typing.pyi"(441,15): "Iterable" expects no type arguments, but 1 given
"stdlib/typing.pyi"(441,24): Variable "typing._T_co" is not valid as a type
"stdlib/typing.pyi"(441,32): Invalid base class "Protocol[_T_co]"
"stdlib/typing.pyi"(443,26): Variable "typing._T_co" is not valid as a type
"stdlib/typing.pyi"(444,26): "Iterator" expects no type arguments, but 1 given
"stdlib/typing.pyi"(444,35): Variable "typing._T_co" is not valid as a type
"stdlib/typing.pyi"(447,17): "Iterable" expects no type arguments, but 1 given
"stdlib/typing.pyi"(447,26): Variable "typing._T_co" is not valid as a type
"stdlib/typing.pyi"(447,34): Invalid base class "Protocol[_T_co]"
"stdlib/typing.pyi"(449,30): "Iterator" expects no type arguments, but 1 given
"stdlib/typing.pyi"(449,39): Variable "typing._T_co" is not valid as a type
"stdlib/typing.pyi"(452,61): Unexpected keyword argument "default" for "TypeVar"
"stdlib/typing.pyi"(453,53): Unexpected keyword argument "default" for "TypeVar"
"stdlib/typing.pyi"(455,16): "Iterator" expects no type arguments, but 1 given
"stdlib/typing.pyi"(455,25): Variable "typing._YieldT_co" is not valid as a type
"stdlib/typing.pyi"(455,38): Invalid base class "Generic[_YieldT_co, _SendT_contra, _ReturnT_co]"
"stdlib/typing.pyi"(456,26): Variable "typing._YieldT_co" is not valid as a type
"stdlib/typing.pyi"(458,26): Variable "typing._SendT_contra" is not valid as a type
"stdlib/typing.pyi"(458,47): Variable "typing._YieldT_co" is not valid as a type
"stdlib/typing.pyi"(461,121): Variable "typing._YieldT_co" is not valid as a type
"stdlib/typing.pyi"(464,97): Variable "typing._YieldT_co" is not valid as a type
"stdlib/typing.pyi"(466,26): "Generator" expects no type arguments, but 3 given
"stdlib/typing.pyi"(466,36): Variable "typing._YieldT_co" is not valid as a type
"stdlib/typing.pyi"(466,48): Variable "typing._SendT_contra" is not valid as a type
"stdlib/typing.pyi"(466,63): Variable "typing._ReturnT_co" is not valid as a type
"stdlib/typing.pyi"(474,30): "Generator" expects no type arguments, but 3 given
"stdlib/typing.pyi"(474,40): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(474,45): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(474,50): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(484,48): Variable "typing._T_co" is not valid as a type
"stdlib/typing.pyi"(484,69): Invalid base class "Protocol[_T_co]"
"stdlib/typing.pyi"(487,58): Variable "typing._T_co" is not valid as a type
"stdlib/typing.pyi"(487,79): Invalid base class "Protocol[_T_co]"
"stdlib/typing.pyi"(490,16): Invalid base class "Protocol[_T_co]"
"stdlib/typing.pyi"(492,27): "Generator" expects no type arguments, but 3 given
"stdlib/typing.pyi"(492,37): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(492,42): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(492,47): Variable "typing._T_co" is not valid as a type
"stdlib/typing.pyi"(498,16): "Awaitable" expects no type arguments, but 1 given
"stdlib/typing.pyi"(498,26): Variable "typing._ReturnT_co_nd" is not valid as a type
"stdlib/typing.pyi"(498,43): Invalid base class "Generic[_YieldT_co, _SendT_contra_nd, _ReturnT_co_nd]"
"stdlib/typing.pyi"(502,26): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(510,26): Variable "typing._SendT_contra_nd" is not valid as a type
"stdlib/typing.pyi"(510,50): Variable "typing._YieldT_co" is not valid as a type
"stdlib/typing.pyi"(513,121): Variable "typing._YieldT_co" is not valid as a type
"stdlib/typing.pyi"(516,97): Variable "typing._YieldT_co" is not valid as a type
"stdlib/typing.pyi"(523,0): Class typing.AwaitableGenerator has abstract attributes "__await__", "send", "throw"
"stdlib/typing.pyi"(524,4): "Awaitable" expects no type arguments, but 1 given
"stdlib/typing.pyi"(524,14): Variable "typing._ReturnT_co_nd" is not valid as a type
"stdlib/typing.pyi"(525,4): "Generator" expects no type arguments, but 3 given
"stdlib/typing.pyi"(525,14): Variable "typing._YieldT_co" is not valid as a type
"stdlib/typing.pyi"(525,26): Variable "typing._SendT_contra_nd" is not valid as a type
"stdlib/typing.pyi"(525,44): Variable "typing._ReturnT_co_nd" is not valid as a type
"stdlib/typing.pyi"(526,4): Invalid base class "Generic[_YieldT_co, _SendT_contra_nd, _ReturnT_co_nd, _S]"
"stdlib/typing.pyi"(531,20): Invalid base class "Protocol[_T_co]"
"stdlib/typing.pyi"(533,27): "AsyncIterator" expects no type arguments, but 1 given
"stdlib/typing.pyi"(533,41): Variable "typing._T_co" is not valid as a type
"stdlib/typing.pyi"(536,20): "AsyncIterable" expects no type arguments, but 1 given
"stdlib/typing.pyi"(536,34): Variable "typing._T_co" is not valid as a type
"stdlib/typing.pyi"(536,42): Invalid base class "Protocol[_T_co]"
"stdlib/typing.pyi"(538,27): "Awaitable" expects no type arguments, but 1 given
"stdlib/typing.pyi"(538,37): Variable "typing._T_co" is not valid as a type
"stdlib/typing.pyi"(539,27): "AsyncIterator" expects no type arguments, but 1 given
"stdlib/typing.pyi"(539,41): Variable "typing._T_co" is not valid as a type
"stdlib/typing.pyi"(541,21): "AsyncIterator" expects no type arguments, but 1 given
"stdlib/typing.pyi"(541,35): Variable "typing._YieldT_co" is not valid as a type
"stdlib/typing.pyi"(541,48): Invalid base class "Generic[_YieldT_co, _SendT_contra]"
"stdlib/typing.pyi"(542,27): "Coroutine" expects no type arguments, but 3 given
"stdlib/typing.pyi"(542,37): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(542,42): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(542,47): Variable "typing._YieldT_co" is not valid as a type
"stdlib/typing.pyi"(544,27): Variable "typing._SendT_contra" is not valid as a type
"stdlib/typing.pyi"(544,48): "Coroutine" expects no type arguments, but 3 given
"stdlib/typing.pyi"(544,58): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(544,63): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(544,68): Variable "typing._YieldT_co" is not valid as a type
"stdlib/typing.pyi"(549,9): "Coroutine" expects no type arguments, but 3 given
"stdlib/typing.pyi"(549,19): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(549,24): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(549,29): Variable "typing._YieldT_co" is not valid as a type
"stdlib/typing.pyi"(552,98): "Coroutine" expects no type arguments, but 3 given
"stdlib/typing.pyi"(552,108): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(552,113): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(552,118): Variable "typing._YieldT_co" is not valid as a type
"stdlib/typing.pyi"(553,24): "Coroutine" expects no type arguments, but 3 given
"stdlib/typing.pyi"(553,34): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(553,39): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(555,26): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(564,16): Invalid base class "Protocol[_T_co]"
"stdlib/typing.pyi"(570,17): "Iterable" expects no type arguments, but 1 given
"stdlib/typing.pyi"(570,26): Variable "typing._T_co" is not valid as a type
"stdlib/typing.pyi"(570,34): "Container" expects no type arguments, but 1 given
"stdlib/typing.pyi"(570,44): Variable "typing._T_co" is not valid as a type
"stdlib/typing.pyi"(570,52): Invalid base class "Protocol[_T_co]"
"stdlib/typing.pyi"(575,15): "Reversible" expects no type arguments, but 1 given
"stdlib/typing.pyi"(575,26): Variable "typing._T_co" is not valid as a type
"stdlib/typing.pyi"(575,34): "Collection" expects no type arguments, but 1 given
"stdlib/typing.pyi"(575,45): Variable "typing._T_co" is not valid as a type
"stdlib/typing.pyi"(578,41): Variable "typing._T_co" is not valid as a type
"stdlib/typing.pyi"(581,43): "Sequence" expects no type arguments, but 1 given
"stdlib/typing.pyi"(581,52): Variable "typing._T_co" is not valid as a type
"stdlib/typing.pyi"(583,27): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(584,27): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(586,26): "Iterator" expects no type arguments, but 1 given
"stdlib/typing.pyi"(586,35): Variable "typing._T_co" is not valid as a type
"stdlib/typing.pyi"(587,30): "Iterator" expects no type arguments, but 1 given
"stdlib/typing.pyi"(587,39): Variable "typing._T_co" is not valid as a type
"stdlib/typing.pyi"(589,22): "Sequence" expects no type arguments, but 1 given
"stdlib/typing.pyi"(589,31): Variable "typing._T" is not valid as a type
"stdlib/typing.pyi"(591,40): Variable "typing._T" is not valid as a type
"stdlib/typing.pyi"(594,41): Variable "typing._T" is not valid as a type
"stdlib/typing.pyi"(597,43): "MutableSequence" expects no type arguments, but 1 given
"stdlib/typing.pyi"(597,59): Variable "typing._T" is not valid as a type
"stdlib/typing.pyi"(600,45): Variable "typing._T" is not valid as a type
"stdlib/typing.pyi"(603,47): "Iterable" expects no type arguments, but 1 given
"stdlib/typing.pyi"(603,56): Variable "typing._T" is not valid as a type
"stdlib/typing.pyi"(611,28): Variable "typing._T" is not valid as a type
"stdlib/typing.pyi"(613,29): "Iterable" expects no type arguments, but 1 given
"stdlib/typing.pyi"(613,38): Variable "typing._T" is not valid as a type
"stdlib/typing.pyi"(615,38): Variable "typing._T" is not valid as a type
"stdlib/typing.pyi"(616,28): Variable "typing._T" is not valid as a type
"stdlib/typing.pyi"(617,31): "Iterable" expects no type arguments, but 1 given
"stdlib/typing.pyi"(617,40): Variable "typing._T" is not valid as a type
"stdlib/typing.pyi"(617,48): Invalid type comment or annotation
"stdlib/typing.pyi"(619,18): "Collection" expects no type arguments, but 1 given
"stdlib/typing.pyi"(619,29): Variable "typing._T_co" is not valid as a type
"stdlib/typing.pyi"(624,28): "AbstractSet" expects no type arguments, but 1 given
"stdlib/typing.pyi"(624,40): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(625,28): "AbstractSet" expects no type arguments, but 1 given
"stdlib/typing.pyi"(625,40): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(626,28): "AbstractSet" expects no type arguments, but 1 given
"stdlib/typing.pyi"(626,40): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(627,28): "AbstractSet" expects no type arguments, but 1 given
"stdlib/typing.pyi"(627,40): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(628,29): "AbstractSet" expects no type arguments, but 1 given
"stdlib/typing.pyi"(628,41): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(628,50): "AbstractSet" expects no type arguments, but 1 given
"stdlib/typing.pyi"(628,62): Variable "typing._T_co" is not valid as a type
"stdlib/typing.pyi"(629,28): "AbstractSet" expects no type arguments, but 1 given
"stdlib/typing.pyi"(629,40): Variable "typing._T" is not valid as a type
"stdlib/typing.pyi"(629,48): "AbstractSet" expects no type arguments, but 1 given
"stdlib/typing.pyi"(629,60): Variable "typing._T_co" is not valid as a type
"stdlib/typing.pyi"(629,68): Variable "typing._T" is not valid as a type
"stdlib/typing.pyi"(630,29): "AbstractSet" expects no type arguments, but 1 given
"stdlib/typing.pyi"(630,41): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(630,50): "AbstractSet" expects no type arguments, but 1 given
"stdlib/typing.pyi"(630,62): Variable "typing._T_co" is not valid as a type
"stdlib/typing.pyi"(631,29): "AbstractSet" expects no type arguments, but 1 given
"stdlib/typing.pyi"(631,41): Variable "typing._T" is not valid as a type
"stdlib/typing.pyi"(631,49): "AbstractSet" expects no type arguments, but 1 given
"stdlib/typing.pyi"(631,61): Variable "typing._T_co" is not valid as a type
"stdlib/typing.pyi"(631,69): Variable "typing._T" is not valid as a type
"stdlib/typing.pyi"(633,32): "Iterable" expects no type arguments, but 1 given
"stdlib/typing.pyi"(633,41): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(635,17): "AbstractSet" expects no type arguments, but 1 given
"stdlib/typing.pyi"(635,29): Variable "typing._T" is not valid as a type
"stdlib/typing.pyi"(637,25): Variable "typing._T" is not valid as a type
"stdlib/typing.pyi"(639,29): Variable "typing._T" is not valid as a type
"stdlib/typing.pyi"(642,21): Variable "typing._T" is not valid as a type
"stdlib/typing.pyi"(643,28): Variable "typing._T" is not valid as a type
"stdlib/typing.pyi"(644,26): "AbstractSet" expects no type arguments, but 1 given
"stdlib/typing.pyi"(644,38): Variable "typing._T" is not valid as a type
"stdlib/typing.pyi"(644,46): Invalid type comment or annotation
"stdlib/typing.pyi"(645,4): Signatures of "__iand__" and "__and__" are incompatible
"stdlib/typing.pyi"(645,27): "AbstractSet" expects no type arguments, but 1 given
"stdlib/typing.pyi"(645,39): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(645,48): Invalid type comment or annotation
"stdlib/typing.pyi"(646,27): "AbstractSet" expects no type arguments, but 1 given
"stdlib/typing.pyi"(646,39): Variable "typing._T" is not valid as a type
"stdlib/typing.pyi"(646,47): Invalid type comment or annotation
"stdlib/typing.pyi"(647,4): Signatures of "__isub__" and "__sub__" are incompatible
"stdlib/typing.pyi"(647,27): "AbstractSet" expects no type arguments, but 1 given
"stdlib/typing.pyi"(647,39): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(647,48): Invalid type comment or annotation
"stdlib/typing.pyi"(650,32): "Mapping" expects no type arguments, but 2 given
"stdlib/typing.pyi"(650,40): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(650,45): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(653,29): "AbstractSet" expects no type arguments, but 1 given
"stdlib/typing.pyi"(653,47): Variable "typing._KT_co" is not valid as a type
"stdlib/typing.pyi"(653,55): Variable "typing._VT_co" is not valid as a type
"stdlib/typing.pyi"(653,65): Invalid base class "Generic[_KT_co, _VT_co]"
"stdlib/typing.pyi"(654,32): "Mapping" expects no type arguments, but 2 given
"stdlib/typing.pyi"(654,40): Variable "typing._KT_co" is not valid as a type
"stdlib/typing.pyi"(654,48): Variable "typing._VT_co" is not valid as a type
"stdlib/typing.pyi"(655,4): Return type "set[tuple[Any, Any]]" of "__and__" incompatible with return type "AbstractSet" in supertype "AbstractSet"
"stdlib/typing.pyi"(655,29): "Iterable" expects no type arguments, but 1 given
"stdlib/typing.pyi"(655,38): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(655,57): Variable "typing._KT_co" is not valid as a type
"stdlib/typing.pyi"(655,65): Variable "typing._VT_co" is not valid as a type
"stdlib/typing.pyi"(656,30): "Iterable" expects no type arguments, but 1 given
"stdlib/typing.pyi"(656,39): Variable "typing._T" is not valid as a type
"stdlib/typing.pyi"(656,51): Variable "typing._T" is not valid as a type
"stdlib/typing.pyi"(658,26): "Iterator" expects no type arguments, but 1 given
"stdlib/typing.pyi"(658,41): Variable "typing._KT_co" is not valid as a type
"stdlib/typing.pyi"(658,49): Variable "typing._VT_co" is not valid as a type
"stdlib/typing.pyi"(659,30): "Iterator" expects no type arguments, but 1 given
"stdlib/typing.pyi"(659,45): Variable "typing._KT_co" is not valid as a type
"stdlib/typing.pyi"(659,53): Variable "typing._VT_co" is not valid as a type
"stdlib/typing.pyi"(660,4): Return type "set[tuple[Any, Any] | Any]" of "__or__" incompatible with return type "AbstractSet" in supertype "AbstractSet"
"stdlib/typing.pyi"(660,28): "Iterable" expects no type arguments, but 1 given
"stdlib/typing.pyi"(660,37): Variable "typing._T" is not valid as a type
"stdlib/typing.pyi"(660,55): Variable "typing._KT_co" is not valid as a type
"stdlib/typing.pyi"(660,63): Variable "typing._VT_co" is not valid as a type
"stdlib/typing.pyi"(660,73): Variable "typing._T" is not valid as a type
"stdlib/typing.pyi"(661,29): "Iterable" expects no type arguments, but 1 given
"stdlib/typing.pyi"(661,38): Variable "typing._T" is not valid as a type
"stdlib/typing.pyi"(661,56): Variable "typing._KT_co" is not valid as a type
"stdlib/typing.pyi"(661,64): Variable "typing._VT_co" is not valid as a type
"stdlib/typing.pyi"(661,74): Variable "typing._T" is not valid as a type
"stdlib/typing.pyi"(662,4): Return type "set[tuple[Any, Any]]" of "__sub__" incompatible with return type "AbstractSet" in supertype "AbstractSet"
"stdlib/typing.pyi"(662,29): "Iterable" expects no type arguments, but 1 given
"stdlib/typing.pyi"(662,38): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(662,57): Variable "typing._KT_co" is not valid as a type
"stdlib/typing.pyi"(662,65): Variable "typing._VT_co" is not valid as a type
"stdlib/typing.pyi"(663,30): "Iterable" expects no type arguments, but 1 given
"stdlib/typing.pyi"(663,39): Variable "typing._T" is not valid as a type
"stdlib/typing.pyi"(663,51): Variable "typing._T" is not valid as a type
"stdlib/typing.pyi"(664,4): Return type "set[tuple[Any, Any] | Any]" of "__xor__" incompatible with return type "AbstractSet" in supertype "AbstractSet"
"stdlib/typing.pyi"(664,29): "Iterable" expects no type arguments, but 1 given
"stdlib/typing.pyi"(664,38): Variable "typing._T" is not valid as a type
"stdlib/typing.pyi"(664,56): Variable "typing._KT_co" is not valid as a type
"stdlib/typing.pyi"(664,64): Variable "typing._VT_co" is not valid as a type
"stdlib/typing.pyi"(664,74): Variable "typing._T" is not valid as a type
"stdlib/typing.pyi"(665,30): "Iterable" expects no type arguments, but 1 given
"stdlib/typing.pyi"(665,39): Variable "typing._T" is not valid as a type
"stdlib/typing.pyi"(665,57): Variable "typing._KT_co" is not valid as a type
"stdlib/typing.pyi"(665,65): Variable "typing._VT_co" is not valid as a type
"stdlib/typing.pyi"(665,75): Variable "typing._T" is not valid as a type
"stdlib/typing.pyi"(667,28): "AbstractSet" expects no type arguments, but 1 given
"stdlib/typing.pyi"(667,40): Variable "typing._KT_co" is not valid as a type
"stdlib/typing.pyi"(668,32): "Mapping" expects no type arguments, but 2 given
"stdlib/typing.pyi"(668,40): Variable "typing._KT_co" is not valid as a type
"stdlib/typing.pyi"(668,48): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(669,4): Return type "set[Any]" of "__and__" incompatible with return type "AbstractSet" in supertype "AbstractSet"
"stdlib/typing.pyi"(669,29): "Iterable" expects no type arguments, but 1 given
"stdlib/typing.pyi"(669,38): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(669,51): Variable "typing._KT_co" is not valid as a type
"stdlib/typing.pyi"(670,30): "Iterable" expects no type arguments, but 1 given
"stdlib/typing.pyi"(670,39): Variable "typing._T" is not valid as a type
"stdlib/typing.pyi"(670,51): Variable "typing._T" is not valid as a type
"stdlib/typing.pyi"(672,26): "Iterator" expects no type arguments, but 1 given
"stdlib/typing.pyi"(672,35): Variable "typing._KT_co" is not valid as a type
"stdlib/typing.pyi"(673,30): "Iterator" expects no type arguments, but 1 given
"stdlib/typing.pyi"(673,39): Variable "typing._KT_co" is not valid as a type
"stdlib/typing.pyi"(674,4): Return type "set[Any]" of "__or__" incompatible with return type "AbstractSet" in supertype "AbstractSet"
"stdlib/typing.pyi"(674,28): "Iterable" expects no type arguments, but 1 given
"stdlib/typing.pyi"(674,37): Variable "typing._T" is not valid as a type
"stdlib/typing.pyi"(674,49): Variable "typing._KT_co" is not valid as a type
"stdlib/typing.pyi"(674,58): Variable "typing._T" is not valid as a type
"stdlib/typing.pyi"(675,29): "Iterable" expects no type arguments, but 1 given
"stdlib/typing.pyi"(675,38): Variable "typing._T" is not valid as a type
"stdlib/typing.pyi"(675,50): Variable "typing._KT_co" is not valid as a type
"stdlib/typing.pyi"(675,59): Variable "typing._T" is not valid as a type
"stdlib/typing.pyi"(676,4): Return type "set[Any]" of "__sub__" incompatible with return type "AbstractSet" in supertype "AbstractSet"
"stdlib/typing.pyi"(676,29): "Iterable" expects no type arguments, but 1 given
"stdlib/typing.pyi"(676,38): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(676,51): Variable "typing._KT_co" is not valid as a type
"stdlib/typing.pyi"(677,30): "Iterable" expects no type arguments, but 1 given
"stdlib/typing.pyi"(677,39): Variable "typing._T" is not valid as a type
"stdlib/typing.pyi"(677,51): Variable "typing._T" is not valid as a type
"stdlib/typing.pyi"(678,4): Return type "set[Any]" of "__xor__" incompatible with return type "AbstractSet" in supertype "AbstractSet"
"stdlib/typing.pyi"(678,29): "Iterable" expects no type arguments, but 1 given
"stdlib/typing.pyi"(678,38): Variable "typing._T" is not valid as a type
"stdlib/typing.pyi"(678,50): Variable "typing._KT_co" is not valid as a type
"stdlib/typing.pyi"(678,59): Variable "typing._T" is not valid as a type
"stdlib/typing.pyi"(679,30): "Iterable" expects no type arguments, but 1 given
"stdlib/typing.pyi"(679,39): Variable "typing._T" is not valid as a type
"stdlib/typing.pyi"(679,51): Variable "typing._KT_co" is not valid as a type
"stdlib/typing.pyi"(679,60): Variable "typing._T" is not valid as a type
"stdlib/typing.pyi"(681,30): "Collection" expects no type arguments, but 1 given
"stdlib/typing.pyi"(681,41): Variable "typing._VT_co" is not valid as a type
"stdlib/typing.pyi"(682,32): "Mapping" expects no type arguments, but 2 given
"stdlib/typing.pyi"(682,40): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(682,45): Variable "typing._VT_co" is not valid as a type
"stdlib/typing.pyi"(684,26): "Iterator" expects no type arguments, but 1 given
"stdlib/typing.pyi"(684,35): Variable "typing._VT_co" is not valid as a type
"stdlib/typing.pyi"(685,30): "Iterator" expects no type arguments, but 1 given
"stdlib/typing.pyi"(685,39): Variable "typing._VT_co" is not valid as a type
"stdlib/typing.pyi"(687,14): "Collection" expects no type arguments, but 1 given
"stdlib/typing.pyi"(687,25): Variable "typing._KT" is not valid as a type
"stdlib/typing.pyi"(687,31): Invalid base class "Generic[_KT, _VT_co]"
"stdlib/typing.pyi"(691,31): Variable "typing._KT" is not valid as a type
"stdlib/typing.pyi"(691,42): Variable "typing._VT_co" is not valid as a type
"stdlib/typing.pyi"(694,23): Variable "typing._KT" is not valid as a type
"stdlib/typing.pyi"(694,34): Variable "typing._VT_co" is not valid as a type
"stdlib/typing.pyi"(696,23): Variable "typing._KT" is not valid as a type
"stdlib/typing.pyi"(696,40): Variable "typing._VT_co" is not valid as a type
"stdlib/typing.pyi"(696,49): Variable "typing._T" is not valid as a type
"stdlib/typing.pyi"(696,56): Variable "typing._VT_co" is not valid as a type
"stdlib/typing.pyi"(696,65): Variable "typing._T" is not valid as a type
"stdlib/typing.pyi"(697,23): "ItemsView" expects no type arguments, but 2 given
"stdlib/typing.pyi"(697,33): Variable "typing._KT" is not valid as a type
"stdlib/typing.pyi"(697,38): Variable "typing._VT_co" is not valid as a type
"stdlib/typing.pyi"(698,22): "KeysView" expects no type arguments, but 1 given
"stdlib/typing.pyi"(698,31): Variable "typing._KT" is not valid as a type
"stdlib/typing.pyi"(699,24): "ValuesView" expects no type arguments, but 1 given
"stdlib/typing.pyi"(699,35): Variable "typing._VT_co" is not valid as a type
"stdlib/typing.pyi"(703,21): "Mapping" expects no type arguments, but 2 given
"stdlib/typing.pyi"(703,29): Variable "typing._KT" is not valid as a type
"stdlib/typing.pyi"(703,34): Variable "typing._VT" is not valid as a type
"stdlib/typing.pyi"(705,31): Variable "typing._KT" is not valid as a type
"stdlib/typing.pyi"(705,43): Variable "typing._VT" is not valid as a type
"stdlib/typing.pyi"(707,31): Variable "typing._KT" is not valid as a type
"stdlib/typing.pyi"(710,23): Variable "typing._KT" is not valid as a type
"stdlib/typing.pyi"(710,34): Variable "typing._VT" is not valid as a type
"stdlib/typing.pyi"(712,23): Variable "typing._KT" is not valid as a type
"stdlib/typing.pyi"(712,40): Variable "typing._VT" is not valid as a type
"stdlib/typing.pyi"(712,48): Variable "typing._VT" is not valid as a type
"stdlib/typing.pyi"(714,23): Variable "typing._KT" is not valid as a type
"stdlib/typing.pyi"(714,40): Variable "typing._T" is not valid as a type
"stdlib/typing.pyi"(714,47): Variable "typing._VT" is not valid as a type
"stdlib/typing.pyi"(714,53): Variable "typing._T" is not valid as a type
"stdlib/typing.pyi"(715,31): Variable "typing._KT" is not valid as a type
"stdlib/typing.pyi"(715,36): Variable "typing._VT" is not valid as a type
"stdlib/typing.pyi"(723,25): "MutableMapping" expects no type arguments, but 2 given
"stdlib/typing.pyi"(723,40): Variable "typing._KT" is not valid as a type
"stdlib/typing.pyi"(723,45): Variable "typing._T" is not valid as a type
"stdlib/typing.pyi"(723,62): Variable "typing._KT" is not valid as a type
"stdlib/typing.pyi"(723,95): Variable "typing._T" is not valid as a type
"stdlib/typing.pyi"(725,30): Variable "typing._KT" is not valid as a type
"stdlib/typing.pyi"(725,44): Variable "typing._VT" is not valid as a type
"stdlib/typing.pyi"(725,55): Variable "typing._VT" is not valid as a type
"stdlib/typing.pyi"(747,47): Variable "typing._KT" is not valid as a type
"stdlib/typing.pyi"(747,52): Variable "typing._VT" is not valid as a type
"stdlib/typing.pyi"(747,71): Variable "typing._VT" is not valid as a type
"stdlib/typing.pyi"(749,24): "Iterable" expects no type arguments, but 1 given
"stdlib/typing.pyi"(749,39): Variable "typing._KT" is not valid as a type
"stdlib/typing.pyi"(749,44): Variable "typing._VT" is not valid as a type
"stdlib/typing.pyi"(749,64): Variable "typing._VT" is not valid as a type
"stdlib/typing.pyi"(751,31): Variable "typing._VT" is not valid as a type
"stdlib/typing.pyi"(760,9): Invalid base class "Generic[AnyStr]"
"stdlib/typing.pyi"(769,28): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(781,38): Variable "typing.AnyStr" is not valid as a type
"stdlib/typing.pyi"(783,23): "IO" expects no type arguments, but 1 given
"stdlib/typing.pyi"(787,46): Variable "typing.AnyStr" is not valid as a type
"stdlib/typing.pyi"(789,51): Variable "typing.AnyStr" is not valid as a type
"stdlib/typing.pyi"(802,20): "IO" expects no type arguments, but 1 given
"stdlib/typing.pyi"(805,23): Variable "typing.AnyStr" is not valid as a type
"stdlib/typing.pyi"(811,20): "IO" expects no type arguments, but 1 given
"stdlib/typing.pyi"(814,20): "IO" expects no type arguments, but 1 given
"stdlib/typing.pyi"(817,25): "IO" expects no type arguments, but 1 given
"stdlib/typing.pyi"(817,43): "Iterable" expects no type arguments, but 1 given
"stdlib/typing.pyi"(820,32): "Iterable" expects no type arguments, but 1 given
"stdlib/typing.pyi"(820,41): Variable "typing.AnyStr" is not valid as a type
"stdlib/typing.pyi"(822,26): Variable "typing.AnyStr" is not valid as a type
"stdlib/typing.pyi"(824,26): "Iterator" expects no type arguments, but 1 given
"stdlib/typing.pyi"(824,35): Variable "typing.AnyStr" is not valid as a type
"stdlib/typing.pyi"(826,27): "IO" expects no type arguments, but 1 given
"stdlib/typing.pyi"(826,30): Variable "typing.AnyStr" is not valid as a type
"stdlib/typing.pyi"(830,15): "IO" expects no type arguments, but 1 given
"stdlib/typing.pyi"(834,13): "IO" expects no type arguments, but 1 given
"stdlib/typing.pyi"(845,26): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(850,16): Invalid type comment or annotation
"stdlib/typing.pyi"(854,35): Invalid type comment or annotation
"stdlib/typing.pyi"(869,28): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(870,17): "Mapping" expects no type arguments, but 2 given
"stdlib/typing.pyi"(870,30): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(872,19): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(879,17): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(879,31): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(891,23): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(891,31): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(897,19): Variable "typing._T" is not valid as a type
"stdlib/typing.pyi"(897,29): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(897,37): Variable "typing._T" is not valid as a type
"stdlib/typing.pyi"(899,24): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(899,32): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(901,27): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(901,35): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(921,23): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(924,21): Invalid type comment or annotation
"stdlib/typing.pyi"(925,13): Invalid type comment or annotation
"stdlib/typing.pyi"(932,46): "Iterable" expects no type arguments, but 1 given
"stdlib/typing.pyi"(932,66): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(937,72): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(939,29): "Iterable" expects no type arguments, but 1 given
"stdlib/typing.pyi"(939,38): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(939,47): Invalid type comment or annotation
"stdlib/typing.pyi"(940,35): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(941,33): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(941,41): Invalid type comment or annotation
"stdlib/typing.pyi"(948,17): "Mapping" expects no type arguments, but 2 given
"stdlib/typing.pyi"(949,15): Invalid type comment or annotation
"stdlib/typing.pyi"(951,27): Invalid type comment or annotation
"stdlib/typing.pyi"(952,27): Invalid type comment or annotation
"stdlib/typing.pyi"(958,22): Invalid type comment or annotation
"stdlib/typing.pyi"(961,28): Invalid type comment or annotation
"stdlib/typing.pyi"(963,21): Invalid type comment or annotation
"stdlib/typing.pyi"(963,38): Variable "typing._T" is not valid as a type
"stdlib/typing.pyi"(964,21): Variable "typing._T" is not valid as a type
"stdlib/typing.pyi"(964,28): Variable "typing._T" is not valid as a type
"stdlib/typing.pyi"(965,29): Invalid type comment or annotation
"stdlib/typing.pyi"(966,4): Return type "dict_items[str, object]" of "items" incompatible with return type "ItemsView" in supertype "Mapping"
"stdlib/typing.pyi"(967,4): Return type "dict_keys[str, object]" of "keys" incompatible with return type "KeysView" in supertype "Mapping"
"stdlib/typing.pyi"(968,4): Return type "dict_values[str, object]" of "values" incompatible with return type "ValuesView" in supertype "Mapping"
"stdlib/typing.pyi"(971,32): Invalid type comment or annotation
"stdlib/typing.pyi"(971,62): Invalid type comment or annotation
"stdlib/typing.pyi"(973,42): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(975,33): Invalid type comment or annotation
"stdlib/typing.pyi"(975,63): Invalid type comment or annotation
"stdlib/typing.pyi"(977,8): Signatures of "__ror__" of "_TypedDict" and "__or__" of "dict[str, Any]" are unsafely overlapping
"stdlib/typing.pyi"(977,43): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(979,33): Invalid type comment or annotation
"stdlib/typing.pyi"(979,63): Invalid type comment or annotation
"stdlib/typing.pyi"(986,23): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(989,24): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(992,71): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(1026,38): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(1026,60): "Mapping" expects no type arguments, but 2 given
"stdlib/typing.pyi"(1026,73): Variable "typing.Any" is not valid as a type
"stdlib/typing.pyi"(1027,13): Variable "typing.Any" is not valid as a type
"stdlib/typing_extensions.pyi"(342,17): Metaclass conflict: the metaclass of a derived class must be a (non-strict) subclass of the metaclasses of all its bases
"stdlib/typing_extensions.pyi"(353,22): Invalid type comment or annotation
"stdlib/typing_extensions.pyi"(356,28): Invalid type comment or annotation
"stdlib/typing_extensions.pyi"(358,21): Invalid type comment or annotation
"stdlib/typing_extensions.pyi"(363,29): Invalid type comment or annotation
"stdlib/typing_extensions.pyi"(366,32): Invalid type comment or annotation
"stdlib/typing_extensions.pyi"(366,44): Invalid type comment or annotation
"stdlib/typing_extensions.pyi"(368,8): Overloaded function signature 2 will never be matched: signature 1's parameter type(s) are the same or broader
"stdlib/typing_extensions.pyi"(370,33): Invalid type comment or annotation
"stdlib/typing_extensions.pyi"(370,45): Invalid type comment or annotation
"stdlib/typing_extensions.pyi"(372,8): Overloaded function signature 2 will never be matched: signature 1's parameter type(s) are the same or broader
"stdlib/typing_extensions.pyi"(374,33): Invalid type comment or annotation
"stdlib/typing_extensions.pyi"(374,45): Invalid type comment or annotation
"stdlib/typing_extensions.pyi"(406,20): Invalid base class "Protocol"
"stdlib/typing_extensions.pyi"(496,26): Invalid type comment or annotation
"stdlib/typing_extensions.pyi"(496,39): Invalid type comment or annotation
"stdlib/typing_extensions.pyi"(527,51): Invalid type comment or annotation
"stdlib/typing_extensions.pyi"(529,45): Invalid type comment or annotation
"stdlib/typing_extensions.pyi"(568,17): Invalid base class "Protocol"
"stdlib/typing_extensions.pyi"(611,17): Invalid type comment or annotation
"stdlib/typing_extensions.pyi"(614,36): Invalid type comment or annotation
"check_collections/check_namedtuple.py"(7,6): "tuple[Any, ...]" has no attribute "name"
"check_collections/check_namedtuple.py"(8,7): "tuple[Any, ...]" has no attribute "name"
"check_collections/check_namedtuple_2.py"(9,32): Variable "check_collections.check_namedtuple_2.WifiConfig" is not valid as a type
"check_sys/check_stdio.py"(6,17): Argument 1 to "write" of "IO" has incompatible type "bytes"; expected "str"
"check_sys/check_stdio.py"(11,17): Argument 1 to "write" of "IO" has incompatible type "bytes"; expected "str"
"check_sys/check_stdio.py"(28,15): Item "BinaryIO" of "BinaryIO | Any" has no attribute "readinto"
"check_sys/check_stdio.py"(33,20): Item "BinaryIO" of "BinaryIO | Any" has no attribute "readinto"
"check_sys/check_stdio.py"(41,8): No overload variant of "write" of "IO" matches argument types "bytearray", "int"
"check_sys/check_stdio.py"(42,8): Item "BinaryIO" of "BinaryIO | Any" has no attribute "readinto"
"check_sys/check_stdio.py"(43,8): Item "BinaryIO" of "BinaryIO | Any" has no attribute "readinto"
```
