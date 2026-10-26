"""Build an experimental micropython-lib stub collection without changing stubber.

Run from the stubs repository:
    .venv/bin/python experiment/build_lib_stubs.py

Requires micropython-stubber, Ruff and uv, plus local MicroPython source checkouts.
The wrapper runs on Python 3.11+ (tomllib); the stubs target Python 3.9+.
Edit micropython_lib_stubs_manifest.py to expand the collection. Nothing is uploaded or registered
in the package database. Generated files are never written to the source trees.
Use --enrich-from PATH to select additional existing doc/reference stubs.
Recipes: just build-lib; just publish-lib-test (TestPyPI token in UV_PUBLISH_TOKEN).
"""

from __future__ import annotations

import argparse
import ast
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import tomllib
from importlib.metadata import version
from pathlib import Path

import tomli_w
from packaging.version import Version
from stubber.codemod.enrich import enrich_folder, source_target_candidates
from stubber.freeze.freeze_manifest_2 import make_path_vars
from stubber.tools.manifestfile import MODE_FREEZE, ManifestFile
from stubber.utils.stubmaker import generate_pyi_files

ROOT = Path(__file__).resolve().parents[1]
NAME = "micropython-lib-stubs"
INITIAL_VERSION = "0.0.1.dev0"
STDLIB_BASELINE = "1.29.0"
MARKER = ".lib-stubs-experiment"


def revision(path: Path) -> str:
    return subprocess.check_output(["git", "-C", str(path), "rev-parse", "HEAD"], text=True).strip()


def collect_sources(manifest: Path, mpy: Path, lib: Path, destination: Path) -> list[dict[str, str]]:
    resolver = ManifestFile(MODE_FREEZE, make_path_vars(mpy_path=mpy, mpy_lib_path=lib))
    cwd = Path.cwd()
    try:
        resolver.execute(str(manifest.resolve()))
    finally:
        # Manifest evaluation can change cwd, including when a nested require fails.
        os.chdir(cwd)
    if resolver.c_modules():
        raise ValueError(f"Native modules cannot be stubbed: {resolver.c_modules()}")
    files: dict[Path, Path] = {}
    for item in resolver.files():
        target = Path(item.target_path)
        source = Path(item.full_path).resolve()
        if target.is_absolute() or ".." in target.parts or target.suffix != ".py":
            raise ValueError(f"Unsupported manifest target: {target}")
        if target in files and files[target] != source:
            raise ValueError(f"Conflicting manifest target: {target}")
        files[target] = source
    if not files:
        raise ValueError("Manifest resolved no Python files")
    records = []
    for target, source in sorted(files.items()):
        output = destination / target
        output.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, output)
        records.append({"source": str(source), "target": target.as_posix()})
    return records


def generate_stubs(folder: Path) -> None:
    # stubgen otherwise treats usb/device as top-level device, losing the namespace.
    for source in list(folder.rglob("*.py")):
        for parent in source.relative_to(folder).parents:
            if parent != Path("."):
                (folder / parent / "__init__.py").touch(exist_ok=True)
    expected = {p.with_suffix(".pyi") for p in folder.rglob("*.py")}
    if not generate_pyi_files(folder):
        raise RuntimeError("stubber failed to generate stubs")
    missing = sorted(str(p.relative_to(folder)) for p in expected if not p.is_file())
    if missing:
        raise RuntimeError(f"Missing generated stubs: {', '.join(missing)}")


def enrich_stubs(folder: Path, sources: list[Path]) -> list[dict[str, object]]:
    coverage = []
    for source in sources:
        if not source.is_dir():
            raise FileNotFoundError(f"Enrichment source does not exist: {source}")
        matches = [m for m in source_target_candidates(source, folder, ".pyi") if m.is_match]
        count = 0
        if matches:
            count = enrich_folder(source, folder, write_back=True, ext=".pyi", copy_docstr=True)
        print(f"Enrichment {source}: {len(matches)} matches, {count} files enriched")
        matched = {match.target.resolve() for match in matches}
        unmatched = sorted(p.relative_to(folder).as_posix() for p in folder.rglob("*.pyi") if p.resolve() not in matched)
        coverage.append({"source": str(source), "matches": len(matches), "enriched": count, "unmatched": unmatched})
    return coverage


