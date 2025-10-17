# Board Comparison Tool - Architecture and Design Decisions

## Overview

The MicroPython Board Comparison Tool is designed to help developers understand API differences across various MicroPython boards and versions. This document outlines the architectural decisions, design patterns, and rationale behind key implementation choices.

## System Architecture

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    User Interface Layer                      │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │   Board      │  │   Compare    │  │   Search     │      │
│  │  Explorer    │  │   Boards     │  │    APIs      │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│                    Data Access Layer                         │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  SQL.js (In-Browser SQLite)  │  JSON API             │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│                      Data Layer                              │
│  ┌──────────────┐         ┌───────────────────────────┐    │
│  │  SQLite DB   │         │  Simplified JSON (24KB)   │    │
│  │  (4.8MB)     │         │  + Optional Detailed JSON │    │
│  └──────────────┘         └───────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
                          ↑
┌─────────────────────────────────────────────────────────────┐
│                  Data Processing Layer                       │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │ Stub Scanner │  │   Database   │  │  Export      │     │
│  │  (AST)       │  │   Builder    │  │  Engine      │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
└─────────────────────────────────────────────────────────────┘
                          ↑
┌─────────────────────────────────────────────────────────────┐
│                      Source Layer                            │
│        MicroPython Stub Files (.pyi) in publish/            │
└─────────────────────────────────────────────────────────────┘
```

## Key Design Decisions

### 1. Parser Selection: Python AST vs libcst

**Decision:** Use Python's built-in `ast` module instead of `libcst`

**Rationale:**
- **Zero external dependencies**: `ast` is part of Python's standard library
- **Sufficient for stub files**: `.pyi` files have simpler syntax than full Python code
- **Better performance**: Native C implementation is faster than pure Python libcst
- **Stability**: Standard library APIs are more stable across Python versions
- **Simplicity**: Easier to understand and maintain

**Trade-offs:**
- Less detailed CST (Concrete Syntax Tree) information
- Cannot preserve exact formatting (not needed for our use case)
- Limited to Python's supported syntax version

### 2. Database Schema Design

**Decision:** Normalized relational schema with many-to-many relationships

**Rationale:**
- **Space efficiency**: Modules/classes shared across boards stored once
- **Query performance**: Indexed relationships enable fast cross-board queries
- **Data integrity**: Foreign key constraints prevent orphaned records
- **Scalability**: Can support multiple versions without duplication

**Schema Highlights:**
```sql
boards (id, version, port, board)
modules (id, name, docstring)
board_modules (board_id, module_id)  -- Many-to-many
classes (id, module_id, name, docstring)
methods (id, module_id, class_id, name, return_type, ...)
parameters (id, method_id, name, type_hint, position, ...)
```

**Trade-offs:**
- More complex queries than flat structure
- Requires join operations for data retrieval
- Benefits far outweigh costs for this use case

### 3. Dual Export Strategy

**Decision:** Provide both simplified (24KB) and detailed (168MB) JSON exports

**Rationale:**
- **Fast initial load**: 24KB JSON loads instantly for board lists
- **On-demand details**: Database queries via SQL.js for class/method info
- **Bandwidth efficiency**: Don't download 168MB if not needed
- **Flexibility**: Simplified JSON works without SQL.js

**Implementation:**
- `export_to_json()`: Module names only (24KB)
- `export_detailed_to_json()`: Full API data (168MB) - optional
- In-browser: SQL.js queries 4.8MB database on-demand

### 4. Frontend Architecture: Multi-View SPA

**Decision:** Single-page application with three distinct views

**Rationale:**
- **Separation of concerns**: Each view has a specific purpose
- **Better UX**: No page reloads, smooth transitions
- **Code organization**: Modular JavaScript functions
- **State management**: Simple global state for selected boards

**Views:**
1. **Board Explorer**: Single board inspection
2. **Compare Boards**: Side-by-side comparison with diff mode
3. **Search APIs**: Cross-board feature discovery

### 5. SQL.js for In-Browser Queries

**Decision:** Use SQL.js to query SQLite database directly in browser

**Rationale:**
- **No backend required**: True static site hosting
- **Powerful queries**: Full SQL support for complex comparisons
- **Efficient**: Only loads 4.8MB database, not 168MB JSON
- **Familiar**: Standard SQL syntax for queries
- **Graceful degradation**: Falls back to JSON if unavailable

**Trade-offs:**
- ~500KB SQL.js library overhead
- WebAssembly requirement (modern browsers only)
- Initial database load time (~1-2 seconds)

### 6. Pydantic Models for Type Safety

**Decision:** Use Pydantic models for all data structures

**Rationale:**
- **Type validation**: Catch errors early in data processing
- **Self-documenting**: Models serve as documentation
- **IDE support**: Better autocomplete and type checking
- **Serialization**: Easy conversion to/from dictionaries and JSON
- **Consistency**: Same models used throughout the pipeline

**Models:**
```python
Parameter → Method → Class → Module → Board
```

### 7. Color-Coded Diff Visualization

**Decision:** Use color coding (green/red/yellow) for differences

**Rationale:**
- **Quick visual scanning**: Colors draw attention to differences
- **Intuitive**: Green=unique to left, Red=unique to right
- **Accessible**: Combined with text labels ([UNIQUE])
- **Standard convention**: Similar to git diff output

### 8. Expandable Tree View

**Decision:** Hierarchical tree structure for board explorer

**Rationale:**
- **Natural hierarchy**: Modules → Classes → Methods
- **Progressive disclosure**: Show details on-demand
- **Performance**: Don't render everything upfront
- **Familiar UX**: Similar to file explorers

## Data Flow

### 1. Database Building Flow

```
.pyi files → StubScanner (AST) → Pydantic Models → DatabaseBuilder → SQLite
                                                         ↓
                                              JSON Export (simplified)
                                              JSON Export (detailed - optional)
