"""
Test to verify that initSqlJs is only called once when using the optimized methods

This test should show:
1. SQL.js initialized once in Python
2. JavaScript functions use the existing instance
3. No duplicate initialization
"""

import asyncio

import js
from sqlite_wasm import SQLite


async def test_single_initialization():
    """Test that SQL.js is initialized only once"""

    print("🔧 Testing single SQL.js initialization...")

    # Step 1: Initialize SQL.js once
    print("📝 Step 1: Initializing SQL.js...")
    sql = await SQLite.initialize(version="1.13.0", cdn="cdnjs")
    print("✅ SQL.js initialized in Python")

    # Step 2: Test Option 1 (should NOT call initSqlJs again)
    print("\n📝 Step 2: Testing Option 1 (direct JS fetch)...")
    try:
        # This should reuse the existing SQL.js instance
        result = await js.window.dbOptimizer.loadDatabaseFromUrl(
            "./board_comparison.db",
            sql._sql,  # Pass the existing SQL.js instance
        )
        print("✅ Option 1: Used existing SQL.js instance")
    except Exception as e:
        print(f"❌ Option 1 failed: {e}")

    # Step 3: Test Option 4 (should NOT call initSqlJs again)
    print("\n📝 Step 3: Testing Option 4 (IndexedDB cache)...")
    try:
        # This should reuse the existing SQL.js instance
        result = await js.window.dbOptimizer.loadDatabaseWithCache(
            "./board_comparison.db",
            "test_cache_key",
            sql._sql,  # Pass the existing SQL.js instance
        )
        print("✅ Option 4: Used existing SQL.js instance")
    except Exception as e:
        print(f"❌ Option 4 failed: {e}")

    # Step 4: Test the new data loading methods
    print("\n📝 Step 4: Testing new parallel data loading methods...")
    try:
        # Load data using the optimized methods
        data = await sql.load_database_data("./board_comparison.db")
        print(f"✅ Loaded database data: {len(data)} bytes")

        # Create database from data
        db = sql.create_database_from_data(data)

        # Test query
        result = db.exec("SELECT count(*) as count FROM boards")
        if result and len(result) > 0:
            count = result[0]["values"][0][0]
            print(f"✅ Database query successful: {count} boards")

    except Exception as e:
        print(f"❌ Data loading test failed: {e}")

    print("\n🎉 Test completed!")
    print("📊 Check console logs to verify initSqlJs was called only once")


# Usage instructions for PyScript:
#
# In the browser console, you should see:
# ✅ "Calling window.initSqlJs..." (once during Python initialization)
# ✅ "Using provided SQL.js instance" (for JavaScript optimization calls)
# ❌ NO additional "SQL.js initialized in..." messages from JavaScript
#
# If you see multiple "SQL.js initialized" messages, then initSqlJs is being
# called multiple times and we need to debug further.

# Run this test:
# await test_single_initialization()
