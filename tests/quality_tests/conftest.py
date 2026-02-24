"""Pytest configuration file for snippets tests.

- snip_path_fx
  returns the path to the feature folder (feat_xxxx) or check folder (check_xxxx)

- type_stub_cache_path
  Is used to install the type stubs for the given portboard and version and cache it for 24 hours to speed up tests
  Returns the path to the cache folder

- install_stubs
  is the function that does the actual pip install to a folder

- copy_type_stubs_fx
  copies the type stubs from the cache to the feature folder

- pytest_runtest_makereport 
  is used to add the caplog to the test report to make it avaialble to VSCode test explorer

"""

import json
import shutil
import subprocess
import time
from pathlib import Path

import fasteners
import pytest
from loguru import logger as log
from mpflash.versions import get_preview_mp_version, get_stable_mp_version, micropython_versions
from packaging.version import Version

SNIPPETS_PREFIX = "tests/quality_tests/"
MAX_CACHE_AGE = 24 * 60 * 60  # 24 hours


def pytest_addoption(parser: pytest.Parser):
    parser.addoption(
        "--stable-only",
        action="store_true",
        default=False,
        help="Only run tests for the current stable MicroPython release, skipping preview versions.",
    )


def major_minor(versions):
    """Create a list of the most recent version for each major.minor."""
    mm_groups = {}
    for v in versions:
        if v.endswith("-preview"):
            mm_groups["preview"] = [v]
            continue
        major_minor = f"{Version(v).major}.{Version(v).minor}"
        if major_minor not in mm_groups or "-preview" in v:
            mm_groups[major_minor] = [v]
        else:
            mm_groups[major_minor].append(v)
    return [max(v) for v in mm_groups.values()]


def get_test_versions(config: pytest.Config) -> list[str]:
    """Get the list of MicroPython versions to test based on --stable-only flag.
    
    Args:
        config: The pytest Config object.
        
    Returns:
        List of version strings to test (e.g., ['v1.27.0'] or ['v1.27.0', 'v1.26.0', 'v1.25.0']).
    """
    stable_only = config.getoption("--stable-only", default=False)
    if stable_only:
        return [get_stable_mp_version()]
    else:
        # Only the recent versions (last 3 major.minor releases)
        return sorted(major_minor(micropython_versions(minver="v1.24.0")), reverse=True)[:3]


def flat_version(version):
    """Converts a version string to a flat version string. (simplified)"""
    return version.replace(".", "_").replace("-", "_")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    pytest_runtest_makereport hook implementation.

    Executes all other hooks to obtain the report object. Looks at actual failing test calls, not setup/teardown. Adds the caplog errors and warnings to the report.

    Args:
        item: The pytest Item object.
        call: The pytest CallInfo object.

    Returns:
        The pytest Report object.

    """
    outcome = yield
    report = outcome.get_result()

    # we only look at actual failing test calls, not setup/teardown
    if report.when == "call" and report.failed:
        # add the caplog errors and warnings to the report
        if not "caplog" in item.funcargs:
            return
        caplog = item.funcargs["caplog"]
        report_txt = (
            "\n"
            + "\n".join([r.message for r in caplog.records])
            + "\n\n"
            + str(report.longreprtext)
        )
        report.longrepr = report_txt

        return report


# @pytest.fixture(scope="session")
# def type_stub_cache_path_fx(
#     portboard: str,
#     version: str,
#     stub_source: str,
#     pytestconfig: pytest.Config,
#     request: pytest.FixtureRequest,
# ) -> Path:
#     """
#     Installs a copy of the type stubs for the given portboard and version. Returns the path to the cache folder.

#     Args:
#         portboard: The portboard.
#         version: The version.
#         stub_source: The stub source.
#         pytestconfig: The pytest Config object.
#         request: The pytest FixtureRequest object.

#     Returns:
#         Path: The path to the cache folder.
#     """

#     log.debug(f"setup install type_stubs to cache: {stub_source}, {version}, {portboard}")
#     cache_key = f"stubber/{stub_source}/{version}/{portboard}"
#     flatversion = flat_version(version)
#     tsc_path = Path(
#         request.config.cache.makedir(f"typings_{flatversion}_{portboard}_stub_{stub_source}") # type: ignore
#     )
#     # prevent simultaneous updates to the cache
#     cache_lock = fasteners.InterProcessLock(tsc_path.parent / f"{tsc_path.name}.lock")
#     # check if stubs are already installed to the cache
#     with cache_lock:
#         if (tsc_path / "micropython.pyi").exists():
#             # check if stubs are in the cache
#             timestamp = request.config.cache.get(cache_key, None)
#             # if timestamp is not older than 24 hours, use cache

#             if timestamp and timestamp > (time.time() - MAX_CACHE_AGE):
#                 log.debug(f"Using cached type stubs for {portboard} {version}")
#                 return tsc_path

#         ok = install_stubs(portboard, version, stub_source, pytestconfig, tsc_path)
#         if not ok:
#             pytest.skip(f"Could not install stubs for {portboard} {version}")
#         # add the timestamp to the cache
#         request.config.cache.set(cache_key, time.time())

#     return tsc_path


