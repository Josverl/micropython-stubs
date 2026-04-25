"""Pytest configuration file for snippets tests.

- snip_path_fx
  Creates an isolated per-test workspace by *copying* the feature folder files.
  Source files are copied (not symlinked) so that pyright's project-root discovery
  always resolves relative to the workspace rather than the original folder.
  Only ``typings/`` remains a symlink to the shared stub cache.

- type_stub_cache_path_fx
  Session-scoped fixture that installs type stubs once per (version, portboard, stub_source)
  and caches them for 24 hours.  An inter-process lock prevents simultaneous installations
  from parallel workers.

- install_stubs
  is the function that does the actual pip install to a folder

- copy_type_stubs_fx
  Links the cached type stubs into the isolated workspace for each test.

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
from mpflash.versions import get_preview_mp_version, get_stable_mp_version

SNIPPETS_PREFIX = "tests/quality_tests/"
MAX_CACHE_AGE = 24 * 60 * 60  # 24 hours

# Fallback version strings used when the GitHub API is unreachable.
# Keep in sync with the most recent stable + preview release.
_FALLBACK_STABLE_VERSION = "v1.28.0"
_FALLBACK_PREVIEW_VERSION = "v1.29.0-preview"


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


@pytest.fixture(scope="session")
def type_stub_cache_path_fx(
    portboard: str,
    version: str,
    stub_source: str,
    pytestconfig: pytest.Config,
    request: pytest.FixtureRequest,
) -> Path:
    """
    Installs type stubs for the given portboard and version to a persistent cache.
    Returns the path to the cache folder.

    The cache is valid for MAX_CACHE_AGE seconds (24 hours).
    An inter-process lock ensures that parallel test workers do not install the
    same stubs simultaneously.

    Args:
        portboard: The portboard.
        version: The version.
        stub_source: The stub source.
        pytestconfig: The pytest Config object.
        request: The pytest FixtureRequest object.

    Returns:
        Path: The path to the cache folder.
    """
    log.debug(f"setup install type_stubs to cache: {stub_source}, {version}, {portboard}")
    cache_key = f"stubber/{stub_source}/{version}/{portboard}"
    flatversion = flat_version(version)
    tsc_path = Path(
        request.config.cache.makedir(f"typings_{flatversion}_{portboard}_stub_{stub_source}")  # type: ignore
    )
    # prevent simultaneous updates to the cache across parallel workers
    cache_lock = fasteners.InterProcessLock(tsc_path.parent / f"{tsc_path.name}.lock")
    with cache_lock:
        if (tsc_path / "micropython.pyi").exists():
            # stubs appear to be installed – check the freshness timestamp
            timestamp = request.config.cache.get(cache_key, None)
            if timestamp and timestamp > (time.time() - MAX_CACHE_AGE):
                log.debug(f"Using cached type stubs for {portboard} {version}")
                return tsc_path

        ok = install_stubs(portboard, version, stub_source, pytestconfig, tsc_path)
        if not ok:
            pytest.skip(f"Could not install stubs for {portboard} {version}")
        # record the installation timestamp
        request.config.cache.set(cache_key, time.time())

    return tsc_path


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
        # use the latest preview version; fall back to the hardcoded constant
        # when the GitHub API is unreachable (no network / sandboxed environment).
        try:
            version = get_preview_mp_version()
        except Exception:
            version = _FALLBACK_PREVIEW_VERSION
        if not version.endswith("-preview"):
            raise ValueError(f"Expected preview version, got {version}")
    elif version == "latest":
        # use the latest stable release; same offline fallback logic.
        try:
            version = get_stable_mp_version()
        except Exception:
            version = _FALLBACK_STABLE_VERSION

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

    # _mpy_shed is gitignored inside publish/micropython-stdlib-stubs/ (generated
    # from reference/ by build.py) so it is absent in a fresh clone.  Copy it from
    # the reference folder when it is missing so that type stubs that import from
    # _mpy_shed (e.g. stdlib/sys/__init__.pyi) can be resolved correctly.
    _mpy_shed_src = pytestconfig.inipath.parent / "reference" / "_mpy_shed"
    _mpy_shed_dst = tsc_path / "_mpy_shed"
    if _mpy_shed_src.exists() and not _mpy_shed_dst.exists():
        shutil.copytree(_mpy_shed_src, _mpy_shed_dst)

    return True


@pytest.fixture(scope="function")
def snip_path_fx(feature: str, tmp_path: Path, pytestconfig: pytest.Config) -> Path:
    """
    Create an isolated per-test workspace based on the feat_<feature> or check_<feature> folder.

    Each test receives a unique temporary directory that contains:
    - real copies of all source files from the original feature folder, and
    - config files copied from _configs/ (pyproject.toml, etc.).

    The ``typings/`` sub-directory is intentionally omitted here; it is added by
    ``copy_type_stubs_fx`` from the shared stub cache.

    Using an isolated workspace per test means that parallel test workers never
    write to the same directory at the same time, eliminating the need for the
    per-folder ``typecheck_lock``.

    Args:
        feature: The feature name (used to locate feat_<feature> / check_<feature>).
        tmp_path: pytest's built-in per-test temporary directory.
        pytestconfig: The pytest Config object.

    Returns:
        Path: The path to the isolated workspace, or the (non-existing) feature
        folder when no matching directory was found.
    """
    my_path = Path(__file__).parent.absolute()
    source_path = my_path / f"feat_{feature}"
    if not source_path.exists():
        source_path = my_path / f"check_{feature}"
    if not source_path.exists():
        # Return the (non-existing) path so that the test can skip cleanly.
        return source_path

    workspace = tmp_path

    # Copy all files / sub-directories from the feature folder into the workspace
    # as REAL filesystem entries (not symlinks).
    #
    # Why not symlinks?  Pyright resolves symlinked directories to their real paths
    # before performing project-root discovery, so it would end up looking for
    # ``typings/`` next to the *original* feature folder rather than in the
    # workspace.  Copying the source files avoids that resolution entirely.
    _SKIP_NAMES = {"typings", "typecheck_lock.file"}
    for item in source_path.iterdir():
        if item.name in _SKIP_NAMES:
            continue
        dest = workspace / item.name
        if item.is_dir():
            shutil.copytree(item, dest)
        else:
            shutil.copy2(item, dest)

    # Copy per-folder type-checker config files from _configs/ so that each
    # workspace is self-contained and can be used directly from the command line.
    config_path = my_path / "_configs"
    for file in config_path.glob("*.*"):
        if file.name == "readme.md":
            continue
        try:
            shutil.copy(file, workspace)
        except Exception as e:
            log.warning(f"Could not copy {file} to {workspace}: {e}")

    return workspace


@pytest.fixture(scope="function")
def copy_type_stubs_fx(
    portboard: str,
    version: str,
    feature: str,
    type_stub_cache_path_fx: Path,
    snip_path_fx: Path,
    stub_source: str,
    pytestconfig: pytest.Config,
):
    """
    Links the cached type stubs into the isolated workspace for this test.

    Because each test already has its own isolated workspace (provided by
    ``snip_path_fx``), there is no need for a per-folder lock here – multiple
    tests can safely prepare their workspaces simultaneously.

    Args:
        portboard: The portboard.
        version: The version.
        feature: The feature name.
        type_stub_cache_path_fx: Path to the shared stub cache for this (version, portboard).
        snip_path_fx: Path to the isolated workspace for this test.
        stub_source: The stub source.
        pytestconfig: The pytest Config object.
    """
    log.trace(f"- copy_type_stubs: {version}, {portboard} to {feature}")
    if not snip_path_fx or not snip_path_fx.exists():
        pytest.skip(f"no feature folder for {feature}")

    typings_path = snip_path_fx / "typings"
    # Remove any pre-existing typings artefact (symlink or real directory).
    if typings_path.is_symlink():
        typings_path.unlink()
    elif typings_path.exists():
        shutil.rmtree(typings_path, ignore_errors=True)

    # Point the workspace's typings/ at the shared stub cache via a symlink.
    # Falling back to a full copy on platforms that do not support symlinks.
    try:
        typings_path.symlink_to(type_stub_cache_path_fx)
    except (OSError, NotImplementedError):
        shutil.copytree(type_stub_cache_path_fx, typings_path)


def pytest_terminal_summary(terminalreporter, exitstatus, config: pytest.Config):
    stats = {}
    for status in ["passed", "failed", "xfailed", "skipped"]:
        stats[status] = snipcount(terminalreporter, status)
    # simple straigth forward scoring
    stats["snippet_score"] = int(stats["passed"] - stats["failed"])
    
    # Always write stats to file (even if score is 0 or negative)
    # This ensures compare_score.py can reliably read the file
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
