from typing import Any

_reconnectState: Any
_reconnectTime: int

def autoConnect() -> None: ...

btnA: Any
btnB: Any
btnC: Any

def cfgRead() -> None: ...
def cfgWrite() -> None: ...
def doConnect() -> None: ...
def isconnected() -> None: ...

json: Any
lcd: Any
machine: Any
network: Any

def reconnect() -> None: ...
def saveWiFi() -> None: ...
def screenShow() -> None: ...

time: Any
wlan_ap: Any
wlan_sta: Any
