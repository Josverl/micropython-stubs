import logging
from pathlib import Path
from typing import Dict, List

import pytest
from test_snippets import SOURCES, run_typechecker

# only snippets tests
pytestmark = pytest.mark.snippets

log = logging.getLogger()

HERE = Path(__file__).parent.absolute()

@pytest.mark.parametrize("portboard", ["stdlib"],scope="session") 
@pytest.mark.parametrize("version", ["-"],scope="session") 
@pytest.mark.parametrize("feature", ["stdlib"],scope="session") 
@pytest.mark.parametrize("stub_source", SOURCES,scope="session") 
@pytest.mark.parametrize("snip_path", [HERE / "feat_stdlib_only"],scope="session") 
@pytest.mark.parametrize(
        "linter",
        ["pyright", "mypy"],
)
def test_typecheck_stdlib(
    type_stub_cache_path: Path,
    stub_source: str,
    portboard: str,
    feature: str,
    snip_path: Path,
    version: str,
    linter:str,
    copy_type_stubs,  # Avoid needing autouse fixture
    caplog: pytest.LogCaptureFixture,
    pytestconfig: pytest.Config,
):
    
    if not snip_path or not snip_path.exists():
        FileNotFoundError(f"no feature folder for {feature}")
    caplog.set_level(logging.INFO)
    log.info(f"Typechecker {linter} : {portboard}, {feature} from {stub_source}")

    info_msg, errorcount = run_typechecker(snip_path, version, portboard, pytestconfig, linter=linter)
    assert errorcount == 0, info_msg