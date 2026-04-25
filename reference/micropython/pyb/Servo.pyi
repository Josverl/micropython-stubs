""" """

from __future__ import annotations

from typing import overload


class Servo:
  def __init__(self, id: int, /) -> None:
    ...

  @overload
  def angle(self) -> int:
    ...

  @overload
  def angle(self, angle: int | float, time: int = 0, /) -> None:
    ...

  @overload
  def speed(self) -> int:
    ...

  @overload
  def speed(self, speed: int | float, time: int = 0, /) -> None:
    ...

  @overload
  def pulse_width(self) -> int:
    ...

  @overload
  def pulse_width(self, value: int, /) -> None:
    ...

  @overload
  def calibration(self) -> tuple[int, int, int, int, int]:
    ...

  @overload
  def calibration(self, pulse_min: int, pulse_max: int, pulse_centre: int, /) -> None:
    ...

  @overload
  def calibration(
    self,
    pulse_min: int,
    pulse_max: int,
    pulse_centre: int,
    pulse_angle_90: int,
    pulse_speed_100: int,
    /,
  ) -> None:
    ...
