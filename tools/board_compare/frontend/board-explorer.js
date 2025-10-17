/**
 * MicroPython Board Explorer & Comparison Tool
 * Enhanced frontend with multiple views and detailed comparisons
 */

// Icon utilities for consistent visual representation using Font Awesome
const Icons = {
    // Core concept icons with Font Awesome classes
    package: { faClass: 'fas fa-box-archive', alt: 'Package' },
    module: { faClass: 'fas fa-cube', alt: 'Module' },
    board: { faClass: 'fas fa-microchip', alt: 'Board' },
    class: { faClass: 'fas fa-object-group', alt: 'Class' },
    function: { faClass: 'fas fa-bolt', alt: 'Function' },
    method: { faClass: 'fas fa-bolt', alt: 'Method' },
    constant: { faClass: 'fas fa-circle', alt: 'Constant' },
    variable: { faClass: 'fas fa-circle-dot', alt: 'Variable' },
    property: { faClass: 'fas fa-ellipsis', alt: 'Property' },
    
    // Action icons
    search: { faClass: 'fas fa-search', alt: 'Search' },
    explorer: { faClass: 'fas fa-microscope', alt: 'Explorer' },
    compare: { faClass: 'fas fa-balance-scale', alt: 'Compare' },
    share: { faClass: 'fas fa-share', alt: 'Share' },
    retry: { faClass: 'fas fa-redo', alt: 'Retry' },
    
    // File/folder icons
    folder: { faClass: 'fas fa-folder', alt: 'Folder' },
    file: { faClass: 'fas fa-file', alt: 'File' },
    
    // Utility function to create Font Awesome icon span with accessibility
    create: function(iconKey, extraClasses = '') {
        const icon = this[iconKey];
        if (!icon) return '';
        return `<i class="${icon.faClass} fa-icon ${extraClasses}" aria-label="${icon.alt}" title="${icon.alt}"></i>`;
    }
};

// Global state
let boardData = { boards: [] };
let currentBoard = null;
let db = null;

// Initialize when page loads
async function init() {
    try {
        // Load SQL.js and database - required for all functionality
        await loadDatabase();
        
        // Load board list from database
        await loadBoardList();
        
        // Populate all board selects
        populateBoardSelects();
        
        // Check for URL parameters and restore state
        await restoreFromURL();
    } catch (error) {
        console.error('Error loading data:', error);
        showError('Failed to load board data: ' + error.message);
    }
}

// Restore state from URL parameters (shareable links)
async function restoreFromURL() {
    const params = new URLSearchParams(window.location.search);
    
    // Switch to requested view
    const view = params.get('view');
    if (view === 'compare') {
        switchPage('compare');
    } else if (view === 'search') {
        switchPage('search');
    } else if (view === 'explorer') {
        switchPage('explorer');
    }
    
    // Restore comparison state
    if (params.has('board1') && params.has('board2')) {
        const board1Key = params.get('board1');
        const board2Key = params.get('board2');
        
        // Find board indices
        const board1Idx = boardData.boards.findIndex(b => `${b.port}-${b.board}` === board1Key);
        const board2Idx = boardData.boards.findIndex(b => `${b.port}-${b.board}` === board2Key);
        
        if (board1Idx >= 0 && board2Idx >= 0) {
            // Set board selections
            document.getElementById('board1').value = board1Idx.toString();
            document.getElementById('board2').value = board2Idx.toString();
        
            // Apply diff mode if specified
            if (params.get('diff') === 'true') {
                document.getElementById('hide-common').checked = true;
            }
            
            // Apply detailed mode if specified
            if (params.get('detailed') === 'true') {
                document.getElementById('detailed-compare').checked = true;
            }
            
            // Trigger comparison
            await compareBoards();
        }
    }
    
    // Restore explorer state
    if (params.has('board') && (view === 'explorer' || !view)) {
        const boardKey = params.get('board');
        const boardIdx = boardData.boards.findIndex(b => `${b.port}-${b.board}` === boardKey);
        
        if (boardIdx >= 0) {
            document.getElementById('explorer-board').value = boardIdx.toString();
            await loadBoardDetails();
        
            // Optionally expand specific module
            if (params.has('module')) {
                const moduleName = params.get('module');
                // Wait a bit for rendering
                setTimeout(() => {
                    const moduleElement = document.querySelector(`[data-module="${moduleName}"]`);
                    if (moduleElement) {
                        moduleElement.click();
                        moduleElement.scrollIntoView({ behavior: 'smooth', block: 'center' });
                    }
                }, 500);
            }
        }
    }
    
    // Restore search state
    if (params.has('search') && (view === 'search' || !view)) {
        const query = params.get('search');
        document.getElementById('search-input').value = query;
        await searchAPIs();
    }
}

