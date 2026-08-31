from pathlib import Path

import pytest


@pytest.fixture(scope="session")
def stdlib_package_path(pytestconfig: pytest.Config) -> Path:
    return pytestconfig.rootpath / "publish" / "micropython-stdlib-stubs"


def test_micropython_stdlib_package_contains_no_python_files(stdlib_package_path: Path):
    """The stub-only stdlib package must not ship runtime Python modules."""
    package_roots = ("stdlib", "_mpy_shed", "stubs")
    python_files = sorted(
        path.relative_to(stdlib_package_path).as_posix()
        for package_root in package_roots
        for path in (stdlib_package_path / package_root).rglob("*.py")
    )

    assert not python_files, "micropython-stdlib-stubs contains runtime .py files:\n" + "\n".join(python_files)
