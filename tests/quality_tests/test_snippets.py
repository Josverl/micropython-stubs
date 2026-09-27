import logging
import sys
from pathlib import Path

import pytest
import typecheck
from conftest import get_test_versions
from typecheck import LINTER_PARAMS, copy_config_files, port_and_board, run_typechecker

# only snippets tests
pytestmark = [pytest.mark.snippets]

log = logging.getLogger()

# features that are not supported by all ports or boards and/or require a specific version
# format: <port>-<board>:<condition> or <feature>:<condition>
# if the conditon IS met, the feature is skipped - so please read as SKIP if condition or prefix with 'skip'
# condition: version<1.21.0 or not port.startswith('esp')

# features that are supported by neary all ports and boards
CORE = [
    "micropython",
    "stdlib",
    "asyncio:skip port in ['esp8266', 'webassembly']",
    "machine:skip port in ['windows', 'unix', 'webassembly']",
]
RP2_CORE = CORE + ["asm_pio:skip version < 1.24.0"]
# a dictionary of features to verify for each port or port_board
PORTBOARD_FEATURES = {
    "stm32": CORE,
    "stm32-pybv11": CORE,
    "esp32": CORE
    + [
        "networking",
        "bluetooth:skip version<1.20.0",
        "espnow:skip version<1.21.0",
    ],
    "esp32-esp32_generic_c6:skip version<1.24.0": CORE + ["networking", "bluetooth", "espnow"],
    "esp32-esp32_generic_s3:skip version<1.24.0": CORE + ["networking", "bluetooth", "espnow"],
    #
    "esp8266": CORE + ["networking"],  # TODO: New MCU stubs for esp8266, "espnow>=1.21.0"],
    "samd": CORE,
    "samd-seeed_wio_terminal": CORE,
    # "samd-ADAFRUIT_ITSYBITSY_M4_EXPRESS": CORE,
    "rp2": RP2_CORE,
    "rp2-pico:skip version>1.20.0": RP2_CORE,  # renamed later to rp2-rpi_pico
    "rp2-pico_w:skip version>1.20.0": RP2_CORE + ["networking"],
    #
    "rp2-rpi_pico:skip version<1.21.0": RP2_CORE,
    "rp2-rpi_pico_w:skip version<1.21.0": RP2_CORE
    + [
        "networking",
        "bluetooth:skip version<1.21.0",
        "aioble:skip version<1.21.0",
    ],
    "rp2-rpi_pico2:skip version<1.24.0": RP2_CORE,
    "rp2-rpi_pico2_w:skip version<1.25.0": RP2_CORE
    + [
        "networking",
        "bluetooth",
        "aioble",
    ],
    # "rp2-pimoroni_picolipo_16mb": CORE,
    "webassembly:skip version<1.23.0": CORE,
    "windows": CORE,
    "unix": CORE,
}

SOURCES = ["local"]  # , "pypi"] # do not pull from PyPI all the time

HERE = (Path(__file__).parent).resolve()
sys.path.append(str(HERE.parent.parent / ".github/workflows"))


def pytest_generate_tests(metafunc: pytest.Metafunc):
    """
    Generates a test parameterization for each portboard, version and feature defined in:
    - SOURCES
    - VERSIONS (filtered by --stable-only if requested)
    - PORTBOARD_FEATURES
    """
    versions = get_test_versions(metafunc.config)
    argnames = "stub_source, version, portboard, feature"
    args_lst = []
    copy_config_files()
    for src in SOURCES:
        for version in versions:
            # skip latest for pypi
            if src == "pypi" and version in {"preview", "latest"}:
                continue
            for key in PORTBOARD_FEATURES.keys():
                portboard = key
                if ":" in portboard:
                    portboard, condition = portboard.split(":", 1)
                    port, board = port_and_board(portboard)
                    if stub_ignore(condition, version, port, board, linter="pytest", is_source=False):
                        continue
                else:
                    port, board = port_and_board(portboard)

                # add the check_<port> feature
                args_lst.append([src, version, portboard, port])
                for feature in PORTBOARD_FEATURES[key]:
                    if ":" in feature:
                        # Check version for features, split feature in name and version
                        feature, condition = feature.split(":", 1)
                        if stub_ignore(condition, version, port, board, linter="pytest", is_source=False):
                            continue
                    feature = feature.strip()
                    args_lst.append([src, version, portboard, feature])
    metafunc.parametrize(argnames, args_lst, scope="session")


def stub_ignore(line, version, port, board, linter="pyright", is_source=True) -> bool:
    """Thin wrapper that keeps the historic signature used by this module."""
    return typecheck.stub_ignore(line, version, port, board, linter=linter, is_source=is_source, strict=not is_source)


@pytest.mark.parametrize(
    "linter",
    LINTER_PARAMS,
)
def test_typecheck(
    linter: str,
    stub_source: str,
    version: str,
    portboard: str,
    feature: str,
    snip_path_fx: Path,
    copy_type_stubs_fx,  # Avoid needing autouse fixture
    caplog: pytest.LogCaptureFixture,
    pytestconfig: pytest.Config,
):
    if not snip_path_fx or not snip_path_fx.exists():
        pytest.skip(f"no feature folder for {feature}")
    caplog.set_level(logging.INFO)

    log.info(f"Typecheck {linter} on {portboard}, {feature} {version} from {stub_source}")

    info_msg, errorcount = run_typechecker(snip_path_fx, version, portboard, pytestconfig, linter=linter)
    assert errorcount == 0, info_msg
