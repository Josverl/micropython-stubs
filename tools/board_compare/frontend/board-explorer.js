/**
 * MicroPython Board Explorer & Comparison Tool
 * Enhanced frontend with multiple views and detailed comparisons
 */

// Global state
let boardData = { boards: [] };
let currentBoard = null;
let db = null;

// Initialize when page loads
async function init() {
    try {
        // Load simplified board data
        const response = await fetch('board_comparison.json');
        boardData = await response.json();
        
        // Populate all board selects
        populateBoardSelects();
        
        // Try to load SQL.js and database for detailed queries
        await loadDatabase();
    } catch (error) {
        console.error('Error loading data:', error);
        showError('Failed to load board data: ' + error.message);
    }
}

// Load SQLite database using SQL.js
async function loadDatabase() {
    try {
        // Load SQL.js library
        const SQL = await initSqlJs({
            locateFile: file => `https://sql.js.org/dist/${file}`
        });
        
        // Load the database file
        const response = await fetch('board_comparison.db');
        const buffer = await response.arrayBuffer();
        db = new SQL.Database(new Uint8Array(buffer));
        
        console.log('Database loaded successfully');
    } catch (error) {
        console.warn('Could not load database:', error);
        // Continue without database - basic comparison will still work
    }
}

function populateBoardSelects() {
    const selects = ['explorer-board', 'board1', 'board2'];
    
    selects.forEach(selectId => {
        const select = document.getElementById(selectId);
        if (!select) return;
        
        // Clear and add default option
        select.innerHTML = '<option value="">Select a board...</option>';
        
        // Add board options
        boardData.boards.forEach((board, idx) => {
            const name = `${board.port}-${board.board} (v${board.version})`;
            const option = document.createElement('option');
            option.value = idx;
            option.textContent = name;
            select.appendChild(option);
        });
    });
}

// Page Navigation
function switchPage(pageName) {
    // Update nav tabs
    document.querySelectorAll('.nav-tab').forEach(tab => {
        tab.classList.remove('active');
    });
    event.target.classList.add('active');
    
    // Update pages
    document.querySelectorAll('.page').forEach(page => {
        page.classList.remove('active');
    });
    document.getElementById(`${pageName}-page`).classList.add('active');
}

// ===== BOARD EXPLORER =====

async function loadBoardDetails() {
    const select = document.getElementById('explorer-board');
    const boardIdx = select.value;
    
    if (!boardIdx) {
        document.getElementById('explorer-content').innerHTML = '<div class="loading"><p>Select a board to explore its modules and APIs</p></div>';
        return;
    }
    
    currentBoard = boardData.boards[parseInt(boardIdx)];
    
    // Show loading
    document.getElementById('explorer-content').innerHTML = '<div class="loading"><div class="spinner"></div><p>Loading board details...</p></div>';
    
    // Get detailed module information from database
    const modules = await getBoardModules(currentBoard);
    
    // Display module tree
    displayModuleTree(modules);
}

async function getBoardModules(board) {
    if (!db) {
        // Fallback to simple module list
        return board.modules.map(name => ({ name, classes: [], functions: [] }));
    }
    
    try {
        // Query database for detailed module info
        const stmt = db.prepare(`
            SELECT m.id, m.name, m.docstring 
            FROM modules m
            JOIN board_modules bm ON m.id = bm.module_id
            JOIN boards b ON bm.board_id = b.id
            WHERE b.version = ? AND b.port = ? AND b.board = ?
            ORDER BY m.name
        `);
        stmt.bind([board.version, board.port, board.board]);
        
        const modules = [];
        while (stmt.step()) {
            const row = stmt.getAsObject();
            
            // Get classes for this module
            const classes = getModuleClasses(row.id);
            const functions = getModuleFunctions(row.id);
            const constants = getModuleConstants(row.id);
            
            modules.push({
                id: row.id,
                name: row.name,
                docstring: row.docstring,
                classes: classes,
                functions: functions,
                constants: constants
            });
        }
        stmt.free();
        
        return modules;
    } catch (error) {
        console.error('Error querying modules:', error);
        return board.modules.map(name => ({ name, classes: [], functions: [] }));
    }
}

