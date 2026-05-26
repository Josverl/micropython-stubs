from __future__ import annotations

import importlib.util
from types import ModuleType
from typing import Any
import pytest
import subprocess
import sys
from pathlib import Path


def _load_setup_script_module():
    repo_root = Path(__file__).resolve().parents[2]
    script_path = repo_root / "setup_micropython_stubs.py"
    spec = importlib.util.spec_from_file_location("setup_micropython_stubs", script_path)
    assert spec is not None
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    setattr(module, "qprint", lambda *args, **kwargs: None)
    return module


def test_pick_package_by_name_prefers_latest_stable():
    mod: ModuleType = _load_setup_script_module()
    packages = [
        mod.StubPackage("micropython-rp2-stubs", "1.28.0", "rp2", "GENERIC"),
        mod.StubPackage("micropython-rp2-stubs", "1.28.0-preview", "rp2", "GENERIC"),
        mod.StubPackage("micropython-rp2-rpi_pico_w-stubs", "1.28.0", "rp2", "RPI_PICO_W"),
        mod.StubPackage("micropython-rp2-stubs", "1.27.0", "rp2", "GENERIC"),
    ]

    selected = mod.select_stub_package(packages, package_name="micropython-rp2-stubs", version="latest")

    assert selected.package == "micropython-rp2-stubs"
    assert selected.version == "1.28.0"
    assert selected.board == "GENERIC"


def test_package_sort_key_ignores_trailing_stubs_suffix():
    mod = _load_setup_script_module()
    packages = [
        "micropython-zeta-stubs",
        "micropython-alpha-stubs",
        "micropython-beta",
    ]

    ordered = sorted(packages, key=mod.package_sort_key)

    assert ordered == [
        "micropython-alpha-stubs",
        "micropython-beta",
        "micropython-zeta-stubs",
    ]


def test_render_pyproject_replaces_typings_and_source_paths():
    mod = _load_setup_script_module()
    template = (
        'include = ["src"]\n'
        'extraPaths = ["src/lib"]\n'
        'files = "src/*.py"\n'
        'mypy_path = "src/lib,typings"\n'
        'ignore = ["**/typings"]\n'
        'exclude = ["typings/**"]\n'
        'stubPath = "typings"\n'
        'typeshedPath = "typings"\n'
        'mypy_path = "typings"\n'
        'custom_typeshed_dir = "typings"\n'
        'extra-paths = ["typings"]\n'
        'typeshed = "./typings-stdlib"\n'
        'exclude = ["typings[\\/].*"]\n'
    )

    rendered = mod.render_pyproject(template, "stubs_custom", source_location="different")

    assert 'include = ["different"]' in rendered
    assert 'extraPaths = ["different/lib"]' in rendered
    assert 'files = "different/*.py"' in rendered
    assert 'mypy_path = "different/lib,stubs_custom"' in rendered

    assert '"**/stubs_custom"' in rendered
    assert 'stubPath = "stubs_custom"' in rendered
    assert 'typeshedPath = "stubs_custom"' in rendered
    assert 'mypy_path = "stubs_custom"' in rendered
    assert 'custom_typeshed_dir = "stubs_custom"' in rendered
    assert 'extra-paths = ["stubs_custom"]' in rendered
    assert 'typeshed = "./stubs_custom-stdlib"' in rendered
    assert 'exclude = ["stubs_custom/**"]' in rendered
    assert "stubs_custom[\\\\/].*" in rendered


def test_source_location_choices_lists_relative_directories(tmp_path: Path):
    mod = _load_setup_script_module()
    (tmp_path / "src").mkdir()
    (tmp_path / "app").mkdir()
    (tmp_path / ".hidden").mkdir()
    (tmp_path / "_private").mkdir()

    choices = mod.source_location_choices(tmp_path)

    assert choices == ["src", ".", "app"]


def test_build_ty_stdlib_typeshed(tmp_path: Path):
    mod = _load_setup_script_module()
    typings = tmp_path / "typings"
    output = tmp_path / "typings-stdlib"

    (typings / "stdlib" / "pkg").mkdir(parents=True)
    (typings / "stdlib" / "pkg" / "alpha.pyi").write_text("# alpha\n", encoding="utf-8")
    (typings / "time.pyi").write_text("# time\n", encoding="utf-8")

    mod.build_ty_stdlib_typeshed(typings_dir=typings, output_dir=output, clean=True)

    assert (output / "stdlib" / "pkg" / "alpha.pyi").exists()
    assert (output / "stdlib" / "time.pyi").exists()


