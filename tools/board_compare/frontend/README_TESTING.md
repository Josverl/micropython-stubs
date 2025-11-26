# Testing Guide - Board Comparison Frontend

## Test Scripts Overview

This directory contains several test scripts for validating the board comparison functionality:

### 1. Python SQL Tests (No HTTP server required)

#### `test_performance.py`
**Purpose**: Validates numbered SQL parameters in Python sqlite3 environment  
**Requirements**: 
- `board_comparison.db` database file
- Python sqlite3 module (built-in)

**Usage**:
```powershell
python test_performance.py
```

**What it tests**:
- Level 1, 2, and 3 comparison queries with numbered parameters
- 4 comparison scenarios:
  - ESP32 (esp32_generic) vs RP2 (rpi_pico)
  - ESP32 Generic vs ESP32 S3
  - ESP32 v1.25.0 vs v1.26.0 (same board, different versions)
  - ESP32 (esp32_generic) vs STM32 (stm32)

**Expected output**:
```
✅ Scenario 1: ESP32 vs RP2
   Modules: 24 unique ESP32, 2 unique RP2, 46 common
✅ Scenario 2: ESP32 Generic vs S3
   Modules: 0 unique Generic, 1 unique S3, 70 common
✅ Scenario 3: ESP32 v1.25.0 vs v1.26.0
   Modules: 1 unique v1.25.0, 0 unique v1.26.0, 70 common
✅ Scenario 4: ESP32 vs STM32
   Modules: 26 unique ESP32, 3 unique STM32, 44 common
```

---

#### `compare_esp32_stm32.py`
**Purpose**: Detailed comparison output for ESP32 vs STM32 boards  
**Requirements**: Same as test_performance.py

**Usage**:
```powershell
python compare_esp32_stm32.py
```

**What it tests**:
- All 3 levels of comparison with detailed breakdown
- Validates numbered parameters in standalone script context

**Expected output**:
```
ESP32 (esp32_generic) vs STM32 (stm32) - v1.26.0

Level 1: Modules
- ESP32: 70 modules, STM32: 47 modules
- Unique to ESP32: 26, Unique to STM32: 3, Common: 44

Level 2: Classes/Functions/Constants
- Classes: 34 unique ESP32, 24 unique STM32
- Functions: 4 unique ESP32, 4 unique STM32
- Constants: 59 unique ESP32, 3 unique STM32

Level 3: Methods/Attributes
- Methods: 207 unique ESP32, 291 unique STM32, 12 classes differ
- Attributes: 76 unique ESP32, 134 unique STM32
```

---

### 2. Frontend Browser Tests (HTTP server required)

#### Prerequisites
Before running browser tests:

1. **Start HTTP Server** (VSCode Task):
   - Press `Ctrl+Shift+P` → `Tasks: Run Task`
   - Select: `http.server: board explorer`
   - OR run manually:
     ```powershell
     python -m http.server 8080
     ```

2. **Verify Server**:
   - Open http://localhost:8080/board-explorer-mpy.html in browser
   - Should see "Initializing PyScript..." message
   - Wait ~30s for database to load

---

#### `test_frontend_comparison.py`
**Purpose**: Automated Playwright test for numbered parameters in production web app  
**Requirements**:
- HTTP server running on port 8080
- Playwright installed: `pip install playwright` + `playwright install chromium`

**Usage**:
```powershell
# 1. Start HTTP server in separate terminal
python -m http.server 8080

# 2. Run test in another terminal
python test_frontend_comparison.py
```

**What it tests**:
- Database loads successfully in PyScript environment
- Board selection works (ESP32 v1.26.0 vs STM32 v1.26.0)
- Comparison executes without JavaScript errors
- Statistics match expected values:
  - Level 1: 26/44/3 modules
  - Level 2: 34/24 classes
  - Level 3: 207/291 methods

**Expected output**:
```
✅✅✅ TEST PASSED: Numbered parameters work correctly!
   ✅ level1_unique1: expected=26, actual=26
   ✅ level1_unique2: expected=3, actual=3
   ✅ level1_common: expected=44, actual=44
   ✅ level2_classes1: expected=34, actual=34
   ✅ level2_classes2: expected=24, actual=24
   ✅ level3_methods1: expected=207, actual=207
   ✅ level3_methods2: expected=291, actual=291
   ✅ No JavaScript errors
```

---

#### `test_simple_frontend.py`
**Purpose**: Minimal test to verify page loads and database initializes  
**Requirements**: Same as test_frontend_comparison.py

**Usage**:
```powershell
python test_simple_frontend.py
```

**What it tests**:
- Page loads without errors
- Database initializes successfully
- No JavaScript errors during initialization

---

### 3. Manual Browser Testing (Recommended for verification)

While automated tests validate functionality, manual testing confirms user experience:

1. **Start HTTP Server**: `python -m http.server 8080`

2. **Open Browser**: http://localhost:8080/board-explorer-mpy.html?view=compare

3. **Wait for Database**: ~30 seconds for "Loaded database. Application ready!" message

