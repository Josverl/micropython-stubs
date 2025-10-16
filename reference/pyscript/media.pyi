"""
Pyscript 2025.2.3 type-stub.
see: https://docs.pyscript.net/2025.2.3/api/
"""
# Copyright (c) 2020-2025 Jos Verlinde
# MIT Licensed

from typing import Any, Literal

class Device:
    """
    Device represents a media input or output device.

    Represents devices such as a microphone, camera, or headset.
    Provides access to device properties and streams.
    """

    def __init__(self, device: Any) -> None:
        """
        Initialize a Device wrapper.

        Args:
            device: The JavaScript MediaDeviceInfo object to wrap
        """
        ...

    @property
    def id(self) -> str:
        """
        Get the device identifier.

        Returns:
            A unique identifier for the device that persists across sessions
        """
        ...

    @property
    def group(self) -> str:
        """
        Get the device group identifier.

        Returns:
            A group identifier shared by devices that belong to the same
            physical device (e.g., a monitor with both camera and microphone)
        """
        ...

    @property
    def kind(self) -> Literal["videoinput", "audioinput", "audiooutput"]:
        """
        Get the device kind.

        Returns:
            The type of device: "videoinput", "audioinput", or "audiooutput"
        """
        ...

    @property
    def label(self) -> str:
        """
        Get the device label.

        Returns:
            A human-readable description of the device
            (e.g., "External USB Webcam")
        """
        ...

    def __getitem__(self, key: str) -> Any: ...

    @classmethod
    async def load(
        cls,
        audio: bool | dict[str, Any] = False,
        video: bool | dict[str, Any] = False,
    ) -> "Device":
        """
        Load a device and request access to its stream.

        Requests user permission to access the specified media devices
        and returns a Device instance with an active stream.

        Args:
            audio: True to request audio, False to skip, or a dict with
                   constraints (e.g., {"echoCancellation": True})
            video: True to request video, False to skip, or a dict with
                   constraints (e.g., {"width": 1280, "height": 720})

        Returns:
            A Device instance with an active media stream

        Example:
            # Request audio and video
            device = await Device.load(audio=True, video=True)

            # Request video with constraints
            device = await Device.load(
                video={"width": 1920, "height": 1080}
            )
        """
        ...

    async def get_stream(self) -> Any:
        """
        Get the media stream from this device.

        Returns:
            A JavaScript MediaStream object for this device

        Example:
            device = await Device.load(video=True)
            stream = await device.get_stream()
            # Use stream with video element
        """
        ...

async def list_devices() -> list[dict[str, str]]:
    """
    List all available media input and output devices.

    Return the list of the currently available media input and output devices,
    such as microphones, cameras, headsets, and so forth.

    Returns:
        A list of dictionaries representing the available media devices.
        Each dictionary has the following keys:
        * deviceId: A string identifier for the device that persists across
          sessions. It is un-guessable by other applications and unique to
          the origin of the calling application. Reset when user clears cookies.
        * groupId: A string group identifier. Two devices have the same group
          identifier if they belong to the same physical device (e.g., a
          monitor with both a built-in camera and microphone).
        * kind: An enumerated value that is either "videoinput", "audioinput",
          or "audiooutput".
        * label: A string describing this device (e.g., "External USB Webcam").

    Note:
        The returned list will omit any devices that are blocked by the document
        Permission Policy: microphone, camera, speaker-selection (for output
        devices), and so on. Access to particular non-default devices is also
        gated by the Permissions API, and the list will omit devices for which
        the user has not granted explicit permission.

    Example:
        devices = await list_devices()
        for device in devices:
            print(f"{device['kind']}: {device['label']}")

    """
    ...
