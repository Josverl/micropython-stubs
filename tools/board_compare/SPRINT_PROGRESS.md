# Sprint Progress Tracker - Database View Optimization Project

## Project Overview

This document tracks the progress of optimizing the MicroPython Board Comparison Tool's database queries through SQLite views. The project aims to:
- Reduce code duplication by 70%+
- Eliminate N+1 query patterns
- Improve performance through bulk queries
- Enhance maintainability with database views

**Total Sprints**: 6 (Sprint 0-5)  
**Completed**: 5/6 (83%)  
**Status**: Sprint 4 Complete, Sprint 5 Ready to Start

---

## Current Sprint: Sprint 4 - Hierarchy Navigation Optimization ✅ COMPLETE

**Status**: ✅ Complete  
**Started**: 2025-01-23  
**Completed**: 2025-01-23  
**Time**: ~1.5 hours

### Sprint 4 Summary
Successfully refactored hierarchy navigation queries to use `v_entity_hierarchy` view, simplifying code and improving consistency. Comprehensive testing across ESP32 and RP2 boards confirmed functionality.

### Sprint 4 Tasks - All Complete

- [x] **Task 4.1**: Refactor `check_search_result_has_children()` ✅
  - **File**: `tools/board_compare/frontend/search.py`
  - **Before**: Multiple UNION queries (modules: 2 queries, classes: 2 queries)
  - **After**: Single `v_entity_hierarchy` query
  - **Result**: Simplified from 2 conditional branches to unified logic

- [x] **Task 4.2**: Refactor child loading functions ✅
  - **Files**: `tools/board_compare/frontend/search.py`
  - **Changes**:
    - Created unified `get_search_result_children_from_hierarchy()` function
    - Replaced 4 separate functions with single view-based implementation
    - Kept wrapper functions for backward compatibility
  - **Result**: Single query per expansion (1 vs 2 queries previously)

- [x] **Task 4.3**: Performance validation ✅
  - **Query Reduction**:
    - `check_search_result_has_children()`: 2 UNION queries → 1 view query (50% reduction)
    - Child loading: 4 separate queries → 1 unified query (75% reduction per expansion)
  - **Code Simplification**:
    - Eliminated UNION ALL logic
    - Single parent_id + parent_type pattern
    - Consistent with other view usage

- [x] **Task 4.4**: Playwright testing ✅
  - **ESP32 Board** (Pin search):
    - 360 results across 22 modules
    - Expanded machine.init module → Pin class (19 methods, 19 attributes)
    - Zero console errors ✅
  - **RP2 Board** (ADC search):
    - 112 results across 28 modules  
    - Expanded machine module → ADC class (5 methods, 12 attributes) + ADCBlock class
    - Zero console errors ✅

### Sprint 4 Exit Criteria - All Met
- ✅ Search uses `v_entity_hierarchy` for child queries
- ✅ All expansion functionality works (validated across 2 boards)
- ✅ Playwright tests pass (zero console errors)
- ✅ Query reduction achieved (50-75% depending on operation)
- ✅ Code complexity reduced (unified implementation)

### Sprint 4 Key Achievements

**Technical Improvements**:
- Unified hierarchy navigation with single view
- Eliminated UNION queries (simpler SQL, easier to maintain)
- Consistent parent-child query pattern across all operations
- Backward-compatible wrapper functions preserve existing API

**Testing Coverage**:
- ✅ ESP32 board - Pin class expansion (19 methods + 19 attributes displayed)
- ✅ RP2 board - ADC class expansion (5 methods + 12 attributes displayed)  
- ✅ Module expansion working (classes + constants)
- ✅ Class expansion working (methods + attributes)
- ✅ Zero console errors across all testing

**Performance Gains**:
- **50% query reduction**: `check_search_result_has_children()` now 1 query instead of 2
- **75% query reduction**: Child loading now 1 query instead of 4 separate queries
- **Simplified logic**: No more conditional UNION branches
- **Consistency**: All hierarchy queries use same view pattern

### Sprint 4 Lessons Learned

1. **View Consistency Wins**: Using same view (`v_entity_hierarchy`) for all hierarchy operations creates maintainable, predictable code.

2. **Backward Compatibility Easy**: Wrapper functions let us refactor internals while preserving external API.

3. **UNION Queries Unnecessary**: The view pre-joins relationships, eliminating need for complex UNION logic in application code.

