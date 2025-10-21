# MicroPython Board Explorer - PyScript Refactoring Plan

## Current Code Analysis

The current `main.py` file is a monolithic 3,612-line PyScript application with three main functional areas:

1. **Board Explorer** - Single board module tree browsing
2. **Compare Boards** - Side-by-side board comparison with diff capabilities  
3. **Search APIs** - Cross-board API search functionality

Additional supporting functionality includes:
- HTML template management
- Database access utilities
- URL state management
- Event handling
- UI components (dropdowns, trees, etc.)

## Refactoring Strategy

### Goals
- **Maintainability**: Break down monolithic code into focused modules
- **Testability**: Enable unit testing of individual components via MCP servers
- **Reusability**: Create shared utilities and components
- **Separation of Concerns**: Clear boundaries between UI, data, and business logic
- **PyScript Compatibility**: Maintain full PyScript functionality

### Module Structure (6 Modules Total)

```
frontend/
├── main.py                    # Application entry point & coordination (1)
├── database.py               # Database connection & query utilities (2)
├── ui_manager.py             # Templates, events, navigation, components (3) 
├── explorer.py               # Board Explorer functionality (4)
├── compare.py                # Board comparison functionality (5)
├── search.py                 # API search functionality (6)
├── sqlite_wasm.py            # SQLite wrapper (already exists - keep as is)
└── tests/                    # Testing (separate from application modules)
    ├── test_explorer.py
    ├── test_compare.py  
    ├── test_search.py
    ├── test_database.py
    ├── test_ui_manager.py
    └── test_integration.py
```

## Detailed Refactoring Tasks (6 Modules)
note that pyscript requires the files/modules to be added to pyscript.toml

### Phase 1: Database Layer (Priority: High)

#### Task 1.1: Create Database Module  
**File**: `database.py`
**Purpose**: All database operations, state management, and board utilities
**Dependencies**: None (imports sqlite_wasm)
**Testing**: Database query validation via MCP data store connections

```python
# Consolidate all database functionality:
# - Global app_state dictionary (SQL, db, boards, current_board)
# - Global comparison_data dictionary  
# - Global U_MODULES constant
# - load_database()
# - load_board_list_from_db()  
# - get_board_modules()
# - get_module_classes(), get_class_methods(), get_method_parameters()
# - get_class_bases(), get_class_attributes()
# - get_module_functions(), get_module_constants()
# - All search-related database queries
# - All comparison database queries
# 
# Board utility functions (from board_utils.py):
# - format_board_name() - consolidate with duplicate in main.py
# - find_board_in_list()
# - get_icon_class() - merge with get_entity_icon() from main.py
```

### Phase 2: UI Infrastructure (Priority: High)

#### Task 2.1: Create UI Manager Module
**File**: `ui_manager.py`
**Purpose**: All UI operations - templates, events, navigation, components
**Dependencies**: `database.py`, page modules (circular - needs careful handling)
**Testing**: UI interaction validation via MCP browser automation

```python
# Consolidate all UI functionality:
# - Template functions: get_template(), populate_template(), show_loading(), show_error(), show_message()
# - Template creators: create_module_item(), create_class_item(), create_function_item(), etc.
# - Event handling: setup_event_handlers() and all event handler functions
# - Navigation: switch_page(), populate_board_selects()
# - URL management: update_*_url(), share_*(), populate_*_from_url()
# - Components: make_dropdown_searchable(), initialize_searchable_dropdowns()
# - Status: update_status()
# - Tree rendering: render_module_tree_dom(), toggle_module(), toggle_class()
```

### Phase 3: Page Modules (Priority: Medium)

#### Task 3.1: Explorer Module
**File**: `explorer.py`
**Purpose**: Board exploration functionality
**Dependencies**: `database.py`, `ui_manager.py`
**Testing**: Explorer functionality tests via MCP browser automation

```python
# Extract explorer-specific functions:
# - load_board_details() 
# - Explorer-specific logic and utilities
# - Board detail rendering logic
# - Module tree population for single board
```

