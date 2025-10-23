#!/usr/bin/env python3
"""
Test that only Option 4 (IndexedDB caching) is available after cleanup.
"""

import asyncio

from playwright.async_api import async_playwright


async def test_option4_only():
    """Test that we only have IndexedDB caching functionality."""

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        # Enable console logging
        page.on("console", lambda msg: print(f"[BROWSER] {msg.text}"))

        # Navigate to the test page
        await page.goto("http://127.0.0.1:8000/board-explorer-mpy.html")

        # Wait for the dbOptimizer to be available
        await page.wait_for_function("window.dbOptimizer", timeout=15000)

        print("\n=== Checking available dbOptimizer methods ===")

        # Check what methods are available
        available_methods = await page.evaluate("""
            Object.keys(window.dbOptimizer).filter(key => typeof window.dbOptimizer[key] === 'function')
        """)

        print(f"Available methods: {available_methods}")

        # Verify we only have the expected methods for Option 4
        expected_methods = [
            "performanceNow",
            "loadDatabaseWithCache",
            "loadDatabaseFromNetwork",
            "getFromIndexedDB",
            "saveToIndexedDB",
            "validateCache",
            "saveToIndexedDBWithMetadata",
            "getCacheMetadata",
            "saveCacheMetadata",
            "clearCache",
            "deleteFromIndexedDB",
        ]

        missing_methods = [m for m in expected_methods if m not in available_methods]
        extra_methods = [m for m in available_methods if m not in expected_methods]

        if missing_methods:
            print(f"❌ Missing expected methods: {missing_methods}")
        if extra_methods:
            print(f"⚠️  Extra methods found: {extra_methods}")
        if not missing_methods and not extra_methods:
            print("✅ All expected methods present, no extra methods")

        # Check that old option methods are gone
        removed_methods = ["loadDatabaseFromUrl"]  # This was the main old method
        for method in removed_methods:
            if method in available_methods:
                print(f"❌ Old method still exists: {method}")
            else:
                print(f"✅ Old method removed: {method}")

        print("\n=== Testing IndexedDB caching functionality ===")

        # Clear any existing cache
        await page.evaluate("""
            (async () => {
                if (window.dbOptimizer) {
                    await window.dbOptimizer.clearCache();
                    console.log('Cache cleared for test');
                }
            })()
        """)

        # Test loading database with cache
        await page.evaluate("""
            (async () => {
                try {
                    const result = await window.dbOptimizer.loadDatabaseWithCache(
                        'http://127.0.0.1:8000/board_comparison.db'
                    );
                    console.log('Database loaded successfully with caching');
                    console.log('Timing:', result.timing);
                } catch (error) {
                    console.error('Database loading failed:', error);
                }
            })()
        """)

        print("\n✅ Test completed - check console output above for results")

        await browser.close()


if __name__ == "__main__":
    print("Testing that only Option 4 (IndexedDB caching) is available...")
    asyncio.run(test_option4_only())