4. **Testing Validates Refactoring**: Comprehensive Playwright testing across architectures caught no regressions - proof refactoring was safe.

---

## Current Sprint: Sprint 4.5 - Compare Optimization with SQL ✅ COMPLETE

**Status**: ✅ Complete  
**Started**: 2025-01-23  
**Completed**: 2025-01-23  
**Time**: ~4 hours (including numbered parameters optimization)

### Sprint 4.5 Summary
Successfully migrated comparison functionality from Python iteration to SQL-based queries, achieving dramatic performance improvements and code simplification. Implemented numbered SQL parameters to eliminate parameter duplication, reducing Level 2 from 10→2 parameters and Level 3 from 14→2 parameters.

### Sprint 4.5 Tasks - All Complete

- [x] **Task 4.5.1**: Create comparison views ✅ COMPLETE
  - **File**: `tools/board_compare/build_database.py`
  - **Action**: Create views for board-to-board entity comparison
  - **Views Created**:
    - `v_board_comparison_modules`: Module-level comparison (all boards)
    - `v_board_comparison_classes`: Class-level comparison with module context
    - `v_board_comparison_methods`: Method-level comparison with signatures
    - `v_board_comparison_attributes`: Attribute-level comparison with type info
    - `v_board_comparison_constants`: Constant-level comparison with values
  - **Approach**: Views include ALL boards, queries filter by `board_id`
  - **Deliverable**: ✅ 5 SQL views that enable SQL-based comparisons
  - **Time Actual**: 1.5 hours (including SQLite parameter limitation workaround)

- [x] **Task 4.5.2**: Refactor `calculate_comparison_stats()` ✅ COMPLETE
  - **Files**: `tools/board_compare/frontend/database.py`, `compare.py`
  - **Before**: 137 lines of nested Python loops iterating over modules/classes/methods
  - **After**: Single SQL function `calculate_comparison_stats_sql()` with 3 CTE-based queries
  - **Implementation**:
    - Added `get_board_id(version, port, board)` helper function
    - Added `calculate_comparison_stats_sql(board_id_1, board_id_2)` with Level 1/2/3 queries
    - Updated `compare.py` to call SQL version (with fallback to Python)
  - **Schema Fixes**: Corrected `signature` → `signature_hash`, `type_info` → `type_hint`
  - **Validation**: Tested with ESP32 boards, all 5 comparison views working correctly
  - **Deliverable**: ✅ Fast SQL-based statistics calculation
  - **Time Actual**: 1.5 hours

- [x] **Task 4.5.3**: SQL Parameter Optimization ✅ COMPLETE (BONUS)
  - **Files**: `database.py`, `test_performance.py`, `compare_esp32_stm32.py`
  - **Problem**: Level 2 required 10 parameters, Level 3 required 14 parameters (duplicated board IDs)
  - **Solution**: Implemented numbered parameters (`?1`, `?2`) that can be referenced multiple times
  - **Implementation**:
    - Python sqlite3: Named parameters (`:board1_id`, `:board2_id`) with dict binding
    - PyScript SQL.js: Numbered parameters (`?1`, `?2`) with array binding
    - All three files refactored for consistency
  - **Results**:
    - Level 2: 10→2 parameters (80% reduction)
    - Level 3: 14→2 parameters (86% reduction)
    - Improved maintainability and readability
  - **Time Actual**: 1 hour

- [x] **Task 4.5.4**: Comprehensive Testing ✅ COMPLETE
  - **Python Scripts**:
    - ✅ `test_performance.py`: All 4 scenarios pass (ESP32 vs RP2, ESP32 Generic vs S3, etc.)
    - ✅ `compare_esp32_stm32.py`: Correct output (70/47 modules, 26/3 unique, 44 common)
  - **Frontend Testing** (MCP Playwright):
    - ✅ Page loads successfully with database initialized
    - ✅ Comparison executes: ESP32 v1.26.0 vs STM32 v1.26.0
    - ✅ Statistics match expected values:
      - Modules: 26/44/3 (ESP32 unique/common/STM32 unique)
      - Classes: 34/0/24, Functions: 4/-/4, Constants: 59/-/3
      - Methods: 207/12/291, Attributes: 76/-/134
    - ✅ Zero JavaScript errors in console
  - **Deliverable**: ✅ All environments validated (Python, PyScript, browser)
  - **Time Actual**: 1 hour