// Update URL with current state (for shareable links)
function updateURL(params) {
    const url = new URL(window.location);
    
    // Clear existing params
    url.search = '';
    
    // Add new params
    for (const [key, value] of Object.entries(params)) {
        if (value !== null && value !== undefined && value !== '') {
            url.searchParams.set(key, value);
        }
    }
    
    // Update URL without reload
    window.history.pushState({}, '', url);
    
    // Update share button if exists
    updateShareButton(url.toString());
}

// Update share button with current URL
function updateShareButton(url) {
    const shareButtons = document.querySelectorAll('.share-btn');
    shareButtons.forEach(btn => {
        btn.onclick = () => {
            navigator.clipboard.writeText(url).then(() => {
                const originalText = btn.textContent;
                btn.textContent = '✓ Copied!';
                setTimeout(() => {
                    btn.textContent = originalText;
                }, 2000);
            });
        };
        btn.style.display = 'inline-block';
    });
}

// Load SQLite database using SQL.js
async function loadDatabase() {
    try {
        console.log('Loading SQL.js library...');
        
        // Try to use initSqlJs if already loaded, otherwise load it
        let SQL;
        if (typeof window.initSqlJs === 'function') {
            SQL = await window.initSqlJs({
                locateFile: file => `https://cdnjs.cloudflare.com/ajax/libs/sql.js/1.8.0/${file}`
            });
        } else {
            throw new Error('SQL.js not loaded');
        }
        
        console.log('SQL.js loaded, fetching database...');
        
        // Load the database file
        const response = await fetch('board_comparison.db');
        if (!response.ok) {
            throw new Error(`Failed to load database: ${response.statusText}`);
        }
        const buffer = await response.arrayBuffer();
        db = new SQL.Database(new Uint8Array(buffer));
        
        console.log('Database loaded successfully');
        
        // Test database connection
        const testStmt = db.prepare("SELECT name FROM sqlite_master WHERE type='table' LIMIT 1");
        testStmt.step();
        testStmt.free();
        
    } catch (error) {
        console.error('Could not load database:', error);
        throw new Error('Database is required for this tool. Please ensure board_comparison.db is available and SQL.js can be loaded.');
    }
}

// Load board list from database
async function loadBoardList() {
    if (!db) {
        throw new Error('Database not loaded');
    }
    
    try {
        const stmt = db.prepare(`
            SELECT DISTINCT version, port, board
            FROM boards
            ORDER BY version DESC, port, board
        `);
        
        boardData.boards = [];
        while (stmt.step()) {
            const row = stmt.getAsObject();
            boardData.boards.push({
                version: row.version,
                port: row.port,
                board: row.board
            });
        }
        stmt.free();
        
        console.log(`Loaded ${boardData.boards.length} boards from database`);
    } catch (error) {
        console.error('Error loading board list:', error);
        throw error;
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
            const name = `${board.port}-${board.board} (${board.version})`;
            const option = document.createElement('option');
            option.value = idx;
            option.textContent = name;
            select.appendChild(option);
        });
    });
}

