applyTo: "tools/board_compare/**"
description: Guidance for working on the board comparison scanner, database builder, and frontend data contract.
---

## Purpose
Compare MicroPython APIs (modules/classes/methods/params/constants) across boards & versions using:
- scan_stubs.py (libcst-based extractor)
- build_database.py (normalized SQLite builder)
- frontend/ (SQL.js-powered explorers & diff views)

## Agent tooling
MCP Server Usage (Agents)
- For DB queries: use Data Access MCP server rather than custom ad-hoc scripts; ensures consistent environment (no local sqlite binary reliance).
- For UI automation: use PlayWright MCP server; do not embed manual sleeps—use explicit waits for selectors / network idle.

### Playwright Guidelines
- the pages can be server as http://localhost:8080 for testing via python. There is a VSCode task defined for this.
  The server is a VSCode task - you can stop / start / restart is via the VSCode tasks
    "label": "http.server: board explorer",
    "detail": "Start the python board_explorer server on port 8080",
   the frontend folder will be served as the root.
- Run headless by default; allow headed mode via env flag.

## Core Data Flow
stubs (.pyi) -> scan_stubs.py -> Pydantic models (models.py) -> build_database.py -> normalized SQLite (frontend/board_comparison.db) -> browser (SQL.js queries + UI state in URL).

## Key Conventions
- Parsing: libcst (not ast) to preserve structure & decorators; keep extraction logic idempotent.
- Hidden typing artifacts: _is_typing_related filters (keep logic consistent in both scanner & builder; update both if changed).
- Version normalization: input may be v1.26.0 / 1.26.0 / v1_26_0; display form stored as v1.26.0; directory form uses underscores (v1_26_0).
- Signature hashing: Methods must include context (module_id + class_id) + structural flags + ordered param signature. DO NOT revert to global method hashing or collisions reappear. If adding new structural properties (e.g., kw-only markers, decorators that change semantics), incorporate them BEFORE schema-dependent usage.
- Decorators: All decorator names captured (decorators list) plus boolean flags (classmethod/staticmethod/property) for backward compatibility.
- Positional-only params: Already supported (params.posonly_params). Maintain when refactoring.
- Optional parameters = any with default; variadics (*args/**kwargs) flagged is_variadic.
- Orphan cleanup required after deletions (see _cleanup_orphaned_records). Always call when pruning.

## Schema (stable contract)
Tables (CREATE order): boards, unique_modules, board_module_support, unique_classes, board_class_support, unique_class_bases, unique_class_attributes, board_class_attribute_support, unique_methods, board_method_support, unique_parameters, unique_module_constants, board_module_constant_support.
Do not rename columns casually—frontend expects:
- boards(version, port, board, package_name, package_version)
- unique_methods(decorators JSON text, overloads int)
- unique_class_attributes / unique_module_constants(is_hidden int)

## Adding New Metadata
1. models.py: add field(s) (ensure Optional / defaults). 
2. scan_stubs.py: populate in extractor.
3. build_database.py: extend schema creation + insertion helpers + hashing if it alters uniqueness.
4. Write migration logic: attempt ALTER TABLE with try/except OperationalError.
5. Update frontend queries (board-explorer.js) only after DB is reproducible.
6. Add test covering extraction + DB presence.

## Common Tasks
- Build DB for one version: python build_database.py --version v1.26.0 --db frontend/board_comparison.db
- Add stdlib: python build_database.py --version v1.26.0 --stdlib-dir ../../publish/micropython-stdlib-stubs --db frontend/board_comparison.db
- List versions: python build_database.py --list-versions --db frontend/board_comparison.db
- Clean just one version: python build_database.py --version v1.26.0 --clean-only
- Full reset (destructive): python build_database.py --reset-db
(Automations: prefer integrating into higher-level workflows instead of ad-hoc scripting.)

## Do / Avoid
DO:
- Keep hashing deterministic & short (current SHA256[:16] OK).
- Represent new many-to-many relationships with bridge tables (board_*_support style).
- Use MCP Data Store / JSON exports for queries instead of ad-hoc sqlite binaries (not installed).
- Preserve commented-out large JSON exporters unless reintroducing a streaming / paginated frontend.

AVOID:
- Re-enabling detailed JSON (168MB) in CI—frontend should rely on SQLite.
- Introducing cascading deletes; rely on explicit cleanup to avoid silent data loss.
- Broad schema rewrites breaking published pages without version gating.

## Testing Focus
Add or update tests when:
- Signature hash logic changes (collision regression test).
- New decorator or parameter category added.
- Filtering rules for typing artifacts change (ensure visibility toggles unaffected).
- Version normalization edge cases (v1_2_3 vs 1.2.3 vs v1.2.3) remain stable.

## Performance Notes
- DB size target: ~5–6 MB for typical multi-version sets; watch growth when adding textual fields.
- Indexes already cover signature_hash, module/class/method lookup; add new indexes only if query latency demonstrated.

## Frontend Contract Highlights
- Methods: decorators stored as JSON string (parse client-side).
- Hidden fields: is_hidden (0/1) indicates suppress-by-default (typing noise).
- Overloads aggregated numeric count; if true overload resolution needed in future, store distinct signatures instead of bumping counter.

## Extensibility Guidelines
If adding inheritance expansion or resolution chains:
- Either create derived view or new table (eager resolution) – avoid N+1 traversal client-side for many boards.
If adding semantic diffing (signature compare):
- Precompute normalized signature text & store hash for O(1) equality checks.

## Debugging Tips
- Duplicate method unexpectedly? Check context parameters to _get_method_signature_hash_with_context.
- Missing positional-only params? Confirm params.posonly_params iteration not removed.
- Decorators empty? Verify _get_decorator_name path covers Attribute and Name nodes.

## Safety Checklist Before Commit
- Can rebuild DB from scratch with no errors.
- New columns guarded by ALTER TABLE try/except.
- Frontend still loads (open board-explorer.html locally with fresh DB).
- No unintended increase in DB size >20% without justification.

## When Unsure
Prefer adding a focused test & small schema extension over mutating existing semantics. Document any intentional hash or filtering changes in ARCHITECTURE.md.