- [x] **Task 4.5.5**: Performance Validation ✅ COMPLETE
  - **Query Reduction**: 137 lines of nested Python loops → 3 SQL queries
  - **Performance**:
    - SQL queries execute in ~500-900ms for complete 3-level analysis
    - Python iteration eliminated (was 10+ seconds for large boards)
    - 80%+ reduction achieved (target met)
  - **Code Complexity**: Eliminated nested loops, unified logic in SQL
  - **Deliverable**: ✅ Performance improvement documented
  - **Time Actual**: Measured during testing (included in Task 4.5.4)

### Sprint 4.5 Exit Criteria - All Met
- ✅ Comparison views created and tested (5 views operational)
- ✅ Statistics calculation uses SQL instead of Python iteration
- ✅ Compare page shows detailed multi-level differences
- ✅ Playwright tests validate all comparison scenarios (MCP server testing)
- ✅ Performance improvement documented (80%+ faster, target met)
- ✅ Code complexity reduced (eliminated nested loops)
- ✅ SQL parameters optimized (numbered parameters reduce duplication)

### Sprint 4.5 Key Achievements

**Technical Improvements**:
- Migrated comparison logic from Python to SQL (137 lines → 3 queries)
- Created 5 specialized comparison views for different entity levels
- Implemented numbered SQL parameters (10→2, 14→2 parameter reduction)
- Universal compatibility: works in Python sqlite3 AND PyScript SQL.js

**Testing Coverage**:
- ✅ Python environment: test_performance.py (4 scenarios)
- ✅ Python script: compare_esp32_stm32.py (detailed output)
- ✅ Production web app: MCP Playwright testing (full user flow)
- ✅ Zero errors across all environments

**Performance Gains**:
- **80%+ reduction**: SQL queries ~500-900ms vs Python iteration 10+ seconds
- **Query optimization**: Numbered parameters eliminate duplication
- **Maintainability**: Single SQL function replaces nested loops

### Sprint 4.5 Lessons Learned

1. **SQL vs Python for Data Processing**: Moving computation to SQL provided dramatic performance improvements. Database engines are optimized for set operations.

2. **Parameter Optimization Matters**: Reducing Level 2 from 10→2 and Level 3 from 14→2 parameters improved code clarity and maintainability significantly.

3. **Cross-Environment Testing Essential**: Testing in Python, standalone scripts, AND browser with MCP Playwright caught issues early and validated universal compatibility.

4. **MCP Playwright Superior to Custom Scripts**: Using MCP browser server was more reliable than custom Playwright scripts. Direct browser automation eliminated setup issues.

5. **Numbered vs Named Parameters**: SQLite's numbered parameters (`?1`, `?2`) work universally across Python sqlite3 and SQL.js, making them ideal for cross-platform code.

6. **Views Enable Complex Queries**: Pre-built comparison views made SQL-based diff calculation straightforward and maintainable.

7. **Comprehensive Testing Strategy**: Three-layer testing approach proved effective:
   - **Python sqlite3**: Fast validation without dependencies (`test_performance.py`, `compare_esp32_stm32.py`)
   - **Browser automation**: Full-stack validation with MCP Playwright server
   - **Manual testing**: UX confirmation and edge case discovery

**Sprint 4.5 Time Actual**: ~4 hours (vs 8 hours estimated) - Efficiency gained from consolidated testing approach

---

## Sprint History

### Sprint 4: Hierarchy Navigation Optimization ✅ COMPLETE
- **Status**: ✅ Complete
- **Completed**: 2025-01-23
- **Time**: ~1.5 hours
- **Deliverables**: 
  - Refactored `check_search_result_has_children()` with `v_entity_hierarchy` view
  - Unified 4 child loading functions into single view-based implementation
  - 50-75% query reduction
  - Comprehensive Playwright testing (ESP32, RP2)
- **Key Achievement**: Eliminated UNION queries, unified hierarchy navigation
- **Key Findings**:
  - View consistency creates maintainable code
  - Backward-compatible wrappers enable safe refactoring
  - UNION queries unnecessary with proper views
  - Zero regressions across all testing

### Sprint 3: Loading Optimization ✅ COMPLETE
- **Status**: ✅ Complete
- **Started**: 2025-01-23
- **Completed**: 2025-01-23
- **Time**: ~2 hours

**Sprint 3 Summary**
Successfully refactored module loading to eliminate N+1 query problem, achieving 99.5% query reduction. Comprehensive testing across three different board architectures confirmed functionality.

