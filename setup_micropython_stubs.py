#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = ["questionary"]
# ///
from __future__ import annotations

import argparse
import fnmatch
import json
import re
import shutil
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.request import urlopen
import questionary
from questionary import Style
from questionary import print as qprint

__version__ = "0.1.28"
BRANCH_NAME = "copilot/create-micropython-stubs-script"
REPO_ROOT_URL = f"https://raw.githubusercontent.com/Josverl/micropython-stubs/{BRANCH_NAME}"
DEFAULT_STUB_PACKAGES_URL = f"{REPO_ROOT_URL}/data/stub-packages.json"
PYPROJECT_TEMPLATE_URL = f"{REPO_ROOT_URL}/examples/src/pyproject.toml"


DEFAULT_STABLE_VERSION = "v1.28.0.*"
KNOWN_TYPE_CHECKERS = {"pyright", "mypy", "ty", "pyrefly", "zuban"}
TYPE_CHECKER_NONE = "none"
DEFAULT_SOURCE_LOCATION = "src"



# qprint
STYLE_BOLD = "bold green"
STYLE_NORMAL = "cyan"
STYLE_WARNING = "bold darkorange"

STUB_STYLE= Style(
        [
            ("qmark", "limegreen bold"),  # "?" prefix — bold, inherits fg
            ("question", "bold"),  # question text
            ("answer", "fg:green bold"),  # confirmed answer
            ("pointer", "fg:forestgreen bold"),  # selection cursor
            ("selected", "fg:green"),  # ticked checkbox item
            ("search_success", "bold fg:limegreen"),
            ("search_none", "bold fg:red"),
            ("highlighted", "fg: yellow bold bg:limegreen"), # currently highlighted autocomplete match
            ("separator", "fg:default"),
            ("instruction", "fg:default italic"),
            ("text", STYLE_NORMAL),
            # Autocomplete dropdown — dark background, dim text, no glare
            ("completion-menu", "bg:ansiblack fg:ansiwhite"),
            ("completion-menu.completion", "bg:ansiblack fg:ansiwhite"),
            ("completion-menu.completion.current", "bg:ansidarkgray fg:ansimagenta bold"),
            ("completion-menu.meta", "bg:ansiblack fg:ansidarkgray"),
            ("completion-menu.meta.completion", "bg:ansiblack fg:ansidarkgray"),
            ("completion-menu.meta.completion.current", "bg:ansiyellow fg:ansigray"),
        ]
)




def _ty_typeshed_dir_name(stub_path: str) -> str:
    return f"{stub_path}-stdlib"


def _ty_typeshed_config_path(stub_path: str) -> str:
    return f"./{_ty_typeshed_dir_name(stub_path)}"


@dataclass(frozen=True)
class StubPackage:
    package: str
    version: str
    port: str
    board: str


def _normalize_version(version: str) -> str:
    return version.strip().lower().lstrip("v")


def _stub_version_specifier(version: str) -> str:
    normalized = _normalize_version(version)
    parts = normalized.split(".")
    if all(part.isdigit() for part in parts):
        return f"=={normalized}.*"
    return f"=={normalized}"


def _stub_requirement(package: StubPackage) -> str:
    return f"{package.package}{_stub_version_specifier(package.version)}"


def _version_key(version: str) -> tuple[int, int, int, int]:
    value = _normalize_version(version)
    preview = 1 if "preview" in value else 0
    nums = value.split("-")[0].split(".")
    try:
        padded = [int(part) for part in nums] + [0, 0, 0]
    except ValueError as exc:
        raise ValueError(f"Unsupported version value in package metadata: {version}") from exc
    major, minor, patch = padded[:3]
    return (major, minor, patch, -preview)


