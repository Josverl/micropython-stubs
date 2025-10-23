# MicroPython Board Explorer - Search Treeview Requirements

## Current Date: October 21, 2025

## 🎯 PRIMARY OBJECTIVES

### 1. Search Results Display Structure
- **Hierarchical Treeview**: Search results should display as an expandable tree structure
- **Result-Based Grouping**: Results grouped by container  (e.g.modules :"stm", "machine", or classes : "Pin")
- **Entity Type Categories**: Within each module, group by entity types (classes, constants, functions, methods, attributes)
- **Expandable/Collapsible**: Users can expand modules to see their contents, expand classes to see methods/attributes

### 2. Visual Representation Requirements
- **Proper Icons**: Each entity type should show appropriate Font Awesome icons
  - 🧊 `fa-cube` - Modules
  - ⧉ `fa-object-group` - Classes  
  - ⚡ `fa-bolt` - Functions/Methods
  - ● `fa-circle` - Constants
  - 🏷️ `fa-tag` - Attributes
  - 📋 `fa-list` - Parameters

- **Board/Version Context**: Every top level item in the tree-view should display board and version badges
  - Format: `[STM32 v1.26.0]`, `[ESP32 v1.25.0]`, etc.
  - Inherited from parent module context when not directly available

### 3. Expansion Behavior Requirements

#### Level 1: Module  / Class Level (Always Visible)
```
🧊 stm [STM32 v1.26.0] (5 constants) ▶️
🧊 machine [ESP32 v1.26.0] (1 class) ▶️  
⧉ Pin [STM32 v1.26.0] (4 attributes) ▶️  ( Direct search match )
● SPI_I2SPR = 0x20                        ( Direct search match )    
```

#### Level 2: Entity Categories (Visible After Module Expansion)
```
🧊 stm [STM32 v1.26.0] ▼
  ● Constants (5) ▶️
  ⧉ Classes (0)
  ⚡ Functions (0)

🧊 machine [ESP32 v1.26.0] ▼  
  ⧉ Classes (1) ▶️
    └─ ⧉ I2S ▶️

🧊 Pin [STM32 v1.26.0] ▼
  🏷️ Attributes (4) ▶️
```

#### Level 3: Individual Items (Visible After Category Expansion)
```
🧊 stm [STM32 v1.26.0] ▼
  ● Constants (5) ▼
    └─ ● I2S2EXT = 0x40003400
    └─ ● I2S3EXT = 0x40004000  
    └─ ● RCC_PLLI2SCFGR = 0x40023884
    └─ ● SPI_I2SCFGR = 0x1C
    └─ ● SPI_I2SPR = 0x20

🧊 machine [ESP32 v1.26.0] ▼  
  ⧉ Classes (1) ▼
    └─ ⧉ I2S ▼
        └─ ⚡ __init__(id, ...)
        └─ ⚡ deinit()
        └─ ⚡ read(buf)
        └─ ⚡ write(buf)
```

### 4. What Should Be Visible

#### Initially Visible (Collapsed State)
- Module names with summary counts: "stm (5 constants)", "machine (1 class)"
- Expansion arrows (▶️) indicating expandable content
- direct matches of other entities 
- Board/version badges for each entity on level 1
- icons matching the entity type 


#### After First Level Expansion (Module → Categories)
- Entity type categories with counts: "Constants (5)", "Classes (1)"
- Category-appropriate icons
- Sub-expansion arrows for categories with content

#### After Second Level Expansion (Categories → Items)
- Individual entities (classes, methods, constants, attributes)
- Complete signatures/values where available
- Hierarchical indentation (└─ indicators)
- Entity-specific icons

### 5. What Should NOT Be Visible

#### Hidden Until Expansion
- Individual entity details (method signatures, constant values)
- Empty categories (e.g., "Functions (0)" should be hidden or grayed out)
- Duplicate entities across different boards (deduplicated intelligently)

#### Always Hidden
- Internal/private entities (unless specifically searched)
- Database implementation details
- Raw SQL query results

### 6. Interactive Behavior Requirements

