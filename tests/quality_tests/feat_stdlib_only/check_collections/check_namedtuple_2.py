# ref: https://github.com/Josverl/micropython-stubs/issues/731
 
from collections import namedtuple
from typing import Union, Dict

WifiConfig = namedtuple('WifiConfig', ('ssid', 'password'))
# reveal_type(WifiConfig) 

def read_wifi_config() -> Union[WifiConfig, None]:
  try:
    data:Dict[str,str] = {}

    return WifiConfig(
        ssid=data['ssid'],
        password=data.get('password'),
    )
  except:
    return None