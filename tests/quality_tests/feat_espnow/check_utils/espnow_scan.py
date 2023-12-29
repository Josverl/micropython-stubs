import sys
import time
import network
import espnow

MAX_CHANNEL = 14  # Maximum wifi channel to scan (2.4MHz band)
NUM_PINGS = 10  # The default number of pings to send on each channel
PING_MSG = b"ping"  # The message to send in each packet to the peer
CHANNEL_SETTLING_TIME = 0.0  # Delay after setting channel before testing (seconds)
MIN_PING_RESPONSE_PC = 10  # Minimum acceptable ping response rate (percent)

sta, ap = (network.WLAN(i) for i in (network.STA_IF, network.AP_IF))


def set_channel(channel):
    if sta.isconnected():
        raise OSError("can not set channel when connected to wifi network.")
    if ap.isconnected():
        raise OSError("can not set channel when clients are connected to AP_IF.")
    if sta.active() and sys.platform != "esp8266":
        try:
            sta.config(channel=channel)  # On ESP32 use STA interface
        except RuntimeError as err:
            if channel < 12:
                print(f"Error setting channel: {err}")
            return None
        return sta.config("channel")
    else:
        # On ESP8266, use the AP interface to set the channel of the STA interface
        ap_save = ap.active()
        ap.active(True)
        ap.config(channel=channel)
        ap.active(ap_save)
        return ap.config("channel")


# Return the fraction of pings to peer which succeed.
def ping_peer(enow, peer, channel, num_pings, verbose):
    if set_channel(channel) is None:
        return 0.0
    time.sleep(CHANNEL_SETTLING_TIME)
    msg = PING_MSG + bytes([channel])  # type: ignore
    #TODO Operator "+" not supported for types "Literal[b"ping"]" and "bytes"
    frac = sum((enow.send(peer, msg) for _ in range(num_pings))) / num_pings
    if verbose:
        print(f"Channel {channel:2d}: ping response rate = {frac * 100:3.0f}%.")
    return frac


def scan(peer, num_pings=NUM_PINGS, verbose=False):
    """Scan the wifi channels to find the given espnow peer device.

    If the peer is found, the channel will be printed and the channel number
    returned.
    Will:
        - scan using the STA_IF;
        - leave the STA_IF running on the selected channel of the peer.

    Args:
        peer (bytes): The MAC address of the peer device to find.
        num_pings (int, optional):
            Number of pings to send for each channel. (default=20).
        verbose (bool): Print results of each channel test.

    Returns:
        int: The channel number of the peer (or 0 if not found)
    """
    if not sta.active() and not ap.active():
        sta.active(True)  # One of the WLAN interfaces must be active
    enow = espnow.ESPNow()
    enow.active(True)
    try:
        enow.add_peer(peer)  # If user has not already registered peer
    except OSError:
        pass

    # A list of the ping success rates (fraction) for each channel
    ping_fracs = [
        ping_peer(enow, peer, channel, num_pings, verbose)
        for channel in range(1, MAX_CHANNEL + 1)
    ]
    max_frac = max(ping_fracs)
    if max_frac < (MIN_PING_RESPONSE_PC + 5) / 100:
        print(f"No channel found with response rate above {MIN_PING_RESPONSE_PC}%")
        return 0
    # Get a list of channel numbers within 5% of max ping success rate
    found = [chan + 1 for chan, rate in enumerate(ping_fracs) if rate >= max_frac - 0.05]

    # Because of channel cross-talk we may get more than one channel to be found
    # If 3 channels found, select the middle one
    # If 2 channels found: select first one if it is channel 1 else second
    # If 1 channels found, select it
    count = len(found)
    index = (count // 2) if not (count == 2 and found[0] == 1) else 0
    channel = found[index]
    print(f"Setting wifi radio to channel {channel} ({max_frac * 100:3.0f}% response)")
    return set_channel(channel)
