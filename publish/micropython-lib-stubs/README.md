# micropython-lib-stubs

Experimental version 0.0.1.dev1, generated with existing micropython-stubber helpers.
This is a library supplement, not a replacement for board and stdlib stubs.
Only a universal wheel is built; no source distribution is needed for normal installation.
Dependencies: micropython-stdlib-stubs>=1.29.0.
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

Source-backed imports in this build: `aiorepl`, `logging`, `usb.device`, `usb.device.cdc`, `usb.device.core`.
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