def add_origin_docstrings(folder: Path, lib: Path, records: list[dict[str, str]]) -> None:
    locations = {Path(record["target"]).with_suffix(".pyi"): Path(record["source"]).relative_to(lib).as_posix() for record in records}
    for stub in folder.rglob("*.pyi"):
        relative = stub.relative_to(folder)
        parts = relative.with_suffix("").parts
        module = ".".join(parts[:-1] if parts[-1] == "__init__" else parts)
        location = locations.get(relative)
        if location is not None:
            origin = f"Module: '{module}' from micropython-lib\n\nlocation: {location}"
        else:
            directories = sorted(
                {
                    Path(record["source"])
                    .parents[len(Path(record["target"]).relative_to(relative.parent).parts) - 1]
                    .relative_to(lib)
                    .as_posix()
                    + "/"
                    for record in records
                    if Path(record["target"]).is_relative_to(relative.parent)
                }
            )
            origin = f"Module: '{module}' from micropython-lib\n\n"
            origin += "\n".join(f"location: {directory}" for directory in directories)
        content = stub.read_bytes()
        tree = ast.parse(content)
        existing = ast.get_docstring(tree, clean=False)
        if existing is not None:
            node = tree.body[0]
            assert node.end_lineno is not None and node.end_col_offset is not None
            lines = content.splitlines(keepends=True)
            start = sum(map(len, lines[: node.lineno - 1])) + node.col_offset
            end = sum(map(len, lines[: node.end_lineno - 1])) + node.end_col_offset
            origin += "\n\n" + existing
            content = content[:start] + content[end:]
        docstring = '"""\n' + origin.replace("\\", "\\\\").replace('"""', '\\"""') + '\n"""\n'
        stub.write_bytes(docstring.encode("utf-8") + content.lstrip(b"\r\n"))


