# MicroPython Board Comparison Tool - GitHub Pages Setup

This directory contains the static web viewer for comparing MicroPython boards.

## Deployment to GitHub Pages

To deploy this tool to GitHub Pages:

1. Ensure the `board_comparison.json` file is generated and present in this directory
2. Copy the contents of this `frontend` directory to the `docs` folder in the repository root
3. Enable GitHub Pages in repository settings to serve from the `docs` folder
4. The tool will be available at: `https://josverl.github.io/micropython-stubs/`

## Files

- `index.html` - PyScript version (requires modern browser with WebAssembly support)
- `index-vanilla.html` - Vanilla JavaScript version (works in all browsers, recommended)
- `app.py` - PyScript application code
- `pyscript.json` - PyScript configuration
- `board_comparison.json` - Generated board data (updated by GitHub Actions)

## Local Testing

To test locally:

```bash
# Start a simple HTTP server
python -m http.server 8000

# Open in browser
# http://localhost:8000/index-vanilla.html  (recommended)
# or
# http://localhost:8000/index.html  (PyScript version)
```

## Updating the Data

The board comparison data is automatically updated weekly by the GitHub Actions workflow defined in `.github/workflows/update_board_comparison.yml`.

You can also manually update it by running:

```bash
cd ../..  # Go to tools/board_compare
python build_database.py --version v1_26_0 --db board_comparison.db --json frontend/board_comparison.json
```
