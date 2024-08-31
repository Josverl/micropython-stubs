import functools
import json
import logging
import re
import shutil
import subprocess
import time
import urllib.request
from pathlib import Path

import fasteners
import pytest

# only snippets tests
pytestmark = [pytest.mark.snippets]

log = logging.getLogger()

HERE = Path(__file__).parent.absolute()
_docker = None

# Cache for the Docker Hub tag list, shared across pytest-xdist workers so every
# worker collects the same parametrization (otherwise xdist aborts with
# "Different tests were collected between gw0 and gwN"). 24h TTL.
_DOCKER_TAGS_CACHE_FILE = HERE / ".docker_tags_cache.json"
_DOCKER_TAGS_CACHE_TTL = 24 * 60 * 60

# Fallback list of known micropython/unix Docker image versions (used when Docker Hub is unreachable)
_KNOWN_UNIX_VERSIONS = [
    "v1.20.0",
    "v1.21.0",
    "v1.22.0",
    "v1.23.0",
    "v1.24.0",
    "v1.24.1",
    "v1.25.0",
    "v1.26.0",
    "v1.27.0",
]


@functools.lru_cache()
def get_unix_docker_versions(minver: str = "v1.20.0") -> list:
    """
    Retrieve available version tags for the micropython/unix Docker image from Docker Hub.

    Falls back to a known static list when Docker Hub is unreachable.

    Result is cached to a JSON file (24h TTL) under an inter-process lock so
    every pytest-xdist worker computes the same parametrization matrix.

    Note: Fetches up to 100 tags. The micropython/unix image currently has far fewer
    than 100 version tags, so pagination is not required.

    Args:
        minver: The minimum version to include (default: v1.20.0, when typing module support was added).

    Returns:
        list: Sorted list of version strings (e.g. ["v1.20.0", "v1.21.0", ...]).
    """
    from packaging.version import Version

    min_version = Version(minver.lstrip("v"))
    version_pattern = re.compile(r"^v\d+\.\d+(\.\d+)?$")

    def _filter_and_sort(tags):
        versions = [
            t for t in tags if version_pattern.match(t) and Version(t.lstrip("v")) >= min_version
        ]
        return sorted(versions, key=lambda v: Version(v.lstrip("v")))

    # Fast path: file cache fresh.
    try:
        if _DOCKER_TAGS_CACHE_FILE.exists():
            data = json.loads(_DOCKER_TAGS_CACHE_FILE.read_text())
            if (
                time.time() - float(data.get("ts", 0)) < _DOCKER_TAGS_CACHE_TTL
                and data.get("minver") == minver
            ):
                tags = data.get("tags")
                if isinstance(tags, list) and tags:
                    return _filter_and_sort(tags)
    except Exception:
        pass

    # Slow path: serialize Docker Hub call across workers.
    lock = fasteners.InterProcessLock(str(_DOCKER_TAGS_CACHE_FILE) + ".lock")
    with lock:
        try:
            if _DOCKER_TAGS_CACHE_FILE.exists():
                data = json.loads(_DOCKER_TAGS_CACHE_FILE.read_text())
                if (
                    time.time() - float(data.get("ts", 0)) < _DOCKER_TAGS_CACHE_TTL
                    and data.get("minver") == minver
                ):
                    tags = data.get("tags")
                    if isinstance(tags, list) and tags:
                        return _filter_and_sort(tags)
        except Exception:
            pass

        try:
            url = "https://hub.docker.com/v2/repositories/micropython/unix/tags?page_size=100"
            with urllib.request.urlopen(url, timeout=10) as response:
                data = json.loads(response.read().decode())
            tags = [entry["name"] for entry in data.get("results", [])]
        except Exception:
            log.warning(
                "Could not fetch micropython/unix tags from Docker Hub; using fallback list",
                exc_info=True,
            )
            tags = list(_KNOWN_UNIX_VERSIONS)

        try:
            _DOCKER_TAGS_CACHE_FILE.write_text(
                json.dumps({"ts": time.time(), "minver": minver, "tags": tags})
            )
        except Exception:
            pass

        return _filter_and_sort(tags)


@functools.lru_cache()
def is_docker_running():
    global _docker
    if _docker is not None:
        return _docker
    try:
        result = subprocess.run(["docker", "info"], capture_output=True, text=True)
        _docker = result.returncode == 0
    except FileNotFoundError:
        _docker = False
    return _docker



@pytest.fixture(scope="session")
def copy_mpy_typings_fx(snip_path_fx: Path, ext: str, pytestconfig: pytest.Config):
    """
    Copy the typings.py(i) and the typings_extension.py(i) files to  snip_path
    """
    lib_path = snip_path_fx / "lib"
    lib_path.mkdir(exist_ok=True)
    specs = ["typing*", "abc"]
    for spec in specs:
        for file in lib_path.glob(f"{spec}.*"):
            file.unlink()
        for file in (pytestconfig.rootpath / "mip").glob(f"{spec}{ext}"):
            shutil.copy(file, lib_path)
    return True


@pytest.mark.parametrize("ext", [".py", ".mpy"], scope="session")
@pytest.mark.parametrize("mp_version", get_unix_docker_versions(), scope="session")
@pytest.mark.parametrize("feature", ["stdlib"], scope="session")
@pytest.mark.parametrize(
    "check_file",
    sorted({f.name for f in (HERE / "feat_typing").glob("check_*.py")}),
    scope="session",
)
@pytest.mark.parametrize("snip_path_fx", [HERE / "feat_typing"], scope="session")
def test_typing_runtime(
    copy_mpy_typings_fx,
    feature: str,
    snip_path_fx: Path,  # Not a fixture - overriden by parameterize
    check_file,
    mp_version: str,
    caplog: pytest.LogCaptureFixture,
    pytestconfig: pytest.Config,
):
    if not is_docker_running():
        pytest.skip("Docker is not running")

    if not snip_path_fx or not snip_path_fx.exists():
        FileNotFoundError(f"no feature folder for {feature}")
    caplog.set_level(logging.INFO)
    # log.info(f"Typechecker {linter} : {portboard}, {feature} from {stub_source}")

    cmd = f"docker run -u 1000 -v {snip_path_fx}:/code -v {snip_path_fx}/lib:/usr/lib/micropython --rm micropython/unix:{mp_version} micropython /code/{check_file}"
    log.info(f"Running {cmd}")
    result = subprocess.run(cmd, shell=True, cwd=snip_path_fx, text=True, capture_output=True)
    error = [
        line
        for line in result.stderr.split("\n") + result.stdout.split("\n")
        if "Traceback" not in line
    ]
    if error and "Unable to find image 'micropython/unix:" in error[0]:
        pytest.skip(error[0])
    assert result.returncode == 0, error