4. **Test Comparison**:
   - Board 1 Version: `v1.26.0`
   - Board 1: `esp32_generic`
   - Board 2 Version: `v1.26.0`
   - Board 2: `stm32`
   - Click "Compare Boards"

5. **Verify Statistics** (should appear within 10 seconds):
   ```
   Level 1: Modules       26 unique    44    3 unique
   Level 2: Classes       34           0 differ    24
   Level 2: Functions     4            —     4
   Level 2: Constants     59           —     3
   Level 3: Methods       207          12 differ   291
   Level 3: Attributes    76           —     134
   ```

6. **Check Console** (F12 → Console tab):
   - Should see "Database ready! Found 38 boards."
   - Should see "Comparing boards: esp32_generic (v1.26.0) vs stm32 (v1.26.0)"
   - **No red error messages**

---

## MCP Playwright Server Testing (Alternative to automated scripts)

If Playwright scripts fail due to environment issues, use the MCP Playwright server directly:

### Available MCP Tools
The repository includes a Playwright MCP server that can be controlled via tools:
- `mcp_microsoft_pla_browser_navigate` - Navigate to URL
- `mcp_microsoft_pla_browser_click` - Click elements
- `mcp_microsoft_pla_browser_type` - Fill inputs
- `mcp_microsoft_pla_browser_wait_for` - Wait for conditions
- `mcp_microsoft_pla_browser_snapshot` - Get page structure
- `mcp_microsoft_pla_browser_console_messages` - Check for errors

### Example MCP Testing Workflow
```python
# 1. Navigate to compare page
mcp_microsoft_pla_browser_navigate(url="http://localhost:8080/board-explorer-mpy.html?view=compare")

# 2. Wait for database load (90s timeout)
mcp_microsoft_pla_browser_wait_for(time=10)

# 3. Fill board selections
mcp_microsoft_pla_browser_type(element="Board 1 Version", ref="e37", text="v1.26.0")
mcp_microsoft_pla_browser_type(element="Board 1", ref="e40", text="esp32_generic")
mcp_microsoft_pla_browser_type(element="Board 2 Version", ref="e44", text="v1.26.0")
mcp_microsoft_pla_browser_type(element="Board 2", ref="e47", text="stm32")

# 4. Click compare
mcp_microsoft_pla_browser_click(element="Compare Boards button", ref="e54")

# 5. Wait for results
mcp_microsoft_pla_browser_wait_for(time=15)

# 6. Check console for errors
mcp_microsoft_pla_browser_console_messages(onlyErrors=true)
```

---

## Troubleshooting

### HTTP Server Issues
**Problem**: "Connection refused" or timeout errors  
**Solution**:
1. Check if server is running: `netstat -an | findstr 8080`
2. Restart server: `Ctrl+C` then `python -m http.server 8080`
3. Try different port: `python -m http.server 8081` (update test URLs)

### Database Loading Issues
**Problem**: "Database not found" or infinite loading  
**Solution**:
1. Verify `board_comparison.db` exists in frontend directory
2. Check file size: Should be ~27-28 MB
3. Clear browser cache: `Ctrl+Shift+Delete` → Clear cache
4. Check browser console for specific error messages

### Playwright Installation Issues
**Problem**: "Playwright not installed" or "Browser not found"  
**Solution**:
```powershell
pip install playwright
playwright install chromium
```

### Test Timeout Issues
**Problem**: Test times out waiting for elements  
**Solution**:
1. PyScript initialization can take 30+ seconds on first load
2. Increase timeouts in test scripts if needed
3. Use `domcontentloaded` instead of `networkidle` for faster page loads
4. Check that correct element IDs are used (inspect page HTML)

---

## Test Coverage Summary

| Test | Python sqlite3 | PyScript SQL.js | Browser UI | Numbered Params |
|------|----------------|-----------------|------------|-----------------|
| test_performance.py | ✅ | ❌ | ❌ | ✅ |
| compare_esp32_stm32.py | ✅ | ❌ | ❌ | ✅ |
| test_frontend_comparison.py | ❌ | ✅ | ✅ | ✅ |
| test_simple_frontend.py | ❌ | ✅ | ✅ | ❌ |
| Manual Browser Testing | ❌ | ✅ | ✅ | ✅ |
| MCP Playwright Server | ❌ | ✅ | ✅ | ✅ |

**Recommendation**: Run all three test types:
1. Python tests (fast, no dependencies)
2. Automated browser tests (validates full stack)
3. Manual browser testing (confirms UX)

---

## Sprint 4.5 Validation

The numbered parameters optimization (Sprint 4.5 Task 4.5.3) was validated using:

1. ✅ **Python Environment**: `test_performance.py` - All 4 scenarios pass
2. ✅ **Standalone Script**: `compare_esp32_stm32.py` - Correct output
3. ✅ **Production Web App**: MCP Playwright - Statistics match, zero errors

**Conclusion**: Numbered parameters work correctly in all environments (Python sqlite3, PyScript SQL.js, browser runtime).
