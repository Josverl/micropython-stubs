from pathlib import Path
import json
from natsort import natsorted


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

        # for frozen modules use the parent folder name (stm32, esp32, rp2) to identify the system
        # todo: update logic in generating the frozen manifest files
        if "-frozen" in file.as_posix():
            sysname = file.parent.parent.name + "-" + file.parent.name
        else:
            sysname = firmware["sysname"]

        yield (
            firmware["machine"],  # micropython
            firmware["version"],
            sysname,
            mod_count,
            stub_ver,
            firmware,
            file.parent.name,
            file.parent.as_posix(),
        )


all = read_manifests(Path("./stubs"))
# ('UM_TINYPICO', 'esp32-UM_TINYPICO',  'micropython','v1.17', 2, '1.3.7', 'stubs/micropython-1_17-frozen/esp32/UM_TINYPICO')
all = natsorted(all, key=lambda tup: (tup[0], tup[1], tup[2]), reverse=True)

for m in all:
    line = "| [{0}]({6})| {1} | {2} | {3} | {4} | {5} ".format(*m)
    print(line)
    pass
# line = "| [{0}]({6})| {1} | {2} | {3} | {4} | {5} ".format(
#     file.parent.name,
#     sysname,
#     firmware["version"],
#     firmware["machine"],
#     mod_count,
#     stub_ver,
#     file.parent.as_posix(),
# )
# print(line)
