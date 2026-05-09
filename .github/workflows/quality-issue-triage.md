---
on:
  issues:
    types: [opened, labeled]
  workflow_dispatch:
    inputs:
      issue_number:
        description: 'Issue number to triage when run manually'
        required: false
        default: ''

permissions:
  contents: read
  issues: read
  pull-requests: read

tools:
  github:
    toolsets: [default]

network: defaults

safe-outputs:
  add-comment:
    max: 3
  add-labels:
    max: 5
  create-issue:
    max: 10
  link-sub-issue:
    max: 10

---

# quality-issue-triage

Triage quality issues for MicroPython type stubs in this repository.

## Instructions

First resolve the target issue number:

1. If `${{ github.event.issue.number }}` is present, use that value.
2. Otherwise, read `${{ github.event.inputs.issue_number }}` and treat it as the target issue number.
3. If neither value is present, empty, or not a positive integer, call `missing_data` with a short message explaining that `workflow_dispatch` requires `issue_number`, then stop.

After resolving the target issue number, fetch that issue via GitHub tools and use it as the single source of truth for title, body, labels, and URL in all steps below.

When triggered by `issues`:

1. Only continue if the issue currently has a label named `Quality` (case-insensitive).
   - If it does not, stop with no action.

2. Inspect the issue title and body and decide whether it is specifically about one or more problems in type stubs maintained in this repository.
   - In scope examples: wrong or missing types in `.pyi` stubs, incorrect signatures, bad module/class/function definitions, typing regressions in published stubs.
   - Out of scope examples: runtime firmware bugs, hardware troubleshooting, general feature requests unrelated to stubs, documentation-only requests not tied to stub defects.

3. If out of scope:
   - Add label `More info required`.
   - Add a brief comment explaining that this tracker is for stub quality issues and asking the reporter to clarify the exact stub module(s), symbols, and expected typing behavior.
   - Stop processing.

4. If in scope, check information completeness:
   - The report must include either:
     - a minimal reproduction snippet directly in the issue, or
     - a stubs playground link starting with `https://josverl.github.io/stubs_playground` and containing embedded repro code in URL parameters or fragment.
       - Accept as embedded repro when parameter/fragment keys such as `code`, `snippet`, or `source` contain code text.
   - If neither is present:
     - add label `More info required`,
     - add a comment requesting a minimal repro snippet or a stubs playground link with embedded repro code,
     - stop processing.

5. Determine the affected target scope and add one scope label:
   - Infer the MicroPython port from issue content when possible.
   - Validate candidate ports in this priority order:
     1) official MicroPython port names by listing `micropython/micropython` directories under `ports/` via GitHub MCP tools,
     2) package/board naming in this repository from `data/stub-packages.json`.
   - If cross-repo validation is unavailable, use `data/stub-packages.json` as the authoritative fallback.
   - If the issue clearly targets stdlib stubs rather than a port package, use `scope:stdlib`.
   - For ports, use label format `scope:port:<port>`, e.g. `scope:port:rp2`.
   - If the chosen scope label does not exist yet, create it and then apply it.
     - Use color `#0E8A16` (green) for consistency with other triage labels.
     - Use description `Stub quality scope label for triage routing: <scope>.`
   - If scope cannot be determined confidently, add label `More info required`, request clarification, and stop.

6. Determine whether the issue describes multiple distinct problems or mixes defects with feature requests:
   - Group findings into unique problem types.
   - If there is only one problem type, add a short acknowledgement comment and stop.
   - If there are multiple unique problem types, create one sub-issue per unique problem type.

7. For each sub-issue:
   - Use a concise title prefixed with `Quality:` and describe exactly one distinct problem.
   - Include a clear description with:
     - affected stub package/version (if known),
     - affected module(s)/symbol(s),
     - current behavior,
     - expected behavior,
     - link back to the parent issue.

8. Link each created sub-issue to the parent issue and add a summary comment on the parent issue listing the created sub-issues.

When triggered manually (`workflow_dispatch`):

- Use `${{ github.event.inputs.issue_number }}` as described above.
- Apply the exact same triage behavior as the `issues` trigger path (including label checks, scope routing, and optional sub-issue creation) to the fetched issue.

## Notes

- Keep actions focused, deterministic, and minimal.
- Do not modify code, pull requests, or unrelated issues.
