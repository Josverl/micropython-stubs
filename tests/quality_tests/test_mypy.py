import logging
from pathlib import Path

import pytest
from test_snippets import SOURCES, run_typechecker

# only snippets tests
pytestmark = [pytest.mark.snippets]

log = logging.getLogger()

HERE = Path(__file__).parent.absolute()

# running test for all issues , so need to test with boards that have as much functionality as possible
@pytest.mark.parametrize("portboard", ["esp32","rp2-rpi_pico_w"], scope="session")
@pytest.mark.parametrize("version", ["v1.24.1","v1.25.0-preview"], scope="session")
@pytest.mark.parametrize("feature", ["stdlib"], scope="session")
@pytest.mark.parametrize("stub_source", SOURCES, scope="session")
@pytest.mark.parametrize("snip_path", [HERE / "feat_mypy"], scope="session")
@pytest.mark.parametrize(
    "linter",
    ["mypy"],
)
def test_mypy(
    type_stub_cache_path_fx: Path,
    stub_source: str,
    portboard: str,
    feature: str,
    snip_path: Path,
    version: str,
    linter: str,
    copy_type_stubs_fx,  # Avoid needing autouse fixture
    caplog: pytest.LogCaptureFixture,
    pytestconfig: pytest.Config,
):

    if not snip_path or not snip_path.exists():
        FileNotFoundError(f"no feature folder for {feature}")
    caplog.set_level(logging.INFO)
    log.info(f"Typechecker {linter} : {portboard}, {feature} from {stub_source}")

    info_msg, errorcount = run_typechecker(snip_path, version, portboard, pytestconfig, linter=linter)
    assert errorcount == 0, info_msg