def test_main_builds_ty_stdlib_after_install(monkeypatch, tmp_path: Path):
    mod = _load_setup_script_module()
    packages = [
        mod.StubPackage("micropython-rp2-stubs", "1.28.0", "rp2", "GENERIC"),
    ]
    sleep_calls: list[float] = []

    monkeypatch.setattr(mod, "_load_stub_packages_from_url", lambda timeout=15: packages)
    monkeypatch.setattr(mod, "_load_pyproject_template_from_url", lambda timeout=15: "[tool.ty.src]\ninclude = [\".\"]\n")
    monkeypatch.setattr(mod.time, "sleep", lambda seconds: sleep_calls.append(seconds))

    def _fake_install(package, target: Path):
        (target / "stdlib").mkdir(parents=True, exist_ok=True)
        (target / "stdlib" / "math.pyi").write_text("# math\n", encoding="utf-8")
        (target / "time.pyi").write_text("# time\n", encoding="utf-8")

    monkeypatch.setattr(mod, "install_stubs", _fake_install)

    rc = mod.main(
        [
            "--project-dir",
            str(tmp_path),
            "--package",
            "micropython-rp2-stubs",
            "--type-checker",
            "ty",
        ]
    )

    assert rc == 0
    assert sleep_calls == [1]
    assert (tmp_path / "typings-stdlib" / "stdlib" / "math.pyi").exists()
    assert (tmp_path / "typings-stdlib" / "stdlib" / "time.pyi").exists()


def test_write_optional_dependencies_creates_section(tmp_path: Path):
    mod = _load_setup_script_module()
    pyproject = tmp_path / "pyproject.toml"
    pyproject.write_text("[tool.black]\nline-length = 120\n", encoding="utf-8")

    pkg = mod.StubPackage("micropython-rp2-stubs", "1.28.0", "rp2", "GENERIC")
    mod.write_optional_dependencies(pyproject, package=pkg, target="typings")

    content = pyproject.read_text(encoding="utf-8")
    assert "[project.optional-dependencies]" in content
    assert "# install to folder typings" in content
    assert "stubs = [" in content
    assert '"micropython-rp2-stubs==1.28.0.*"' in content


def test_write_optional_dependencies_replaces_stubs_entry_only(tmp_path: Path):
    mod = _load_setup_script_module()
    pyproject = tmp_path / "pyproject.toml"
    pyproject.write_text(
        """
[project.optional-dependencies]
dev = ["pytest"]
# install to folder typings
# uv pip install -r pyproject.toml --extra stubs --target typings
stubs = [
  "micropython-old-stubs==1.0.0.*"
]
""".strip()
        + "\n",
        encoding="utf-8",
    )

    pkg = mod.StubPackage("micropython-esp32-stubs", "1.28.0", "esp32", "GENERIC")
    mod.write_optional_dependencies(pyproject, package=pkg, target="typings")

    content = pyproject.read_text(encoding="utf-8")
    assert "dev = [\"pytest\"]" in content
    assert "micropython-old-stubs" not in content
    assert '"micropython-esp32-stubs==1.28.0.*"' in content


def test_ensure_gitignore_typings_adds_once(tmp_path: Path):
    mod = _load_setup_script_module()
    gitignore = tmp_path / ".gitignore"
    gitignore.write_text("node_modules\n", encoding="utf-8")

    mod.ensure_gitignore_typings_with_mode(tmp_path, mode="always")
    mod.ensure_gitignore_typings_with_mode(tmp_path, mode="always")

    lines = gitignore.read_text(encoding="utf-8").splitlines()
    assert lines.count("typings*") == 1


def test_ensure_gitignore_typings_asks_and_can_skip(tmp_path: Path, monkeypatch):
    mod = _load_setup_script_module()
    gitignore = tmp_path / ".gitignore"
    gitignore.write_text("node_modules\n", encoding="utf-8")

    monkeypatch.setattr(mod, "prompt_for_gitignore_update", lambda project_dir, pattern: False)
    mod.ensure_gitignore_typings_with_mode(tmp_path, mode="ask")

    lines = gitignore.read_text(encoding="utf-8").splitlines()
    assert "typings*" not in lines