def _load_stub_packages_from_url(timeout: int = 15) -> list[StubPackage]:
    response_obj = urlopen(DEFAULT_STUB_PACKAGES_URL, timeout=timeout)  # noqa: S310
    if response_obj is None:
        raise RuntimeError(f"Could not open package metadata URL: {DEFAULT_STUB_PACKAGES_URL}")
    with response_obj as response:
        payload = json.load(response)
    return [StubPackage(*row[:4]) for row in payload.get("packages", []) if len(row) >= 4]


def _load_pyproject_template_from_url(timeout: int = 15) -> str:
    response_obj = urlopen(PYPROJECT_TEMPLATE_URL, timeout=timeout)  # noqa: S310
    if response_obj is None:
        raise RuntimeError(f"Could not open pyproject template URL: {PYPROJECT_TEMPLATE_URL}")
    with response_obj as response:
        payload = response.read()
    return payload.decode("utf-8")


def package_sort_key(package_name: str) -> tuple[str, str]:
    normalized = package_name.removesuffix("-stubs")
    return (normalized, package_name)


def select_stub_package(
    packages: list[StubPackage],
    package_name: str,
    version: str,
) -> StubPackage:
    lookup = package_name.lower()
    candidates = [pkg for pkg in packages if pkg.package.lower() == lookup]

    if not candidates:
        raise ValueError(f"No matching stub package found for package '{package_name}'.")

    matching = filter_packages_by_version(candidates, version=version)
    if not matching:
        versions = sorted({_normalize_version(pkg.version) for pkg in candidates})
        raise ValueError(f"Version '{version}' not found. Available versions: {', '.join(versions)}")
    return max(matching, key=lambda pkg: _version_key(pkg.version))


def filter_packages_by_version(candidates: list[StubPackage], version: str) -> list[StubPackage]:
    req_version = _normalize_version(version)
    if req_version == "latest":
        filtered = [pkg for pkg in candidates if "preview" not in pkg.version.lower()]
        return filtered or candidates

    if "*" in req_version:
        if req_version.endswith(".*"):
            base = req_version[:-2]
            filtered = []
            for pkg in candidates:
                normalized = _normalize_version(pkg.version)
                if normalized == base or normalized.startswith(f"{base}."):
                    filtered.append(pkg)
            return filtered
        return [pkg for pkg in candidates if fnmatch.fnmatch(_normalize_version(pkg.version), req_version)]

    return [pkg for pkg in candidates if _normalize_version(pkg.version) == req_version]

def extract_tool_sections(template: str) -> dict[str, str]:
    pattern = re.compile(r"(?ms)^\[tool\.(?P<name>[^\]]+)\]\n(?P<body>.*?)(?=^\[tool\.|\Z)")
    sections: dict[str, str] = {}
    for match in pattern.finditer(template):
        name = match.group("name").strip().lower()
        body_lines = match.group("body").splitlines()
        # Drop trailing separator comments/blank lines that belong to the next block.
        while body_lines and (not body_lines[-1].strip() or body_lines[-1].lstrip().startswith("#")):
            body_lines.pop()
        body = "\n".join(body_lines)
        sections[name] = f"[tool.{name}]\n{body}\n"
    return sections


def available_type_checkers(sections: dict[str, str]) -> list[str]:
    checker_names = {name.split(".", 1)[0] for name in sections}
    available = [name for name in sorted(checker_names) if name in KNOWN_TYPE_CHECKERS]
    return available or sorted(sections)


def ordered_type_checker_choices(checkers: list[str]) -> list[str]:
    ordered: list[str] = []
    if "pyright" in checkers:
        ordered.append("pyright")
    ordered.extend(name for name in checkers if name not in {"pyright", TYPE_CHECKER_NONE})
    ordered.append(TYPE_CHECKER_NONE)
    return ordered


def sections_for_type_checker(sections: dict[str, str], type_checker: str) -> list[tuple[str, str]]:
    selected: list[tuple[str, str]] = []
    for name in sorted(sections):
        if name == type_checker or name.startswith(f"{type_checker}."):
            selected.append((f"tool.{name}", sections[name]))
    return selected


