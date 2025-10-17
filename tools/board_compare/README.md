# MicroPython Board Comparison Tool

This tool provides a database and web viewer to compare MicroPython APIs across different boards and versions.

## Overview

The board comparison tool consists of three main components:

1. **Stub Scanner** (`scan_stubs.py`) - Extracts API information from .pyi stub files using Python's AST parser
2. **Database Builder** (`build_database.py`) - Creates and populates a SQLite database with normalized board/module/class/method information
3. **Web Viewer** (`frontend/`) - A static website using PyScript to visualize and compare boards

## Features

- Compare modules, classes, methods, and parameters across different boards
- Identify unique modules/APIs available only on specific boards
- View detailed method signatures including parameters and return types
- Export database to JSON for easy consumption by the web frontend
- Normalized database schema for efficient storage and querying

## Installation

Install the required dependencies:

```bash
pip install pydantic
```

The tools use only Python standard library for parsing (no libcst dependency required), plus Pydantic for data models.

## Usage

### 1. Build the Database

To create a database for MicroPython version 1.26.0:

```bash
cd tools/board_compare
python build_database.py --version v1_26_0 --db board_comparison.db --json frontend/board_comparison.json
```

Options:
- `--publish-dir`: Path to the publish directory (default: `../../publish`)
- `--version`: MicroPython version to process (default: `v1_26_0`)
- `--db`: Output SQLite database path (default: `board_comparison.db`)
- `--json`: Optional JSON output for the web frontend

### 2. View the Web Interface

The frontend is a static site that can be hosted on GitHub Pages or any web server.

To test locally, you can use Python's built-in HTTP server:

```bash
cd tools/board_compare/frontend
python -m http.server 8000
```

Then open http://localhost:8000 in your browser.

### 3. Deploy to GitHub Pages

To deploy the viewer to GitHub Pages:

1. Copy the `frontend` folder contents to a `docs` folder in the repository root (or a `gh-pages` branch)
2. Ensure `board_comparison.json` is included
3. Enable GitHub Pages in the repository settings
4. The site will be available at `https://josverl.github.io/micropython-stubs/`

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
└── frontend/              # Web viewer
    ├── index.html         # Main HTML page
    ├── app.py             # PyScript application
    ├── pyscript.json      # PyScript configuration
    └── board_comparison.json  # Generated data file
```

## Limitations

- Currently supports only .pyi stub files
- Complex type annotations may be simplified in the database
- The web interface requires a modern browser with WebAssembly support for PyScript

## Future Enhancements

- Add filtering by module type (standard library, hardware-specific, etc.)
- Show method signature differences in detail
- Add search functionality
- Export comparison reports
- Support for multiple MicroPython versions in one database
- Visual diff view for method signatures
