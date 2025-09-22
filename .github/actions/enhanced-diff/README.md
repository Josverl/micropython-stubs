# Enhanced Diff Action

This GitHub Action provides enhanced diff checking for the micropython-stubs workflow. It determines whether a commit should be made based on the types of files that have changed.

## Key Features

- **Smart Commit Logic**: Only commits when non-JSON files are changed
- **JSON File Inclusion**: Includes JSON files in commits when they occur alongside other changes
- **Detailed Reporting**: Provides comprehensive output about what files changed
- **Python-based**: Uses Python instead of bash/PowerShell for better cross-platform compatibility

## Logic

The action categorizes changed files into two groups:

1. **JSON files** (`.json` extension, case-insensitive)
2. **Non-JSON files** (all other files)

### Commit Decision

- ✅ **Commit proceeds** when non-JSON files are changed (JSON files are included)
- ❌ **Commit skipped** when only JSON files are changed

### Examples

| Changed Files | JSON Files | Non-JSON Files | Commit? | Rationale |
|---------------|------------|----------------|---------|-----------|
| `stub.py`, `config.json` | 1 | 1 | ✅ Yes | Non-JSON files trigger commit |
| `config.json`, `package.json` | 2 | 0 | ❌ No | Only JSON files changed |
| `README.md`, `main.py` | 0 | 2 | ✅ Yes | Non-JSON files trigger commit |
| *(no changes)* | 0 | 0 | ❌ No | No changes detected |

## Inputs

- `verbose` (optional): Set to `"true"` for detailed output. Default: `"false"`

## Outputs

- `changed`: `"true"` if commit should proceed, `"false"` otherwise
- `count`: Total number of changed files
- `json_count`: Number of JSON files changed
- `non_json_count`: Number of non-JSON files changed (determines commit decision)

## Usage

```yaml
- name: Check for relevant changes
  uses: ./.github/actions/enhanced-diff
  id: diff
  with:
    verbose: "true"

- name: Show results
  run: |
    echo "Should commit: ${{steps.diff.outputs.changed}}"
    echo "Total files: ${{steps.diff.outputs.count}}"
    echo "Non-JSON files: ${{steps.diff.outputs.non_json_count}}"
    echo "JSON files: ${{steps.diff.outputs.json_count}}"

- name: Commit changes
  if: ${{steps.diff.outputs.changed == 'true'}}
  run: git commit -am "Update files"
```

## Files

- `action.yml`: GitHub Action definition
- `check_changes.py`: Main Python script with diff logic
- `test_enhanced_diff.py`: Test suite for the diff logic
- `README.md`: This documentation

## Testing

Run the test suite to verify the logic:

```bash
cd .github/actions/enhanced-diff
python test_enhanced_diff.py
```

## Migration from stub-diff

This action replaces the previous `stub-diff` action with enhanced logic. The key differences:

1. **Language**: Python instead of PowerShell
2. **Logic**: JSON-aware commit decisions instead of pattern-based
3. **Outputs**: Additional outputs for JSON vs non-JSON file counts
4. **Cross-platform**: Better compatibility across different runners