function getModuleClasses(moduleId) {
    if (!db) return [];
    
    try {
        const stmt = db.prepare(`
            SELECT id, name, docstring
            FROM classes
            WHERE module_id = ?
            ORDER BY name
        `);
        stmt.bind([moduleId]);
        
        const classes = [];
        while (stmt.step()) {
            const row = stmt.getAsObject();
            classes.push({
                id: row.id,
                name: row.name,
                docstring: row.docstring,
                methods: getClassMethods(moduleId, row.id)
            });
        }
        stmt.free();
        
        return classes;
    } catch (error) {
        console.error('Error querying classes:', error);
        return [];
    }
}

function getModuleFunctions(moduleId) {
    if (!db) return [];
    
    try {
        const stmt = db.prepare(`
            SELECT name, return_type, is_async
            FROM methods
            WHERE module_id = ? AND class_id IS NULL
            ORDER BY name
        `);
        stmt.bind([moduleId]);
        
        const functions = [];
        while (stmt.step()) {
            const row = stmt.getAsObject();
            functions.push(row);
        }
        stmt.free();
        
        return functions;
    } catch (error) {
        console.error('Error querying functions:', error);
        return [];
    }
}

function getClassMethods(moduleId, classId) {
    if (!db) return [];
    
    try {
        const stmt = db.prepare(`
            SELECT name, return_type, is_async, is_property, is_classmethod, is_staticmethod
            FROM methods
            WHERE module_id = ? AND class_id = ?
            ORDER BY name
        `);
        stmt.bind([moduleId, classId]);
        
        const methods = [];
        while (stmt.step()) {
            const row = stmt.getAsObject();
            methods.push(row);
        }
        stmt.free();
        
        return methods;
    } catch (error) {
        console.error('Error querying methods:', error);
        return [];
    }
}

function getModuleConstants(moduleId) {
    if (!db) return [];
    
    try {
        const stmt = db.prepare(`
            SELECT name FROM module_constants WHERE module_id = ? ORDER BY name
        `);
        stmt.bind([moduleId]);
        
        const constants = [];
        while (stmt.step()) {
            constants.push(stmt.getAsObject().name);
        }
        stmt.free();
        
        return constants;
    } catch (error) {
        console.error('Error querying constants:', error);
        return [];
    }
}

function displayModuleTree(modules) {
    let html = `
        <div class="detail-view">
            <div class="detail-header">${currentBoard.port}-${currentBoard.board} (v${currentBoard.version})</div>
            <div class="detail-section">
                <h3>📦 Modules (${modules.length})</h3>
                <div class="module-tree">
    `;
    
    modules.forEach(module => {
        const hasChildren = module.classes.length > 0 || module.functions.length > 0;
        html += `
            <div class="tree-item">
                <div class="tree-node" onclick="toggleModule('module-${module.name}', event)">
                    <span class="tree-icon">${hasChildren ? '📁' : '📄'}</span>
                    <strong>${module.name}</strong>
                    <span style="color: #666; font-size: 0.9em;">
                        (${module.classes.length} classes, ${module.functions.length} functions)
                    </span>
                </div>
                <div id="module-${module.name}" class="tree-children hidden">
        `;
        
        // Add classes
        if (module.classes.length > 0) {
            module.classes.forEach(cls => {
                html += `
                    <div class="tree-item">
                        <div class="tree-node" onclick="showClassDetails('${module.name}', '${cls.name}', event)">
                            <span class="tree-icon">🔷</span>
                            <span style="color: #667eea; font-weight: 600;">class ${cls.name}</span>
                            <span style="color: #666; font-size: 0.9em;">(${cls.methods.length} methods)</span>
                        </div>
                    </div>
                `;
            });
        }
        
        // Add functions
        if (module.functions.length > 0) {
            module.functions.forEach(func => {
                const asyncMarker = func.is_async ? 'async ' : '';
                html += `
                    <div class="tree-item">
                        <div class="tree-node">
                            <span class="tree-icon">⚡</span>
                            <span>${asyncMarker}${func.name}()</span>
                        </div>
                    </div>
                `;
            });
        }
        
        html += `
                </div>
            </div>
        `;
    });
    
    html += `
                </div>
            </div>
        </div>
    `;
    
    document.getElementById('explorer-content').innerHTML = html;
}