def assemble_package(
    sources: Path,
    package: Path,
    root: Path,
    lib: Path,
    provenance: dict[str, object],
    records: list[dict[str, str]],
    package_version: str,
    existing_metadata: Path | None = None,
) -> None:
    package.mkdir()
    for stub in sources.rglob("*.pyi"):
        target = package / stub.relative_to(sources)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(stub, target)
    metadata_path = (
        existing_metadata
        if existing_metadata is not None and existing_metadata.is_file()
        else root / "publish/template/pyproject_hatch.toml"
    )
    with metadata_path.open("rb") as stream:
        metadata = tomllib.load(stream)
    project = metadata["project"]
    project.update(name=NAME, version=package_version)
    if metadata_path == root / "publish/template/pyproject_hatch.toml":
        project["description"] = "Experimental manifest-selected micropython-lib stubs"
        project["requires-python"] = ">=3.9"
        project["classifiers"] = [
            "Development Status :: 3 - Alpha" if c.startswith("Development Status ::") else c for c in project["classifiers"]
        ]
        project["dependencies"] = [f"micropython-stdlib-stubs>={STDLIB_BASELINE}"]
    targets = metadata["tool"]["hatch"]["build"]["targets"]
    targets.pop("sdist", None)
    targets["wheel"]["include"] = list(
        dict.fromkeys(targets["wheel"]["include"] + ["provenance.json", "UPSTREAM_LICENSE.md", "UPSTREAM_NOTICES.md"])
    )
    (package / "pyproject.toml").write_text(tomli_w.dumps(metadata), encoding="utf-8")
    (package / "LICENSE.md").write_text(
        (root / "LICENSE.md").read_text(encoding="utf-8").rstrip() + "\n\n## Upstream licensing\n\n"
        "Stubs derived from micropython-lib are also subject to the applicable\n"
        "upstream terms in UPSTREAM_LICENSE.md.\n"
        "Source license and author notices are retained in\n"
        "UPSTREAM_NOTICES.md.\n",
        encoding="utf-8",
    )
    shutil.copyfile(lib / "LICENSE", package / "UPSTREAM_LICENSE.md")
    notices = []
    for source in records:
        path = Path(source["source"])
        comments = [
            line.strip()
            for line in path.read_text(encoding="utf-8").splitlines()
            if line.lstrip().startswith("#")
            and re.search(r"\b(licen[cs]e|copyright|authors?|contributors?|SPDX|written by)\b", line, re.IGNORECASE)
        ]
        if comments:
            notices.append(f"--- {path.relative_to(lib)} ---\n" + "\n".join(comments))
    (package / "UPSTREAM_NOTICES.md").write_text("\n\n".join(notices) + "\n", encoding="utf-8")
    (package / "provenance.json").write_text(json.dumps(provenance, indent=2) + "\n", encoding="utf-8")
    imports = sorted(
        {".".join(p.parts[:-1] if p.stem == "__init__" else p.with_suffix("").parts) for p in (Path(r["target"]) for r in records)}
    )
    (package / "README.md").write_text(
        f"""# {NAME}

Experimental version {package_version}, generated with existing micropython-stubber helpers.
This is a library supplement, not a replacement for board and stdlib stubs.
Only a universal wheel is built; no source distribution is needed for normal installation.
Dependencies: {", ".join(project["dependencies"])}.
Dependencies are independent of the experimental distribution version and source revisions.
Edits to the output pyproject.toml are preserved on rebuild.

## Use

Build with `just build-lib`, then upload the existing wheel with `just publish-lib-test`.
Set `UV_PUBLISH_TOKEN` to a TestPyPI token in your shell before publishing.
Credential setup is external to this experiment; the recipe delegates authentication to uv.
The publish recipe always targets `https://test.pypi.org/legacy/`, not production PyPI.
TestPyPI does not allow reusing an uploaded version/filename. Bump the version in
this package's pyproject.toml, or run the build script with `--version 0.0.1.dev1`.
Rebuilds preserve the existing package version unless `--version` overrides it.

Install the wheel with `uv pip install --target ./typings dist/*.whl`.
Configure your type checker to use `typings` as its stub path. Install compatible
board stubs in the same target first, then this collection. Overlapping modules
(notably logging and possibly board-frozen libraries) are replaced by this collection.
No Python runtime implementations are included.

Source-backed imports in this build: {", ".join(f"`{name}`" for name in imports)}.
The manifest resolver includes dependencies; edit the manifest to expand the set.
The exact manifest, file inventory, commits, stubber version and enrichment coverage
are recorded in provenance.json. Source commits are not a firmware compatibility claim.
Before enrichment, each stub receives a module docstring identifying its source repository
and relative source location; enrichment may replace it with reference documentation.
For synthetic namespace initializers, locations refer to the contributing source folders.

## Limitations

Source-derived signatures may contain Any or incomplete types. Enrichment is applied
only where matching existing reference/doc stubs exist; zero matches is valid and
reported. Hardware APIs still require appropriate board stubs. No hardware execution
or completeness certification is implied. Building does not upload the package.

[UPSTREAM_NOTICES.md](./UPSTREAM_NOTICES.md) retains only source license and author comments.
[UPSTREAM_LICENSE.md](./UPSTREAM_LICENSE.md) contains micropython-lib's license texts.
""",
        encoding="utf-8",
    )


