# Deploying the Board Comparison Tool to GitHub Pages

This guide shows how to deploy the MicroPython Board Comparison Tool to GitHub Pages.

## Quick Start

The easiest way to deploy is using the vanilla JavaScript version:

1. **Build the database and JSON:**
   ```bash
   cd tools/board_compare
   python build_database.py --version v1_26_0 --json frontend/board_comparison.json
   ```

2. **Copy files to docs folder:**
   ```bash
   # From repository root
   mkdir -p docs/board-compare
   cp tools/board_compare/frontend/index-vanilla.html docs/board-compare/index.html
   cp tools/board_compare/frontend/board_comparison.json docs/board-compare/
   cp tools/board_compare/frontend/README.md docs/board-compare/
   ```

3. **Enable GitHub Pages:**
   - Go to repository Settings → Pages
   - Set source to "Deploy from a branch"
   - Select the `main` branch and `/docs` folder
   - Save

4. **Access the tool:**
   - The tool will be available at: `https://josverl.github.io/micropython-stubs/board-compare/`

## Alternative: PyScript Version

If you want to use the PyScript version instead:

```bash
# Copy PyScript version
cp tools/board_compare/frontend/index.html docs/board-compare/
cp tools/board_compare/frontend/app.py docs/board-compare/
cp tools/board_compare/frontend/pyscript.json docs/board-compare/
cp tools/board_compare/frontend/board_comparison.json docs/board-compare/
```

**Note:** The PyScript version requires a modern browser with WebAssembly support and may load slower due to downloading the Python runtime.

## Automatic Updates

The database is automatically updated weekly by the GitHub Actions workflow:
- File: `.github/workflows/update_board_comparison.yml`
- Schedule: Every Sunday at 2 AM UTC
- Can be manually triggered from the Actions tab

To update the deployed version:
1. The workflow updates `tools/board_compare/frontend/board_comparison.json`
2. You need to copy it to `docs/board-compare/board_comparison.json`
3. Commit and push the changes

## File Structure

```
docs/
└── board-compare/
    ├── index.html              # Main viewer (vanilla JS or PyScript)
    ├── board_comparison.json   # Board data (24KB)
    ├── app.py                  # (Optional, for PyScript version)
    ├── pyscript.json          # (Optional, for PyScript version)
    └── README.md              # Documentation
```

## Customization

You can customize the viewer by editing:
- Colors and styling in the `<style>` section of `index.html` or `index-vanilla.html`
- Comparison logic in the JavaScript section
- Add filters, search, or other features as needed

## Performance

- **Database size:** ~4.8MB (SQLite, not deployed)
- **JSON size:** ~24KB (deployed)
- **Load time:** < 1 second for JSON version
- **Supports:** 20+ boards for each MicroPython version

## Troubleshooting

**Issue:** Boards don't appear in dropdowns
- **Solution:** Check that `board_comparison.json` is in the same directory as `index.html`
- Open browser console (F12) to check for loading errors

**Issue:** PyScript version shows error
- **Solution:** Check browser console for errors
- Try using the vanilla JavaScript version instead (rename `index-vanilla.html` to `index.html`)

**Issue:** Data is outdated
- **Solution:** Re-run `build_database.py` with latest stubs
- Copy updated JSON to docs folder
- Commit and push changes

## Adding More Versions

To support multiple MicroPython versions:

1. Build databases for each version:
   ```bash
   python build_database.py --version v1_26_0 --json frontend/v1_26_0.json
   python build_database.py --version v1_25_0 --json frontend/v1_25_0.json
   ```

2. Modify the frontend to include a version selector

3. Load the appropriate JSON based on user selection