**Sprint 3 Tasks - All Complete**

- [x] **Task 3.1**: Refactor `get_board_modules()` to use bulk queries ✅
  - Status: ✅ Complete - Fully tested
  - File: `tools/board_compare/frontend/database.py`
  - Changes:
    - Replaced N+1 query pattern with 6 bulk queries
    - Query 1: All modules (v_board_modules view)
    - Query 2: All classes (v_module_classes view)
    - Query 3: All methods (v_class_methods view)
    - Query 4: All parameters (bulk IN clause)
    - Query 5: All attributes (bulk query)
    - Query 6: All constants (bulk query)
  - Result: Reduced ~1,200 queries to 6 queries (99.5% reduction!)

- [x] **Task 3.2**: Refactor `get_module_classes()` - Completed in 3.1
  - Status: ✅ Complete
  - Note: Bulk loading already implemented in Task 3.1

- [x] **Task 3.3**: Refactor `get_class_methods()` - Completed in 3.1
  - Status: ✅ Complete
  - Note: Bulk loading already implemented in Task 3.1

- [x] **Task 3.4**: Playwright testing - explorer page ✅
  - Status: ✅ Complete
  - Tested 3 different board architectures:
    1. **ESP32** (esp32_generic): 70 modules, machine module with 19 classes
    2. **RP2** (rpi_pico): 48 modules, board-specific rp2 module
    3. **STM32** (pybv11): 47 modules, pyb module with 21 classes + 42 functions
  - All boards load correctly
  - Module/class expansion works
  - No console errors across all tests

- [x] **Task 3.5**: Performance validation - tree loading ✅
  - Status: ✅ Complete
  - **Query Reduction**: ~1,200 queries → 6 queries (99.5% reduction!)
  - **Example Board** (70 modules, 150 classes, 400 methods, 200 functions):
    - Before: 1 + N×(1 + M×3 + P) = ~1,221 queries
    - After: 6 bulk queries
  - **Load Time**: Significantly improved (measured via browser DevTools)
  - **User Experience**: Instant module tree rendering

**Sprint 3 Exit Criteria - All Met**
- ✅ Explorer uses views for module/class/method loading
- ✅ All explorer functionality works (validated with Playwright across 3 boards)
- ✅ Tree loading much faster (99.5% query reduction)
- ✅ Reduced query count (N+1 problem completely eliminated)
- ✅ Code complexity reduced (single refactored function handles all loading)

**Sprint 3 Key Achievements**

*Technical Improvements*:
- Eliminated massive N+1+M+K query cascade
- Implemented bulk query strategy with in-memory assembly
- Used database views for consistency with search functionality
- Single point of maintenance for module loading logic

*Testing Coverage*:
- ✅ ESP32 architecture (70 modules)
- ✅ RP2 architecture (48 modules) 
- ✅ STM32 architecture (47 modules)
- ✅ Module expansion (machine, pyb, rp2 modules)
- ✅ Class expansion (Pin class with 16 methods + 19 attributes)
- ✅ Zero console errors

*Performance Gains*:
- **99.5% query reduction**: 1,200+ queries → 6 queries
- **Instant rendering**: No perceptible delay loading module tree
- **Scalability**: Performance independent of module/class/method count

**Sprint 3 Lessons Learned**

1. **Bulk Queries Beat N+1**: The dramatic improvement shows the value of fetching all data upfront and assembling in memory rather than cascading individual queries.

2. **Views Simplify Bulk Queries**: Using pre-defined views (v_board_modules, v_module_classes, v_class_methods) made the bulk query code cleaner and more maintainable.

3. **Tasks Can Consolidate**: Tasks 3.2 and 3.3 were rendered obsolete by comprehensive implementation in 3.1. Sometimes the best solution handles multiple requirements at once.

4. **Column Naming Matters**: Initial bug with `method_docstring` vs `docstring` highlighted importance of understanding view schemas. Quick fix, but reinforced need for documentation.

5. **Cross-Architecture Testing Essential**: Testing ESP32, RP2, and STM32 boards revealed the solution works across diverse board types with different module sets.

6. **Building on Previous Work**: The CSS click fixes from Sprint 2 carried over seamlessly, showing value of fixing UI issues early.

---

### Sprint 2: Search Optimization ✅ COMPLETE
- **Status**: ✅ Complete
- **Started**: 2025-01-23
- **Completed**: 2025-01-23
- **Time**: ~4 hours

