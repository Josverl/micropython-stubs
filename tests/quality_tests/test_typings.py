import logging
import shutil
import subprocess
from pathlib import Path

import pytest
from test_snippets import SOURCES, run_typechecker

# only snippets tests
pytestmark = [pytest.mark.snippets]

log = logging.getLogger()

HERE = Path(__file__).parent.absolute()

@pytest.fixture(scope="session")
def copy_mpy_typings( snip_path:Path, ext:str,pytestconfig: pytest.Config):
    """
    Copy the typings.py and the typings_extension.py files to  snip_path
    """
    lib_path = snip_path / "lib"
    lib_path.mkdir(exist_ok=True)
    for file in lib_path.glob("typing*.py*"):
        file.unlink()

    for file in (pytestconfig.rootpath / "mip").glob(f"typing*{ext}"):
        shutil.copy(file, lib_path )
    return True




@pytest.mark.parametrize("ext", [".py",".mpy"], scope="session")
@pytest.mark.parametrize("mp_version", ["v1.20.0","latest"], scope="session")
@pytest.mark.parametrize("version", ["preview"], scope="session")
@pytest.mark.parametrize("feature", ["stdlib"], scope="session")
@pytest.mark.parametrize("check_file", [f.name for f in (HERE / "feat_typing").glob("check_*.py")], scope="session")
@pytest.mark.parametrize("snip_path", [HERE / "feat_typing"], scope="session")
def test_typing_runtime(
    copy_mpy_typings,
    feature: str,
    snip_path: Path,
    check_file,
    version: str,
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
    error = [line for line in result.stdout.split("\n") if "Traceback" not in line]
    assert result.returncode == 0, error