def replace_output(package: Path, output: Path) -> None:
    if output.exists():
        marker = output / MARKER
        if not marker.is_file() or marker.read_text(encoding="utf-8").strip() != NAME:
            raise ValueError(f"Refusing to replace unowned output: {output}")
        backup = output.with_name(output.name + ".previous")
        if backup.exists():
            raise FileExistsError(f"Previous output backup already exists: {backup}")
        output.rename(backup)
        try:
            package.rename(output)
        except OSError:
            backup.rename(output)
            raise
        shutil.rmtree(backup)
    else:
        package.rename(output)


def build(
    root: Path,
    manifest: Path,
    mpy: Path,
    lib: Path,
    output: Path,
    enrichment: list[Path],
    package_version: str | None = None,
) -> Path:
    print(f"micropython-stubber {version('micropython-stubber')}")
    print(f"Manifest: {manifest}\nMicroPython: {mpy}\nmicropython-lib: {lib}\nOutput: {output}")
    resolved = output.resolve()
    protected = [root.resolve(), mpy.resolve(), lib.resolve(), (root / "stubs").resolve()]
    if (
        output.is_symlink()
        or any(path.is_relative_to(resolved) for path in protected)
        or any(resolved.is_relative_to(path) for path in protected[1:])
    ):
        raise ValueError(f"Unsafe output directory: {output}")
    if output.exists() and not (output / MARKER).is_file():
        raise ValueError(f"Refusing to replace unowned output: {output}")
    package_version = resolve_package_version(output, package_version)
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".lib-stubs-", dir=output.parent) as temp:
        work = Path(temp)
        staged = work / "sources"
        records = collect_sources(manifest, mpy, lib, staged)
        generate_stubs(staged)
        add_origin_docstrings(staged, lib, records)
        coverage = enrich_stubs(staged, enrichment)
        subprocess.run([sys.executable, "-m", "ruff", "check", "--select", "I", "--fix", str(staged)], check=True)
        subprocess.run([sys.executable, "-m", "ruff", "format", "--line-length", "140", str(staged)], check=True)
        provenance: dict[str, object] = {
            "manifest": manifest.read_text(encoding="utf-8"),
            "micropython": revision(mpy),
            "micropython-lib": revision(lib),
            "stubber": version("micropython-stubber"),
            "files": records,
            "enrichment": coverage,
        }
        package = work / "package"
        assemble_package(staged, package, root, lib, provenance, records, package_version, output / "pyproject.toml")
        subprocess.run(["uv", "build", "--wheel", "--no-sources"], cwd=package, check=True)
        if not list((package / "dist").glob("*.whl")):
            raise RuntimeError("Build did not produce a wheel")
        (package / MARKER).write_text(NAME + "\n", encoding="utf-8")
        replace_output(package, output)
    print(f"Built {len(records)} source files into {output / 'dist'}")
    return output


def resolve_package_version(output: Path, override: str | None = None) -> str:
    if override is not None:
        return str(Version(override))
    metadata = output / "pyproject.toml"
    if metadata.exists():
        with metadata.open("rb") as stream:
            return str(Version(tomllib.load(stream)["project"]["version"]))
    return INITIAL_VERSION


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=Path(__file__).with_name("micropython_lib_stubs_manifest.py"))
    parser.add_argument("--mpy", type=Path, default=ROOT / "repos/micropython")
    parser.add_argument("--lib", type=Path, default=ROOT / "repos/micropython-lib")
    parser.add_argument("--output", type=Path, default=ROOT / "publish" / NAME)
    parser.add_argument("--version", help="Override the existing output package version (preserved by default)")
    parser.add_argument("--enrich-from", type=Path, action="append", help="Existing matching doc/reference stubs; repeatable")
    args = parser.parse_args()
    build(
        ROOT,
        args.manifest.resolve(),
        args.mpy.resolve(),
        args.lib.resolve(),
        args.output.absolute(),
        [p.resolve() for p in args.enrich_from] if args.enrich_from else [ROOT / "reference/micropython"],
        args.version,
    )


if __name__ == "__main__":
    main()
