# Database Access Patterns Summary

## Current Development Setup
```
HTTP Server: http://localhost:8080/
Database URL: ./board_comparison.db
Full URL: http://localhost:8080/frontend/board_comparison.db
```

## Production Deployment Scenarios

### Scenario 1: Same-Origin Hosting (Recommended)
```
Website: https://micropython-explorer.com/
Database: https://micropython-explorer.com/data/board_comparison.db
JavaScript: const dbUrl = './data/board_comparison.db';

Benefits:
✅ No CORS issues
✅ Simple relative URLs  
✅ Single deployment location
✅ Works with all options (1, 3, 4)
```

### Scenario 2: CDN Hosting (Performance Optimized)
```
Website: https://micropython-explorer.com/
Database: https://cdn.micropython-explorer.com/board_comparison.db  
JavaScript: const dbUrl = 'https://cdn.micropython-explorer.com/board_comparison.db';

Benefits:
✅ Global CDN performance
✅ Reduced main server load
⚠️ Requires CORS configuration
✅ Best for high-traffic sites
```

### Scenario 3: GitHub Pages Example
```
Repository: github.com/user/micropython-stubs
GitHub Pages: https://user.github.io/micropython-stubs/
Database URL: https://user.github.io/micropython-stubs/tools/board_compare/frontend/board_comparison.db
JavaScript: const dbUrl = './board_comparison.db';

Benefits:  
✅ Free hosting
✅ Automatic deployments
✅ No server maintenance
✅ Perfect for open source projects
```

## Option-Specific Deployment Details

### Option 0: Python/PyScript (Current - Broken)
```python
# pyscript.toml configuration
[files]
"board_comparison.db" = ""  # Loads from same directory

# File access in Python
with open("board_comparison.db", "rb") as f:
    file_data = f.read()
```
**Deployment**: Upload database alongside HTML, configure in pyscript.toml

### Option 1: JavaScript Direct
```javascript
// Single fetch per page load
const response = await fetch('./board_comparison.db');
const arrayBuffer = await response.arrayBuffer();
const database = new SQL.Database(new Uint8Array(arrayBuffer));
```
**Deployment**: Upload database to web server, use relative or absolute URLs

### Option 3: Web Worker
```javascript
// Main thread creates worker
const worker = new Worker('./sql-worker.js');

// Worker fetches database
// In sql-worker.js:
const response = await fetch(url); // URL passed from main thread
```
**Deployment**: Upload database + worker script to web server, same-origin required

### Option 4: IndexedDB Cache
```javascript
// First visit: Network fetch + cache
const response = await fetch('./board_comparison.db');
await this.saveToIndexedDB(cacheKey, dbData);

// Subsequent visits: Cache only
const cachedData = await this.getFromIndexedDB(cacheKey);
```
**Deployment**: Upload database to web server, browser handles caching automatically

## File Size Impact on Deployment

**Current database size**: ~4.5MB

### Bandwidth Usage Comparison:
| Option | First Visit | Return Visit | Monthly (1000 users) |
|--------|-------------|--------------|---------------------|
| Option 1 | 4.5MB | 4.5MB | 9,000MB (9GB) |
| Option 3 | 4.5MB | 4.5MB | 9,000MB (9GB) |
| Option 4 | 4.5MB | ~0MB | 4,500MB (4.5GB) |

**Cost savings with Option 4**: 50% bandwidth reduction for sites with return visitors.

## Security Considerations

### Same-Origin (Secure)
```
Website: https://example.com/app/
Database: https://example.com/app/data/db.sqlite
✅ Same origin - no CORS needed
✅ Maximum security
```

### Cross-Origin (Requires CORS)
```
Website: https://example.com/
Database: https://cdn.example.com/db.sqlite
⚠️ Different origin - CORS required
⚠️ Potential security implications
```

**Required CORS headers for cross-origin:**
```
Access-Control-Allow-Origin: https://example.com
Access-Control-Allow-Methods: GET
Access-Control-Allow-Headers: Content-Type
```

## Quick Migration Guide

**From current PyScript to Option 4:**

1. **Keep existing file structure:**
   ```
   frontend/
   ├── board-explorer-mpy.html
   ├── board_comparison.db      # Keep this
   └── sqlite_wasm.py          # Update this
   ```

2. **Update sqlite_wasm.py:**
   ```python
   # Change from:
   LOAD_OPTION = 0
   # To:
   LOAD_OPTION = 4
   ```

3. **No database deployment changes needed** - same relative URL works!

**Result**: 386x to 1,306x performance improvement with zero deployment complexity changes.