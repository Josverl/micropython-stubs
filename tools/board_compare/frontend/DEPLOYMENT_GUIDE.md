# Database Deployment Guide

This guide explains how to deploy the SQLite database for each optimization option.

## Current Setup (Development)

The database is currently served from:
```
http://localhost:8080/frontend/board_comparison.db
```

## Production Deployment Options

### Option 1: JavaScript Direct Fetch

**What you need to deploy:**
- `board_comparison.db` file
- Updated JavaScript with production database URL

**Steps:**
1. Upload `board_comparison.db` to your web server
2. Update the database URL in JavaScript:
   ```javascript
   // Change from:
   const dbUrl = './board_comparison.db';
   // To:
   const dbUrl = 'https://your-domain.com/data/board_comparison.db';
   ```

**Example deployment structures:**
```
# Static hosting (GitHub Pages, Netlify)
your-repo/
├── index.html
├── main.js
├── data/
│   └── board_comparison.db  # Accessible as /data/board_comparison.db
└── assets/

# CDN hosting
https://cdn.your-site.com/
├── databases/
│   └── board_comparison.db  # Global distribution
└── assets/
```

### Option 3: Web Worker

**What you need to deploy:**
- `board_comparison.db` file  
- `sql-worker.js` file
- Updated URLs in both main script and worker

**Steps:**
1. Upload both `board_comparison.db` and `sql-worker.js` to web server
2. Update worker creation:
   ```javascript
   // Ensure worker script is accessible
   const worker = new Worker('./sql-worker.js'); // or full URL
   ```
3. Update database URL in worker script:
   ```javascript
   // In sql-worker.js, update fetch URL for production
   ```

**Same-origin requirement:** Worker and main page must be served from same domain.

### Option 4: IndexedDB Caching  

**What you need to deploy:**
- `board_comparison.db` file (initial download only)
- JavaScript with cache management

**Steps:**
1. Upload `board_comparison.db` to web server
2. Update database URL for initial fetch:
   ```javascript
   async loadDatabaseWithCache(url, cacheKey = 'board_comparison_db') {
       // url should point to production database location
   }
   ```

**Benefits for deployment:**
- Users only download database once
- Reduces server bandwidth after first visit
- Better performance for returning users
- Automatic cache invalidation possible

## Recommended Production Setup

### For GitHub Pages / Static Hosting

```bash
# Directory structure
your-repo/
├── index.html
├── js/
│   ├── main.js
│   └── sql-worker.js
├── data/
│   └── board_comparison.db
└── css/
    └── style.css
```

**JavaScript configuration:**
```javascript
// Use relative URLs for same-origin deployment
const DATABASE_URL = './data/board_comparison.db';

// Or use full URLs for CDN deployment  
const DATABASE_URL = 'https://cdn.your-site.com/board_comparison.db';
```

### For CDN Distribution

```bash
# Main site
https://your-site.com/
├── index.html
├── main.js
└── ...

# CDN for database
https://cdn.your-site.com/
└── board_comparison.db
```

**CORS configuration needed:**
```
Access-Control-Allow-Origin: https://your-site.com
Access-Control-Allow-Methods: GET
```

## File Size Considerations

Current database size: ~4.5MB (typical for board comparison data)

**Bandwidth impact:**
- **Option 1**: 4.5MB download every visit
- **Option 3**: 4.5MB download every visit  
- **Option 4**: 4.5MB first visit, ~0KB subsequent visits

**Recommendation:** Use Option 4 (IndexedDB) to minimize bandwidth costs.

## Cache Management (Option 4)

**Cache invalidation strategies:**

1. **Version-based caching:**
   ```javascript
   const DB_VERSION = "v2.1.0";
   const cacheKey = `board_comparison_${DB_VERSION}`;
   ```

2. **Timestamp-based caching:**
   ```javascript
   const cacheKey = `board_comparison_${Date.now()}`;
   ```

3. **Manual cache clearing:**
   ```javascript
   // Provide UI button to clear cache
   async clearCache() {
       await this.deleteFromIndexedDB('board_comparison_db');
   }
   ```

## Testing Deployment

**Local testing:**
```bash
# Test with simple HTTP server
python -m http.server 8080
# Access: http://localhost:8080
```

**Production testing checklist:**
- [ ] Database file accessible via direct URL
- [ ] CORS headers configured (if cross-origin)
- [ ] JavaScript console shows no 404 errors
- [ ] Database loads and returns 38 boards
- [ ] Cache works on second page visit (Option 4)

## Monitoring

**Key metrics to track:**
- Database download time
- Cache hit rate (Option 4)
- Error rates for database loading
- User retention (faster loading = better retention)

**Browser DevTools monitoring:**
```javascript
// Add performance logging
console.log(`Database loaded in ${loadTime}ms`);
console.log(`Cache source: ${isCached ? 'IndexedDB' : 'Network'}`);
```