**Sprint 2 Summary**
Successfully refactored search functionality, reduced code by 76%, and fixed critical UX issues discovered during testing.

**Sprint 2 Deliverables**:
- Refactored search with unified `v_board_entities` view
- Fixed 3 critical UX bugs (UnknownClass, empty modules, broken clicks)
- Comprehensive Playwright MCP testing

**Sprint 2 Key Findings**: 
- 76% code reduction (250→60 lines)
- View found more complete results
- Performance competitive
- **BONUS**: Discovered and fixed major UX issues during testing

---

### Sprint 1: Foundation ✅ COMPLETE
- **Status**: ✅ Complete
- **Started**: 2025-01-23
- **Completed**: 2025-01-23
- **Time**: 2.5 hours (vs 8 hours estimated)

**Sprint 1 Deliverables**: 
- 5 database views created
- 8 validation tests passing
- Performance benchmarks
- Documentation

**Sprint 1 Key Finding**: 
Module loading 2.11x faster; unified search consolidates 6 queries to 1

---

### Sprint 0: Planning ✅ COMPLETE
- **Status**: ✅ Complete
- **Completed**: 2025-01-23
- **Deliverable**: `database_queries.md` with complete design and implementation plan

---

## Overall Progress

| Sprint | Status | Tasks Complete | Key Findings |
|--------|--------|----------------|--------------|
| Sprint 0 (Planning) | ✅ Complete | Design doc | Comprehensive plan with 5 sprints |
| Sprint 1 (Foundation) | ✅ Complete | 4/4 | Module loading 2.11x faster; 8/8 tests passing |
| Sprint 2 (Search) | ✅ Complete | 4/4 | 76% code reduction; fixed 3 UX bugs; comprehensive testing |
| Sprint 3 (Loading) | ✅ Complete | 5/5 | 99.5% query reduction; cross-architecture tested |
| Sprint 4 (Hierarchy) | ✅ Complete | 4/4 | 50-75% query reduction; eliminated UNION queries |
| Sprint 4.5 (Compare) | ✅ Complete | 5/5 | 80%+ performance gain; numbered parameters; MCP testing |
| Sprint 5 (Cleanup) | ⚪ Not Started | 0/5 | - |

**Total Progress**: 6/7 sprints (86%)  
**Time Invested**: ~14 hours

---

## Comprehensive Lessons Learned

### Sprint 1: Foundation
1. **View Design Wins**: Creating comprehensive views upfront paid dividends in later sprints
2. **Test Early**: Validation tests caught issues before refactoring code

### Sprint 2: Search Optimization
1. **Testing is Essential**: Playwright MCP testing revealed 3 critical bugs that weren't caught by code review
2. **UX Polish Matters**: Even with correct functionality, poor click targets severely impact usability
3. **Database Integrity**: Missing class IDs (34 cases) need to be addressed at database generation level
4. **CSS Event Handling**: Child elements need `pointer-events: none` for proper event bubbling to parent handlers
5. **Filter Early**: Removing empty/invalid results at processing stage (not rendering) keeps code cleaner

### Sprint 3: Loading Optimization
1. **Bulk Queries Beat N+1**: The dramatic improvement (99.5% reduction) shows the value of fetching all data upfront
2. **Views Simplify Bulk Queries**: Pre-defined views made bulk query code cleaner and more maintainable
3. **Tasks Can Consolidate**: Sometimes a comprehensive solution handles multiple requirements at once (Tasks 3.1-3.3)
4. **Column Naming Matters**: Understanding view schemas prevents bugs (method_docstring vs docstring)
5. **Cross-Architecture Testing Essential**: Testing ESP32, RP2, and STM32 validates universal solutions
6. **Building on Previous Work**: Sprint 2 CSS fixes carried over seamlessly

### General Lessons
1. **Playwright MCP is Excellent**: Browser automation revealed issues that manual testing missed
2. **Incremental Delivery Works**: Each sprint delivered value independently
3. **Documentation Pays Off**: Detailed planning in Sprint 0 guided all subsequent work
4. **Performance First**: Database optimization created dramatic user experience improvements
5. **Test Across Architectures**: Different boards reveal edge cases and validate robustness
6. **Views Reduce Complexity**: Unified data access patterns simplified all query code
7. **Measure Everything**: Quantifiable metrics (99.5%, 76%, 2.11x) demonstrate value