// Page Navigation
function switchPage(pageName, eventTarget = null) {
    // Update nav tabs
    document.querySelectorAll('.nav-tab').forEach(tab => {
        tab.classList.remove('active');
    });
    
    // Find and activate the correct tab
    if (eventTarget) {
        eventTarget.classList.add('active');
    } else {
        // Find the tab by matching the page name
        const tabs = document.querySelectorAll('.nav-tab');
        tabs.forEach(tab => {
            const onclick = tab.getAttribute('onclick');
            if (onclick && onclick.includes(`'${pageName}'`)) {
                tab.classList.add('active');
            }
        });
    }
    
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
    
    // Show initial loading with progress
    document.getElementById('explorer-content').innerHTML = `
        <div class="loading">
            <div class="spinner"></div>
            <p>Loading <strong>${currentBoard.port}-${currentBoard.board}</strong> details...</p>
            <div class="progress-step">Initializing...</div>
        </div>
    `;
    
    try {
        // Small delay to show initial message
        await new Promise(resolve => setTimeout(resolve, 300));
        
        // Update progress for fetching modules
        document.getElementById('explorer-content').innerHTML = `
            <div class="loading">
                <div class="spinner"></div>
                <p>Fetching modules for <strong>${currentBoard.port}-${currentBoard.board}</strong>...</p>
                <div class="progress-step">Step 1 of 3</div>
            </div>
        `;
        
        // Get detailed module information from database
        const modules = await getBoardModules(currentBoard);
        
        // Small delay to show progress
        await new Promise(resolve => setTimeout(resolve, 200));
        
        // Update progress for processing classes and methods
        document.getElementById('explorer-content').innerHTML = `
            <div class="loading">
                <div class="spinner"></div>
                <p>Processing classes and methods...</p>
                <div class="progress-step">Step 2 of 3</div>
            </div>
        `;
        
        // Small delay to show processing step
        await new Promise(resolve => setTimeout(resolve, 200));
        
        // Update progress for building interface
        document.getElementById('explorer-content').innerHTML = `
            <div class="loading">
                <div class="spinner"></div>
                <p>Building module tree interface...</p>
                <div class="progress-step">Step 3 of 3</div>
            </div>
        `;
        
        // Small delay to show final step
        await new Promise(resolve => setTimeout(resolve, 150));
        
        // Display module tree
        displayModuleTree(modules);
        
        // Update URL for shareable links
        updateURL({
            view: 'explorer',
            board: `${currentBoard.port}-${currentBoard.board}`
        });
    } catch (error) {
        console.error('Error loading board details:', error);
        document.getElementById('explorer-content').innerHTML = `
            <div class="detail-view">
                <h3 style="color: #dc3545;">⚠️ Loading Error</h3>
                <p style="color: #666; margin: 15px 0;">${error.message}</p>
                <button onclick="loadBoardDetails()" style="margin-top: 15px; padding: 10px 20px; background: #667eea; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600;">
                    ${Icons.create('retry')} Try Again
                </button>
            </div>
        `;
    }
}

