# runs on MicroPython (and Python)
# get file and folder information and return this as JSON
# params : folder , traverse subdirectory , output format, gethash
# intended to allow simple processing of files
# jos_verlinde@hotmail.com
import json
import logging
import os
from typing import Any, Dict, List, Optional, Tuple, Union
import ubinascii
import uhashlib

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


def listdir(path=".", sub=False, JSON=True, gethash=False):
    # Lists the file information of a folder
    li :List[dict]= []  # type: List[dict]
    if path == ".":  # Get current folder name
        path = os.getcwd()
    files = os.listdir(path)
    for file in files:
        # get size of each file
        info = {"Path": path, "Name": file, "Size": 0}
        if path[-1] == "/":
            full = "%s%s" % (path, file)
        else:
            full = "%s/%s" % (path, file)
        log.debug("os.stat({})".format(full))
        subdir = []
        try:
            stat = os.stat(full)
            if stat[0] & 0x4000:  # stat.S_IFDIR
                info["Type"] = "dir"
                # recurse folder(s)
                if sub == True:
                    log.debug("Folder :{}".format(full))
                    subdir = listdir(path=full, sub=True, JSON=False, gethash=gethash)
            else:
                info["Size"] = stat[6]
                info["Type"] = "file"
                if gethash:
                    with open(full, "rb") as f:
                        h = uhashlib.sha256(f.read())
                        info["Hash"] = ubinascii.hexlify(h.digest())
        except OSError as e:
            log.error("error:{} processing file:{}".format(e, full))
            info["OSError"] = e.args[0]
            info["Type"] = "OSError"
        info["Fullname"] = full
        li.append(info)
        # recurse folder(s)
        if sub == True:
            li = li + subdir
    if JSON == True:
        return json.dumps(li)
    else:
        return li