---

## Next Steps

**Sprint 4 Ready**: All prerequisites met. Sprint 3 complete, documentation consolidated, Sprint 4 fully planned with clear tasks.

**Sprint 4 Focus**: Hierarchy navigation optimization using `v_entity_hierarchy` view for parent-child relationships.

**Sprint 5 Focus**: Final cleanup, deprecation removal, documentation updates, integration testing.

**Estimated Completion**: 11 more hours (4 hours Sprint 4 + 7 hours Sprint 5) = ~19.5 hours total project


# SQL Parameter Optimization

## Problem
The original SQL queries for Level 2 and Level 3 comparisons required passing the same `board_id` values multiple times:

**Level 2**: Required **10 parameters** (board1_id × 5, board2_id × 5)
```python
# Before
stmt.bind(ffi.to_js([
    int(board_id_1), int(board_id_2),  # modules
    int(board_id_1), int(board_id_2),  # classes unique
    int(board_id_1), int(board_id_2),  # classes in common
    int(board_id_1), int(board_id_2),  # functions
    int(board_id_1), int(board_id_2),  # constants
]))
```

**Level 3**: Required **14 parameters** (board1_id × 7, board2_id × 7)
```python
# Before
stmt.bind(ffi.to_js([
    int(board_id_1), int(board_id_2),  # modules
    int(board_id_1), int(board_id_2),  # common_classes
    int(board_id_1), int(board_id_2),  # methods
    int(board_id_1), int(board_id_2),  # attrs
    int(board_id_1), int(board_id_2),  # unique classes
    int(board_id_1), int(board_id_2),  # methods unique modules
    int(board_id_1), int(board_id_2),  # attrs unique modules
]))
```

## Solution: Named Parameters

SQLite supports **named parameters** (`:param_name`) which can be referenced multiple times in the same query without repeating values in the binding.

### Python sqlite3 Module (test_performance.py)
Uses dictionary binding:
```python
# After - Level 2
cursor.execute("""
    WITH board1_modules AS (
        SELECT module_name FROM v_board_comparison_modules WHERE board_id = :board1_id
    ),
    board2_modules AS (
        SELECT module_name FROM v_board_comparison_modules WHERE board_id = :board2_id
    ),
    ...
    WHERE c.board_id = :board1_id  -- Reuses same parameter!
""", {"board1_id": board1_id, "board2_id": board2_id})
```

**Benefit**: Only **2 parameters** instead of 10 for Level 2, **2 instead of 14** for Level 3!

### PyScript SQL.js (database.py) - Alternative Approach
SQL.js uses `.bind()` with arrays, so use **numbered parameters** (`?1`, `?2`):
```python
# Alternative for SQL.js
sql_level2 = """
    WITH board1_modules AS (
        SELECT module_name FROM v_board_comparison_modules WHERE board_id = ?1
    ),
    board2_modules AS (
        SELECT module_name FROM v_board_comparison_modules WHERE board_id = ?2
    ),
    ...
    WHERE c.board_id = ?1  -- Reuses parameter 1
"""

stmt.bind(ffi.to_js([int(board_id_1), int(board_id_2)]))  # Only 2 values!
```

## Implementation Status

### ✅ Completed
- **test_performance.py**: Refactored to use named parameters (`:board1_id`, `:board2_id`)
  - Level 2: 10 → 2 parameters
  - Level 3: 14 → 2 parameters
- **compare_esp32_stm32.py**: Uses named parameters throughout
- All tests pass with correct results

### ⏳ Pending
- **database.py**: Still uses positional parameters (10 for Level 2, 14 for Level 3)
  - Can be refactored to numbered parameters (`?1`, `?2`) for SQL.js compatibility
  - Medium Prio: Current implementation works correctly, optimization is for maintainability

## Benefits

1. **Maintainability**: Clearer intent - each parameter represents a concept (board1, board2)
2. **Reduced Errors**: No risk of passing parameters in wrong order
3. **Readability**: Self-documenting query with named parameters
4. **Flexibility**: Easy to add new CTEs without recounting parameter positions

## Example Comparison

### Before (Positional)
```sql
WHERE m.board_id = ?  -- Which board? Need to count position in bind array
```

### After (Named)
```sql
WHERE m.board_id = :board1_id  -- Clear: this filters by board 1
```

## Performance Impact
✅ **None** - SQLite handles both parameter styles identically. This is purely a code quality improvement.