def test_ensure_gitignore_typings_asks_and_can_add(tmp_path: Path, monkeypatch):
    mod = _load_setup_script_module()
    gitignore = tmp_path / ".gitignore"
    gitignore.write_text("node_modules\n", encoding="utf-8")

    monkeypatch.setattr(mod, "prompt_for_gitignore_update", lambda project_dir, pattern: True)
    mod.ensure_gitignore_typings_with_mode(tmp_path, mode="ask")

    lines = gitignore.read_text(encoding="utf-8").splitlines()
    assert "typings*" in lines


def test_write_pyproject_keeps_existing_section_without_force(tmp_path: Path):
    mod = _load_setup_script_module()
    pyproject = tmp_path / "pyproject.toml"
    pyproject.write_text(
        """
[tool.black]
line-length = 120

[tool.pyright]
typeCheckingMode = "basic"
""".strip()
        + "\n",
        encoding="utf-8",
    )

    section = """
[tool.pyright]
typeCheckingMode = "standard"
stubPath = "typings"
""".strip()

    mod.update_pyproject(pyproject, section_header="tool.pyright", section_text=section, force=False)

    result = pyproject.read_text(encoding="utf-8")
    assert "[tool.black]" in result
    assert "line-length = 120" in result
    assert "typeCheckingMode = \"basic\"" in result
    assert "typeCheckingMode = \"standard\"" not in result


def test_write_pyproject_overwrites_existing_section_with_force(tmp_path: Path):
    mod = _load_setup_script_module()
    pyproject = tmp_path / "pyproject.toml"
    pyproject.write_text(
        """
[tool.black]
line-length = 120

[tool.pyright]
typeCheckingMode = "basic"
""".strip()
        + "\n",
        encoding="utf-8",
    )

    section = """
[tool.pyright]
typeCheckingMode = "standard"
stubPath = "typings"
""".strip()

    mod.update_pyproject(pyproject, section_header="tool.pyright", section_text=section, force=True)

    result = pyproject.read_text(encoding="utf-8")
    assert "[tool.black]" in result
    assert "line-length = 120" in result
    assert "typeCheckingMode = \"standard\"" in result
    assert "stubPath = \"typings\"" in result
    assert "typeCheckingMode = \"basic\"" not in result


def test_write_pyproject_appends_missing_section(tmp_path: Path):
    mod = _load_setup_script_module()
    pyproject = tmp_path / "pyproject.toml"
    pyproject.write_text(
        """
[tool.black]
line-length = 120
""".strip()
        + "\n",
        encoding="utf-8",
    )

    section = """
[tool.mypy]
mypy_path = "typings"
""".strip()

    mod.update_pyproject(pyproject, section_header="tool.mypy", section_text=section, force=False)

    result = pyproject.read_text(encoding="utf-8")
    assert "[tool.black]" in result
    assert "[tool.mypy]" in result
    assert "mypy_path = \"typings\"" in result


def test_extract_tool_sections_reads_template_sections():
    mod = _load_setup_script_module()
    template = """
[tool.pyright]
typeCheckingMode = "standard"

[tool.mypy]
mypy_path = "typings"
""".strip()

    sections = mod.extract_tool_sections(template)

    assert set(sections) == {"mypy", "pyright"}
    assert "[tool.pyright]" in sections["pyright"]
    assert "[tool.mypy]" in sections["mypy"]


def test_extract_tool_sections_drops_trailing_separator_comments():
    mod = _load_setup_script_module()
    template = """
[tool.ty.terminal]
output-format = "full"
error-on-warning = false

# ###################################################################
# mypy global options:

[tool.mypy]
mypy_path = "typings"
""".strip()

    sections = mod.extract_tool_sections(template)

    assert "# mypy global options:" not in sections["ty.terminal"]
    assert sections["ty.terminal"].strip().endswith("error-on-warning = false")


def test_available_type_checkers_filters_known_names():
    mod = _load_setup_script_module()
    sections = {
        "pyright": "[tool.pyright]\n",
        "mypy": "[tool.mypy]\n",
        "ty.environment": "[tool.ty.environment]\n",
        "ty.src": "[tool.ty.src]\n",
        "black": "[tool.black]\n",
    }

    checkers = mod.available_type_checkers(sections)

    assert checkers == ["mypy", "pyright", "ty"]


