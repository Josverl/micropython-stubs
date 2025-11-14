# MicroPython Board Comparison Tool

This tool provides a database and web viewer to compare MicroPython APIs across different boards and versions.

## Overview

The board comparison tool consists of three main components:

1. **Stub Scanner** (`scan_stubs.py`) - Extracts API information from .pyi stub files using Python's AST parser
2. **Database Builder** (`build_database.py`) - Creates and populates a SQLite database with normalized board/module/class/method information
3. **Web Viewer** (`frontend/`) - Multiple static website versions to visualize and compare boards

## Features

### Enhanced Web Viewer

The tool now includes two frontend options:

#### 1. Board Explorer (`board-explorer.html`) - **NEW**
Comprehensive multi-page interface with:
- **Board Explorer**: Browse a single board's modules, classes, and methods in a tree view
- **Compare Boards**: Side-by-side comparison with options to hide common modules or show detailed class/method differences
- **Search APIs**: Find which boards support specific modules, classes, or methods (e.g., "Neopixel", "I2S", "machine.Pin")

Features:
- Single board module tree browser
- Click on modules/classes to see detailed information
- Diff-style view (hide common elements)
- Class and method level comparisons
- Search across all boards for specific APIs
- SQLite database integration for detailed queries

#### 2. Simple Comparison (`index-vanilla.html`)
Quick module-level comparison:
- Compare modules available on different boards
- Identify unique modules/APIs available only on specific boards
- View common modules shared across platforms
- Lightweight and fast (24KB JSON)

### Database Features

- Compare modules, classes, methods, and parameters across boards
- Normalized SQLite database schema
- Efficient storage and export options
- Export simplified JSON (24KB) or detailed JSON (168MB)

## Installation

Install the required dependencies:

```bash
pip install pydantic
```

The tools use only Python standard library for parsing (AST), plus Pydantic for data models.

## Usage

### 1. Build the Database

To create a database for MicroPython version 1.26.0:

```bash
cd tools/board_compare
python build_database.py --version v1_26_0 \
  --db board_comparison.db \
  --json frontend/board_comparison.json
```

Options:
- `--publish-dir`: Path to the publish directory (default: `../../publish`)
- `--version`: MicroPython version to process (default: `v1_26_0`)
- `--db`: Output SQLite database path (default: `board_comparison.db`)
- `--json`: Optional simplified JSON output for frontend
- `--detailed-json`: Optional detailed JSON with full module/class/method info (large file)

### 2. View the Web Interface

The frontends are static sites that can be hosted on GitHub Pages or any web server.

**Enhanced Explorer (Recommended):**
```bash
cd tools/board_compare/frontend
python -m http.server 8000
# Open http://localhost:8000/board-explorer.html
```

**Simple Comparison:**
```bash
cd tools/board_compare/frontend
python -m http.server 8000
# Open http://localhost:8000/index-vanilla.html
```

### 3. Deploy to GitHub Pages

See `DEPLOYMENT.md` for complete deployment instructions.

## Web Interface Features

### Board Explorer Page
- Select a board to view its complete module tree
- Click on modules to expand and see classes/functions
- Click on classes to see detailed information including:
  - Class docstrings
  - Methods with signatures
  - Properties and decorators

### Compare Boards Page
- Select two boards for side-by-side comparison
- **Hide common modules**: Show only differences (diff mode)
- **Detailed comparison**: View class and method level differences
- Color-coded results:
  - Green: Unique to Board 1
  - Red: Unique to Board 2
  - Yellow: Different implementations
  - White: Common to both

### Search APIs Page
- Search for any module, class, or method name
- Results show which boards have the matching APIs
- Examples:
  - Search "Neopixel" to find all boards with NeoPixel support
  - Search "I2S" to see I2S availability
  - Search "machine.Pin" for Pin class implementations

## Database Schema

The database uses a normalized schema with the following tables:

- **boards** - Board/port/version information
- **modules** - Module definitions
- **board_modules** - Many-to-many relationship between boards and modules
- **classes** - Class definitions within modules
- **methods** - Functions and methods (both module-level and class-level)
- **parameters** - Method/function parameters
- **module_constants** - Module-level constants
- **class_attributes** - Class attributes and constants
- **class_bases** - Base class relationships

## Data Models

The tool uses Pydantic models defined in `models.py`:

- `Board` - Represents a board/port combination with version info
- `Module` - Represents a Python module with classes and functions
- `Class` - Represents a class definition
- `Method` - Represents a function or method
- `Parameter` - Represents a function/method parameter

## Automated Updates

A GitHub Actions workflow can be configured to update the database weekly. See the example workflow in `.github/workflows/update_board_comparison.yml`.

## Architecture

```
tools/board_compare/
├── models.py              # Pydantic data models
├── scan_stubs.py          # Stub file scanner
├── build_database.py      # Database builder
├── README.md              # This file
├── DEPLOYMENT.md          # Deployment guide
└── frontend/              # Web viewers
    ├── board-explorer.html     # Enhanced multi-page viewer (NEW)
    ├── board-explorer.js       # Enhanced viewer logic (NEW)
    ├── index-vanilla.html      # Simple comparison viewer
    ├── index.html              # PyScript version
    ├── app.py                  # PyScript application
    ├── pyscript.json          # PyScript configuration
    ├── board_comparison.json  # Generated simplified data (24KB)
    └── board_comparison.db    # SQLite database (4.8MB)
```

## Requirements

- Python 3.9 or higher
- Pydantic for data models
- Modern web browser (for SQL.js support in enhanced viewer)
- SQLite database file must be accessible to frontend for detailed features

## Limitations

- The detailed JSON export (168MB) is too large for browser loading
- The enhanced viewer requires SQL.js library loaded from CDN
- Complex type annotations may be simplified in the database
- The web interface requires a modern browser with WebAssembly support for database features

## Future Enhancements

- Add filtering by module type (standard library, hardware-specific, etc.)
- Show method signature differences in detail
- Export comparison reports
- Support for multiple MicroPython versions in one database
- Visual diff view for method signatures
- Offline database support
