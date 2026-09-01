"""Legacy Bluetooth Low Energy API for the MicroPython nRF port."""

from __future__ import annotations

from typing import Callable, Final, overload

from _mpy_shed import AnyReadableBuf
from typing_extensions import TypeAlias

_ConnectionHandler: TypeAlias = Callable[[int, int, bytearray | None], object]
_ScanData: TypeAlias = tuple[int, str | None, bytearray]

class constants:
    """Bluetooth event, UUID, and address-type constants."""

    EVT_GAP_CONNECTED: Final[int] = 16
    EVT_GAP_DISCONNECTED: Final[int] = 17
    EVT_GATTS_WRITE: Final[int] = 80
    UUID_CCCD: Final[int] = 0x2902
    ADDR_TYPE_PUBLIC: Final[int] = 0
    ADDR_TYPE_RANDOM_STATIC: Final[int] = 1

    class ad_types:
        """Bluetooth GAP advertising-data type constants."""

        AD_TYPE_FLAGS: Final[int] = 0x01
        AD_TYPE_16BIT_SERVICE_UUID_MORE_AVAILABLE: Final[int] = 0x02
        AD_TYPE_16BIT_SERVICE_UUID_COMPLETE: Final[int] = 0x03
        AD_TYPE_32BIT_SERVICE_UUID_MORE_AVAILABLE: Final[int] = 0x04
        AD_TYPE_32BIT_SERVICE_UUID_COMPLETE: Final[int] = 0x05
        AD_TYPE_128BIT_SERVICE_UUID_MORE_AVAILABLE: Final[int] = 0x06
        AD_TYPE_128BIT_SERVICE_UUID_COMPLETE: Final[int] = 0x07
        AD_TYPE_SHORT_LOCAL_NAME: Final[int] = 0x08
        AD_TYPE_COMPLETE_LOCAL_NAME: Final[int] = 0x09
        AD_TYPE_TX_POWER_LEVEL: Final[int] = 0x0A
        AD_TYPE_CLASS_OF_DEVICE: Final[int] = 0x0D
        AD_TYPE_SIMPLE_PAIRING_HASH_C: Final[int] = 0x0E
        AD_TYPE_SIMPLE_PAIRING_RANDOMIZER_R: Final[int] = 0x0F
        AD_TYPE_SECURITY_MANAGER_TK_VALUE: Final[int] = 0x10
        AD_TYPE_SECURITY_MANAGER_OOB_FLAGS: Final[int] = 0x11
        AD_TYPE_SLAVE_CONNECTION_INTERVAL_RANGE: Final[int] = 0x12
        AD_TYPE_SOLICITED_SERVICE_UUIDS_16BIT: Final[int] = 0x14
        AD_TYPE_SOLICITED_SERVICE_UUIDS_128BIT: Final[int] = 0x15
        AD_TYPE_SERVICE_DATA: Final[int] = 0x16
        AD_TYPE_PUBLIC_TARGET_ADDRESS: Final[int] = 0x17
        AD_TYPE_RANDOM_TARGET_ADDRESS: Final[int] = 0x18
        AD_TYPE_APPEARANCE: Final[int] = 0x19
        AD_TYPE_ADVERTISING_INTERVAL: Final[int] = 0x1A
        AD_TYPE_LE_BLUETOOTH_DEVICE_ADDRESS: Final[int] = 0x1B
        AD_TYPE_LE_ROLE: Final[int] = 0x1C
        AD_TYPE_SIMPLE_PAIRING_HASH_C256: Final[int] = 0x1D
        AD_TYPE_SIMPLE_PAIRING_RANDOMIZER_R256: Final[int] = 0x1E
        AD_TYPE_SERVICE_DATA_32BIT_UUID: Final[int] = 0x20
        AD_TYPE_SERVICE_DATA_128BIT_UUID: Final[int] = 0x21
        AD_TYPE_URI: Final[int] = 0x24
        AD_TYPE_3D_INFORMATION_DATA: Final[int] = 0x3D
        AD_TYPE_MANUFACTURER_SPECIFIC_DATA: Final[int] = 0xFF

class UUID:
    """A 16-bit or vendor-specific 128-bit Bluetooth UUID."""

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, value: int | str | UUID, /) -> None: ...
    def binVal(self) -> int:
        """Return the 16-bit field of this UUID as an integer."""
        ...

