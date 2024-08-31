import logging
import shutil
import subprocess
from pathlib import Path

import pytest
from mpflash.versions import micropython_versions

# only snippets tests
pytestmark = [pytest.mark.snippets]

log = logging.getLogger()

HERE = Path(__file__).parent.absolute()


@pytest.fixture(scope="session")
def fxt_copy_mpy_typings(snip_path: Path, ext: str, pytestconfig: pytest.Config):
    """
    Copy the typings.py and the typings_extension.py files to snip_path
    return the number of files copied
    """
    # lib_path = snip_path / "lib"
    # lib_path.mkdir(exist_ok=True)
    # FIXME: this is a hack to get the lib path in the docker container
    lib_path = snip_path

    specs = [f"typing*", f"abc"]
    for spec in specs:
        for file in lib_path.glob(f"{spec}.*"):
            file.unlink()
        for file in (pytestconfig.rootpath / "mip").glob(f"{spec}{ext}"):
            shutil.copy(file, lib_path)

    return len(list((snip_path / "lib").glob("*.*")))


# test against recent versions , but a few versions  do not have a matching docker image
MPY_DOCKER_IMAGES = [
    v for v in micropython_versions() + ["latest"] if v not in ["v1.22.1", "v1.22.2"]
]


@pytest.mark.parametrize("ext", [".py", ".mpy"], scope="session")
@pytest.mark.parametrize("mp_version", MPY_DOCKER_IMAGES, scope="session")
@pytest.mark.parametrize("feature", ["stdlib"], scope="session")
@pytest.mark.parametrize(
    "check_file", [f.name for f in (HERE / "feat_typing").glob("check_*.py")], scope="session"
)
@pytest.mark.parametrize("snip_path", [HERE / "feat_typing"], scope="session")
def test_typing_runtime(
    fxt_copy_mpy_typings,
    feature: str,
    snip_path: Path,
    check_file,
    mp_version: str,
    caplog: pytest.LogCaptureFixture,
    pytestconfig: pytest.Config,
):

    if not snip_path or not snip_path.exists():
        FileNotFoundError(f"no feature folder for {feature}")
    caplog.set_level(logging.INFO)
    # log.info(f"Typechecker {linter} : {portboard}, {feature} from {stub_source}")

    cmd = f"docker run -u 1000 -e HOME=/foo -v .:/code -v ./lib:/foo/.micropython/lib --rm micropython/unix:{mp_version} micropython {check_file}"
    result = subprocess.run(cmd, shell=True, cwd=snip_path, text=True, capture_output=True)
    error = [
        line
        for line in result.stderr.split("\n") + result.stdout.split("\n")
        if "Traceback" not in line
    ]
    if "Unable to find image 'micropython/unix:" in error[0]:
        pytest.skip(error[0])
    assert result.returncode == 0, error