```

### 2. Frontend Data Flow

```
Page Load → Fetch JSON (24KB) → Populate Dropdowns
                ↓
User Selection → Load SQL.js → Fetch Database (4.8MB)
                ↓
User Action → SQL Query → Render Results
```

## Performance Considerations

### 1. Database Size Optimization

**Techniques:**
- Normalized schema (no duplication)
- Integer IDs instead of strings
- Indexed foreign keys
- Minimal docstring storage

**Results:**
- 20 boards, 12,144 methods = 4.8MB database
- ~240 bytes per method (including all relationships)

### 2. Frontend Loading Strategy

**Approach:**
- **Phase 1**: Load 24KB JSON (instant)
- **Phase 2**: Load SQL.js library (~500KB) in background
- **Phase 3**: Load database (4.8MB) on first interaction
- **Phase 4**: Query on-demand as user navigates

**Benefits:**
- Time to interactive: < 1 second
- Total data transfer: 5.3MB (vs 168MB for detailed JSON)
- Perceived performance: Excellent

### 3. Query Optimization

**Strategies:**
- Indexed foreign keys on all relationships
- Prepared statements for repeated queries
- Limit result sets with WHERE clauses
- Select only needed columns

## Scalability Considerations

### 1. Multiple Versions Support

**Current Design:**
- Single version per database (v1.26.0)
- Version field in boards table

**Future Extension:**
- Multiple databases (one per version)
- Version selector in UI
- Load database dynamically based on selection

### 2. Growing Board Count

**Current:** 20 boards
**Scalability:**
- Linear growth in database size
- Normalized schema prevents duplication
- Can handle 100+ boards efficiently

### 3. API Complexity Growth

**Challenge:** More classes/methods over time
**Mitigation:**
- Pagination for large result sets
- Virtual scrolling for long lists
- Lazy loading of method details

## Testing Strategy

### 1. Unit Tests

**Coverage:**
- Pydantic models validation
- AST parsing edge cases
- Database operations (CRUD)
- JSON export/import

### 2. Integration Tests

**Coverage:**
- End-to-end stub scanning
- Database building from stubs
- Export → Import round-trip
- SQL query correctness

### 3. Frontend Tests

**Approach:**
- Manual testing (no automated UI tests yet)
- Test with different browsers
- Test with/without SQL.js
- Test edge cases (empty results, errors)

## Security Considerations

### 1. Input Validation

**Measures:**
- Pydantic models validate all input data
- SQL parameterized queries (prevent injection)
- JSON schema validation
- Error handling for malformed files

### 2. Client-Side Security

**Measures:**
- No eval() or similar dynamic code execution
- CSP-friendly code (no inline scripts in production)
- XSS prevention (proper HTML escaping)
- HTTPS recommended for GitHub Pages

### 3. Data Integrity

**Measures:**
- Foreign key constraints in database
- Transaction-based database operations
- Atomic file writes
- Backup before updates

## Deployment Architecture

### GitHub Pages Hosting

```
Repository
├── tools/board_compare/
│   ├── *.py (source code - not deployed)
│   └── frontend/
│       ├── board-explorer.html (deployed)
│       ├── board-explorer.js (deployed)
│       ├── board_comparison.json (deployed, 24KB)
│       └── board_comparison.db (deployed, 4.8MB)
└── .github/workflows/
    └── update_board_comparison.yml (weekly rebuild)
