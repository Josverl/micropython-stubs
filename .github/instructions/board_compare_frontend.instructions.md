---
applyTo: "tools/board_compare/frontend/**"
description: Frontend development guidance for the board comparison explorer (HTML5 + PyScript MicroPython runtime, UI + testing practices).
---

## Scope
Applies to all assets in `tools/board_compare/frontend/` (HTML, JS, CSS, PyScript inline/linked code) that render explorers, comparisons, and searches over `board_comparison.db`.

## Runtime & Tech Choices
- HTML5 only (no legacy XHTML quirks; semantic tags encouraged: <header>, <nav>, <main>, <section>, <details>, <footer>). 
- PyScript 2025.10.1 with MicroPython interpreter.
- Use MicroPython event attributes and elements: prefer `mpy-*` attributes; NEVER introduce `py-*` attributes.
  - DO: `<button id="refresh" mpy-click="refresh_boards">Refresh</button>`
  - DO NOT: `<button id="refresh" py-click="refresh_boards">Refresh</button>`
- Keep interpreter selection explicit in configuration (`<py-config>` / config type expected to be `mpy`).
- Avoid features that assume Pyodide (e.g. heavy numpy); keep payload light and compatible with MicroPython.

## PyScript / MicroPython Usage
- Place core logic in dedicated `<script type="mpy">` blocks or external `.py` loaded via `<py-config files>`.
- Use `from pyscript import document, config` for DOM + config introspection; rely on `config['type'] == 'mpy'` for asserts.
- Use `js` (MicroPython proxy to `globalThis`) for low-level browser API access sparingly—wrap in helper functions for testability.
- Event binding: prefer markup-driven `mpy-click`, `mpy-change`, etc. Keep functions pure where possible (return data; separate DOM update side-effects).
- Avoid mutation of `pyscript.config` (read-only semantics per docs).

## PyScript FFI Essentials (`pyscript.ffi`)
Use the unified FFI layer for structured, reliable JS ↔ MicroPython interop. Prefer `pyscript.ffi` over interpreter-specific namespaces unless you need a feature only exposed in `micropython.ffi`.

Key utilities:
- `from pyscript.ffi import to_js` — Convert Python `dict` → JavaScript plain object (NOT Map). Use before passing config/options to JS libraries.
- `from pyscript.ffi import create_proxy` — Wrap a Python/MicroPython callable so JS can invoke it repeatedly without losing the reference. Clean up long‑lived proxies you no longer need.
- `from pyscript.ffi import is_none` — Distinguish `None` / `JsNull` when inspecting interop return values.

Guidelines:
DO:
- Convert only the minimal shape required (`to_js({"board": board_id, "filter": term})`).
- Keep proxies short-lived; if attaching handlers (e.g. resize listeners) store, then later detach & delete.
- Encapsulate FFI boundary in a helper (e.g. `interop_fetchBoards()` returning normalized Python objects) to simplify testing.
- Normalize JS exceptions to Python (`try/except`) at the boundary; surface readable error messages for UI.

AVOID:
- Passing large result sets (> a few thousand rows) through FFI one row at a time—run SQL.js queries wholly in JS, then send only aggregated metrics back if needed.
- Holding stale proxies (memory leak risk). Remove via JS event deregistration + del reference.
- Mutating complex nested objects returned from JS directly—copy/reshape into Python dict first.
- Relying on Pyodide‑specific FFI calls (`pyodide.ffi.to_js`) in this folder.

Patterns:
1. Bulk queries: Run SQL.js in JS, reduce -> small dict, then `to_js` only if returning to another JS consumer; otherwise keep in Python.
2. JS callbacks into MicroPython: `handler = create_proxy(on_compare_done)` then attach; later detach: `js.window.removeEventListener('compareDone', handler); handler.destroy()`.
3. Config passing: Build Python dict; always `to_js` before invoking JS library expecting plain object.

Testing FFI:
- Logic: unit test Python wrappers (simulate JS return via stub object).
- UI (Playwright): ensure mpy-click handlers trigger JS integration path; verify no console errors about missing proxies.
- Include one test that intentionally passes a dict with nested values to confirm `to_js` produces expected JS object structure.

