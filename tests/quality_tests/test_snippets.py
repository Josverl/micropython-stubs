import logging
from pathlib import Path

import pytest
from typecheck import copy_config_files, port_and_board, run_typechecker, stub_ignore

# only snippets tests
pytestmark = pytest.mark.snippets

log = logging.getLogger()

CORE = ["micropython", "stdlib", "uasyncio:skip port=='esp8266'"]

# features that are not supported by all ports or boards and/or require a specific version
# format: <port>-<board>:<condition> or <feature>:<condition>
# if the conditon IS met, the feature is skipped - so please read as SKIP if condition or prefix with 'skip'
# condition: version<1.21.0 or not port.startswith('esp')
PORTBOARD_FEATURES = {
    "stm32": CORE,
    "stm32-pybv11": CORE,
    "esp32": CORE
    + [
        "networking",
        "bluetooth:skip version<1.20.0",
        "espnow:skip version<1.21.0",
    ],
    "esp8266": CORE + ["networking"],  # TODO: New board stubs for esp8266, "espnow>=1.21.0"],
    "samd": CORE,
    "samd-seeed_wio_terminal": CORE,
    # "samd-ADAFRUIT_ITSYBITSY_M4_EXPRESS": CORE,
    "rp2": CORE,
    "rp2-pico:skip version>1.20.0": CORE,  # renamed later to rp2-rpi_pico
    "rp2-pico_w:skip version>1.20.0": CORE + ["networking"],
    #
    "rp2-rpi_pico:skip version<1.21.0": CORE,
    "rp2-rpi_pico_w:skip version<1.21.0": CORE
    + [
        "networking",
        "bluetooth:skip version<1.21.0",
    ],
    # "rp2-pimoroni_picolipo_16mb": CORE,
}

SOURCES = ["local"]  # , "pypi"] # do not pull from PyPI all the time
VERSIONS = [
    "latest",
    "v1.22.0",
    "v1.21.0",
    "v1.20.0",
    # "v1.19.1",
    # "v1.18",
]


def pytest_generate_tests(metafunc: pytest.Metafunc):
    """
    Generates a test parameterization for each portboard, version and feature defined in:
    - SOURCES
    - VERSIONS
    - PORTBOARD_FEATURES
    """
    argnames = "stub_source, version, portboard, feature"
    args_lst = []
    copy_config_files()
    for src in SOURCES:
        for version in VERSIONS:
            # skip latest for pypi
            if src == "pypi" and version in ("preview", "latest"):
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

    # return issues


@pytest.mark.parametrize(
    "linter",
    ["pyright", "mypy"],
)
def test_typecheck(
    linter: str,
    stub_source: str,
    version: str,
    portboard: str,
    feature: str,
    snip_path: Path,
    copy_type_stubs,  # Avoid needing autouse fixture
    caplog: pytest.LogCaptureFixture,
    pytestconfig: pytest.Config,
):
    if not snip_path or not snip_path.exists():
        FileNotFoundError(f"no feature folder for {feature}")
    caplog.set_level(logging.INFO)

    log.info(f"Typecheck {linter} on {portboard}, {feature} {version} from {stub_source}")

    info_msg, errorcount = run_typechecker(snip_path, version, portboard, pytestconfig, linter=linter)
    assert errorcount == 0, info_msg
