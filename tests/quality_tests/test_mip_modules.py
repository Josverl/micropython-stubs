"""
Validate the runtime modules and mip manifests in the `mip/` folder.

Guards against regressions such as https://github.com/Josverl/micropython-stubs/issues/911
where a stale/mismatched `typing.mpy` was published for over a year.
"""

import json
import re
import shutil
import subprocess
from pathlib import Path

import pytest

MPY_SOURCES = ["typing.py", "typing_extensions.py", "abc.py"]
MANIFESTS = ["typing.json", "typing_mpy.json"]


@pytest.fixture(scope="session")
def mip_path(pytestconfig: pytest.Config) -> Path:
    return pytestconfig.rootpath / "mip"


def module_version(mip_path: Path, module: str = "typing.py") -> str:
    match = re.search(r"""^__version__\s*=\s*['"]([^'"]+)['"]""", (mip_path / module).read_text(), re.MULTILINE)
    assert match, f"no __version__ in mip/{module}"
    return match.group(1)


@pytest.mark.parametrize("source", MPY_SOURCES)
def test_mpy_is_up_to_date(mip_path: Path, tmp_path: Path, source: str):
    """The committed .mpy must be a cross-compile of the .py next to it."""
    if not shutil.which("mpy-cross"):
        pytest.skip("mpy-cross is not installed")
    committed = mip_path / f"{Path(source).stem}.mpy"
    assert committed.exists(), f"mip/{committed.name} is missing"

    shutil.copy(mip_path / source, tmp_path / source)
    # compile from within tmp_path so the source path embedded in the .mpy matches x-compile.sh
    subprocess.run(["mpy-cross", source, "-O3"], cwd=tmp_path, check=True, capture_output=True, text=True)

    assert (tmp_path / committed.name).read_bytes() == committed.read_bytes(), (
        f"mip/{committed.name} is out of date with mip/{source} - run mip/x-compile.sh"
    )


@pytest.mark.parametrize("manifest", MANIFESTS)
def test_manifest_urls_match_target(mip_path: Path, manifest: str):
    """Each mip manifest entry must install the file it is named after."""
    package = json.loads((mip_path / manifest).read_text())
    for target, url in package["urls"]:
        assert url.startswith("github:josverl/micropython-stubs/mip/"), f"{manifest}: unexpected url {url}"
        assert url.rsplit("/", 1)[-1] == target, f"{manifest}: {target} is installed from {url}"
        assert (mip_path / target).exists(), f"{manifest}: mip/{target} does not exist"


@pytest.mark.parametrize("manifest", MANIFESTS)
def test_manifest_version_matches_module(mip_path: Path, manifest: str):
    package = json.loads((mip_path / manifest).read_text())
    assert package["version"] == module_version(mip_path), f"{manifest}: version does not match mip/typing.py __version__"


def test_module_versions_are_in_sync(mip_path: Path):
    assert module_version(mip_path, "typing.py") == module_version(mip_path, "typing_extensions.py")