function toggleModule(moduleId, event) {
    event.stopPropagation();
    const element = document.getElementById(moduleId);
    if (element) {
        element.classList.toggle('hidden');
    }
}

async function showClassDetails(moduleName, className, event) {
    event.stopPropagation();
    
    // Find the module and class
    const modules = await getBoardModules(currentBoard);
    const module = modules.find(m => m.name === moduleName);
    if (!module) return;
    
    const cls = module.classes.find(c => c.name === className);
    if (!cls) return;
    
    // Create detail view
    let html = `
        <div class="detail-view" style="margin-top: 20px;">
            <div class="detail-header">${moduleName}.${className}</div>
    `;
    
    if (cls.docstring) {
        html += `
            <div class="detail-section">
                <h3>Description</h3>
                <p style="white-space: pre-wrap; color: #666; line-height: 1.6;">${cls.docstring}</p>
            </div>
        `;
    }
    
    if (cls.methods.length > 0) {
        html += `
            <div class="detail-section">
                <h3>Methods (${cls.methods.length})</h3>
                <div class="method-list">
        `;
        
        cls.methods.forEach(method => {
            const decorators = [];
            if (method.is_property) decorators.push('@property');
            if (method.is_classmethod) decorators.push('@classmethod');
            if (method.is_staticmethod) decorators.push('@staticmethod');
            
            const asyncMarker = method.is_async ? 'async ' : '';
            const returnType = method.return_type ? ` -> ${method.return_type}` : '';
            
            html += `
                <div class="method-item">
                    ${decorators.length > 0 ? `<div style="color: #888; font-size: 0.85em;">${decorators.join(' ')}</div>` : ''}
                    <span class="method-name">${asyncMarker}${method.name}()</span>
                    ${returnType ? `<span class="method-return">${returnType}</span>` : ''}
                </div>
            `;
        });
        
        html += `
                </div>
            </div>
        `;
    }
    
    html += '</div>';
    
    // Append to content
    document.getElementById('explorer-content').insertAdjacentHTML('beforeend', html);
}

// ===== BOARD COMPARISON =====

let comparisonData = null;

function compareBoards() {
    const board1Idx = document.getElementById('board1').value;
    const board2Idx = document.getElementById('board2').value;
    
    if (!board1Idx || !board2Idx) {
        alert('Please select both boards to compare');
        return;
    }
    
    const board1 = boardData.boards[parseInt(board1Idx)];
    const board2 = boardData.boards[parseInt(board2Idx)];
    
    comparisonData = { board1, board2 };
    updateComparison();
}

