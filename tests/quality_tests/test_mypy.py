import logging
from pathlib import Path

import pytest
from conftest import get_test_versions
from test_snippets import SOURCES, run_typechecker

# only snippets tests
pytestmark = [pytest.mark.snippets]

log = logging.getLogger()

HERE = Path(__file__).parent.absolute()


def pytest_generate_tests(metafunc: pytest.Metafunc):
    """Generate test parameters dynamically, respecting --stable-only flag."""
    if "test_mypy" in metafunc.function.__name__:
        versions = get_test_versions(metafunc.config)
        metafunc.parametrize("portboard", ["esp32", "rp2-rpi_pico_w"], scope="session")
        metafunc.parametrize("version", versions, scope="session")
        metafunc.parametrize("feature", ["stdlib"], scope="session")
        metafunc.parametrize("stub_source", SOURCES, scope="session")
        metafunc.parametrize("snip_path", [HERE / "feat_mypy"], scope="session")
        metafunc.parametrize("linter", ["mypy"])


def test_mypy(
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
