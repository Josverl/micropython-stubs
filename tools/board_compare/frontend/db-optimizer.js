/**
 * Database loading optimization functions with IndexedDB caching and cache validation
 * 
 * This module provides SQLite database loading with smart caching using IndexedDB.
 * Features:
 * - HTTP HEAD request validation with Last-Modified, ETag, and Content-Length headers
 * - Automatic cache invalidation when server database is updated
 * - Fallback strategies for network failures
 * - Performance timing and logging
 */

// Database loading optimization functions
window.dbOptimizer = {
    // Performance timing
    performanceNow() {
        return performance.now();
    },

    // IndexedDB caching with cache validation
    async loadDatabaseWithCache(url, cacheKey = 'board_comparison_db', sqlInstance = null) {
        console.log(`${new Date().toLocaleTimeString()} [JS] Loading database with cache key '${cacheKey}'...`);
        const startTime = performance.now();

        try {
            // Check if cache is valid before using it
            const isCacheValid = await this.validateCache(url, cacheKey);

            if (isCacheValid) {
                // Try to load from IndexedDB
                const cachedData = await this.getFromIndexedDB(cacheKey);

                if (cachedData) {
                    console.log(`${new Date().toLocaleTimeString()} [JS] Found valid cached database`);

                    // Use provided SQL.js instance or create new one
                    let SQL;
                    if (sqlInstance) {
                        console.log(`${new Date().toLocaleTimeString()} [JS] Using provided SQL.js instance for cached data`);
                        SQL = sqlInstance;
                    } else {
                        console.log(`${new Date().toLocaleTimeString()} [JS] Creating new SQL.js instance for cached data`);
                        SQL = await initSqlJs({
                            locateFile: file => `https://cdnjs.cloudflare.com/ajax/libs/sql.js/1.13.0/${file}`
                        });
                    }

                    const database = new SQL.Database(new Uint8Array(cachedData));
                    const totalTime = performance.now();

                    console.log(`${new Date().toLocaleTimeString()} [JS] Loaded from cache in ${(totalTime - startTime).toFixed(2)}ms`);
                    return {
                        database: database,
                        timing: {total: totalTime - startTime, source: 'cache'}
                    };
                }
            } else {
                console.log(`${new Date().toLocaleTimeString()} [JS] Cache invalid or outdated, will reload from server`);
            }

            // Load from network and cache
            console.log(`${new Date().toLocaleTimeString()} [JS] Loading from network...`);
            const result = await this.loadDatabaseFromNetwork(url, sqlInstance);

            // Cache the data with metadata from server response
            const dbData = result.database.export();
            await this.saveToIndexedDBWithMetadata(cacheKey, dbData, url, result.response);
            console.log(`${new Date().toLocaleTimeString()} [JS] Database cached for future use`);

            result.timing.source = 'network';
            // Remove response from result to avoid confusion
            delete result.response;
            return result;

        } catch (error) {
            console.error(`${new Date().toLocaleTimeString()} [JS] Cached database load failed:`, error);
            throw error;
        }
    },

    // Internal: Direct network fetch and database creation
    async loadDatabaseFromNetwork(url, sqlInstance = null) {
        console.log(`${new Date().toLocaleTimeString()} [JS] Starting direct fetch from '${url}'...`);
        const startTime = performance.now();

        try {
            const response = await fetch(url);
            if (!response.ok) {
                throw new Error(`HTTP ${response.status}: ${response.statusText}`);
            }

            const fetchTime = performance.now();
            console.log(`${new Date().toLocaleTimeString()} [JS] Fetch completed in ${(fetchTime - startTime).toFixed(2)}ms`);

            const arrayBuffer = await response.arrayBuffer();
            const arrayTime = performance.now();
            console.log(`${new Date().toLocaleTimeString()} [JS] ArrayBuffer created in ${(arrayTime - fetchTime).toFixed(2)}ms`);

            const uint8Array = new Uint8Array(arrayBuffer);
            const arrayCreateTime = performance.now();
            console.log(`${new Date().toLocaleTimeString()} [JS] Uint8Array created in ${(arrayCreateTime - arrayTime).toFixed(2)}ms`);

            // Use provided SQL.js instance or create new one
            let SQL;
            let initTime = arrayCreateTime;
            if (sqlInstance) {
                console.log(`${new Date().toLocaleTimeString()} [JS] Using provided SQL.js instance`);
                SQL = sqlInstance;
            } else {
                console.log(`${new Date().toLocaleTimeString()} [JS] Creating new SQL.js instance`);
                SQL = await initSqlJs({
                    locateFile: file => `https://cdnjs.cloudflare.com/ajax/libs/sql.js/1.13.0/${file}`
                });
                initTime = performance.now();
                console.log(`${new Date().toLocaleTimeString()} [JS] SQL.js initialized in ${(initTime - arrayCreateTime).toFixed(2)}ms`);
            }

            const database = new SQL.Database(uint8Array);
            const totalTime = performance.now();

            console.log(`${new Date().toLocaleTimeString()} [JS] Database created in ${(totalTime - initTime).toFixed(2)}ms`);
            console.log(`${new Date().toLocaleTimeString()} [JS] Total time: ${(totalTime - startTime).toFixed(2)}ms`);

            return {
                database: database,
                response: response, // Include response for header capture
                timing: {
                    total: totalTime - startTime,
                    fetch: fetchTime - startTime,
                    arrayBuffer: arrayTime - fetchTime,
                    uint8Array: arrayCreateTime - arrayTime,
                    sqlInit: initTime - arrayCreateTime,
                    dbCreate: totalTime - initTime
                }
            };
        } catch (error) {
            console.error(`${new Date().toLocaleTimeString()} [JS] Database load failed:`, error);
            throw error;
        }
    },

    // IndexedDB helper functions
    getFromIndexedDB(key) {
        return new Promise((resolve, reject) => {
            const request = indexedDB.open('SQLiteCache', 2);

            request.onerror = () => {
                console.log(`${new Date().toLocaleTimeString()} [JS] IndexedDB open error:`, request.error);
                resolve(null);
            };
            request.onupgradeneeded = (event) => {
                const db = event.target.result;
                if (!db.objectStoreNames.contains('databases')) {
                    db.createObjectStore('databases');
                }
                if (!db.objectStoreNames.contains('metadata')) {
                    db.createObjectStore('metadata');
                }
            };

            request.onsuccess = (event) => {
                const db = event.target.result;

                if (!db.objectStoreNames.contains('databases')) {
                    console.log(`${new Date().toLocaleTimeString()} [JS] No databases store found`);
                    resolve(null);
                    return;
                }

                const transaction = db.transaction(['databases'], 'readonly');
                const store = transaction.objectStore('databases');
                const getRequest = store.get(key);

                getRequest.onerror = () => {
                    console.log(`${new Date().toLocaleTimeString()} [JS] Cache get error:`, getRequest.error);
                    resolve(null);
                };
                getRequest.onsuccess = () => {
                    console.log(`${new Date().toLocaleTimeString()} [JS] Cache get result for '${key}':`, getRequest.result ? 'found' : 'not found');
                    resolve(getRequest.result);
                };
            };
        });
    },

    saveToIndexedDB(key, data) {
        return new Promise((resolve, reject) => {
            const request = indexedDB.open('SQLiteCache', 2);

            request.onerror = () => reject(request.error);
            request.onupgradeneeded = (event) => {
                const db = event.target.result;
                if (!db.objectStoreNames.contains('databases')) {
                    db.createObjectStore('databases');
                }
                if (!db.objectStoreNames.contains('metadata')) {
                    db.createObjectStore('metadata');
                }
            };

            request.onsuccess = (event) => {
                const db = event.target.result;
                const transaction = db.transaction(['databases'], 'readwrite');
                const store = transaction.objectStore('databases');
                const putRequest = store.put(data, key);

                putRequest.onerror = () => reject(putRequest.error);
                putRequest.onsuccess = () => resolve();
            };
        });
    },

    // Cache validation and metadata methods
    async validateCache(url, cacheKey) {
        try {
            // Get cached metadata
            const metadata = await this.getCacheMetadata(cacheKey);

            if (!metadata) {
                console.log(`${new Date().toLocaleTimeString()} [JS] No cache metadata found`);
                return false;
            }

            console.log(`${new Date().toLocaleTimeString()} [JS] Validating cache using HTTP HEAD request...`);

            // Primary strategy: HEAD request to check server state
            try {
                const headResponse = await fetch(url, {method: 'HEAD'});

                if (!headResponse.ok) {
                    console.log(`${new Date().toLocaleTimeString()} [JS] Server returned ${headResponse.status}, using cache`);
                    return true; // Use cache if server is unavailable
                }

                // Check Last-Modified header
                const serverLastModified = headResponse.headers.get('Last-Modified');
                if (serverLastModified && metadata.lastModified) {
                    const serverModTime = new Date(serverLastModified).getTime();
                    const cachedModTime = metadata.lastModified;

                    if (serverModTime > cachedModTime) {
                        console.log(`${new Date().toLocaleTimeString()} [JS] Server file newer: ${new Date(serverModTime).toLocaleString()} > ${new Date(cachedModTime).toLocaleString()}`);
                        return false;
                    }

                    if (serverModTime === cachedModTime) {
                        console.log(`${new Date().toLocaleTimeString()} [JS] Last-Modified match - cache is current`);
                        return true;
                    }
                }

                // Check ETag header
                const serverETag = headResponse.headers.get('ETag');
                if (serverETag && metadata.etag) {
                    if (serverETag !== metadata.etag) {
                        console.log(`${new Date().toLocaleTimeString()} [JS] ETag mismatch - cache invalid`);
                        return false;
                    }

                    console.log(`${new Date().toLocaleTimeString()} [JS] ETag match - cache is current`);
                    return true;
                }

                // Check Content-Length as fallback
                const serverContentLength = headResponse.headers.get('Content-Length');
                if (serverContentLength && metadata.contentLength) {
                    const serverSize = parseInt(serverContentLength);
                    if (serverSize !== metadata.contentLength) {
                        console.log(`${new Date().toLocaleTimeString()} [JS] Content-Length mismatch: ${serverSize} != ${metadata.contentLength}`);
                        return false;
                    }
                }

                // If we have headers but no reliable comparison method, use time-based fallback
                if (!serverLastModified && !serverETag && !serverContentLength) {
                    const maxAgeMs = 5 * 60 * 1000; // 5 minutes for files without headers
                    const cacheAge = Date.now() - metadata.timestamp;

                    if (cacheAge > maxAgeMs) {
                        console.log(`${new Date().toLocaleTimeString()} [JS] No server headers, cache too old: ${Math.round(cacheAge / 1000 / 60)}min`);
                        return false;
                    }
                }

                console.log(`${new Date().toLocaleTimeString()} [JS] Cache validation passed via HTTP HEAD`);
                return true;

            } catch (error) {
                console.log(`${new Date().toLocaleTimeString()} [JS] HEAD request failed:`, error.message);

                // Fallback: time-based validation if network fails
                const maxAgeMs = 10 * 60 * 1000; // 10 minutes when can't check server
                const cacheAge = Date.now() - metadata.timestamp;

                if (cacheAge > maxAgeMs) {
                    console.log(`${new Date().toLocaleTimeString()} [JS] Network check failed and cache too old: ${Math.round(cacheAge / 1000 / 60)}min`);
                    return false;
                }

                console.log(`${new Date().toLocaleTimeString()} [JS] Network check failed but cache recent, using cache`);
                return true;
            }

        } catch (error) {
            console.log(`${new Date().toLocaleTimeString()} [JS] Cache validation error:`, error);
            return false; // If validation fails, reload from server
        }
    },

    async saveToIndexedDBWithMetadata(key, data, url, serverResponse = null) {
        try {
            let metadata = {
                timestamp: Date.now(),
                url: url,
                size: data.length
            };

            // If we have the server response from the initial fetch, use it
            if (serverResponse) {
                const lastModified = serverResponse.headers.get('Last-Modified');
                const etag = serverResponse.headers.get('ETag');
                const contentLength = serverResponse.headers.get('Content-Length');

                if (lastModified) {
                    metadata.lastModified = new Date(lastModified).getTime();
                    console.log(`${new Date().toLocaleTimeString()} [JS] Captured Last-Modified: ${lastModified}`);
                }
                if (etag) {
                    metadata.etag = etag;
                    console.log(`${new Date().toLocaleTimeString()} [JS] Captured ETag: ${etag}`);
                }
                if (contentLength) {
                    metadata.contentLength = parseInt(contentLength);
                    console.log(`${new Date().toLocaleTimeString()} [JS] Captured Content-Length: ${contentLength}`);
                }
            } else {
                // Fallback: separate HEAD request
                try {
                    console.log(`${new Date().toLocaleTimeString()} [JS] Fetching metadata via HEAD request...`);
                    const headResponse = await fetch(url, {method: 'HEAD'});
                    const lastModified = headResponse.headers.get('Last-Modified');
                    const etag = headResponse.headers.get('ETag');
                    const contentLength = headResponse.headers.get('Content-Length');

                    if (lastModified) metadata.lastModified = new Date(lastModified).getTime();
                    if (etag) metadata.etag = etag;
                    if (contentLength) metadata.contentLength = parseInt(contentLength);
                } catch (e) {
                    console.log(`${new Date().toLocaleTimeString()} [JS] Could not fetch server metadata:`, e.message);
                }
            }

            // Save both data and metadata
            await Promise.all([
                this.saveToIndexedDB(key, data),
                this.saveCacheMetadata(key, metadata)
            ]);

            console.log(`${new Date().toLocaleTimeString()} [JS] Saved to cache with metadata:`, {
                timestamp: new Date(metadata.timestamp).toLocaleString(),
                lastModified: metadata.lastModified ? new Date(metadata.lastModified).toLocaleString() : 'none',
                etag: metadata.etag || 'none',
                size: metadata.size
            });
        } catch (error) {
            console.error(`${new Date().toLocaleTimeString()} [JS] Failed to save with metadata:`, error);
            // Fallback to basic save
            await this.saveToIndexedDB(key, data);
        }
    },

    getCacheMetadata(key) {
        return new Promise((resolve) => {
            const request = indexedDB.open('SQLiteCache', 2);

            request.onerror = () => resolve(null);
            request.onupgradeneeded = (event) => {
                const db = event.target.result;
                if (!db.objectStoreNames.contains('databases')) {
                    db.createObjectStore('databases');
                }
                if (!db.objectStoreNames.contains('metadata')) {
                    db.createObjectStore('metadata');
                }
            };

            request.onsuccess = (event) => {
                const db = event.target.result;

                if (!db.objectStoreNames.contains('metadata')) {
                    resolve(null);
                    return;
                }

                const transaction = db.transaction(['metadata'], 'readonly');
                const store = transaction.objectStore('metadata');
                const getRequest = store.get(key + '_meta');

                getRequest.onerror = () => resolve(null);
                getRequest.onsuccess = () => resolve(getRequest.result);
            };
        });
    },

    saveCacheMetadata(key, metadata) {
        return new Promise((resolve, reject) => {
            const request = indexedDB.open('SQLiteCache', 2);

            request.onerror = () => reject(request.error);
            request.onupgradeneeded = (event) => {
                const db = event.target.result;
                if (!db.objectStoreNames.contains('databases')) {
                    db.createObjectStore('databases');
                }
                if (!db.objectStoreNames.contains('metadata')) {
                    db.createObjectStore('metadata');
                }
            };

            request.onsuccess = (event) => {
                const db = event.target.result;
                const transaction = db.transaction(['metadata'], 'readwrite');
                const store = transaction.objectStore('metadata');
                const putRequest = store.put(metadata, key + '_meta');

                putRequest.onerror = () => reject(putRequest.error);
                putRequest.onsuccess = () => resolve();
            };
        });
    },

    // Manual cache control methods
    async clearCache(cacheKey = null) {
        const keys = cacheKey ? [cacheKey] : ['board_comparison_db'];

        for (const key of keys) {
            await Promise.all([
                this.deleteFromIndexedDB(key),
                this.deleteFromIndexedDB(key + '_meta')
            ]);
        }

        console.log(`${new Date().toLocaleTimeString()} [JS] Cache cleared for keys:`, keys);
    },

    deleteFromIndexedDB(key) {
        return new Promise((resolve, reject) => {
            const request = indexedDB.open('SQLiteCache', 2);

            request.onerror = () => reject(request.error);
            request.onsuccess = (event) => {
                const db = event.target.result;

                // Try to delete from both stores
                const dbTransaction = db.transaction(['databases'], 'readwrite');
                const dbStore = dbTransaction.objectStore('databases');
                dbStore.delete(key);

                if (db.objectStoreNames.contains('metadata')) {
                    const metaTransaction = db.transaction(['metadata'], 'readwrite');
                    const metaStore = metaTransaction.objectStore('metadata');
                    metaStore.delete(key);
                }

                resolve();
            };
        });
    }
};