def test_sections_for_type_checker_includes_nested_ty_sections():
    mod = _load_setup_script_module()
    sections = {
        "mypy": "[tool.mypy]\nmypy_path = \"typings\"\n",
        "ty.environment": "[tool.ty.environment]\nextra-paths = [\"typings\"]\n",
        "ty.src": "[tool.ty.src]\ninclude = [\".\"]\n",
    }

    selected = mod.sections_for_type_checker(sections, "ty")

    assert selected == [
        ("tool.ty.environment", sections["ty.environment"]),
        ("tool.ty.src", sections["ty.src"]),
    ]


def test_filter_packages_by_wildcard_version():
    mod = _load_setup_script_module()
    packages = [
        mod.StubPackage("micropython-rp2-stubs", "1.28.0", "rp2", "GENERIC"),
        mod.StubPackage("micropython-rp2-stubs", "1.28.0-preview", "rp2", "GENERIC"),
        mod.StubPackage("micropython-rp2-stubs", "1.27.0", "rp2", "GENERIC"),
    ]

    filtered = mod.filter_packages_by_version(packages, version="v1.28.0.*")

    assert [pkg.version for pkg in filtered] == ["1.28.0"]


def test_build_parser_defaults_stable_version():
    mod = _load_setup_script_module()
    parser = mod.cli_parser()

    args = parser.parse_args([])

    assert args.version == "v1.28.0.*"
    assert args.type_checker is None
    assert args.force is False
    assert args.update_gitignore == "ask"
    assert not hasattr(args, "packages_url")


def test_normalize_type_checker_selection_allows_none():
    mod = _load_setup_script_module()

    assert mod.normalize_type_checker_selection(None) is None
    assert mod.normalize_type_checker_selection("") is None
    assert mod.normalize_type_checker_selection("none") is None
    assert mod.normalize_type_checker_selection("  NoNe  ") is None
    assert mod.normalize_type_checker_selection("mypy") == "mypy"


def test_ordered_type_checker_choices_puts_pyright_first_and_none_last():
    mod = _load_setup_script_module()

    ordered = mod.ordered_type_checker_choices(["mypy", "pyright", "ty", "zuban"])

    assert ordered == ["pyright", "mypy", "ty", "zuban", "none"]


def test_main_with_type_checker_none_installs_without_pyproject_changes(monkeypatch, tmp_path: Path):
    mod = _load_setup_script_module()
    packages = [
        mod.StubPackage("micropython-rp2-stubs", "1.28.0", "rp2", "GENERIC"),
    ]
    install_calls: list[tuple[str, Path]] = []
    captured: dict[str, object] = {}
    select_calls: list[dict[str, object]] = []

    monkeypatch.setattr(mod.sys.stdin, "isatty", lambda: True)
    monkeypatch.setattr(mod.sys.stdout, "isatty", lambda: True)

    class _Prompt:
        def __init__(self, value):
            self.value = value

        def ask(self):
            return self.value

    class _FormPrompt:
        def ask(self):
            return {
                "project_dir": str(tmp_path),
                "source_location": "lib_src",
                "type_checker": "none",
                "update_gitignore": False,
                "confirm_apply": True,
            }

    def _form(**kwargs):
        captured["fields"] = sorted(kwargs)
        return _FormPrompt()

    def _path(*args, **kwargs):
        return _Prompt(str(tmp_path))

    def _select(*args, **kwargs):
        select_calls.append(kwargs)
        return _Prompt("none" if len(select_calls) == 1 else "lib_src")

    monkeypatch.setattr(mod, "_load_stub_packages_from_url", lambda timeout=15: packages)
    (tmp_path / "lib_src").mkdir()
    monkeypatch.setattr(
        mod,
        "_load_pyproject_template_from_url",
        lambda timeout=15: "[tool.pyright]\nstubPath = \"typings\"\n\n[tool.mypy]\nmypy_path = \"typings\"\n",
    )
    monkeypatch.setattr(mod.questionary, "select", _select)
    monkeypatch.setattr(mod.questionary, "confirm", lambda *args, **kwargs: _Prompt(True))
    monkeypatch.setattr(mod.questionary, "path", _path)
    monkeypatch.setattr(mod.questionary, "form", _form)
    monkeypatch.setattr(mod, "update_pyproject", lambda *args, **kwargs: (_ for _ in ()).throw(AssertionError("pyproject should not be updated")))
    monkeypatch.setattr(
        mod,
        "write_optional_dependencies",
        lambda *args, **kwargs: (_ for _ in ()).throw(AssertionError("optional dependencies should not be written")),
    )
    monkeypatch.setattr(mod, "ensure_gitignore_typings_with_mode", lambda *args, **kwargs: None)
    monkeypatch.setattr(mod, "install_stubs", lambda package, target: install_calls.append((package.package, target)))

    rc = mod.main(
        [
            "--package",
            "micropython-rp2-stubs",
        ]
    )

    assert rc == 0
    assert captured["fields"] == ["confirm_apply", "type_checker", "update_gitignore"]
    assert len(select_calls) == 2
    assert select_calls[0]["choices"] == ["src", ".", "lib_src"]
    assert select_calls[0]["default"] == "src"
    assert select_calls[1]["choices"] == ["pyright", "mypy", "none"]
    assert select_calls[1]["default"] == "pyright"
    assert install_calls == [("micropython-rp2-stubs", tmp_path / "typings")]
    assert not (tmp_path / "pyproject.toml").exists()