Troubleshooting:
- Getting a JS Map instead of object: confirm you imported `pyscript.ffi.to_js` (not interpreter-specific variant).
- Memory growth: audit for unused `create_proxy` handlers.
- `None` comparison issues: use `is_none(value)` instead of `value is None` when receiving cross-boundary values.

When Unsure: Start with pure Python data prep, add minimal FFI conversions, then iterate with profiling (browser performance panel) if interactions appear slow.

## Data Access
- Primary data source: `board_comparison.db` (SQLite) loaded client-side via SQL.js (WASM). Do NOT load the deprecated large detailed JSON (168MB).
- Keep DB fetch isolated in a single initialization module (e.g. `db.js` or `db.mpy`) that:
  1. Fetches the binary with proper cache headers (Cache-Control: no-cache if dev).
  2. Exposes query helpers: `getModules(boardId)`, `compareBoards(a,b)`, `searchApis(term)`.
- All queries should be parameterized or composed safely—no dynamic SQL injection via user input.

## Performance & UX
- Lazy load heavy sections (e.g. method diffs) only when expanded.
- Pre-compute frequent counts (module_count, method_count) server-side (already in schema) rather than iterating large result sets client-side.
- Use progressive enhancement: basic static module list renders immediately; interactive filters hydrate after DB ready event.
- Provide a global loading state; hide it only after initial essential queries resolve.
- Avoid blocking long loops on the main thread—chunk processing with `requestAnimationFrame` if dataset grows.

## Accessibility & Semantics
- Use button elements for actions (NOT bare divs).
- Associate diff color coding with text + ARIA labels (e.g. green unique => `aria-label="Unique to Board A"`).
- Provide keyboard navigation (tab order) for board selection and search.

## Styling & Structure
- Prefer small CSS modules (scoped via BEM or utility classes). Avoid inline styles beyond dynamic width adjustments.
- Theme tokens (colors for diff states) defined once (e.g. `--color-unique-a`, `--color-unique-b`, `--color-common`).
- Keep CSS footprint minimal: aim for <10KB uncompressed; consolidate repetitive rules; use logical properties (`margin-block`, `padding-inline`) where possible.
- Accessibility first: maintain WCAG AA contrast (≥4.5:1 normal text, ≥3:1 large text). Test diff colors over light/dark backgrounds; provide non-color indicators (icons/labels/ARIA).
- Font stack: use a readable system stack (e.g. `font-family: system-ui, Segoe UI, Roboto, sans-serif;`); avoid custom webfonts unless essential.
- Prefer MicroPython (`<script type="mpy">`) over adding new standalone `.js` files. Only exception: the existing db-optimizer script (do not add further JS unless performance profiling proves necessity).
- Use native HTML `<template>` elements for repeated UI fragments (module rows, method entries). Clone via `document.getElementById('tmpl-module').content.cloneNode(true)` rather than constructing large HTML strings in Python.
- Keep Python code focused on data/state; let HTML + CSS handle structure/presentation. Minimize inline style mutation—toggle classes instead.

## Event & State Model
- URL state encoding (board A, board B, active tab, search term) must remain stable; parse on load, update via `history.replaceState` NOT full reload.
- Do not introduce hash fragments for internal routing unless enhancing deep links—use query string keys (`?view=compare&boardA=...`).

## Testing Strategy
1. you should be realistic during testing. do not bee optimistic. 
   expect to see explicit proof of success, the absense of error does not means success.
   - use logging / console output to confirm steps completed.
   - consider edge cases and potential failure points.
   - be prepared to debug via browser dev tools (console, network, performance).
   - most pages require both a version and a board to be entered
       - Use version 1.26.0 or 1.25.0, boards esp32 or stm32
       - search terms : pi, SEC_, asm_, I2S
    
1. Logic tests (pytest):
   - Extract core comparison logic and search normalization into pure Python modules runnable under standard CPython pytest (avoid browser dependencies).
   - Mirror minimal dataset fixtures (small in-memory SQLite or dict mocks).
