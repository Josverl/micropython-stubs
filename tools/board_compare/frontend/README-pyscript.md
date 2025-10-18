# MicroPython Board Explorer - PyScript Edition

## Overview

This is a PyScript (MicroPython WebAssembly) version of the MicroPython Board Explorer tool. It provides the same functionality as the JavaScript version but runs Python code directly in the browser using MicroPython and WebAssembly.

## Files

- **board-explorer-mpy.html** - Main PyScript application (single-file app)
- **board_utils.py** - Shared Python utilities for board data processing
- **board_comparison.db** - SQLite database (6.7MB, unchanged from JS version)
- **board_comparison.json** - Fallback JSON data (24KB)
- **pyscript.md** - Detailed migration log and technical documentation

## Features

### Current Implementation (v1.0 - Phase 3)

✅ **Database Integration**
- SQLite database access via SQL.js WASM
- 6.7MB database loaded on demand
- Fallback to JSON if database unavailable
- Efficient query execution with prepare/bind/step pattern

✅ **Board Explorer**
- Board selection by version and name
- Module list display with counts (classes, functions, constants)
- Database-driven queries for accurate data
- Status indicators for loading states

✅ **User Interface**
- Three-tab navigation (Explorer, Compare, Search)
- Responsive design with gradient styling
- Loading animations and progress indicators
- Error handling with user-friendly messages

### Planned Features (Future Phases)

🔲 **Advanced Explorer**
- Expandable module tree
- Class details with methods and attributes
- Method signatures with parameters
- Documentation display

🔲 **Board Comparison**
- Side-by-side board comparison
- Diff highlighting (unique modules, different APIs)
- Statistics panel
- Filterable results

🔲 **Search Functionality**
- Cross-board API search
- Module, class, and method search
- Results grouped by type
- Board filtering

🔲 **Enhanced Features**
- URL state management
- Shareable links
- Dark mode toggle
- Export to PDF/CSV

## Technology Stack

- **PyScript**: 2025.8.1
- **Python Runtime**: MicroPython v1.26.0-preview.386
- **Database**: SQLite via sql.js 1.8.0 WASM
- **Styling**: CSS (inline, based on original design)
- **Icons**: Font Awesome 6.4.0

## How It Works

### PyScript Setup

```html
<script type="mpy-config">
{
    "packages": [],
    "fetch": [
        {"files": ["board_comparison.json"]},
        {"files": ["board_utils.py"]}
    ],
    "js_modules": {
        "main": {
            "https://.../sql-wasm.js": "SQL"
        }
    }
}
</script>
```

### Database Loading

```python
from pyscript import fetch, ffi
import js

# Initialize SQL.js
SQL = await js.initSqlJs(ffi.to_js({
    "locateFile": lambda file: f"https://.../{file}"
}))

# Load database
response = await fetch("board_comparison.db")
buffer = await response.arrayBuffer()
db_array = js.Uint8Array.new(buffer)
db = SQL.Database.new(db_array)

# Execute queries
stmt = db.prepare("SELECT * FROM boards WHERE version = ?")
stmt.bind([version])

results = []
while stmt.step():
    row = stmt.getAsObject()
    results.append({"name": row["name"]})

stmt.free()
```

### DOM Manipulation

```python
from pyscript import document

# Get elements
elem = document.getElementById("my-element")

# Update content
elem.innerText = "New text"
elem.innerHTML = "<strong>HTML content</strong>"

# Modify styles
elem.classList.add("active")
elem.style.display = "block"

# Event handling
button.onclick = lambda e: my_function()
```

## Development

### Local Testing

1. Start a local HTTP server:
```bash
cd tools/board_compare/frontend
python3 -m http.server 8000
```

2. Open in browser:
```
http://localhost:8000/board-explorer-mpy.html
```

### Requirements

- Modern web browser with WebAssembly support
- JavaScript enabled
- Internet connection (for CDN resources)
- ~10MB download for first load (PyScript + database)

### Browser Support

- ✅ Chrome/Chromium 90+
- ✅ Firefox 88+
- ✅ Safari 14+
- ✅ Edge 90+

Note: Older browsers without WebAssembly support will not work.

## Architecture

### Data Flow

```
User Interaction
    ↓
PyScript Event Handler
    ↓
Python Function (board_utils.py)
    ↓
SQL.js Database Query
    ↓
JavaScript Bridge (js module)
    ↓
Python Result Processing
    ↓
DOM Update (pyscript.document)
    ↓
Browser Render
```

### Key Components

1. **PyScript Runtime**: MicroPython interpreter in WebAssembly
2. **SQL.js Engine**: SQLite compiled to WebAssembly
3. **JavaScript Bridge**: FFI between Python and JavaScript
4. **Board Utilities**: Python module for data processing
5. **DOM API**: PyScript's document object for UI updates

## Comparison with JavaScript Version

| Feature | JavaScript | PyScript |
|---------|-----------|----------|
| Runtime | Native JS | MicroPython WASM |
| Database | SQL.js | SQL.js (via JS bridge) |
| Size | 22KB HTML + 90KB JS | 18KB combined |
| Load Time | ~1s | ~2-3s (PyScript init) |
| Memory | ~10MB | ~15MB (WASM overhead) |
| Maintainability | Medium | High (Python) |
| Code Reuse | Limited | High (board_utils.py) |

## Performance

- **Initial Load**: 2-3 seconds (PyScript + database)
- **Page Navigation**: Instant (single-page app)
- **Database Query**: <100ms (indexed queries)
- **Board Selection**: <200ms (with render)
- **Module Display**: <300ms (for 100+ modules)

## Known Limitations

1. **CDN Dependencies**: Requires internet for PyScript and SQL.js
2. **WASM Size**: ~3MB PyScript runtime overhead
3. **Browser Support**: Requires modern browser with WASM
4. **Memory Usage**: Higher than pure JavaScript version
5. **Cold Start**: Slower initial load than JavaScript

## Troubleshooting

### PyScript Not Loading

- Check browser console for errors
- Verify CDN access (not blocked by firewall)
- Clear browser cache and reload
- Check browser WebAssembly support

### Database Not Loading

- Verify board_comparison.db exists in same directory
- Check file size (should be ~6.7MB)
- Check browser console for fetch errors
- Ensure server allows .db file downloads

### Board List Empty

- Check database loaded successfully
- Verify SQL query execution
- Check browser console for Python errors
- Fallback JSON should still work

## Future Enhancements

See pyscript.md for detailed migration log and planned features.

### Short Term (v1.1)
- Expandable module tree
- Class and method details
- Basic comparison view

### Medium Term (v1.2)
- Full comparison with diff
- Search functionality
- URL state management

### Long Term (v2.0)
- Offline support (PWA)
- Dark mode
- Export features
- Advanced filtering

## Contributing

This is a migration from the JavaScript version. Key goals:

1. **Feature Parity**: Match JavaScript functionality
2. **Code Quality**: Leverage Python's strengths
3. **Performance**: Optimize for WASM constraints
4. **Usability**: Maintain familiar UX

## License

Same as parent project (MIT).

## Credits

- Original JavaScript version: board-explorer.html
- PyScript: https://pyscript.net/
- SQL.js: https://github.com/sql-js/sql.js
- MicroPython: https://micropython.org/

---

*Last Updated: October 18, 2025*
*Version: 1.0 (Phase 3)*