def test_main_creates_selected_source_folder_when_missing(monkeypatch, tmp_path: Path):
    mod = _load_setup_script_module()
    packages = [
        mod.StubPackage("micropython-rp2-stubs", "1.28.0", "rp2", "GENERIC"),
    ]

    monkeypatch.setattr(mod.sys.stdin, "isatty", lambda: True)
    monkeypatch.setattr(mod.sys.stdout, "isatty", lambda: True)

    class _Prompt:
        def __init__(self, value):
            self.value = value

        def ask(self):
            return self.value

    class _FormPrompt:
        def ask(self):
            return {
                "type_checker": "none",
                "update_gitignore": False,
                "confirm_apply": True,
            }

    select_calls: list[dict[str, object]] = []

    def _select(*args, **kwargs):
        select_calls.append(kwargs)
        return _Prompt("src" if len(select_calls) == 1 else "none")

    monkeypatch.setattr(mod, "_load_stub_packages_from_url", lambda timeout=15: packages)
    monkeypatch.setattr(mod, "_load_pyproject_template_from_url", lambda timeout=15: "[tool.mypy]\nmypy_path = \"typings\"\n")
    monkeypatch.setattr(mod.questionary, "path", lambda *args, **kwargs: _Prompt(str(tmp_path)))
    monkeypatch.setattr(mod.questionary, "select", _select)
    monkeypatch.setattr(mod.questionary, "confirm", lambda *args, **kwargs: _Prompt(True))
    monkeypatch.setattr(mod.questionary, "form", lambda **kwargs: _FormPrompt())
    monkeypatch.setattr(mod, "update_pyproject", lambda *args, **kwargs: None)
    monkeypatch.setattr(mod, "write_optional_dependencies", lambda *args, **kwargs: None)
    monkeypatch.setattr(mod, "ensure_gitignore_typings_with_mode", lambda *args, **kwargs: None)
    monkeypatch.setattr(mod, "install_stubs", lambda package, target: None)

    rc = mod.main(["--package", "micropython-rp2-stubs"])

    assert rc == 0
    assert select_calls[0]["choices"] == ["src", "."]
    assert (tmp_path / "src").is_dir()


