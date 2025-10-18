# PyScript Board Explorer - Debug Summary

## Problem

The `board-explorer-mpy.html` page was developed in Codespaces without access to CDN resources, leading to PyScript module loading errors:

```
ImportError: no module named 'board_utils'
```

Additionally, the `js.initSqlJs` was not available, causing database initialization to fail.

## Root Causes

### 1. PyScript 2025.8.1 `fetch` Configuration Not Working
The `mpy-config` used:
```json
{
  "fetch": [
    {"files": ["board_utils.py"]}
  ]
}
```

This configuration is not reliably loading local Python files in PyScript 2025.8.1 (MicroPython WASM).

**Solution**: Removed `fetch` configuration and implemented dynamic module loading via `fetch()` API and `exec()`.

### 2. `js_modules` Configuration Not Loading SQL.js
The configuration attempted to load SQL.js via:
```json
{
  "js_modules": {
    "main": {
      "https://cdnjs.cloudflare.com/ajax/libs/sql.js/1.8.0/sql-wasm.js": "SQL"
    }
  }
}
```

This was not making `initSqlJs` available to Python code.

**Solution**: Added `<script>` tag to load SQL.js before PyScript, making it available on `window` object.

### 3. Module Functions Not Available After Dynamic Load
When using `exec(content, globals())`, the functions weren't accessible via the `board_utils` namespace.

**Solution**: Created a `BoardUtils` class and used `setattr()` to attach loaded functions to it.

## Changes Made

### 1. Updated `board-explorer-mpy.html`

#### Removed problematic `mpy-config`:
```html
<!-- BEFORE -->
<script type="mpy-config">
{
    "packages": [],
    "fetch": [
        {"files": ["board_utils.py"]}
    ],
    "js_modules": {
        "main": {
            "https://cdnjs.cloudflare.com/ajax/libs/sql.js/1.8.0/sql-wasm.js": "SQL"
        }
    }
}
</script>

<!-- AFTER -->
<script type="mpy-config">
{
    "packages": []
}
</script>
```

#### Added SQL.js script tag:
```html
<!-- Added before PyScript module -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/sql.js/1.8.0/sql-wasm.js"></script>
```

#### Created dynamic board_utils loader:
```python
# Create a namespace for board_utils
class BoardUtils:
    pass

board_utils = BoardUtils()

# Dynamically load board_utils module
async def load_board_utils():
    """Load board_utils.py dynamically"""
    try:
        response = await fetch("board_utils.py")
        if response.ok:
            content = await response.text()
            # Create a local namespace for the module
            module_globals = {}
            exec(content, module_globals)
            
            # Copy all functions to the board_utils object
            for name, obj in module_globals.items():
                if not name.startswith("_"):
                    setattr(board_utils, name, obj)
            
            return True
        else:
            return False
    except Exception as e:
        print(f"Failed to load board_utils: {e}")
        return False
```

#### Updated database initialization:
```python
# Access SQL.js via window object
SQL = await window.initSqlJs(ffi.to_js({
    "locateFile": lambda file, *args: f"https://cdnjs.cloudflare.com/ajax/libs/sql.js/1.8.0/{file}"
}))
```

Note: Lambda now accepts `*args` because JavaScript calls it with additional parameters.

#### Updated main() initialization:
```python
async def main():
    """Main entry point for the application."""
    update_status("Loading board utilities...", "info")
    
    # Load board_utils module dynamically
    utils_loaded = await load_board_utils()
    if not utils_loaded:
        update_status("Error: Failed to load board utilities.", "error")
    else:
        app_state["board_utils_loaded"] = True
    
    # ... rest of initialization
```

## Testing Results

✅ **Module Loading**: `board_utils.py` now loads successfully
✅ **Database Access**: SQL.js initializes and database loads (6.7MB)
✅ **Board Selection**: Dropdowns populate with boards from database
✅ **No Errors**: PyScript initializes without import errors
✅ **UI Responsive**: User can select version and board

## Network Requests

The page now makes these successful requests:
- `board_utils.py` → 200 OK (7.6KB)
- `board_comparison.db` → 200 OK (6.7MB)
- `sql-wasm.js` → 200 OK (via CDN)
- All PyScript resources → 200 OK

## Files Modified

- `d:\mypython\micropython-stubs\tools\board_compare\frontend\board-explorer-mpy.html`

## Recommendations for Future Development

1. **Consider using `micropython.mpy` package system** instead of dynamic loading if PyScript documentation updates with better module loading support
2. **Test offline functionality** - current implementation requires CDN access for SQL.js
3. **Add error handling** for when SQL.js fails to load
4. **Document the async initialization pattern** in `README-pyscript.md`

## Technical Pattern Learned

For PyScript 2025.8.1 with MicroPython WASM:
- ✅ Dynamic `fetch()` + `exec()` works well for loading modules
- ✅ External JS libraries loaded via `<script>` tags are accessible via `window` object
- ✅ `ffi.to_js()` bridges Python and JavaScript data types
- ⚠️ `mpy-config` `fetch` configuration unreliable for local files
- ⚠️ `mpy-config` `js_modules` configuration not working with `initSqlJs`

---

*Debug completed: October 18, 2025*
*Status: ✅ Working*
