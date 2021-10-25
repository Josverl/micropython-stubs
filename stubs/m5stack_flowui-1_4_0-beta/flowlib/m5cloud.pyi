from typing import Any

class Btn:
    def attach() -> None: ...
    def deinit() -> None: ...
    def detach() -> None: ...
    def multiBtnCb() -> None: ...
    def restart() -> None: ...
    def timerCb() -> None: ...

class BtnChild:
    def deinit() -> None: ...
    def isPressed() -> None: ...
    def isReleased() -> None: ...
    def pressFor() -> None: ...
    def restart() -> None: ...
    def upDate() -> None: ...
    def wasDoublePress() -> None: ...
    def wasPressed() -> None: ...
    def wasReleased() -> None: ...

class IP5306:
    def getBatteryLevel() -> None: ...
    def init() -> None: ...
    def isChargeFull() -> None: ...
    def isCharging() -> None: ...
    def setCharge() -> None: ...
    def setChargeVolt() -> None: ...
    def setVinMaxCurrent() -> None: ...

class M5Cloud:
    def _backend() -> None: ...
    def _daemonTask() -> None: ...
    def _error() -> None: ...
    def _exec_respond() -> None: ...
    def _msg_deal() -> None: ...
    def _send_data() -> None: ...
    def on_connect() -> None: ...
    def on_data() -> None: ...
    def run() -> None: ...

class MQTTClient:
    def _clean_sock_buffer() -> None: ...
    def _recv_len() -> None: ...
    def _send_str() -> None: ...
    def check_msg() -> None: ...
    def connect() -> None: ...
    def disconnect() -> None: ...
    def lock_msg_rec() -> None: ...
    def ping() -> None: ...
    def publish() -> None: ...
    def set_block() -> None: ...
    def set_callback() -> None: ...
    def set_last_will() -> None: ...
    def socket_connect() -> None: ...
    def subscribe() -> None: ...
    def topic_get() -> None: ...
    def topic_msg_get() -> None: ...
    def unlock_msg_rec() -> None: ...
    def wait_msg() -> None: ...

class Rgb_multi:
    def deinit() -> None: ...
    def setBrightness() -> None: ...
    def setColor() -> None: ...
    def setColorAll() -> None: ...
    def setColorFrom() -> None: ...
    def setShowLock() -> None: ...
    def show() -> None: ...

STA_BUSY: int
STA_DOWNLOAD: int
STA_IDLE: int
STA_UPLOAD: int

class Speaker:
    def _timeout_cb() -> None: ...
    def checkInit() -> None: ...
    def setBeat() -> None: ...
    def setVolume() -> None: ...
    def sing() -> None: ...
    def tone() -> None: ...

_thread: Any
apikey: str
binascii: Any
btn: Any
btnA: Any
btnB: Any
btnC: Any

def btnText() -> None: ...
def cfgRead() -> None: ...
def cfgWrite() -> None: ...

config_normal: str

def const() -> None: ...
def core_start() -> None: ...

display: Any

def flowDeinit() -> None: ...

class flowExit: ...

gc: Any

def getP2PData() -> None: ...
def get_sd_state() -> None: ...
def hwDeinit() -> None: ...

io: Any
json: Any
lcd: Any

def loopExit() -> None: ...
def loopSetIdle() -> None: ...
def loopState() -> None: ...

m5base: Any
machine: Any

def modeSet() -> None: ...

module: Any
network: Any
node_id: str
os: Any
power: Any

def reconnect() -> None: ...
def remoteInit() -> None: ...
def resetDefault() -> None: ...

rgb: Any

def sd_mount() -> None: ...
def sd_umount() -> None: ...
def sendP2PData() -> None: ...
def setP2PData() -> None: ...

speaker: Any

def start() -> None: ...
def startBeep() -> None: ...

sys: Any
timEx: Any
time: Any
timeSchedule: Any
time_ex: Any
timerSch: Any
unit: Any

def wait() -> None: ...
def wait_ms() -> None: ...

wlan_sta: Any
