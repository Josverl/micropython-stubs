#!/usr/bin/env python3
"""
Simple test to verify the application loads with external JavaScript.
"""

import asyncio
import sys
from pathlib import Path

from playwright.async_api import async_playwright


async def test_app_loads():
    """Test that the application loads properly with external JS."""

    frontend_dir = Path(__file__).parent / "frontend"
    html_file = frontend_dir / "board-explorer-mpy.html"

    print("Testing application loading with extracted JavaScript...")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        console_messages = []
        page.on("console", lambda msg: console_messages.append(f"{msg.type}: {msg.text}"))

        try:
            file_url = f"file://{html_file.absolute()}"
            print(f"Loading: {file_url}")
            await page.goto(file_url)

            # Wait for PyScript and dbOptimizer to load
            await page.wait_for_timeout(3000)

            # Check if basic components are available
            checks = []

            # Check if dbOptimizer loaded
            db_optimizer_exists = await page.evaluate("typeof window.dbOptimizer !== 'undefined'")
            checks.append(("dbOptimizer loaded", db_optimizer_exists))

            # Check if PyScript is available
            pyscript_exists = await page.evaluate("typeof pyscript !== 'undefined'")
            checks.append(("PyScript loaded", pyscript_exists))

            # Check if the page title is correct
            title = await page.title()
            title_correct = "MicroPython Board Explorer" in title
            checks.append(("Page title correct", title_correct))

            # Print results
            all_passed = True
            for check_name, passed in checks:
                status = "✅" if passed else "❌"
                print(f"{status} {check_name}")
                if not passed:
                    all_passed = False

            if all_passed:
                print("✅ Application loads successfully with external JavaScript!")
                return True
            else:
                print("❌ Some checks failed")
                return False

        except Exception as e:
            print(f"❌ Test failed with error: {e}")
            return False
        finally:
            await browser.close()


if __name__ == "__main__":
    result = asyncio.run(test_app_loads())
    sys.exit(0 if result else 1)