function updateComparison() {
    if (!comparisonData) return;
    
    const { board1, board2 } = comparisonData;
    const hideCommon = document.getElementById('hide-common').checked;
    
    const modules1 = new Set(board1.modules);
    const modules2 = new Set(board2.modules);
    
    const common = [...modules1].filter(m => modules2.has(m));
    const unique1 = [...modules1].filter(m => !modules2.has(m));
    const unique2 = [...modules2].filter(m => !modules1.has(m));
    
    // Update stats
    document.getElementById('compare-stats').style.display = 'block';
    document.getElementById('compare-stats').innerHTML = `
        <div class="stats">
            <div class="stat-card">
                <div class="stat-value">${common.length}</div>
                <div class="stat-label">Common Modules</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">${unique1.length}</div>
                <div class="stat-label">Unique to ${board1.port}-${board1.board}</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">${unique2.length}</div>
                <div class="stat-label">Unique to ${board2.port}-${board2.board}</div>
            </div>
        </div>
    `;
    
    // Build comparison HTML
    let html = `
        <div class="comparison-grid">
            <div class="board-section">
                <div class="board-header">${board1.port}-${board1.board} (v${board1.version})</div>
                <div class="module-list">
                    <h3>Modules (${modules1.size})</h3>
    `;
    
    // Board 1 modules
    const board1Modules = hideCommon ? unique1 : [...modules1].sort();
    board1Modules.forEach(name => {
        const cssClass = unique1.includes(name) ? 'module-item unique-to-board1' : 'module-item';
        const badge = unique1.includes(name) ? ' [UNIQUE]' : '';
        html += `
            <div class="${cssClass}">
                <div class="module-name">${name}${badge}</div>
            </div>
        `;
    });
    
    if (hideCommon && unique1.length === 0) {
        html += '<p style="color: #666; padding: 20px;">No unique modules</p>';
    }
    
    html += `
                </div>
            </div>
            <div class="board-section">
                <div class="board-header">${board2.port}-${board2.board} (v${board2.version})</div>
                <div class="module-list">
                    <h3>Modules (${modules2.size})</h3>
    `;
    
    // Board 2 modules
    const board2Modules = hideCommon ? unique2 : [...modules2].sort();
    board2Modules.forEach(name => {
        const cssClass = unique2.includes(name) ? 'module-item unique-to-board2' : 'module-item';
        const badge = unique2.includes(name) ? ' [UNIQUE]' : '';
        html += `
            <div class="${cssClass}">
                <div class="module-name">${name}${badge}</div>
            </div>
        `;
    });
    
    if (hideCommon && unique2.length === 0) {
        html += '<p style="color: #666; padding: 20px;">No unique modules</p>';
    }
    
    html += `
                </div>
            </div>
        </div>
    `;
    
    // Show common modules if not hidden
    if (!hideCommon && common.length > 0) {
        html += `
            <div class="detail-view">
                <div class="detail-header">Common Modules (${common.length})</div>
                <div style="columns: 3; column-gap: 20px;">
        `;
        
        common.sort().forEach(name => {
            html += `<div style='break-inside: avoid; padding: 5px;'>📦 ${name}</div>`;
        });
        
        html += `
                </div>
            </div>
        `;
    }
    
    document.getElementById('compare-results').innerHTML = html;
}

// ===== SEARCH APIs =====

function handleSearchEnter(event) {
    if (event.key === 'Enter') {
        searchAPIs();
    }
}

async function searchAPIs() {
    const query = document.getElementById('search-input').value.trim().toLowerCase();
    
    if (!query) {
        alert('Please enter a search term');
        return;
    }
    
    document.getElementById('search-results').innerHTML = '<div class="loading"><div class="spinner"></div><p>Searching...</p></div>';
    
    const results = [];
    
    // Search through all boards
    for (const board of boardData.boards) {
        const boardName = `${board.port}-${board.board}`;
        
        // Check modules
        const matchingModules = board.modules.filter(m => m.toLowerCase().includes(query));
        
        if (matchingModules.length > 0) {
            results.push({
                board: boardName,
                type: 'module',
                matches: matchingModules
            });
        }
        
        // If database is available, search classes and methods
        if (db) {
            try {
                // Search classes
                const classStmt = db.prepare(`
                    SELECT DISTINCT m.name as module_name, c.name as class_name
                    FROM classes c
                    JOIN modules m ON c.module_id = m.id
                    JOIN board_modules bm ON m.id = bm.module_id
                    JOIN boards b ON bm.board_id = b.id
                    WHERE b.port = ? AND b.board = ? AND LOWER(c.name) LIKE ?
                `);
                classStmt.bind([board.port, board.board, `%${query}%`]);
                
                const classes = [];
                while (classStmt.step()) {
                    const row = classStmt.getAsObject();
                    classes.push(`${row.module_name}.${row.class_name}`);
                }
                classStmt.free();
                
                if (classes.length > 0) {
                    results.push({
                        board: boardName,
                        type: 'class',
                        matches: classes
                    });
                }
                
                // Search methods
                const methodStmt = db.prepare(`
                    SELECT DISTINCT m.name as module_name, c.name as class_name, mt.name as method_name
                    FROM methods mt
                    JOIN modules m ON mt.module_id = m.id
                    LEFT JOIN classes c ON mt.class_id = c.id
                    JOIN board_modules bm ON m.id = bm.module_id
                    JOIN boards b ON bm.board_id = b.id
                    WHERE b.port = ? AND b.board = ? AND LOWER(mt.name) LIKE ?
                `);
                methodStmt.bind([board.port, board.board, `%${query}%`]);
                
                const methods = [];
                while (methodStmt.step()) {
                    const row = methodStmt.getAsObject();
                    const methodPath = row.class_name 
                        ? `${row.module_name}.${row.class_name}.${row.method_name}`
                        : `${row.module_name}.${row.method_name}`;
                    methods.push(methodPath);
                }
                methodStmt.free();
                
                if (methods.length > 0) {
                    results.push({
                        board: boardName,
                        type: 'method',
                        matches: methods.slice(0, 10) // Limit to 10
                    });
                }
            } catch (error) {
                console.error('Error searching database:', error);
            }
        }
    }
    
    displaySearchResults(query, results);
}

