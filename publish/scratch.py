from packaging.version import LegacyVersion, parse, Version

import logging
from pathlib import Path
from typing import Dict, List, Tuple

import jsons
from stubber.utils.versions import clean_version

from pysondb import PysonDB

from stubpacker import StubPackage

LOG = logging.getLogger(__name__)
LOG.setLevel("INFO")

# https://peps.python.org/pep-0440/
# https://stackoverflow.com/questions/61883438/is-there-a-way-to-programmatically-confirm-that-a-python-package-version-satisfi

from pkg_resources import Requirement

# req = Requirement.parse("my-stub~=18.0")
# pin = "my-stub==18.0.post2"
# name, version = pin.split("==")
# name == req.name and version in req.specifier


current :Version = parse("v1.18")  # type: ignore

def bump_postrelease(current:Version,) -> Version:
    """ Increases the post release version number"""
    parts = []
    # Epoch
    if current.epoch != 0:
        parts.append(f"{current.epoch}!")
    # Release segment
    parts.append(".".join(str(x) for x in current.release))
    # Pre-release
    if current.pre is not None:
        parts.append("".join(str(x) for x in current.pre))
    # BUMP Post-release
    if current.post is not None:
        parts.append(f".post{current.post + 1}")
    else:
        parts.append(f".post{1}")


    # Development release
    if current.dev is not None:
        parts.append(f".dev{current.dev}")

    # Local version segment
    if current.local is not None:
        parts.append(f"+{current.local}")

    new = parse("".join(parts))
    if not isinstance(new, Version):
        raise ValueError(f"{new} is not a valid version")

    return new 





# p1 :Version  = parse("1.18.0.post1")
# print(p1.__dict__["_version"])
# iv = p1.__dict__["_version"]
# iv.post = (iv.post[0], iv.post[1]+1)

# current.post = 1



db_path = Path(".") / "data" / "package_data.jsondb"
db = PysonDB(db_path.as_posix())


# ######################################
# esp32-generic-stubs
# ######################################
# todo : pass this as parameters
mpy_version = "1.18"
type = "board"
port = "esp32"
board = "GENERIC"

stub_package_name = f"micropython-{port}-{board}-stubs".lower().replace("-generic-stubs", "-stubs")

# find in the database
recs = db.get_by_query(query=lambda x: x["mpy_version"] == mpy_version and x["name"] == stub_package_name)
# dict to list, sort by version
# packages : List[Tuple[str,Dict]]= sorted(
#     [(key, recs[key]) for key in recs],
#     key=lambda x: parse(x[1]["pkg_version"]),
# )

# dict to list
recs = [{"id":key,"data": recs[key]} for key in recs]
# sort 
packages = sorted( recs,  key=lambda x: parse(x["data"]["pkg_version"]))

packages[-1]["data"]


print(f"{stub_package_name} {mpy_version}- {len(known_pkgs)}")
[LOG.info(f"{x['name']} - {x['mpy_version']} - {x['pkg_version']}") for x in known_pkgs]