class Characteristic:
    """A Bluetooth GATT characteristic."""

    PROP_BROADCAST: Final[int] = 0x01
    PROP_READ: Final[int] = 0x02
    PROP_WRITE_WO_RESP: Final[int] = 0x04
    PROP_WRITE: Final[int] = 0x08
    PROP_NOTIFY: Final[int] = 0x10
    PROP_INDICATE: Final[int] = 0x20
    PROP_AUTH_SIGNED_WR: Final[int] = 0x40
    ATTR_CCCD: Final[int] = 0x01

    def __init__(self, uuid: UUID | None, /, *, props: int = PROP_READ | PROP_WRITE, attrs: int = 0) -> None: ...
    def read(self) -> bytearray | None:
        """Read and return the characteristic value when central support is enabled."""
        ...
    def write(self, data: AnyReadableBuf, /, *, with_response: bool = False) -> None:
        """Write *data*, optionally requesting a response when acting as a central."""
        ...
    def uuid(self) -> UUID:
        """Return this characteristic's UUID."""
        ...
    def properties(self) -> int:
        """Return the bit mask of characteristic properties."""
        ...

class Service:
    """A Bluetooth GATT service and its characteristics."""

    PRIMARY: Final[int] = 1
    SECONDARY: Final[int] = 2

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, uuid: UUID, type: int = PRIMARY, /) -> None: ...
    def addCharacteristic(self, characteristic: Characteristic, /) -> None:
        """Register *characteristic* with this service."""
        ...
    def getCharacteristics(self) -> list[Characteristic]:
        """Return the characteristics registered with this service."""
        ...
    def getCharacteristic(self, uuid: UUID, /) -> Characteristic | None:
        """Return the characteristic matching *uuid*, or ``None`` if not found."""
        ...
    def uuid(self) -> UUID:
        """Return this service's UUID."""
        ...

class DefaultDelegate:
    """Default no-op delegate for Bluetooth connection and notification events."""

    def handleConnection(self) -> None: ...
    def handleNotification(self) -> None: ...

class ScanEntry:
    """An advertising report discovered by :class:`Scanner`."""

    def addr(self) -> str:
        """Return the peer address as colon-separated hexadecimal text."""
        ...
    def addr_type(self) -> int:
        """Return the peer address type."""
        ...
    def rssi(self) -> int:
        """Return the received signal strength indicator."""
        ...
    def getScanData(self) -> list[_ScanData]:
        """Return advertising items as ``(type, description, value)`` tuples."""
        ...

class Scanner:
    """Discover nearby Bluetooth Low Energy devices."""

    def scan(self, timeout: int, /) -> list[ScanEntry]:
        """Scan for *timeout* milliseconds and return the advertising reports."""
        ...

class Peripheral:
    """A Bluetooth Low Energy peripheral or central connection."""

    def __init__(self, device_addr: object = None, addr_type: object = None, /) -> None: ...
    def withDelegate(self, delegate: object, /) -> None:
        """Store a delegate used to handle Bluetooth Low Energy events."""
        ...
    def setNotificationHandler(self, func: object, /) -> None:
        """Store the notification handler."""
        ...
    def setConnectionHandler(self, func: _ConnectionHandler, /) -> None:
        """Set the callback receiving ``(event_id, handle, data)`` connection events."""
        ...
    def getServices(self) -> list[Service]:
        """Return the services associated with this peripheral."""
        ...
    def connect(self, device_address: str, /, *, addr_type: int = constants.ADDR_TYPE_PUBLIC) -> None:
        """Connect to *device_address* and discover its services and characteristics."""
        ...
    def advertise(
        self,
        *,
        device_name: str | None = None,
        services: list[Service] | tuple[Service, ...] | None = None,
        data: AnyReadableBuf | None = None,
        connectable: bool | None = None,
    ) -> None:
        """Start advertising the supplied name, services, and raw advertising data."""
        ...
    def advertise_stop(self) -> None:
        """Stop advertising."""
        ...
    def disconnect(self) -> None:
        """Disconnect the current connection."""
        ...
    def addService(self, service: Service, /) -> None:
        """Associate *service* with this peripheral."""
        ...