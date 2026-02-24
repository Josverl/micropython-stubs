# Multi-Version Snippet Score Tracking

## Overview

The snippet quality testing framework now supports tracking scores across multiple MicroPython versions with historical trend data.

## SNIPPET_SCORE Structure

The `SNIPPET_SCORE` GitHub repository variable now uses a structured format:

```json
{
  "stable": {
    "v1.27.0": {
      "pass_rate": 0.95,
      "executed": 100,
      "passed": 95,
      "failed": 5,
      "timestamp": "2026-02-24T12:34:56Z",
      "commit": "abc123",
      "snippet_score": 90
    }
  },
  "preview": {
    "pass_rate": 0.92,
    "executed": 100,
    "passed": 92,
    "failed": 8,
    "timestamp": "2026-02-24T12:34:56Z",
    "version": "v1.28.0-preview",
    "commit": "abc123",
    "snippet_score": 84
  },
  "recent_majors": {
    "pass_rate": 0.93,
    "executed": 300,
    "passed": 279,
    "failed": 21,
    "timestamp": "2026-02-24T12:34:56Z",
    "versions": ["v1.27.0", "v1.26.1", "v1.25.0"],
    "commit": "abc123",
    "snippet_score": 258
  },
  "history": {
    "v1.27.0": [
      {
        "pass_rate": 0.95,
        "executed": 100,
        "passed": 95,
        "failed": 5,
        "timestamp": "2026-02-24T12:34:56Z",
        "commit": "abc123"
      },
      // ... up to 10 most recent records
    ],
    "preview": [
      // ... historical preview results
    ],
    "recent_majors": [
      // ... historical recent_majors results
    ]
  }
}
```

## Version Types

### 1. Stable (`--stable-only`)
- **Purpose**: Gate for PR merges
- **Versions Tested**: Current stable release only (e.g., v1.27.0)
- **Behavior**: **FAILS workflow** on quality drop
- **Storage**: Stored under `stable[version_number]`
- **Usage**: Quality gate that must pass

### 2. Preview (`--preview-only`)
- **Purpose**: Early warning for preview releases
- **Versions Tested**: Most recent preview (e.g., v1.28.0-preview)
- **Behavior**: Non-blocking, logs warnings
- **Storage**: Stored under `preview` (latest only)
- **Usage**: Monitor upcoming release quality

### 3. Recent Majors (`--recent-majors`)
- **Purpose**: Broader compatibility testing
- **Versions Tested**: Last 3 stable major.minor releases (e.g., v1.27.0, v1.26.1, v1.25.0)
- **Behavior**: Non-blocking, logs warnings
- **Storage**: Stored under `recent_majors` (aggregated)
- **Usage**: Detect regressions across supported versions

## Historical Tracking

Each version type maintains up to 10 historical records under the `history` key:
- Stable: Per-version history (e.g., `history["v1.27.0"]`)
- Preview: Aggregated preview history (`history["preview"]`)
- Recent Majors: Aggregated history (`history["recent_majors"]`)

Each history entry includes:
- `pass_rate`: Percentage of tests passed
- `executed`: Number of tests run
- `passed`: Number of passed tests
- `failed`: Number of failed tests
- `timestamp`: ISO 8601 timestamp
- `commit`: Short commit SHA (7 chars)

## Workflow Integration

### Environment Variables

The workflow sets these environment variables for each job:

**Stable Job:**
```yaml
VERSION_TYPE: stable
TEST_VERSION: v1.27.0  # Dynamically determined
```

**Preview Job:**
```yaml
VERSION_TYPE: preview
TEST_VERSION: v1.28.0-preview  # Dynamically determined
```

**Recent Majors Job:**
```yaml
VERSION_TYPE: recent_majors
# TEST_VERSION not set (tests multiple versions)
```

### Comparison Logic

The `compare_score_v2.py` script:

1. Loads baseline from `$SNIPPET_SCORE` environment variable
2. Loads new results from `results/snippet_score.json`
3. Compares based on version type:
   - **Stable**: Compares against `stable[version]` baseline
   - **Preview**: Compares against `preview` baseline
   - **Recent Majors**: Compares against `recent_majors` baseline
4. Updates baseline and history if:
   - Pass rate improves or stays within tolerance
   - No mass-skip detected (>50% of baseline executed)
   - Running on `main` branch
5. Returns exit code:
   - `0`: Success or acceptable drop
   - `1`: Unacceptable quality drop (only for stable with `fail_on_drop=True`)

### Thresholds

```python
PASS_RATE_TOLERANCE = 0.05      # 5% drop allowed
MIN_EXECUTED_FRACTION = 0.50     # 50% of baseline required
MAX_HISTORY_RECORDS = 10         # Keep last 10 records
```

## Usage Examples

### Running Tests Locally

```bash
# Test stable version only
pytest -m 'snippets' --stable-only

# Test preview version only
pytest -m 'snippets' --preview-only

# Test recent major.minor releases (no preview)
pytest -m 'snippets' --recent-majors

# Test all (default - last 3 major.minor including preview if present)
pytest -m 'snippets'
```

### Manual Score Comparison

```bash
# Set environment variables
export VERSION_TYPE=stable
export TEST_VERSION=v1.27.0
export SNIPPET_SCORE='{"stable": {"v1.27.0": {"pass_rate": 0.95, ...}}, ...}'

# Run comparison
python .github/workflows/compare_score_v2.py
```

## Migration from Old Format

The script automatically migrates old `SNIPPET_SCORE` formats:

**Old Format:**
```json
{
  "snippet_score": 90,
  "pass_rate": 0.95,
  "executed": 100,
  "passed": 95,
  "failed": 5
}
```

**Migrated To:**
```json
{
  "stable": {},
  "preview": {},
  "recent_majors": {},
  "history": {}
}
```

First run with new format will establish new baselines.

## Artifacts

Each job uploads test results as artifacts:
- `snippet-results-stable-{run_id}`
- `snippet-results-preview-{run_id}`
- `snippet-results-recent-{run_id}`

These contain:
- `results.xml` / `results_preview.xml` / `results_recent.xml` (JUnit format)
- `snippet_score.json` (detailed metrics)

## Benefits

1. **Version-Specific Tracking**: Track quality for each stable version independently
2. **Historical Trends**: Analyze quality trends over time
3. **Flexible Gating**: Only stable tests block PRs
4. **Early Warnings**: Preview and recent_majors provide advance notice
5. **Comprehensive Testing**: Cover multiple version ranges without blocking workflow
6. **Audit Trail**: Full history with timestamps and commits