def normalize_type_checker_selection(value: str | None) -> str | None:
    normalized = (value or "").strip().lower()
    if not normalized or normalized == TYPE_CHECKER_NONE:
        return None
    return normalized


def source_location_choices(project_dir: str | Path) -> list[str]:
    project_root = Path(project_dir).resolve()
    choices = [DEFAULT_SOURCE_LOCATION, "."]
    if project_root.exists() and project_root.is_dir():
        for child in sorted(project_root.iterdir()):
            if child.is_dir() and not child.name.startswith((".", "_","typings")):
                choices.append(child.name)

    ordered: list[str] = []
    for choice in choices:
        if choice not in ordered:
            ordered.append(choice)
    return ordered


def prompt_for_path(
    message: str,
    default: str,
    *,
    only_directories: bool,
) -> str:
    answer = questionary.path(
        message,
        default=default,
        only_directories=only_directories,
        style=STUB_STYLE,
    ).ask()
    if not answer:
        raise SystemExit("Setup cancelled before applying changes.")
    return answer


def prompt_for_selection(message: str, choices: list[str], default: str | None = None) -> str:
    answer = questionary.select(message, choices=choices, default=default, style=STUB_STYLE).ask()
    if not answer:
        raise SystemExit("Setup cancelled before applying changes.")
    return answer

def prompt_for_gitignore_update(project_dir: Path, pattern: str) -> bool:
    if not sys.stdin.isatty() or not sys.stdout.isatty():
        qprint(
            f"Warning: non-interactive session; skipping .gitignore update for {pattern}. "
            "Use --update-gitignore=always to apply automatically.",
            style=STYLE_WARNING,
            file=sys.stderr,
        )
        return False

    import questionary

    try:
        answer = questionary.confirm(
            f"Add '{pattern}' to {project_dir / '.gitignore'} to avoid committing installed stubs?",
            default=True,
            style=STUB_STYLE,
        ).ask()
        return bool(answer)
    except Exception as exc:
        qprint(
            f"Warning: could not prompt for .gitignore update ({exc}); skipping update. "
            "Use --update-gitignore=always to apply automatically.",
            style=STYLE_WARNING,
            file=sys.stderr,
        )
        return False


def render_pyproject(template: str, stub_path: str, source_location: str = DEFAULT_SOURCE_LOCATION) -> str:
    source_path = (source_location or DEFAULT_SOURCE_LOCATION).strip() or DEFAULT_SOURCE_LOCATION
    source_lib_path = f"{source_path}/lib" if source_path != "." else "./lib"
    source_files_glob = f"{source_path}/*.py"

    rendered = template
    rendered = rendered.replace('include = ["src"]', f'include = ["{source_path}"]')
    rendered = rendered.replace('extraPaths = ["src/lib"]', f'extraPaths = ["{source_lib_path}"]')
    rendered = rendered.replace('files = "src/*.py"', f'files = "{source_files_glob}"')
    rendered = rendered.replace('mypy_path = "src/lib,typings"', f'mypy_path = "{source_lib_path},{stub_path}"')
    rendered = rendered.replace('"**/typings"', f'"**/{stub_path}"')
    rendered = rendered.replace('"typings/**"', f'"{stub_path}/**"')
    rendered = rendered.replace('stubPath = "typings"', f'stubPath = "{stub_path}"')
    rendered = rendered.replace('typeshedPath = "typings"', f'typeshedPath = "{stub_path}"')
    rendered = rendered.replace('mypy_path = "typings"', f'mypy_path = "{stub_path}"')
    rendered = rendered.replace('custom_typeshed_dir = "typings"', f'custom_typeshed_dir = "{stub_path}"')
    rendered = rendered.replace('extra-paths = ["typings"]', f'extra-paths = ["{stub_path}"]')
    rendered = rendered.replace('typeshed = "./typings-stdlib"', f'typeshed = "{_ty_typeshed_config_path(stub_path)}"')
    rendered = rendered.replace('"typings[\\/].*"', f'"{stub_path}[\\\\/].*"')
    return rendered