#### Expansion/Collapse
- **Click Module Header**: Expand/collapse to show entity categories
- **Click Category Header**: Expand/collapse to show individual items  
- **Click Individual Item**: Navigate to detailed view or show tooltip
- **Keyboard Navigation**: Arrow keys for navigation, Enter to expand/collapse

#### Search Integration
- **Real-time Results**: Results update as user types (debounced)
- **Highlight Matches**: Search terms highlighted in results
- **Preserve State**: Expansion state maintained during search refinement

### 7. Performance Requirements
- **Fast Rendering**: Tree should render quickly even with many results
- **Lazy Loading**: Load entity details only when expanded
- **Smooth Animation**: Expand/collapse should be visually smooth
- **Responsive Design**: Work well on different screen sizes

### 8. Testing Strategy

#### MCP Playwright during development 
1. the standard URL for the application is : http://localhost:8000/board-explorer-mpy.html
2. assume that the url is already server - only start a new server if port 8000 is not already in use
3. the MCP server should be used for verification of recent changes


#### Unit Tests Required
1. **Search Result Grouping**: Verify results properly grouped by module and entity type
2. **Icon Assignment**: Confirm correct icons for each entity type
3. **Board Context Inheritance**: Ensure all items have proper board/version info
4. **Expansion Logic**: Verify expand/collapse functionality works correctly

#### Integration Tests Required  
1. **Search → Display Pipeline**: End-to-end search result display
2. **Database Query → Tree Structure**: Verify database results convert to proper tree
3. **User Interaction**: Click-to-expand behavior
4. **URL State Management**: Expansion state preserved in URLs

#### Browser Testing Checklist
- search for multiple items and verify the tree structure for each
  - containers such as : I2S , RingIO
  - entities such as : I2S2EXT, writebyte
- [ ] Module expansion shows entity categories
- [ ] Category expansion shows individual items
- [ ] All items have appropriate icons
- [ ] All items have board/version badges
- [ ] Expansion state is visually clear (arrows, indentation)
- [ ] Performance is acceptable with large result sets

### 9. Current Implementation Status

#### ✅ Working Components (DO NOT BREAK)
- Database query system (`perform_search`)
- Search result conversion (`convert_search_results_to_tree_format`)
- Tree rendering system (`render_module_tree_dom`)
- Expansion logic (`toggleModule`, `toggleClass`)
- Template system for consistent HTML generation

#### ❌ Issues Identified
- Icons showing as module icons instead of entity-specific icons
- Missing board/version badges on some grouped results
- ~~Search results converted to category items instead of expandable tree~~

#### 🔧 What Needs Fixing
- **Icon Assignment**: Ensure entity-specific icons in tree view
- **Board Context**: Fix board/version badge inheritance
- **Tree Preservation**: Maintain expandable tree structure while fixing icons/badges

### 10. Implementation Approach

#### Phase 1: Assess Current Tree Implementation
- Review existing `convert_search_results_to_tree_format`
- Verify expansion functionality still works
- Identify minimal changes needed for icon/badge fixes

#### Phase 2: Fix Icons While Preserving Tree
- Modify template population to use entity-specific icons
- Ensure module templates show module icons, content shows entity icons
- Test expansion behavior remains intact

#### Phase 3: Fix Board Context Inheritance
- Enhance board context propagation to child entities
- Verify badges appear on all tree levels
- Maintain existing expansion logic

#### Phase 4: Comprehensive Testing
- Test complete search → tree → expansion workflow
- Verify all requirements are met
- Performance validation

### 11. Success Criteria

The implementation is successful when:
1. Search results display as expandable tree structure
2. Direct matches appear at level 1
3. Modules show with proper icons and board badges
4. Module expansion reveals entity categories  
5. Class expansion reveals entity categories  
6. All entities have correct icons (not just module icons)
7. All entities have proper board/version context
8. Expansion/collapse animations work smoothly
9. Performance remains acceptable

---

**CRITICAL**: Any changes must preserve the existing expandable tree functionality while fixing the icon and board badge issues. The tree structure and expansion behavior should remain intact.