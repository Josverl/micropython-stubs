"""Play notes, built-in melodies, and pitches on nRF boards."""

from __future__ import annotations

from typing import Final

from machine import Pin
from typing_extensions import TypeAlias

_Note: TypeAlias = str | bytes | None
_Melody: TypeAlias = list[_Note] | tuple[_Note, ...]

DADADADUM: Final[tuple[str, ...]]
ENTERTAINER: Final[tuple[str, ...]]
PRELUDE: Final[tuple[str, ...]]
ODE: Final[tuple[str, ...]]
NYAN: Final[tuple[str, ...]]
RINGTONE: Final[tuple[str, ...]]
FUNK: Final[tuple[str, ...]]
BLUES: Final[tuple[str, ...]]
BIRTHDAY: Final[tuple[str, ...]]
WEDDING: Final[tuple[str, ...]]
FUNERAL: Final[tuple[str, ...]]
PUNCHLINE: Final[tuple[str, ...]]
PYTHON: Final[tuple[str, ...]]
BADDY: Final[tuple[str, ...]]
CHASE: Final[tuple[str, ...]]
BA_DING: Final[tuple[str, ...]]
WAWAWAWAA: Final[tuple[str, ...]]
JUMP_UP: Final[tuple[str, ...]]
JUMP_DOWN: Final[tuple[str, ...]]
POWER_UP: Final[tuple[str, ...]]
POWER_DOWN: Final[tuple[str, ...]]

def reset() -> None:
    """Reset the tempo to 120 beats per minute and four ticks per beat."""
    ...

def set_tempo(*, ticks: int = 0, bpm: int = 0) -> None:
    """
    Set the number of *ticks* per beat and/or the number of beats per minute.

    A value of zero leaves the corresponding setting unchanged.
    """
    ...

def get_tempo() -> tuple[int, int]:
    """Return the current tempo as ``(beats_per_minute, ticks_per_beat)``."""
    ...

def play(music: str | bytes | _Melody, pin: Pin | None = None, wait: bool = True, loop: bool = False) -> None:
    """
    Play a note or sequence of notes on *pin*.

    Notes use forms such as ``"C4:4"`` (note, octave, duration). If *wait* is
    false playback continues in the background; if *loop* is true the sequence
    repeats until :func:`stop` is called.
    """
    ...

def pitch(frequency: int, duration: int = -1, pin: Pin | None = None, wait: bool = True) -> None:
    """
    Play *frequency* in hertz on *pin*.

    A non-negative *duration* is measured in milliseconds. If *wait* is false,
    a finite pitch is stopped asynchronously.
    """
    ...

def stop(pin: Pin | None = None) -> None:
    """Stop music playback and silence *pin*."""
    ...