def _upsert_toml_section(existing_text: str, section_header: str, section_text: str) -> str:
    pattern = re.compile(rf"(?ms)^\[{re.escape(section_header)}\]\n.*?(?=^\[|\Z)")
    replacement = section_text.rstrip() + "\n"
    if pattern.search(existing_text):
        return pattern.sub(replacement, existing_text, count=1)

    if not existing_text.strip():
        return replacement

    return existing_text.rstrip() + "\n\n" + replacement


def _get_toml_section(existing_text: str, section_header: str) -> str | None:
    pattern = re.compile(rf"(?ms)^\[{re.escape(section_header)}\]\n.*?(?=^\[|\Z)")
    match = pattern.search(existing_text)
    if not match:
        return None
    return match.group(0).rstrip() + "\n"


def _render_optional_dependencies_body(existing_body: str, requirement: str, target: str) -> str:
    lines = existing_body.splitlines()
    cleaned: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if re.match(r"^stubs\s*=", stripped):
            if "[" in stripped and "]" not in stripped:
                i += 1
                while i < len(lines) and "]" not in lines[i]:
                    i += 1
                if i < len(lines):
                    i += 1
            else:
                i += 1
            while cleaned and not cleaned[-1].strip():
                cleaned.pop()
            if cleaned and cleaned[-1].strip().startswith("# uv pip install -r pyproject.toml --extra stubs --target"):
                cleaned.pop()
            if cleaned and cleaned[-1].strip().startswith("# install to folder"):
                cleaned.pop()
            continue

        cleaned.append(line)
        i += 1

    while cleaned and not cleaned[-1].strip():
        cleaned.pop()

    if cleaned:
        cleaned.append("")
    cleaned.append(f"# install to folder {target}")
    cleaned.append(f"# uv pip install -r pyproject.toml --extra stubs --target {target}")
    cleaned.append("stubs = [")
    cleaned.append(f'  "{requirement}"')
    cleaned.append("]")
    return "\n".join(cleaned)


def write_optional_dependencies(pyproject_path: Path, package: StubPackage, target: str) -> None:
    pyproject_path.parent.mkdir(parents=True, exist_ok=True)
    requirement = _stub_requirement(package)
    section_header = "project.optional-dependencies"
    existing_text = pyproject_path.read_text(encoding="utf-8") if pyproject_path.exists() else ""
    current = _get_toml_section(existing_text, section_header=section_header)

    if current is None:
        body = _render_optional_dependencies_body("", requirement=requirement, target=target)
    else:
        body = _render_optional_dependencies_body(
            current.split("\n", 1)[1],
            requirement=requirement,
            target=target,
        )

    section_text = f"[{section_header}]\n{body}\n"
    merged = _upsert_toml_section(existing_text, section_header=section_header, section_text=section_text)
    pyproject_path.write_text(merged, encoding="utf-8")
    qprint(f"Updated [{section_header}] stubs dependency: {requirement}", style=STYLE_NORMAL)

def ensure_gitignore_typings_with_mode(project_dir: Path, mode: str) -> None:
    gitignore = project_dir / ".gitignore"
    line = "typings*"
    if mode not in {"ask", "always", "never"}:
        raise ValueError(f"Unsupported gitignore mode: {mode}")

    if not gitignore.exists():
        if mode == "never":
            qprint(f"Skipping .gitignore update: {line} is recommended.", style=STYLE_WARNING)
            return
        if mode == "ask" and not prompt_for_gitignore_update(project_dir, line):
            qprint(f"Skipped .gitignore update for {line}", style=STYLE_WARNING)
            return
        gitignore.write_text(f"{line}\n", encoding="utf-8")
        qprint(f"Created .gitignore with {line}", style=STYLE_NORMAL)
        return

    lines = gitignore.read_text(encoding="utf-8").splitlines()
    active_patterns = {ln.strip() for ln in lines if ln.strip() and not ln.strip().startswith("#")}
    if line in active_patterns or "typings" in active_patterns or "**/typings*" in active_patterns:
        return

    if mode == "never":
        qprint(f"Skipping .gitignore update: {line} is recommended.", style=STYLE_WARNING)
        return
    if mode == "ask" and not prompt_for_gitignore_update(project_dir, line):
        qprint(f"Skipped .gitignore update for {line}", style=STYLE_WARNING)
        return

    content = gitignore.read_text(encoding="utf-8")
    suffix = "" if (not content or content.endswith("\n")) else "\n"
    gitignore.write_text(content + suffix + f"{line}\n", encoding="utf-8")
    qprint(f"Added {line} to {gitignore}", style=STYLE_NORMAL)


