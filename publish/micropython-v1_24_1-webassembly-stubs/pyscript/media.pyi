"""
Pyscript 2025.2.3 type-stub.
see: https://docs.pyscript.net/2025.2.3/api/
"""

from typing import Any

class Device:
    """Device represents a media input or output device, such as a microphone,
    camera, or headset.
    """

    def __init__(self, device) -> None: ...
    @property
    def id(self): ...
    @property
    def group(self): ...
    @property
    def kind(self): ...
    @property
    def label(self): ...
    def __getitem__(self, key) -> Any: ...
    @classmethod
    async def load(cls, audio=..., video=...) -> ...:
        """Load the device stream."""
        ...

    async def get_stream(self) -> ...: ...

async def list_devices() -> list[dict]:
    """
    Return the list of the currently available media input and output devices,
    such as microphones, cameras, headsets, and so forth.

    Output:

        list(dict) - list of dictionaries representing the available media devices.
            Each dictionary has the following keys:
            * deviceId: a string that is an identifier for the represented device
                that is persisted across sessions. It is un-guessable by other
                applications and unique to the origin of the calling application.
                It is reset when the user clears cookies (for Private Browsing, a
                different identifier is used that is not persisted across sessions).

            * groupId: a string that is a group identifier. Two devices have the same
                group identifier if they belong to the same physical device — for
                example a monitor with both a built-in camera and a microphone.

            * kind: an enumerated value that is either "videoinput", "audioinput"
                or "audiooutput".

            * label: a string describing this device (for example "External USB
                Webcam").

    Note: the returned list will omit any devices that are blocked by the document
    Permission Policy: microphone, camera, speaker-selection (for output devices),
    and so on. Access to particular non-default devices is also gated by the
    Permissions API, and the list will omit devices for which the user has not
    granted explicit permission.
    """
    ...
