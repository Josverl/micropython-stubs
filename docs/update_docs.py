from pathlib import Path
import json
from collections import defaultdict
from utils import clean_version
from jinja2 import Environment, FileSystemLoader


def read_manifests(path: Path):
    configs = path.rglob("modules.json")
    for file in configs:
        with open(file) as f:
            modules = json.load(f)

        if isinstance(modules, list):
            # Old module manifest format
            firmware = modules[0]
            stub_ver = modules[1]["stubber"]
            module_count = max(len(modules) - 2, 0)
        else:
            # new module manifest format
            firmware = modules["firmware"]
            stub_ver = modules["stubber"]["version"]
            module_count = len(modules["modules"])

        # avoid getting Key not found errors
        firmware = defaultdict(lambda: None, firmware)

        if "-frozen" in file.as_posix():
            stub_type = "frozen"
        elif "cpython" in file.as_posix():
            stub_type = "cpython"
        elif firmware["family"] in [
            "lvgl",
            "ulab",
        ]:
            stub_type = "library"
        else:
            stub_type = "board"

        # for frozen modules use the parent folder name (stm32, esp32, rp2) to identify the system
        # todo: update logic in generating the frozen manifest files
        if "-frozen" in file.as_posix():
            sysname = file.parent.parent.name + "-" + file.parent.name
        else:
            sysname = firmware["sysname"]

        fw = defaultdict(
            lambda: "-",
            {
                "family": firmware["family"] or "micropython",
                "version": clean_version(firmware["version"] or "-"),
                # version without v-prefix
                # "bare_version": clean_version(firmware["version"] or "-", drop_v=True),
                "port": firmware["port"] or "-",
                "variant": firmware["variant"] or "",
                "type": stub_type,
                "sysname": sysname,
                "module_count": module_count,
                "stubber_version": stub_ver,
                "firmware": firmware,
                "path": file.parent.as_posix(),
            },
        )
        yield fw


def update_firmware_docs():
    # module can be started from two different locations
    if Path.cwd().stem == "docs":
        workspace_root = Path.cwd().parent
    else:
        workspace_root = Path.cwd()

    all = list(read_manifests(workspace_root / "stubs"))

    file_loader = FileSystemLoader(str(workspace_root / "docs/templates"))
    env = Environment(
        loader=file_loader,
        trim_blocks=True,  # trim indents
        lstrip_blocks=True,  # trim left whitespace
    )
    # Process all template files
    for template_file in (workspace_root / "docs/templates").glob("*.j2"):
        template = env.get_template(template_file.name)
        output = template.render(info_list=all)
        # output to doc folder
        md_filename = template_file.with_suffix(".md").name
        print(" - updating:", md_filename)
        with open(workspace_root / "docs" / md_filename, "w") as md_file:
            md_file.write(output)
        # # output to root folder
        # with open(workspace_root / md_filename, "w") as md_file:
        #     md_file.write(output)


if __name__ == "__main__":
    update_firmware_docs()
