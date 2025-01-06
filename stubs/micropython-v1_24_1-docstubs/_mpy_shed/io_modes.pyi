# MIT License
# Howard C Lovatt, 2020 onwards.

from typing import Final, Literal

_OpenTextModeUpdating: Final = Literal[
    "r+",
    "+r",
    "rt+",
    "r+t",
    "+rt",
    "tr+",
    "t+r",
    "+tr",
    "w+",
    "+w",
    "wt+",
    "w+t",
    "+wt",
    "tw+",
    "t+w",
    "+tw",
    "a+",
    "+a",
    "at+",
    "a+t",
    "+at",
    "ta+",
    "t+a",
    "+ta",
    "x+",
    "+x",
    "xt+",
    "x+t",
    "+xt",
    "tx+",
    "t+x",
    "+tx",
]
_OpenTextModeWriting: Final = Literal["w", "wt", "tw", "a", "at", "ta", "x", "xt", "tx"]
_OpenTextModeReading: Final = Literal[
    "r", "rt", "tr", "U", "rU", "Ur", "rtU", "rUt", "Urt", "trU", "tUr", "Utr"
]
_OpenTextMode: Final = _OpenTextModeUpdating | _OpenTextModeWriting | _OpenTextModeReading

_OpenBinaryModeUpdating: Final = Literal[
    "rb+",
    "r+b",
    "+rb",
    "br+",
    "b+r",
    "+br",
    "wb+",
    "w+b",
    "+wb",
    "bw+",
    "b+w",
    "+bw",
    "ab+",
    "a+b",
    "+ab",
    "ba+",
    "b+a",
    "+ba",
    "xb+",
    "x+b",
    "+xb",
    "bx+",
    "b+x",
    "+bx",
]
_OpenBinaryModeWriting: Final = Literal["wb", "bw", "ab", "ba", "xb", "bx"]
_OpenBinaryModeReading: Final = Literal["rb", "br", "rbU", "rUb", "Urb", "brU", "bUr", "Ubr"]
_OpenBinaryMode: Final = _OpenBinaryModeUpdating | _OpenBinaryModeReading | _OpenBinaryModeWriting
