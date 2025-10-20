#!/usr/bin/env python3
"""
Test to verify the dbOptimizer JavaScript extraction works correctly.
This should verify that the external db-optimizer.js file is properly loaded
and provides the same functionality as the previous inline code.
"""

import asyncio
import sys
from pathlib import Path

from playwright.async_api import async_playwright


async def test_extracted_js():
    """Test that the extracted JavaScript file loads and works properly."""

    frontend_dir = Path(__file__).parent / "frontend"
    html_file = frontend_dir / "board-explorer-mpy.html"
    js_file = frontend_dir / "db-optimizer.js"

    print(f"Testing extracted JavaScript functionality...")
    print(f"HTML file: {html_file}")
    print(f"JS file: {js_file}")

    if not html_file.exists():
        print(f"❌ HTML file not found: {html_file}")
        return False

    if not js_file.exists():
        print(f"❌ JS file not found: {js_file}")
        return False

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        # Set up console monitoring
        console_messages = []
        page.on("console", lambda msg: console_messages.append(f"{msg.type}: {msg.text}"))

        try:
            # Navigate to the HTML file
            file_url = f"file://{html_file.absolute()}"
            print(f"Loading: {file_url}")
            await page.goto(file_url)

            # Wait for page to load
            await page.wait_for_timeout(2000)

            # Check if dbOptimizer is available
            db_optimizer_exists = await page.evaluate("typeof window.dbOptimizer !== 'undefined'")

            if not db_optimizer_exists:
                print("❌ window.dbOptimizer not found")
                print("Console messages:")
                for msg in console_messages:
                    print(f"  {msg}")
                return False

            print("✅ window.dbOptimizer is available")

            # Check if key methods exist
            methods_to_check = [
                "loadDatabaseWithCache",
                "validateCache",
                "loadDatabaseFromNetwork",
                "getFromIndexedDB",
                "saveToIndexedDB",
                "clearCache",
            ]

            missing_methods = []
            for method in methods_to_check:
                method_exists = await page.evaluate(f"typeof window.dbOptimizer.{method} === 'function'")
                if method_exists:
                    print(f"✅ dbOptimizer.{method}() exists")
                else:
                    print(f"❌ dbOptimizer.{method}() missing")
                    missing_methods.append(method)

            if missing_methods:
                print(f"❌ Missing methods: {missing_methods}")
                return False

            # Test a simple method call
            try:
                perf_now = await page.evaluate("window.dbOptimizer.performanceNow()")
                if isinstance(perf_now, (int, float)) and perf_now > 0:
                    print(f"✅ dbOptimizer.performanceNow() works: {perf_now:.2f}")
                else:
                    print(f"❌ dbOptimizer.performanceNow() returned invalid value: {perf_now}")
                    return False
            except Exception as e:
                print(f"❌ Error calling dbOptimizer.performanceNow(): {e}")
                return False

            print("✅ All tests passed - JavaScript extraction successful!")
            return True

        except Exception as e:
            print(f"❌ Test failed with error: {e}")
            print("Console messages:")
            for msg in console_messages:
                print(f"  {msg}")
            return False
        finally:
            await browser.close()


if __name__ == "__main__":
    result = asyncio.run(test_extracted_js())
    sys.exit(0 if result else 1)