#### Task 3.2: Compare Module  
**File**: `compare.py`
**Purpose**: Board comparison functionality  
**Dependencies**: `database.py`, `ui_manager.py`
**Testing**: Comparison logic validation

```python
# Extract comparison functions:
# - compare_boards()
# - compare_module_contents(), compare_class_contents() 
# - filter_module_to_show_differences(), filter_class_to_show_differences()
# - calculate_comparison_stats()
# - update_comparison()
# - All comparison-specific logic
```

#### Task 3.3: Search Module
**File**: `search.py`  
**Purpose**: API search functionality
**Dependencies**: `database.py`, `ui_manager.py`
**Testing**: Search functionality tests

```python
# Extract search functions:
# - search_apis()
# - perform_search()
# - enhance_results_with_children(), group_results_hierarchically()  
# - convert_search_results_to_tree_format()
# - display_search_results()
# - create_search_result_item(), get_entity_icon()
# - All search result helper functions
# - Search-specific navigation (open_search_result, highlight_search_target)
```

### Phase 4: Main Application (Priority: Low)

#### Task 4.1: Simplify Main Entry Point
**File**: `main.py` (dramatically simplified)
**Purpose**: Application initialization and coordination only
**Dependencies**: All other modules
**Testing**: Integration tests via MCP browser automation

```python
# Minimal main.py structure:
# - Import all modules  
# - Initialize database
# - Set up UI manager
# - Initialize page modules
# - Start application (main() function)
# - Handle initial URL routing
```

## Testing Strategy with MCP Servers

### 1. Database Testing via MCP Data Store
- **Server**: `mcp_data_store_*` tools
- **Coverage**: All database query functions
- **Approach**: 
  - Connect to SQLite database via MCP
  - Validate query results against expected schemas
  - Test edge cases and error handling

### 2. Browser Automation Testing  
- **Server**: `mcp_microsoft_pla_browser_*` tools
- **Coverage**: UI interactions, navigation, event handling
- **Approach**:
  - Navigate to PyScript application
  - Test page switching functionality  
  - Validate form interactions
  - Test search and comparison workflows
  - Screenshot comparisons for visual validation

### 3. Code Structure Validation
- **Server**: `mcp_pylance_mcp_s_*` tools  
- **Coverage**: Import structure, syntax validation, type checking
- **Approach**:
  - Validate import dependencies
  - Check for syntax errors after refactoring
  - Ensure type consistency
  - Validate module boundaries

### 4. Integration Testing
- **Server**: Multiple MCP servers combined
- **Coverage**: End-to-end workflows
- **Approach**:
  - Load application via browser automation
  - Execute database queries via data store MCP
  - Validate complete user workflows

## Implementation Timeline (Simplified)

### Sprint 1: Database Layer
- [ ] Task 1.1: Create `database.py` - Extract all database operations, app state, and board utilities
- [ ] Consolidate `board_utils.py` functions into `database.py` (eliminate duplication)
- [ ] Test database connectivity via MCP data store
- [ ] Validate all database queries work from new module

### Sprint 2: UI Infrastructure  
- [ ] Task 2.1: Create `ui_manager.py` - Consolidate all UI operations
- [ ] Test template rendering and event handling via browser MCP
- [ ] Validate navigation and component functionality

### Sprint 3: Page Modules
- [ ] Task 3.1: Create `explorer.py` - Board exploration functionality
- [ ] Task 3.2: Create `compare.py` - Board comparison functionality  
- [ ] Task 3.3: Create `search.py` - API search functionality
- [ ] Test each page module individually

### Sprint 4: Integration & Main App
- [ ] Task 4.1: Simplify `main.py` - Application coordination only
- [ ] Resolve any circular dependencies between modules
- [ ] Comprehensive integration testing via MCP browser automation
- [ ] Performance validation

### Sprint 5: Testing & Polish
- [ ] Complete test suite via MCP servers
- [ ] Browser compatibility testing across the 6-module structure
- [ ] Documentation updates for new architecture
- [ ] Performance comparison with original monolith

## Migration Strategy