async function getBoardModules(board) {
    if (!db) {
        throw new Error('Database not available');
    }
    
    try {
        // Query database for detailed module info
        const stmt = db.prepare(`
            SELECT um.id, um.name, um.docstring 
            FROM unique_modules um
            JOIN board_module_support bms ON um.id = bms.module_id
            JOIN boards b ON bms.board_id = b.id
            WHERE b.version = ? AND b.port = ? AND b.board = ?
            ORDER BY um.name
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
        throw error;
    }
}

function getModuleClasses(moduleId) {
    if (!db) return [];
    
    try {
        const stmt = db.prepare(`
            SELECT uc.id, uc.name, uc.docstring
            FROM unique_classes uc
            WHERE uc.module_id = ?
            ORDER BY uc.name
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
            SELECT um.name, um.return_type, um.is_async
            FROM unique_methods um
            WHERE um.module_id = ? AND um.class_id IS NULL
            ORDER BY um.name
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
            SELECT um.name, um.return_type, um.is_async, um.is_property, um.is_classmethod, um.is_staticmethod
            FROM unique_methods um
            WHERE um.module_id = ? AND um.class_id = ?
            ORDER BY um.name
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
            SELECT umc.name FROM unique_module_constants umc WHERE umc.module_id = ? ORDER BY umc.name
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
            <div class="detail-header">${currentBoard.port}-${currentBoard.board} (${currentBoard.version})</div>
            <div class="detail-section">
                <h3>${Icons.create('module')} Modules (${modules.length})</h3>
                <div class="module-tree">
    `;
    
    modules.forEach(module => {
        const hasChildren = module.classes.length > 0 || module.functions.length > 0;
        html += `
            <div class="tree-item">
                <div class="tree-node" onclick="toggleModule('module-${module.name}', event)">
                    <span class="tree-icon">${hasChildren ? Icons.create('folder') : Icons.create('module')}</span>
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
                            <span class="tree-icon">${Icons.create('class')}</span>
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
                            <span class="tree-icon">${Icons.create('function')}</span>
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

async function compareBoards() {
    const board1Idx = document.getElementById('board1').value;
    const board2Idx = document.getElementById('board2').value;
    
    if (!board1Idx || !board2Idx) {
        alert('Please select both boards to compare');
        return;
    }
    
    if (!db) {
        alert('Database not available for comparison');
        return;
    }
    
    console.log('Starting board comparison...');
    
    const board1 = boardData.boards[parseInt(board1Idx)];
    const board2 = boardData.boards[parseInt(board2Idx)];
    
    console.log('Comparing:', board1, 'vs', board2);
    
    // Show initial loading with delay
    document.getElementById('compare-results').innerHTML = `
        <div class="loading">
            <div class="spinner"></div>
            <p>Preparing comparison...</p>
            <div class="progress-step">Initializing...</div>
        </div>
    `;
    
    try {
        // Small delay to show initial message
        await new Promise(resolve => setTimeout(resolve, 500));
        
        // Update progress for board 1
        document.getElementById('compare-results').innerHTML = `
            <div class="loading">
                <div class="spinner"></div>
                <p>Fetching modules for <strong>${board1.port}-${board1.board}</strong>...</p>
                <div class="progress-step">Step 1 of 3</div>
            </div>
        `;
        
        console.log('Fetching modules for board 1...');
        const modules1 = await getBoardModules(board1);
        
        // Small delay to show progress
        await new Promise(resolve => setTimeout(resolve, 300));
        
        // Update progress for board 2
        document.getElementById('compare-results').innerHTML = `
            <div class="loading">
                <div class="spinner"></div>
                <p>Fetching modules for <strong>${board2.port}-${board2.board}</strong>...</p>
                <div class="progress-step">Step 2 of 3</div>
            </div>
        `;
        
        console.log('Fetching modules for board 2...');
        const modules2 = await getBoardModules(board2);
        
        // Small delay to show progress
        await new Promise(resolve => setTimeout(resolve, 300));
        
        // Update progress for comparison
        document.getElementById('compare-results').innerHTML = `
            <div class="loading">
                <div class="spinner"></div>
                <p>Analyzing differences...</p>
                <div class="progress-step">Step 3 of 3</div>
            </div>
        `;
        
        // Small delay to show final step
        await new Promise(resolve => setTimeout(resolve, 200));
        
        console.log(`Board 1 has ${modules1.length} modules, Board 2 has ${modules2.length} modules`);
        
        comparisonData = { board1, board2, modules1, modules2 };
        updateComparison();
        
        // Update URL for shareable links
        const hideCommon = document.getElementById('hide-common').checked;
        const showDetails = document.getElementById('detailed-compare').checked;
        updateURL({
            view: 'compare',
            board1: `${board1.port}-${board1.board}`,
            board2: `${board2.port}-${board2.board}`,
            diff: hideCommon ? 'true' : 'false',
            detailed: showDetails ? 'true' : 'false'
        });
    } catch (error) {
        console.error('Error during comparison:', error);
        document.getElementById('compare-results').innerHTML = `
            <div class="detail-view">
                <h3 style="color: #dc3545;">⚠️ Comparison Error</h3>
                <p style="color: #666; margin: 15px 0;">${error.message}</p>
                <button onclick="compareBoards()" style="margin-top: 15px; padding: 10px 20px; background: #667eea; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600;">
                    ${Icons.create('retry')} Try Again
                </button>
            </div>
        `;
    }
}

function updateComparison() {
    if (!comparisonData) return;
    
    console.log('Updating comparison display...');
    
    const { board1, board2, modules1, modules2 } = comparisonData;
    const hideCommon = document.getElementById('hide-common').checked;
    const showDetails = document.getElementById('detailed-compare').checked; // Fixed ID
    
    // Get module names for comparison
    const moduleNames1 = new Set(modules1.map(m => m.name));
    const moduleNames2 = new Set(modules2.map(m => m.name));
    
    const commonNames = [...moduleNames1].filter(m => moduleNames2.has(m));
    const uniqueNames1 = [...moduleNames1].filter(m => !moduleNames2.has(m));
    const uniqueNames2 = [...moduleNames2].filter(m => !moduleNames1.has(m));
    
    console.log(`Common: ${commonNames.length}, Unique to 1: ${uniqueNames1.length}, Unique to 2: ${uniqueNames2.length}`);
    
    // Update stats
    document.getElementById('compare-stats').style.display = 'block';
    document.getElementById('compare-stats').innerHTML = `
        <div class="stats">
            <div class="stat-card">
                <div class="stat-value">${commonNames.length}</div>
                <div class="stat-label">Common Modules</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">${uniqueNames1.length}</div>
                <div class="stat-label">Unique to ${board1.port}-${board1.board}</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">${uniqueNames2.length}</div>
                <div class="stat-label">Unique to ${board2.port}-${board2.board}</div>
            </div>
        </div>
    `;
    
    // Build comparison HTML
    let html = `
        <div class="comparison-grid">
            <div class="board-section">
                <div class="board-header">${board1.port}-${board1.board} (${board1.version})</div>
                <div class="module-list">
                    <h3>Modules (${moduleNames1.size})</h3>
    `;
    
    // Board 1 modules
    const board1ModulesToShow = hideCommon ? 
        modules1.filter(m => uniqueNames1.includes(m.name)) : 
        modules1.sort((a, b) => a.name.localeCompare(b.name));
    
    board1ModulesToShow.forEach(module => {
        const isUnique = uniqueNames1.includes(module.name);
        const cssClass = isUnique ? 'module-item unique-to-board1' : 'module-item';
        const badge = isUnique ? ' [UNIQUE]' : '';
        
        html += `
            <div class="${cssClass}">
                <div class="module-name">${module.name}${badge}</div>
        `;
        
        // Show detailed information if enabled
        if (showDetails) {
            const classCount = module.classes.length;
            const funcCount = module.functions.length;
            const constCount = module.constants ? module.constants.length : 0;
            
            html += `
                <div class="module-details">
                    ${classCount > 0 ? `<div>Classes: ${classCount}</div>` : ''}
                    ${funcCount > 0 ? `<div>Functions: ${funcCount}</div>` : ''}
                    ${constCount > 0 ? `<div>Constants: ${constCount}</div>` : ''}
                </div>
            `;
            
            // Show classes
            if (classCount > 0) {
                html += '<div class="class-list">';
                module.classes.forEach(cls => {
                    html += `<div class="class-item">${cls.name} (${cls.methods.length} methods)</div>`;
                });
                html += '</div>';
            }
        }
        
        html += '</div>';
    });
    
    if (hideCommon && uniqueNames1.length === 0) {
        html += '<p style="color: #666; padding: 20px;">No unique modules</p>';
    }
    
    html += `
                </div>
            </div>
            <div class="board-section">
                <div class="board-header">${board2.port}-${board2.board} (${board2.version})</div>
                <div class="module-list">
                    <h3>Modules (${moduleNames2.size})</h3>
    `;
    
    // Board 2 modules
    const board2ModulesToShow = hideCommon ? 
        modules2.filter(m => uniqueNames2.includes(m.name)) : 
        modules2.sort((a, b) => a.name.localeCompare(b.name));
    
    board2ModulesToShow.forEach(module => {
        const isUnique = uniqueNames2.includes(module.name);
        const cssClass = isUnique ? 'module-item unique-to-board2' : 'module-item';
        const badge = isUnique ? ' [UNIQUE]' : '';
        
        html += `
            <div class="${cssClass}">
                <div class="module-name">${module.name}${badge}</div>
        `;
        
        // Show detailed information if enabled
        if (showDetails) {
            const classCount = module.classes.length;
            const funcCount = module.functions.length;
            const constCount = module.constants ? module.constants.length : 0;
            
            html += `
                <div class="module-details">
                    ${classCount > 0 ? `<div>Classes: ${classCount}</div>` : ''}
                    ${funcCount > 0 ? `<div>Functions: ${funcCount}</div>` : ''}
                    ${constCount > 0 ? `<div>Constants: ${constCount}</div>` : ''}
                </div>
            `;
            
            // Show classes
            if (classCount > 0) {
                html += '<div class="class-list">';
                module.classes.forEach(cls => {
                    html += `<div class="class-item">${cls.name} (${cls.methods.length} methods)</div>`;
                });
                html += '</div>';
            }
        }
        
        html += '</div>';
    });
    
    if (hideCommon && uniqueNames2.length === 0) {
        html += '<p style="color: #666; padding: 20px;">No unique modules</p>';
    }
    
    html += `
                </div>
            </div>
        </div>
    `;
    
    // Show common modules if not hidden
    if (!hideCommon && commonNames.length > 0) {
        html += `
            <div class="detail-view">
                <div class="detail-header">Common Modules (${commonNames.length})</div>
                <div style="columns: 3; column-gap: 20px;">
        `;
        
        commonNames.sort().forEach(name => {
            html += `<div style='break-inside: avoid; padding: 5px;'>${Icons.create('module')} ${name}</div>`;
        });
        
        html += `
                </div>
            </div>
        `;
    }
    
    document.getElementById('compare-results').innerHTML = html;
    console.log('Comparison display updated');
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
    
    if (!db) {
        alert('Database not available for searching');
        return;
    }
    
    // Enhanced loading indicator for search
    document.getElementById('search-results').innerHTML = `
        <div class="loading">
            <div class="spinner"></div>
            <p>Searching for "<strong>${query}</strong>"...</p>
            <div class="progress-step">Searching across all boards...</div>
        </div>
    `;
    
    const results = [];
    
    // Small delay to show search message
    await new Promise(resolve => setTimeout(resolve, 200));
    
    // Search through all boards using database
    for (const board of boardData.boards) {
        const boardName = `${board.port}-${board.board}`;
        
        try {
            // Search modules
            const moduleStmt = db.prepare(`
                SELECT DISTINCT um.name as module_name
                FROM unique_modules um
                JOIN board_module_support bms ON um.id = bms.module_id
                JOIN boards b ON bms.board_id = b.id
                WHERE b.port = ? AND b.board = ? AND LOWER(um.name) LIKE ?
            `);
            moduleStmt.bind([board.port, board.board, `%${query}%`]);
            
            const modules = [];
            while (moduleStmt.step()) {
                const row = moduleStmt.getAsObject();
                modules.push(row.module_name);
            }
            moduleStmt.free();
            
            if (modules.length > 0) {
                results.push({
                    board: boardName,
                    type: 'module',
                    matches: modules
                });
            }
            
            // Search classes
            const classStmt = db.prepare(`
                SELECT DISTINCT um.name as module_name, uc.name as class_name
                FROM unique_classes uc
                JOIN unique_modules um ON uc.module_id = um.id
                JOIN board_module_support bms ON um.id = bms.module_id
                JOIN boards b ON bms.board_id = b.id
                WHERE b.port = ? AND b.board = ? AND LOWER(uc.name) LIKE ?
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
                SELECT DISTINCT um.name as module_name, uc.name as class_name, umt.name as method_name
                FROM unique_methods umt
                JOIN unique_modules um ON umt.module_id = um.id
                LEFT JOIN unique_classes uc ON umt.class_id = uc.id
                JOIN board_method_support bms ON umt.id = bms.method_id
                JOIN boards b ON bms.board_id = b.id
                WHERE b.port = ? AND b.board = ? AND LOWER(umt.name) LIKE ?
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
    
    displaySearchResults(query, results);
    
    // Update URL for shareable links
    updateURL({
        view: 'search',
        search: query
    });
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
            <div class="search-result-header">${Icons.create('module')} Modules</div>
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
            <div class="search-result-header">${Icons.create('class')} Classes</div>
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
            <div class="search-result-header">${Icons.create('function')} Methods/Functions</div>
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

// Load SQL.js library with better error handling
function loadSqlJs() {
    return new Promise((resolve, reject) => {
        // Check if already loaded
        if (typeof window.initSqlJs === 'function') {
            resolve(window.initSqlJs);
            return;
        }
        
        const script = document.createElement('script');
        script.onload = () => {
            // Wait a bit for the library to initialize
            setTimeout(() => {
                if (typeof window.initSqlJs === 'function') {
                    resolve(window.initSqlJs);
                } else {
                    reject(new Error('SQL.js library did not initialize properly'));
                }
            }, 100);
        };
        script.onerror = (error) => {
            console.error('Failed to load SQL.js from CDN:', error);
            reject(new Error('Failed to load SQL.js library'));
        };
        
        // Try primary CDN first
        script.src = 'https://cdnjs.cloudflare.com/ajax/libs/sql.js/1.8.0/sql-wasm.js';
        document.head.appendChild(script);
    });
}

// Initialize on page load
(async function() {
    try {
        console.log('Starting initialization...');
        
        // Load SQL.js first
        window.initSqlJs = await loadSqlJs();
        console.log('SQL.js loaded successfully');
        
        // Then initialize the app
        await init();
    } catch (error) {
        console.error('Initialization error:', error);
        
        // Try fallback without database
        try {
            console.log('Attempting fallback to JSON data...');
            const response = await fetch('board_comparison.json');
            if (response.ok) {
                boardData = await response.json();
                populateBoardSelects();
                console.log('Loaded fallback JSON data');
            } else {
                throw new Error('No fallback data available');
            }
        } catch (e) {
            console.error('Fallback failed:', e);
            showError('Failed to load board data. Please ensure the database file is available and accessible.');
        }
    }
})();
