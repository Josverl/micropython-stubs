import logging
import shutil
import subprocess
from pathlib import Path
import functools

import pytest
from test_snippets import SOURCES, run_typechecker

# only snippets tests
pytestmark = [pytest.mark.snippets]

log = logging.getLogger()

HERE = Path(__file__).parent.absolute()
_docker = None


@functools.lru_cache()
def is_docker_running():
    global _docker
    if _docker is not None:
        return _docker
    try:
        result = subprocess.run(["docker", "info"], capture_output=True, text=True)
        _docker = result.returncode == 0
    except FileNotFoundError:
        _docker = False
    return _docker


@pytest.fixture(scope="session")
def copy_mpy_typings_fx(snip_path_fx: Path, ext: str, pytestconfig: pytest.Config):
    """
    Copy the typings.py(i) and the typings_extension.py(i) files to  snip_path
    """
    lib_path = snip_path_fx / "lib"
    lib_path.mkdir(exist_ok=True)
    for file in lib_path.glob("typing*.p*"):
        file.unlink()

    for file in (pytestconfig.rootpath / "mip").glob(f"typing*{ext}"):
        shutil.copy(file, lib_path)
    return True


@pytest.mark.parametrize("ext", [".py", ".mpy"], scope="session")
@pytest.mark.parametrize(
    "mp_version",
    [
        # "v1.20.0",
        # "v1.23.0",
        "v1.24.1",
        # "latest",
    ],
    scope="session",
)
@pytest.mark.parametrize("version", ["preview"], scope="session")
@pytest.mark.parametrize("feature", ["stdlib"], scope="session")
@pytest.mark.parametrize(
    "check_file", set([f.name for f in (HERE / "feat_typing").glob("check_*.py")]), scope="session"
)
@pytest.mark.parametrize("snip_path", [HERE / "feat_typing"], scope="session")
def test_typing_runtime(
    copy_mpy_typings_fx,
    feature: str,
    snip_path: Path,
    check_file,
    version: str,
    mp_version: str,
    caplog: pytest.LogCaptureFixture,
    pytestconfig: pytest.Config,
):

    if not is_docker_running():
        pytest.skip("Docker is not running")

    if not snip_path or not snip_path.exists():
        FileNotFoundError(f"no feature folder for {feature}")
    caplog.set_level(logging.INFO)
    # log.info(f"Typechecker {linter} : {portboard}, {feature} from {stub_source}")
    # user = "foo"
    # cmd = f"docker run -u 1000 -e HOME=/{user} -v {snip_path}:/code -v {snip_path}/lib:/foo/.micropython/lib --rm micropython/unix:{mp_version} micropython {check_file}"
    cmd = f"docker run -u 1000 -v {snip_path}:/code -v {snip_path}/lib:/usr/lib/micropython --rm micropython/unix:{mp_version} micropython /code/{check_file}"
    log.info(f"Running {cmd}")
    result = subprocess.run(cmd, shell=True, cwd=snip_path, text=True, capture_output=True)
    error = [line for line in result.stdout.split("\n") if "Traceback" not in line]
    assert result.returncode == 0, error