def update_pyproject(pyproject_path: Path, section_header: str, section_text: str, force: bool = False) -> None:
    pyproject_path.parent.mkdir(parents=True, exist_ok=True)
    recommended = section_text.rstrip() + "\n"

    if pyproject_path.exists():
        existing = pyproject_path.read_text(encoding="utf-8")
        existing_section = _get_toml_section(existing, section_header=section_header)
        if existing_section is None:
            merged = _upsert_toml_section(existing, section_header=section_header, section_text=section_text)
            pyproject_path.write_text(merged, encoding="utf-8")
            qprint(f"Added configuration section [{section_header}] in: {pyproject_path}", style=STYLE_NORMAL)
            return

        if existing_section == recommended:
            qprint(f"Keeping existing section [{section_header}] (already matches recommended settings).", style=STYLE_NORMAL)
            return

        if not force:
            qprint(
                f"Warning: existing section [{section_header}] differs from recommended settings; "
                f"keeping existing values. Use --force to overwrite.",
                style=STYLE_WARNING,
            )
            return

        merged = _upsert_toml_section(existing, section_header=section_header, section_text=section_text)
        pyproject_path.write_text(merged, encoding="utf-8")
        qprint(f"Updated configuration section [{section_header}] in: {pyproject_path}", style=STYLE_NORMAL)
        return

    pyproject_path.write_text(recommended, encoding="utf-8")
    qprint(f"Created configuration with section [{section_header}] in: {pyproject_path}", style=STYLE_NORMAL)


def install_stubs(package: StubPackage, target: Path) -> None:
    version_specifier = _stub_version_specifier(package.version)

    target.mkdir(parents=True, exist_ok=True)
    cmd = [
        "uv",
        "pip",
        "install",
        "-U",
        f"{package.package}{version_specifier}",
        "--target",
        str(target),
    ]
    qprint(f"Install command: {' '.join(cmd)}", style=STYLE_NORMAL)
    result = subprocess.run(cmd, check=False, capture_output=True, text=True)
    if result.stdout:
        qprint(result.stdout, end="", style=STYLE_NORMAL)
    if result.stderr:
        stderr_style = STYLE_NORMAL if result.returncode == 0 else STYLE_WARNING
        qprint(result.stderr, end="", file=sys.stderr, style=stderr_style)

    if result.returncode == 0:
        return

    metadata_error = "Failed to read metadata from installed package" in (result.stderr or "")
    if metadata_error:
        qprint(
            f"Warning: install target appears corrupted ({target}); cleaning and retrying once.",
            style=STYLE_WARNING,
            file=sys.stderr,
        )
        if target.exists():
            shutil.rmtree(target)
        target.mkdir(parents=True, exist_ok=True)
        subprocess.run(cmd, check=True)
        return

    raise subprocess.CalledProcessError(result.returncode, cmd, output=result.stdout, stderr=result.stderr)


def _copy_tree_contents(src: Path, dst: Path) -> int:
    copied = 0
    if not src.exists() or not src.is_dir():
        return copied

    for p in sorted(src.rglob("*")):
        rel = p.relative_to(src)
        target = dst / rel
        if p.is_dir():
            target.mkdir(parents=True, exist_ok=True)
            continue

        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(p, target)
        copied += 1

    return copied


