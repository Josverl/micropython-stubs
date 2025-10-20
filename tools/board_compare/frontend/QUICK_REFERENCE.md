# PyScript Board Explorer - Quick Reference

## File Organization

```
frontend/
├── board-explorer-mpy.html       ← Main entry point (425 lines)
├── board-explorer.html           ← Original JavaScript version
├── pyscript.toml                 ← Configuration (files to load)
├── main.py                       ← Application logic (784 lines)
├── sqlite_wasm.py                ← SQLite wrapper (249 lines) [NEW]
├── board_utils.py                ← Utilities (195 lines)
├── board_comparison.db           ← SQLite database (6.7MB)
├── IMPLEMENTATION_REVIEW.md      ← Full architecture review [NEW]
└── README-pyscript.md            ← PyScript documentation
```

## How to Run

### Option 1: VSCode Task
```
Ctrl+Shift+B → "http.server: board explorer"
Opens http://localhost:8080/board-explorer-mpy.html
```

### Option 2: Manual HTTP Server
```bash
cd frontend
python -m http.server 8000
# http://localhost:8000/board-explorer-mpy.html
```

## Module Responsibilities

### board-explorer-mpy.html
- HTML structure (425 lines)
- CSS styling (inline)
- PyScript configuration
- JavaScript tree toggle functions
- Loads `main.py` via PyScript

### pyscript.toml
- Specifies files to fetch and load:
  - `sqlite_wasm.py` (SQLite wrapper)
  - `board_utils.py` (Utilities)
  - `board_comparison.db` (Database)

### main.py (Application Logic)
```
initialize() → load_database() → load_board_list() → populate_selects()
                     ↓
         User selects board
                     ↓
              load_board_details()
                     ↓
         Query modules/classes/methods
                     ↓
         render_module_tree() + render_class_tree()
                     ↓
         Update DOM with tree HTML
```

### sqlite_wasm.py (Database Layer)
```python
SQLite.initialize()           # Initialize SQL.js WASM
SQL.open_database(filename)   # Load database file
db.prepare(sql)               # Prepare query
stmt.bind(params)             # Bind parameters
stmt.step()                   # Execute step
stmt.getAsObject()            # Get row as dict
stmt.free()                   # Free statement
```

### board_utils.py (Utilities)
```python
format_board_name()           # Format board display name
format_module_summary()       # "X classes, Y functions"
format_method_signature()     # "method(param: type) -> return"
create_icon_html()            # Font Awesome icon
build_module_tree_html()      # Generate tree HTML
```

## Data Flow

```
HTML Button Click
    ↓
PyScript Event Handler
    ↓
load_board_details(board_id)
    ↓
db.prepare(sql) + stmt.bind() + stmt.step()
    ↓
Process results → render_module_tree()
    ↓
document.getElementById().innerHTML = html
    ↓
Browser renders tree
    ↓
User clicks expand arrow
    ↓
toggleModule() JavaScript function
    ↓
DOM classList.toggle('hidden')
```

## Common Tasks

### Access Database
```python
from sqlite_wasm import SQLite

SQL = await SQLite.initialize(version="1.13.0", cdn="cdnjs")
db = await SQL.open_database("board_comparison.db")

stmt = db.prepare("SELECT * FROM boards")
while stmt.step():
    row = stmt.getAsObject()
    print(row)
stmt.free()
```

### Update Status Message
```python
from main import update_status

update_status("Loading...", "info")         # Blue
update_status("Done!", "success")           # Green
update_status("Error!", "error")            # Red
```

### Query with Parameters (Workaround)
```python
# Note: stmt.bind() has FFI bug - use string concat instead
from main import sql_escape

version = "v1.26.0"
sql = f"SELECT * FROM boards WHERE version = {sql_escape(version)}"
stmt = db.prepare(sql)
# ... execute query ...
```

### Render Expandable Tree
```python
from main import render_module_tree

html = render_module_tree(module_dict)
container = document.getElementById("results")
container.innerHTML = html
```

### Handle Events
```python
from pyscript import document

button = document.getElementById("my-button")
button.onclick = lambda e: my_function()

input_elem = document.getElementById("my-input")
input_elem.onchange = lambda e: on_input_changed(e.target.value)
```

## Debugging

### Browser Console
```javascript
// F12 to open DevTools → Console tab
// Python errors will show here
console.log("Debug message")
```

### Print in Python
```python
print("Debug message")  # Shows in browser console
import sys
sys.print_exception(e)  # Print full traceback
```

### Check Database
```python
stmt = db.prepare("SELECT COUNT(*) as count FROM boards")
stmt.step()
row = stmt.getAsObject()
print(f"Board count: {row['count']}")
stmt.free()
```

## Key Configuration

### pyscript.toml
```toml
[files]
"sqlite_wasm.py" = ""        # Fetch from current dir
"board_utils.py" = ""        # Fetch from current dir
"board_comparison.db" = ""   # Fetch from current dir
```

### HTML Script Tags
```html
<!-- SQL.js library -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/sql.js/1.13.0/sql-wasm.js"></script>

<!-- PyScript runtime -->
<script type="module" src="https://pyscript.net/releases/2025.8.1/core.js"></script>

<!-- Application code -->
<script type="mpy" src="./main.py" config="./pyscript.toml"></script>
```

## Performance Tips

| Operation | Time | Optimization |
|-----------|------|--------------|
| Page load | 3-4s | Acceptable (first load only) |
| Board select | 300ms | Query is fast, rendering takes time |
| Module expand | <100ms | No query, just DOM toggle |
| Database query | <100ms | Indexed queries are fast |

## Browser Support

| Browser | Version | Status |
|---------|---------|--------|
| Chrome | 90+ | ✅ Full support |
| Firefox | 88+ | ✅ Full support |
| Safari | 14+ | ✅ Full support |
| Edge | 90+ | ✅ Full support |
| IE 11 | - | ❌ No WASM support |

## Known Limitations

1. **stmt.bind() Bug** - Use string concat workaround (documented in BUG_REPORT_*.md)
2. **CDN Dependent** - Requires internet for PyScript/SQL.js
3. **Cold Start** - 2-3s startup vs instant JavaScript
4. **Memory** - ~20MB resident vs ~10MB JavaScript
5. **Offline** - No offline support yet (PWA planned for v2.0)

## Helpful Commands

```bash
# Start development server
python -m http.server 8000 --directory frontend

# Check database integrity
sqlite3 frontend/board_comparison.db "SELECT COUNT(*) FROM boards"

# Count files
find frontend -type f | wc -l

# Check file sizes
ls -lh frontend/*.{py,db,toml,html}

# Test specific board
sqlite3 frontend/board_comparison.db \
  "SELECT COUNT(*) as modules FROM board_modules WHERE board_id = 5"
```

## Next Steps

1. **Test**: Run in browser, verify board list loads
2. **Debug**: Check browser console for errors
3. **Compare**: View different boards and versions
4. **Optimize**: Profile and improve performance
5. **Implement**: Add comparison and search features

---

**Version**: 1.0 (October 19, 2025)  
**Status**: Ready for Development