```

**Benefits:**
- Free hosting
- HTTPS by default
- CDN distribution
- Version control integration

## Error Handling Strategy

### 1. Graceful Degradation

**Levels:**
1. Full functionality (SQL.js + database)
2. Basic comparison (JSON only)
3. Error message (if JSON fails to load)

### 2. User-Friendly Errors

**Approach:**
- Catch all exceptions
- Display clear error messages
- Provide fallback options
- Log to console for debugging

## Maintenance Considerations

### 1. Weekly Updates

**Automation:**
- GitHub Actions workflow
- Runs every Sunday at 2 AM UTC
- Scans latest published stubs
- Rebuilds database
- Commits updated JSON/DB

### 2. Dependency Management

**Strategy:**
- Minimal dependencies (only Pydantic)
- Pin dependency versions
- Test updates before deployment
- Document breaking changes

## Future Enhancements

### Potential Improvements

1. **Visual diff for method signatures**
   - Side-by-side parameter comparison
   - Highlight changed parameter types
   
2. **Export comparison reports**
   - PDF/CSV export
   - Shareable comparison links
   
3. **Advanced filtering**
   - By module category (stdlib, hardware, network)
   - By API type (sync, async, properties)
   
4. **Historical comparisons**
   - Compare same board across versions
   - Track API evolution
   
5. **Offline support**
   - Service worker for caching
   - Progressive Web App (PWA)

## Lessons Learned

### What Worked Well

1. **AST over libcst**: Simpler, faster, no dependencies
2. **Normalized database**: Efficient storage and queries
3. **Dual export strategy**: Fast loads with detailed data available
4. **SQL.js integration**: Powerful queries without backend
5. **Color-coded diff**: Intuitive visual comparison

### What Could Be Improved

1. **Initial design had 168MB JSON**: Too large, fixed with dual export
2. **No automated UI tests**: Manual testing is time-consuming
3. **SQL.js CDN dependency**: Blocked in some environments
4. **Limited offline support**: Requires internet for first load

## Conclusion

The Board Comparison Tool architecture balances several competing concerns:

- **Performance**: Fast initial loads with on-demand detail loading
- **Functionality**: Rich comparison features with powerful search
- **Simplicity**: No backend required, pure static hosting
- **Maintainability**: Automated updates, minimal dependencies
- **Usability**: Intuitive UI with multiple specialized views

The design is flexible enough to accommodate future enhancements while remaining simple and maintainable in its current form.