def build_ty_stdlib_typeshed(typings_dir: Path, output_dir: Path, clean: bool = True) -> None:
    if not typings_dir.exists() or not typings_dir.is_dir():
        raise ValueError(f"Typings folder does not exist or is not a directory: {typings_dir}")

    merged_stdlib = output_dir / "stdlib"
    if clean and output_dir.exists():
        shutil.rmtree(output_dir)

    merged_stdlib.mkdir(parents=True, exist_ok=True)

    _copy_tree_contents(typings_dir / "stdlib", merged_stdlib)
    for p in sorted(typings_dir.glob("*.pyi")):
        shutil.copy2(p, merged_stdlib / p.name)

    qprint(f"Created Ty stdlib typeshed at: {merged_stdlib}", style=STYLE_NORMAL)



def cli_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Set up MicroPython stubs in a local project using uv.")
    parser.add_argument("--package", help="Exact package name (for example: micropython-rp2-rpi_pico_w-stubs).")
    parser.add_argument(
        "--version",
        default=DEFAULT_STABLE_VERSION,
        help=f"Version number or wildcard (for example: 1.28.0, v1.28.0, v1.28.0.*) or 'stable'. Default: {DEFAULT_STABLE_VERSION}",
    )
    parser.add_argument("--target", default="typings", help="Destination folder for installed stubs.")
    parser.add_argument("--project-dir", default=".", help="Project folder where pyproject.toml is created.")
    parser.add_argument(
        "--type-checker",
        help="Static type checker section to merge from template (for example: pyright, mypy) or 'none' to skip pyproject changes.",
    )
    parser.add_argument("--force", action="store_true", help="Overwrite existing checker sections when they differ from recommended settings.")
    parser.add_argument(
        "--update-gitignore",
        choices=["ask", "always", "never"],
        default="ask",
        help="Whether to add typings* to .gitignore when missing (default: ask).",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    qprint(f"MicroPython-stubs setup script (version {__version__})", style=STYLE_BOLD)
    parser = cli_parser()
    args = parser.parse_args(argv)
    type_checker = normalize_type_checker_selection(args.type_checker)

    try:
        packages = _load_stub_packages_from_url()
    except Exception as exc:
        parser.error(f"Could not load package metadata from URL {DEFAULT_STUB_PACKAGES_URL}: {exc}")

    sections: dict[str, str] = {}
    checkers: list[str] = []
    if type_checker is not None:
        try:
            template = _load_pyproject_template_from_url()
        except Exception as exc:
            parser.error(f"Could not load pyproject template from URL {PYPROJECT_TEMPLATE_URL}: {exc}")

        rendered_template = render_pyproject(template, args.target)
        sections = extract_tool_sections(rendered_template)
        checkers = available_type_checkers(sections)
        if not checkers:
            parser.error(f"No tool sections found in template URL payload: {PYPROJECT_TEMPLATE_URL}")

    package_name = args.package
    project_dir = args.project_dir
    source_location = DEFAULT_SOURCE_LOCATION
    gitignore_mode = args.update_gitignore

    needs_upfront_form = (not type_checker) or (not package_name)
    if needs_upfront_form: 
        if not (sys.stdin.isatty() and sys.stdout.isatty()):
            parser.error("Insufficient CLI options provided, interactive form requires a TTY.")

        project_dir = prompt_for_path(
            "Project folder :",
            default="./",
            only_directories=True,
        )
        source_location = prompt_for_selection(
            "Where is the code located in the project?",
            choices=source_location_choices(project_dir),
            default=DEFAULT_SOURCE_LOCATION,
        )

        form_fields: dict[str, Any] = {}

        if not type_checker:
            try:
                template = _load_pyproject_template_from_url()
            except Exception as exc:
                parser.error(f"Could not load pyproject template from URL {PYPROJECT_TEMPLATE_URL}: {exc}")

            rendered_template = render_pyproject(template, args.target, source_location=source_location)
            sections = extract_tool_sections(rendered_template)
            checkers = available_type_checkers(sections)
            template_checkers = ordered_type_checker_choices(checkers)

            form_fields["type_checker"] = questionary.select(
                "Select static type checker to configure :",
                choices=template_checkers,
                default="pyright" if "pyright" in template_checkers else template_checkers[0],
                style=STUB_STYLE,
            )

        if not package_name:
            filtered = filter_packages_by_version(packages, version=args.version)
            choices = sorted({pkg.package for pkg in filtered}, key=package_sort_key)
            if not choices:
                parser.error(f"No packages available for version filter '{args.version}'.")
            form_fields["package_name"] = questionary.autocomplete(
                "Select MicroPython stubs package (type to search) :",
                choices=choices,
                ignore_case=True,
                match_middle=True,
                validate=lambda text: True if text in choices else "Please select a package from the list",
                style=STUB_STYLE,
            )

        if gitignore_mode == "ask":
            form_fields["update_gitignore"] = questionary.confirm(
                "Add 'typings*' to .gitignore ?:",
                default=True,
                style=STUB_STYLE,
            )

        form_fields["confirm_apply"] = questionary.confirm(
            "Apply configuration and install stubs now? :",
            default=True,
            style=STUB_STYLE,
        )

        answers = questionary.form(**form_fields).ask()
        if not answers or not answers.get("confirm_apply"):
            qprint("Setup cancelled before applying changes.", style=STYLE_WARNING)
            raise SystemExit()

        type_checker = type_checker or normalize_type_checker_selection(answers.get("type_checker"))
        package_name = package_name or answers.get("package_name")
        if gitignore_mode == "ask":
            gitignore_mode = "always" if answers.get("update_gitignore", False) else "never"

    if type_checker is not None:
        try:
            template = _load_pyproject_template_from_url()
        except Exception as exc:
            parser.error(f"Could not load pyproject template from URL {PYPROJECT_TEMPLATE_URL}: {exc}")

        rendered_template = render_pyproject(template, args.target, source_location=source_location)
        sections = extract_tool_sections(rendered_template)
        checkers = available_type_checkers(sections)
        if not checkers:
            parser.error(f"No tool sections found in template URL payload: {PYPROJECT_TEMPLATE_URL}")

    if not package_name:
        parser.error("Package selection is required.")

    try:
        selected = select_stub_package(
            packages,
            package_name=package_name,
            version=args.version,
        )
    except ValueError as exc:
        parser.error(str(exc))

    project_root = Path(project_dir).resolve()
    target = project_root / args.target
    config_path = project_root / "pyproject.toml"

    qprint(f"* Selected package: {selected.package} ({selected.version})", style=STYLE_NORMAL)
    if type_checker is not None:
        selected_sections = sections_for_type_checker(sections, type_checker)
        if not selected_sections:
            parser.error(
                f"Type checker '{type_checker}' not found in template. Available options: {', '.join(checkers)}"
            )

        for section_header, section_text in selected_sections:
            update_pyproject(config_path, section_header=section_header, section_text=section_text, force=args.force)

        write_optional_dependencies(config_path, package=selected, target=args.target)
    ensure_gitignore_typings_with_mode(project_root, mode=gitignore_mode)

    install_stubs(selected, target=target)
    (project_root / source_location).mkdir(parents=True, exist_ok=True)

    if type_checker == "ty":
        ty_typeshed_dir = project_root / _ty_typeshed_dir_name(args.target)
        # Give AV/file indexers a moment to release newly installed stub files.
        time.sleep(1)
        build_ty_stdlib_typeshed(typings_dir=target, output_dir=ty_typeshed_dir, clean=True)

    qprint("Setup complete.", style=STYLE_BOLD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