2. UI tests (Playwright via MCP PlayWright server):
   - Scenarios: load explorer, perform board comparison (hide common modules), search term highlighting, deep-link restoration.
   - Assertions: element presence, diff color classes, URL state sync, keyboard accessibility.
3. Data contract tests:
   - Verify required columns (decorators, overloads, is_hidden) accessible via SQL.js queries.
   - Fail fast if schema changes (instruction: add migration note in ARCHITECTURE.md).

## Playwright Guidelines
- the pages can be server as http://localhost:8080 for testing via python. There is a VSCode task defined for this.
  The server is a VSCode task - you can stop / start / restart is via the VSCode tasks
    "label": "http.server: board explorer",
    "detail": "Start the python board_explorer server on port 8080",
   the frontend folder will be served as the root.
- Run headless by default; allow headed mode via env flag.

- Prefer role-based selectors (`getByRole('button', { name: /Refresh/i })`) or stable IDs; avoid brittle text-only selectors.
- Include at least one test ensuring `mpy-click` handlers executed (e.g. button increments counter / refreshes list).

## Pytest Layout
- Place pure logic tests in `tests/frontend_logic/`.
- Place Playwright specs in `tests/ui/` (naming `test_ui_*.py` or `.ts` if using Playwright's native runner variant—keep consistent; prefer Python if unified).
- Mark UI tests with `@pytest.mark.ui` to allow selective runs.

## MCP Server Usage (Agents)
- For DB queries: use Data Access MCP server rather than custom ad-hoc scripts; ensures consistent environment (no local sqlite binary reliance).
- For UI automation: use PlayWright MCP server; do not embed manual sleeps—use explicit waits for selectors / network idle.

## Deployment (GitHub Pages)
- Build artifact: static HTML, JS, CSS, DB file (`board_comparison.db`).
- GH Action publishes `frontend/` to Pages; ensure relative URLs ("./board_comparison.db") not absolute.
- Avoid cache pitfalls: append version query (`board_comparison.db?v=<short-hash>`) when DB schema changes.

## Do / Avoid
DO:
- Keep MicroPython handlers small; offload heavy iteration to JS/SQL when faster.
- Log non-sensitive diagnostics (`console.log`) behind development flag.
- Centralize UI color logic (avoid magic hex codes sprinkled through code).
- Document any new `mpy-*` attribute usage here.
- Use `<template>` for repeated DOM blocks.
- Run contrast checks (browser dev tools / automated audit) before approving new color tokens.
- Favor MicroPython scripts for new logic instead of adding JavaScript files.

AVOID:
- Using `py-*` attributes (Pyodide) in this folder.
- Embedding large base64 DB payloads in HTML (use external fetch).
- Mixing unrelated responsibilities (DB query + DOM mutation in same function without abstraction).
- Relying solely on color to convey diff meaning (add text/ARIA).
- Adding new `.js` logic files without justification (performance measurement & review required).
- Generating bulky HTML via Python string concatenation (prefer `<template>` cloning).
- Introducing large CSS frameworks or utility libraries (Tailwind, Bootstrap) – maintain lean custom CSS.

## Extension Patterns
- To add method-level diff view: create a derived query producing normalized signature strings + classification; render lazily in expandable panel.
- For offline support: 
   - the dabase is already avaialble offline via IndexDB via the db-optmiser script.
   - consider small service worker caching only DB + essential assets; skip heavy pre-caching of all boards.

## Validation Before Commit
- All `mpy-click` handlers resolve to defined functions (no console errors on load).
- Page loads with only one network fetch for DB (besides CDN libs).
- Playwright UI suite passes (core flows).
- Pytest logic suite passes; no hard-coded paths breaking Windows/Unix portability.

## Troubleshooting
- Event not firing: confirm attribute uses `mpy-click`, not `py-click`.
- DB query slow: ensure relevant indexes exist (schema already has method/module/class hash indexes).
- State not restored: check URL parse runs before initial render (defer DB-dependent UI until after state hydration).

## When Unsure
Start with a pure function version of the feature (data in, diff out) tested via pytest; integrate into UI with minimal DOM wiring; document new attributes or data flows in this file.