def test_main_collects_upfront_questions_before_changes(monkeypatch, tmp_path: Path):
    mod = _load_setup_script_module()
    captured: dict[str, object] = {}
    updated_sections: list[str] = []
    select_calls: list[dict[str, object]] = []

    packages = [
        mod.StubPackage("micropython-rp2-stubs", "1.28.0", "rp2", "GENERIC"),
    ]

    monkeypatch.setattr(mod.sys.stdin, "isatty", lambda: True)
    monkeypatch.setattr(mod.sys.stdout, "isatty", lambda: True)

    class _Prompt:
        def __init__(self, value):
            self.value = value

        def ask(self):
            return self.value

    class _FormPrompt:
        def ask(self):
            return {
                "project_dir": str(tmp_path),
                "source_location": "different",
                "type_checker": "mypy",
                "package_name": "micropython-rp2-stubs",
                "update_gitignore": True,
                "confirm_apply": True,
            }

    def _form(**kwargs):
        captured["fields"] = sorted(kwargs)
        return _FormPrompt()

    def _path(*args, **kwargs):
        return _Prompt(str(tmp_path))

    def _select(*args, **kwargs):
        select_calls.append(kwargs)
        return _Prompt("different" if len(select_calls) == 1 else "mypy")

    monkeypatch.setattr(mod.questionary, "select", _select)
    monkeypatch.setattr(mod.questionary, "autocomplete", lambda *args, **kwargs: _Prompt("micropython-rp2-stubs"))
    monkeypatch.setattr(mod.questionary, "confirm", lambda *args, **kwargs: _Prompt(True))
    monkeypatch.setattr(mod.questionary, "path", _path)
    monkeypatch.setattr(mod.questionary, "form", _form)

    monkeypatch.setattr(mod, "_load_stub_packages_from_url", lambda timeout=15: packages)
    (tmp_path / "different").mkdir()
    monkeypatch.setattr(
        mod,
        "_load_pyproject_template_from_url",
        lambda timeout=15: "[tool.pyright]\ninclude = [\"src\"]\nextraPaths = [\"src/lib\"]\nstubPath = \"typings\"\n\n[tool.mypy]\nfiles = \"src/*.py\"\nmypy_path = \"src/lib,typings\"\n",
    )
    monkeypatch.setattr(mod, "install_stubs", lambda package, target: None)
    monkeypatch.setattr(mod, "write_optional_dependencies", lambda *args, **kwargs: None)
    monkeypatch.setattr(mod, "ensure_gitignore_typings_with_mode", lambda *args, **kwargs: None)
    monkeypatch.setattr(
        mod,
        "update_pyproject",
        lambda pyproject_path, section_header, section_text, force=False: updated_sections.append(section_text),
    )

    rc = mod.main([])

    assert rc == 0
    assert captured["fields"] == ["confirm_apply", "package_name", "type_checker", "update_gitignore"]
    assert len(select_calls) == 2
    assert select_calls[0]["choices"] == ["src", ".", "different"]
    assert select_calls[0]["default"] == "src"
    assert select_calls[1]["choices"] == ["pyright", "mypy", "none"]
    assert select_calls[1]["default"] == "pyright"
    assert len(updated_sections) == 1
    assert 'files = "different/*.py"' in updated_sections[0]
    assert 'mypy_path = "different/lib,typings"' in updated_sections[0]


def test_install_stubs_retries_on_metadata_error(monkeypatch, tmp_path: Path):
    mod = _load_setup_script_module()
    pkg = mod.StubPackage("micropython-esp32-stubs", "1.28.0", "esp32", "GENERIC")
    target = tmp_path / "typings"
    target.mkdir(parents=True, exist_ok=True)
    (target / "leftover.txt").write_text("x", encoding="utf-8")

    calls: list[dict[str, object]] = []

    def _run(cmd, **kwargs):
        calls.append({"cmd": cmd, **kwargs})
        if len(calls) == 1:
            return subprocess.CompletedProcess(
                cmd,
                1,
                stdout="",
                stderr="Failed to read metadata from installed package",
            )
        return subprocess.CompletedProcess(cmd, 0, stdout="ok\n", stderr="")

    monkeypatch.setattr(mod.subprocess, "run", _run)

    mod.install_stubs(pkg, target=target)

    assert len(calls) == 2
    assert calls[0].get("check") is False
    assert calls[1].get("check") is True
    assert not (target / "leftover.txt").exists()


def test_install_stubs_raises_on_non_metadata_error(monkeypatch, tmp_path: Path):
    mod = _load_setup_script_module()
    pkg = mod.StubPackage("micropython-esp32-stubs", "1.28.0", "esp32", "GENERIC")
    target = tmp_path / "typings"

    def _run(cmd, **kwargs):
        return subprocess.CompletedProcess(cmd, 2, stdout="", stderr="network timeout")

    monkeypatch.setattr(mod.subprocess, "run", _run)

    try:
        mod.install_stubs(pkg, target=target)
        assert False, "Expected CalledProcessError"
    except subprocess.CalledProcessError as exc:
        assert exc.returncode == 2