### 1. Incremental Approach
- Extract one module at a time
- Maintain working application at each step  
- Test each extraction before proceeding

### 2. Backwards Compatibility
- Keep original `main.py` as `main_legacy.py` during migration
- Use feature flags to toggle between old/new implementations
- Gradual migration of functionality

### 3. PyScript Considerations  
- Ensure all modules are PyScript-compatible
- Test import mechanisms work in browser environment
- Validate async/await functionality across modules
- Test JavaScript interop from modular code

## Risk Mitigation

### 1. PyScript Import Issues
- **Risk**: Module imports may not work in PyScript environment
- **Mitigation**: Test imports early, use relative imports, maintain flat structure if needed

### 2. Circular Dependencies
- **Risk**: `ui_manager.py` needs page modules, but page modules need `ui_manager.py`
- **Mitigation**: Use late imports within functions, or pass UI functions as parameters to page modules

### 3. JavaScript Interop
- **Risk**: JavaScript integration may break across modules
- **Mitigation**: Centralize JS interop, test thoroughly with MCP browser automation

### 4. Performance Impact
- **Risk**: Multiple modules may impact load time
- **Mitigation**: Monitor bundle size, lazy loading where possible, performance testing

## Success Criteria

### Functional Requirements
- [ ] All existing functionality preserved
- [ ] No regression in user experience  
- [ ] PyScript compatibility maintained
- [ ] Database functionality intact

### Quality Requirements  
- [ ] Code coverage >80% via MCP testing
- [ ] No circular dependencies
- [ ] Clear module boundaries
- [ ] Documented interfaces

### Performance Requirements
- [ ] Load time within 10% of original
- [ ] Runtime performance maintained
- [ ] Memory usage not significantly increased

## Module Responsibility Summary

| Module | Lines (Est.) | Primary Responsibility | Key Dependencies |
|--------|-------------|----------------------|------------------|
| `database.py` | ~850 | All database operations, app state, constants, board utilities | sqlite_wasm |
| `ui_manager.py` | ~1200 | Templates, events, navigation, components | database, pages (late import) |
| `explorer.py` | ~400 | Board exploration functionality | database, ui_manager |  
| `compare.py` | ~800 | Board comparison functionality | database, ui_manager |
| `search.py` | ~600 | API search functionality | database, ui_manager |
| `main.py` | ~200 | Application initialization and coordination | All modules |
| **Total** | **~4050** | **Original: 3612 + 100 (board_utils) = 3712 lines** | |

## Post-Refactoring Benefits

### Development
- **Maintainability**: 6 focused modules instead of 1 monolith (3600+ lines)
- **Testing**: Comprehensive test coverage via MCP servers for each module 
- **Debugging**: Isolated functionality easier to troubleshoot
- **Clear Boundaries**: Each module has a single, well-defined responsibility

### Future Enhancements  
- **New Pages**: Easy to add new page modules following the established pattern
- **UI Improvements**: All UI logic centralized in `ui_manager.py`
- **Database Changes**: All database operations isolated in `database.py`
- **Team Development**: 6 modules allow parallel development without conflicts

## Conclusion

This **6-module refactoring plan** strikes the right balance between the original monolith and over-fragmentation. Each module has a clear, substantial responsibility:

1. **`database.py`** - Data layer, application state, and board utilities (consolidates board_utils.py)
2. **`ui_manager.py`** - All user interface operations  
3. **`explorer.py`** - Board exploration page
4. **`compare.py`** - Board comparison page
5. **`search.py`** - API search page
6. **`main.py`** - Application coordination

**Note**: The existing `board_utils.py` will be consolidated into `database.py` to eliminate duplication and better organize utility functions. The `sqlite_wasm.py` module remains unchanged as an external dependency wrapper.

The structure maintains PyScript compatibility while dramatically improving maintainability and testability. The use of MCP servers ensures comprehensive validation throughout the refactoring process, providing confidence in the migration while establishing a robust testing foundation.

This approach transforms a 3600+ line monolith into 6 manageable, well-defined modules that preserve all existing functionality while enabling future enhancements and team development.