// Web Worker for SQL.js database loading
// This runs in a separate thread to avoid blocking the main UI

console.log('SQL.js Web Worker initialized');

// Import SQL.js in the worker context
importScripts('https://cdnjs.cloudflare.com/ajax/libs/sql.js/1.13.0/sql-wasm.js');

let SQL = null;

// Initialize SQL.js in worker
async function initializeSQL() {
    if (!SQL) {
        SQL = await initSqlJs({
            locateFile: file => `https://cdnjs.cloudflare.com/ajax/libs/sql.js/1.13.0/${file}`
        });
        console.log('SQL.js initialized in worker');
    }
    return SQL;
}

// Handle messages from main thread
self.onmessage = async function(event) {
    const { action, data, id } = event.data;
    
    try {
        switch (action) {
            case 'loadDatabase':
                await handleLoadDatabase(data, id);
                break;
                
            case 'executeQuery':
                await handleExecuteQuery(data, id);
                break;
                
            case 'closeDatabase':
                await handleCloseDatabase(data, id);
                break;
                
            default:
                throw new Error(`Unknown action: ${action}`);
        }
    } catch (error) {
        self.postMessage({
            id: id,
            success: false,
            error: error.message,
            stack: error.stack
        });
    }
};

async function handleLoadDatabase(data, id) {
    const startTime = performance.now();
    const { url } = data;
    
    console.log(`[Worker] Loading database from: ${url}`);
    
    // Initialize SQL.js
    await initializeSQL();
    const initTime = performance.now();
    
    // Fetch database
    const response = await fetch(url);
    if (!response.ok) {
        throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }
    
    const fetchTime = performance.now();
    const arrayBuffer = await response.arrayBuffer();
    const bufferTime = performance.now();
    
    // Create database
    const uint8Array = new Uint8Array(arrayBuffer);
    const database = new SQL.Database(uint8Array);
    const dbTime = performance.now();
    
    // Store database reference (simple approach - in real app might use WeakMap)
    self.currentDatabase = database;
    
    const totalTime = dbTime - startTime;
    
    console.log(`[Worker] Database loaded in ${totalTime.toFixed(2)}ms`);
    
    // Send success response
    self.postMessage({
        id: id,
        success: true,
        timing: {
            total: totalTime,
            init: initTime - startTime,
            fetch: fetchTime - initTime,
            buffer: bufferTime - fetchTime,
            database: dbTime - bufferTime
        }
    });
}

async function handleExecuteQuery(data, id) {
    const startTime = performance.now();
    const { sql, params } = data;
    
    if (!self.currentDatabase) {
        throw new Error('No database loaded');
    }
    
    console.log(`[Worker] Executing query: ${sql}`);
    
    const results = self.currentDatabase.exec(sql, params);
    const endTime = performance.now();
    
    console.log(`[Worker] Query executed in ${(endTime - startTime).toFixed(2)}ms`);
    
    // Send results back to main thread
    self.postMessage({
        id: id,
        success: true,
        results: results,
        timing: {
            query: endTime - startTime
        }
    });
}

async function handleCloseDatabase(data, id) {
    if (self.currentDatabase) {
        self.currentDatabase.close();
        self.currentDatabase = null;
        console.log('[Worker] Database closed');
    }
    
    self.postMessage({
        id: id,
        success: true
    });
}