function displaySearchResults(query, results) {
    if (results.length === 0) {
        document.getElementById('search-results').innerHTML = `
            <div class="detail-view">
                <p style="color: #666;">No results found for "${query}"</p>
            </div>
        `;
        return;
    }
    
    let html = `
        <div class="detail-view">
            <div class="detail-header">Search Results for "${query}"</div>
            <p style="color: #666; margin-bottom: 20px;">Found in ${results.length} board(s)</p>
        </div>
    `;
    
    // Group by type
    const moduleResults = results.filter(r => r.type === 'module');
    const classResults = results.filter(r => r.type === 'class');
    const methodResults = results.filter(r => r.type === 'method');
    
    if (moduleResults.length > 0) {
        html += `<div class="search-result-item">
            <div class="search-result-header">📦 Modules</div>
            <p style="color: #666; margin-bottom: 10px;">Boards with matching modules:</p>
        `;
        moduleResults.forEach(result => {
            html += `<div style="margin-bottom: 10px;">
                <span class="board-badge">${result.board}</span>
                ${result.matches.join(', ')}
            </div>`;
        });
        html += `</div>`;
    }
    
    if (classResults.length > 0) {
        html += `<div class="search-result-item">
            <div class="search-result-header">🔷 Classes</div>
            <p style="color: #666; margin-bottom: 10px;">Boards with matching classes:</p>
        `;
        classResults.forEach(result => {
            html += `<div style="margin-bottom: 10px;">
                <span class="board-badge">${result.board}</span>
                ${result.matches.join(', ')}
            </div>`;
        });
        html += `</div>`;
    }
    
    if (methodResults.length > 0) {
        html += `<div class="search-result-item">
            <div class="search-result-header">⚡ Methods/Functions</div>
            <p style="color: #666; margin-bottom: 10px;">Boards with matching methods:</p>
        `;
        methodResults.forEach(result => {
            html += `<div style="margin-bottom: 10px;">
                <span class="board-badge">${result.board}</span>
                ${result.matches.join(', ')}
            </div>`;
        });
        html += `</div>`;
    }
    
    document.getElementById('search-results').innerHTML = html;
}

function showError(message) {
    document.body.innerHTML = `
        <div class="container">
            <div style="padding: 40px; text-align: center;">
                <h1 style="color: #dc3545;">Error</h1>
                <p style="color: #666; margin-top: 20px;">${message}</p>
            </div>
        </div>
    `;
}

// Load SQL.js library
function loadSqlJs() {
    return new Promise((resolve, reject) => {
        const script = document.createElement('script');
        script.src = 'https://sql.js.org/dist/sql-wasm.js';
        script.onload = () => resolve(window.initSqlJs);
        script.onerror = reject;
        document.head.appendChild(script);
    });
}

// Initialize on page load
(async function() {
    try {
        // Load SQL.js first
        window.initSqlJs = await loadSqlJs();
        // Then initialize the app
        await init();
    } catch (error) {
        console.error('Initialization error:', error);
        // Continue without database
        try {
            const response = await fetch('board_comparison.json');
            boardData = await response.json();
            populateBoardSelects();
        } catch (e) {
            showError('Failed to load board data: ' + e.message);
        }
    }
})();