def install_stubs(portboard, version, stub_source, pytestconfig, tsc_path: Path) -> bool:
    """
    Cleans up prior install to avoid stale files.
    Uses uv pip to install type stubs for the given portboard and version.

    Args:
        portboard: The portboard.
        version: The version.
        stub_source: The stub source.
        pytestconfig: The pytest Config object.
        flatversion: The flat version.
        tsc_path: The path to the cache folder.

    Returns:
        bool: True if the installation was successful, False otherwise.
    """
    if version == "preview":
        # use the latest preview version
        version = get_preview_mp_version()
        if not version.endswith("-preview"):
            raise ValueError(f"Expected preview version, got {version}")
    elif version == "latest":
        # use the latest release version
        version = get_stable_mp_version()

    flatversion = flat_version(version)
    # clean up prior install to avoid stale files
    if tsc_path.exists():
        shutil.rmtree(tsc_path, ignore_errors=True)
    # use pip to install type stubs
    # Install type stubs for portboard and version
    if stub_source == "pypi":
        # Add version
        cmd = f"uv pip install micropython-{portboard}-stubs=={version.lower().lstrip('v')}.* --target {tsc_path}"
    elif stub_source == "pypi-pre":
        # Add version and --pre
        cmd = f"uv pip install micropython-{portboard}-stubs=={version.lower().lstrip('v')}.* --pre --target {tsc_path}"
    else:
        # local source and --pre to pull in a pre-release version of stdlib
        if version == "-":
            # stdlib has no version in publish/path
            foldername = f"micropython-{portboard}-stubs"
        else:
            foldername = f"micropython-{flatversion}-{portboard}-stubs"
        # stubsource = pytestconfig.inipath.parent / f"repos/micropython-stubs/publish/{foldername}"
        stubs_source = pytestconfig.inipath.parent / f"publish/{foldername}"
        stdlib_source = pytestconfig.inipath.parent / f"publish/micropython-stdlib-stubs"
        if not stubs_source.exists():
            pytest.skip(f"Could not find stubs for {portboard} {version} at {stubs_source}")
        # --no-deps - avoids mixing different versions of stdlib
        # > For directories, uv caches based on the last-modified time of the pyproject.toml file,
        #    so that must be updated when stdlib is rebuilt.
        cmd = f"uv pip install --no-deps {stdlib_source} {stubs_source} --pre --target {tsc_path}"

    try:
        log.debug(f"Installing stubs: {cmd}")
        subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        # skip test if source connot be found
        print(f"{e.stderr}")
        pytest.skip(f"{e.stderr}")
        return False
    return True


@pytest.fixture(scope="function")
def snip_path_fx(feature: str, pytestconfig) -> Path:
    """
    Get the path to the feat_ or check_ folder.

    Args:
        feature: The feature.
        pytestconfig: The pytest Config object.

    Returns:
        Path: The path to the feature folder.
    """
    my_path = Path(__file__).parent.absolute()
    # snip_path = pytestconfig.inipath.parent / "tests/quality_tests" / f"feat_{feature}"
    snip_path = my_path / f"feat_{feature}"
    if not snip_path.exists():
        snip_path = my_path / f"check_{feature}"
    return snip_path


@pytest.fixture(scope="function")
def copy_type_stubs_fx(
    portboard: str, 
    version: str, 
    feature: str, 
    # type_stub_cache_path_fx: Path,
    snip_path_fx: Path,
    stub_source: str,
    pytestconfig: pytest.Config
):
    """
    Copies installed/cached type stubs from the cache to the feature folder.

    Args:
        portboard: The portboard.
        version: The version.
        feature: The feature.
        type_stub_cache_path: The path to the cache folder.
        snip_path: The path to the feature folder.
    """
    # cache_lock = fasteners.InterProcessLock(
    #     type_stub_cache_path_fx.parent / f"{type_stub_cache_path_fx.name}.lock"
    # )
    # with cache_lock:
    typecheck_lock = fasteners.InterProcessLock(snip_path_fx / "typecheck_lock.file")
    with typecheck_lock:
        log.trace(f"- copy_type_stubs: {version}, {portboard} to {feature}")
        # print(f"\n - copy_type_stubs : {version}, {portboard} to {feature}")
        if not snip_path_fx or not snip_path_fx.exists():
            # skip if no feature folder
            pytest.skip(f"no feature folder for {feature}")
        typings_path = snip_path_fx / "typings"
        if typings_path.exists():
            shutil.rmtree(typings_path, ignore_errors=True)

        ok = install_stubs(portboard, version, stub_source, pytestconfig, typings_path)
        if not ok:
            pytest.skip(f"Could not install stubs for {portboard} {version}")


def pytest_terminal_summary(terminalreporter, exitstatus, config: pytest.Config):
    stats = {}
    for status in ["passed", "failed", "xfailed", "skipped"]:
        stats[status] = snipcount(terminalreporter, status)
    executed = stats["passed"] + stats["failed"]
    stats["executed"] = executed
    stats["pass_rate"] = round(stats["passed"] / executed, 4) if executed > 0 else 0.0
    # keep for backward compatibility
    stats["snippet_score"] = int(stats["passed"] - stats["failed"])
    if executed > 0:
        # Write stats to file
        (config.rootpath / "results").mkdir(exist_ok=True)
        with open(config.rootpath / "results" / "snippet_score.json", "w") as f:
            json.dump(stats, f, indent=4)

        # print("----------------- Final summary -----------------")
        # print(json.dumps(stats, indent=4))
        # print("-------------------------------------------------")


def snipcount(terminalreporter, status: str):
    # Count the number of test snippets that have a given status
    if not terminalreporter.stats.get(status, []):
        return 0
    return len(
        [rep for rep in terminalreporter.stats[status] if rep.nodeid.startswith(SNIPPETS_PREFIX)]
    )
