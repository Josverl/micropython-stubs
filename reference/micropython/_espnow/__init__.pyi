"""
MicroPython type stub for the _espnow module (ESP32 implementation)

Based on v1.26.0 micropython/ports/esp32/modespnow.c
AI Generated, human verified. Please report any issues.
"""

from typing import Any, Callable, List, Optional, Tuple, Union, Dict, Final
from typing_extensions import Buffer

# Module constants
MAX_DATA_LEN: Final[int] = 250
ADDR_LEN: Final[int] = 6
KEY_LEN: Final[int] = 16
MAX_TOTAL_PEER_NUM: Final[int] = 20
MAX_ENCRYPT_PEER_NUM: Final[int] = 6

class ESPNowBase:
    """
    Base class for ESP-NOW communication protocol.

    ESP-NOW is a connectionless communication protocol for direct communication
    between ESP32 devices without requiring a WiFi access point.
    """

    def __init__(self) -> None:
        """Initialize ESP-NOW instance."""
        ...

    def active(self, flag: Optional[bool] = None) -> bool:
        """
        Get or set the active state of the ESP-NOW interface.

        Args:
            flag: Optional bool to set active state. If None, returns current state.

        Returns:
            Current active state as a bool.
        """
        ...

    def config(self, rxbuf: Optional[int] = None, timeout_ms: Optional[int] = None, **kwargs: Any) -> Optional[Any]:
        """
        Configure ESP-NOW parameters.

        Args:
            rxbuf: Size of receive buffer in bytes (default=526)
            timeout_ms: Default timeout for recv operations in milliseconds (default=300000)
            **kwargs: Additional configuration parameters

        Returns:
            None when setting parameters, or the requested parameter value when getting
        """
        ...

    def irq(self, callback: Optional[Callable[..., None]], *args: Any) -> None:
        """
        Set callback function to be invoked when a message is received.

        Args:
            callback: Function to call on message receipt, or None to disable
            *args: Additional arguments passed to callback
        """
        ...

    def stats(self) -> Tuple[int, int, int, int, int]:
        """
        Get ESP-NOW statistics.

        Returns:
            Tuple of (tx_packets, tx_responses, tx_failures, rx_packets, dropped_rx_packets)
        """
        ...

    def recvinto(self, buffers: List[Union[bytearray, memoryview]], timeout_ms: Optional[int] = None) -> int:
        """
        Receive ESP-NOW message into provided buffers.

        Args:
            buffers: List of buffers [peer_addr_buf, message_buf] where:
                    - peer_addr_buf: 6-byte buffer for peer MAC address
                    - message_buf: buffer for message data (up to 250 bytes)
                    - Optional 3rd/4th elements for RSSI and timestamp on ESP32
            timeout_ms: Timeout in milliseconds, or None for default timeout

        Returns:
            Length of received message, or 0 on timeout
        """
        ...

    def send(self, peer_addr: Optional[Union[bytes, bytearray]], msg: Union[str, bytes, bytearray, Buffer], sync: bool = True) -> bool:
        """
        Send message to peer(s).

        Args:
            peer_addr: 6-byte MAC address of peer, or None to send to all peers
            msg: Message data (up to 250 bytes)
            sync: Wait for acknowledgment if True

        Returns:
            True if successful (or if sync=False and queued successfully),
            False if sync=True and not all peers acknowledged
        """
        ...

    def any(self) -> bool:
        """
        Check if any messages are available to read.

        Returns:
            True if messages are available in receive buffer
        """
        ...

    # Peer management methods
    def set_pmk(self, pmk: Union[bytes, bytearray]) -> None:
        """
        Set the Primary Master Key for encrypted communication.

        Args:
            pmk: 16-byte key for encryption
        """
        ...

    def add_peer(
        self,
        peer_addr: Union[bytes, bytearray],
        lmk: Optional[Union[bytes, bytearray]] = None,
        channel: Optional[int] = None,
        ifidx: Optional[int] = None,
        encrypt: Optional[bool] = None,
    ) -> None:
        """
        Add a peer for ESP-NOW communication.

        Args:
            peer_addr: 6-byte MAC address of peer
            lmk: 16-byte Local Master Key for this peer, or None/empty for no encryption
            channel: WiFi channel (1-11, 0 for current channel)
            ifidx: Network interface index (0=STA, 1=AP)
            encrypt: Enable encryption for this peer
        """
        ...

    def del_peer(self, peer_addr: Union[bytes, bytearray]) -> None:
        """
        Remove a peer from ESP-NOW peer list.

        Args:
            peer_addr: 6-byte MAC address of peer to remove
        """
        ...

    def get_peers(self) -> Tuple[Tuple[bytes, bytes, int, int, bool], ...]:
        """
        Get information about all registered peers.

        Returns:
            Tuple of peer info tuples: (peer_addr, lmk, channel, ifidx, encrypt)
        """
        ...

    def mod_peer(
        self,
        peer_addr: Union[bytes, bytearray],
        lmk: Optional[Union[bytes, bytearray]] = None,
        channel: Optional[int] = None,
        ifidx: Optional[int] = None,
        encrypt: Optional[bool] = None,
    ) -> None:
        """
        Modify an existing peer's settings.

        Args:
            peer_addr: 6-byte MAC address of peer
            lmk: 16-byte Local Master Key, or None to leave unchanged
            channel: WiFi channel, or None to leave unchanged
            ifidx: Network interface index, or None to leave unchanged
            encrypt: Enable/disable encryption, or None to leave unchanged
        """
        ...

    def get_peer(self, peer_addr: Union[bytes, bytearray]) -> Tuple[bytes, bytes, int, int, bool]:
        """
        Get information about a specific peer.

        Args:
            peer_addr: 6-byte MAC address of peer

        Returns:
            Tuple of (peer_addr, lmk, channel, ifidx, encrypt)
        """
        ...

    def peer_count(self) -> Tuple[int, int]:
        """
        Get count of registered peers.

        Returns:
            Tuple of (total_peer_count, encrypted_peer_count)
        """
        ...

    # ESP32-specific RSSI support (when MICROPY_PY_ESPNOW_RSSI is enabled)
    @property
    def peers_table(self) -> Dict[bytes, List[int]]:
        """
        Dictionary of discovered peers with RSSI and timestamp info.

        Returns:
            Dict mapping peer MAC addresses to [rssi, timestamp_ms] lists
            where rssi is signal strength in dBm (-127 to 0)
        """
        ...
