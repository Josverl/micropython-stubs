import itertools
from pathlib import Path
import json
from natsort import natsorted
import jinja2
from collections import defaultdict


def read_manifests(path: Path):
    configs = path.rglob("modules.json")
    for file in configs:
        with open(file) as f:
            modules = json.load(f)

        if isinstance(modules, list):
            # Old module manifest format
            firmware = modules[0]
            stub_ver = modules[1]["stubber"]
            mod_count = max(len(modules) - 2, 0)
        else:
            # new module manifest format
            firmware = modules["firmware"]
            stub_ver = modules["stubber"]["version"]
            mod_count = len(modules["modules"])

        # avoid getting Key not found errors
        firmware = defaultdict(lambda: None, firmware)

        if "-frozen" in file.as_posix():
            stub_type = "frozen"
        elif "cpython" in file.as_posix():
            stub_type = "CPython"
        else:
            stub_type = "board"

        # for frozen modules use the parent folder name (stm32, esp32, rp2) to identify the system
        # todo: update logic in generating the frozen manifest files
        if "-frozen" in file.as_posix():
            sysname = file.parent.parent.name + "-" + file.parent.name
        else:
            sysname = firmware["sysname"]

        v_version = version = firmware["version"] or "-"
        if v_version[0].isdecimal():
            v_version = "v" + version
        fw = defaultdict(
            lambda: "default",
            {
                "family": firmware["family"] or "micropython",
                "version": version,  # version no v-prefix
                "v_version": v_version,  # version with v-prefix
                "port": firmware["port"] or "-",
                "type": stub_type,
                "sysname": sysname,
                "module_count": mod_count,
                "stubber_version": stub_ver,
                "firmware": firmware,
                "path": file.parent.as_posix(),
            },
        )
        yield fw


all = list(read_manifests(Path("./stubs")))


from jinja2 import Environment, FileSystemLoader
from itertools import groupby

file_loader = FileSystemLoader("docs/templates")
env = Environment(
    loader=file_loader,
    trim_blocks=True,  # trim indents
    lstrip_blocks=True,  # trim left whitespace
)

template = env.get_template("firmwares.j2")
output = template.render(firmwares=all)
print(output)

template = env.get_template("firmware_grp.j2")
output = template.render(firmwares=all)
with open("docs/firmwares_2.md", "w") as myfile:
    myfile.write(output)
