import logging
from pathlib import Path
from typing import Dict, List

import pytest

from test_snippets import SOURCES, run_pyright

# only snippets tests
pytestmark = pytest.mark.snippets

log = logging.getLogger()

HERE = Path(__file__).parent.absolute()

@pytest.mark.parametrize("portboard", ["stdlib"],scope="session") 
@pytest.mark.parametrize("version", ["-"],scope="session") 
@pytest.mark.parametrize("feature", ["stdlib"],scope="session") 
@pytest.mark.parametrize("stub_source", SOURCES,scope="session") 
@pytest.mark.parametrize("snip_path", [HERE / "feat_stdlib_only"],scope="session") 
def test_stdlib_pyright(
    type_stub_cache_path: Path,
    stub_source: str,
    portboard: str,
    feature: str,
    snip_path: Path,
    version: str,
    copy_type_stubs,  # Avoid needing autouse fixture
    caplog: pytest.LogCaptureFixture,
    pytestconfig: pytest.Config,
):
    
    if not snip_path or not snip_path.exists():
        FileNotFoundError(f"no feature folder for {feature}")
    caplog.set_level(logging.INFO)
    log.info(f"PYRIGHT {portboard}, {feature} from {stub_source}")

    info_msg, errorcount = run_pyright(snip_path, version, portboard, pytestconfig)
    assert errorcount == 0, info_msg