# MicroPython Board Explorer & Comparison

This directory contains the static web viewer for comparing MicroPython boards.

## ⚠️ Important: Database-Only Frontend

**The frontend now requires the SQLite database** (`board_comparison.db`) for all functionality. The simplified JSON file is no longer used, ensuring you see complete module, class, and method details.

## Files

- **`board-explorer.html`** - Enhanced multi-view explorer (recommended)
  - Board Explorer: Browse single board's complete API tree
  - Compare Boards: Side-by-side comparison with class/method details
  - Search APIs: Find modules, classes, methods across all boards
  - **Requires**: `board_comparison.db` (4.8MB), SQL.js library

- `index-vanilla.html` - Simple vanilla JavaScript version (module-level only)
- `index.html` - PyScript version (Python in browser)
- `app.py` - PyScript application code
- `pyscript.json` - PyScript configuration
- **`board_comparison.db`** - SQLite database with complete API data (4.8MB) **[REQUIRED]**
- `board_comparison.json` - Simplified board list (24KB, used only for fallback)

## MCP Server Integration

The SQLite database can also be accessed via MCP (Model Context Protocol) server for programmatic queries. A store configuration is available at:

- `.vscode/stores/board-comparison.store.json` - MCP server configuration for the SQLite database

This allows AI assistants and other tools to directly query the board comparison database for detailed API information.

## Local Testing

To test locally:

```bash
# Start a simple HTTP server
python -m http.server 8000

# Open in browser
# http://localhost:8000/board-explorer.html  (recommended - full features)
# or
# http://localhost:8000/index-vanilla.html  (simple module comparison)
```

**Note**: The `board-explorer.html` requires SQL.js library from a CDN to query the SQLite database in the browser. If CDN access is blocked, you may need to:
1. Download SQL.js locally (`sql-wasm.js` and `sql-wasm.wasm`)
2. Update the script tag in `board-explorer.html` to point to local files

## Deployment to GitHub Pages

To deploy this tool to GitHub Pages:

1. **Build the database** (required):
   ```bash
   cd ../..  # Go to tools/board_compare
   python build_database.py --version v1.26.0 \
     --db frontend/board_comparison.db \
     --json frontend/board_comparison.json
   ```

2. Copy the contents of this `frontend` directory to the `docs` folder in the repository root
3. **Ensure both files are included**:
   - `board_comparison.db` (4.8MB) - Required for board-explorer.html
   - `board_comparison.json` (24KB) - Used by simpler viewers
4. Enable GitHub Pages in repository settings to serve from the `docs` folder
5. The tool will be available at: `https://josverl.github.io/micropython-stubs/`

## Updating the Data

The board comparison data is automatically updated weekly by the GitHub Actions workflow defined in `.github/workflows/update_board_comparison.yml`.

You can also manually update it by running:

```bash
cd ../..  # Go to tools/board_compare
python build_database.py --version v1.26.0 --db frontend/board_comparison.db --json frontend/board_comparison.json
```

**Note**: Both the database and JSON files should be committed to the repository for GitHub Pages deployment.

## Database Schema

The SQLite database contains the following main tables:

- **`boards`** - MicroPython board information (version, port, board name)
- **`modules`** - Module definitions with docstrings
- **`classes`** - Class definitions within modules
- **`methods`** - Functions and methods with signatures and metadata
- **`parameters`** - Method parameters with type hints and defaults
- **`board_modules`** - Relationship between boards and their available modules

This rich schema enables detailed API comparisons and searches across the entire MicroPython ecosystem.

## Features by Frontend Version

### board-explorer.html (Recommended)
- ✅ Complete API details (modules, classes, methods, parameters)
- ✅ Single board exploration with expandable tree
- ✅ Side-by-side comparison with class/method details
- ✅ Cross-board API search
- ✅ Diff mode (show only differences)
- ⚠️ Requires: SQLite database + SQL.js library

### index-vanilla.html (Simple)
- ✅ Module-level comparison
- ✅ Fast and lightweight
- ✅ No external dependencies
- ❌ No class/method details

### index.html (PyScript)
- ✅ Python-in-browser experience
- ✅ Module-level comparison
- ⚠️ Requires: WebAssembly-capable browser
- ❌ No class/method details
