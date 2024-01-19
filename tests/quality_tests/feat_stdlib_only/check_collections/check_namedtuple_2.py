# ref: https://github.com/Josverl/micropython-stubs/issues/731
 
import json
from collections import namedtuple
from typing import Union

WifiConfig = namedtuple('WifiConfig', ('ssid', 'password'))
# reveal_type(WifiConfig) 

def read_wifi_config() -> Union[WifiConfig, None]:
  try:
    with open("WIFI_FILE", 'r') as f:
      data = json.load(f)
      f.close()
    if not isinstance(data, dict):
        return None
    return WifiConfig(
        ssid=data['ssid'],
        password=data.get('password'),
    )
  except:
    return None