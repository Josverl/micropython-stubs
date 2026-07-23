import logging
from pathlib import Path

import pytest
from test_snippets import SOURCES, run_typechecker

# only snippets tests
pytestmark = [pytest.mark.snippets]

log = logging.getLogger()


@pytest.mark.parametrize("portboard", ["stdlib"], scope="session")
@pytest.mark.parametrize("version", ["-"], scope="session")
@pytest.mark.parametrize("feature", ["stdlib_only"], scope="session")
@pytest.mark.parametrize("stub_source", SOURCES, scope="session")
@pytest.mark.parametrize(
    "linter",
    [
        "pyright",
        "mypy",
        pytest.param(
            "basilisk",
            marks=pytest.mark.xfail(
                reason="Basilisk support is experimental - https://github.com/Nimblesite/Basilisk/issues/312",
                strict=False,
            ),
        ),
    ],
)
def test_typecheck_stdlib_only(
    stub_source: str,
    portboard: str,
    feature: str,
    snip_path_fx: Path,
    version: str,
    linter: str,
    copy_type_stubs_fx,  # Avoid needing autouse fixture
    caplog: pytest.LogCaptureFixture,
    pytestconfig: pytest.Config,
):
    # Use the isolated workspace (snip_path_fx) whose typings/ symlink is refreshed
    # from the freshly built stubs by copy_type_stubs_fx. Running against the original
    # feat_stdlib_only folder would pick up a stale typings/ directory left over from a
    # previous run and report false-positive errors.
    if not snip_path_fx or not snip_path_fx.exists():
        pytest.skip(f"no feature folder for {feature}")
    caplog.set_level(logging.INFO)
    log.info(f"Typechecker {linter} : {portboard}, {feature} from {stub_source}")

    info_msg, errorcount = run_typechecker(snip_path_fx, version, portboard, pytestconfig, linter=linter)
    assert errorcount == 0, info_msg
