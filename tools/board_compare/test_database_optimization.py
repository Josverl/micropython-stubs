"""
Playwright test for database loading optimization
"""

import asyncio
import time

import pytest
from playwright.async_api import Page, async_playwright


@pytest.mark.asyncio
async def test_database_optimization_with_playwright():
    """Test database loading optimizations using Playwright for proper error visibility"""

    async with async_playwright() as p:
        # Launch browser with dev tools for debugging
        browser = await p.chromium.launch(
            headless=False,  # Set to True for CI/CD
            devtools=True,  # Open dev tools to see console
            slow_mo=1000,  # Slow down for debugging
        )

        page = await browser.new_page()

        # Collect console logs and errors
        console_logs = []
        errors = []

        page.on("console", lambda msg: console_logs.append(f"[{msg.type}] {msg.text}"))
        page.on("pageerror", lambda exc: errors.append(f"Page error: {exc}"))

        server_process = None
        try:
            # Start local server first
            print("Starting local HTTP server...")
            server_process = await start_local_server()

            # Wait a moment for server to start
            await asyncio.sleep(2)

            # Navigate to test page
            print("Loading test page...")
            await page.goto("http://localhost:8080/frontend/test-database-optimization.html")

            # Wait for PyScript to initialize
            print("Waiting for PyScript to initialize...")
            await page.wait_for_selector("text=Ready to test", timeout=30000)

            # Test Option 1: JavaScript Direct
            print("\n=== Testing Option 1: JavaScript Direct ===")
            await test_js_option(page, 1, "JS Direct")

            # Test Option 4: IndexedDB Cache
            print("\n=== Testing Option 4: IndexedDB Cache ===")
            await test_js_option(page, 4, "IndexedDB Cache")

            # Test Python option (this should reveal the import error)
            print("\n=== Testing Python Option ===")
            try:
                # Try to call Python function
                result = await page.evaluate("""
                    window.testPythonOption ? window.testPythonOption(0) : 'Function not available'
                """)
                print(f"Python test result: {result}")
            except Exception as e:
                print(f"Python test failed: {e}")

            # Print all console logs and errors
            print("\n=== Console Logs ===")
            for log in console_logs[-20:]:  # Last 20 logs
                print(log)

            print("\n=== Errors ===")
            for error in errors:
                print(error)

            # Wait a bit to see results
            await asyncio.sleep(5)

        finally:
            await browser.close()
            # Stop server
            try:
                if server_process:
                    server_process.terminate()
            except Exception:
                pass  # Server might already be stopped


async def test_js_option(page: Page, option_num: int, option_name: str):
    """Test a JavaScript option"""
    try:
        start_time = time.time()

        # Clear results first
        await page.click("button:text('Clear Results')")
        await asyncio.sleep(0.5)

        # Click the option button
        await page.click(f"button:text('Option {option_num}')")

        # Wait for completion (look for success or failure message)
        await page.wait_for_function(
            "document.getElementById('results').textContent.includes('SUCCESS') || document.getElementById('results').textContent.includes('FAILED')",
            timeout=60000,
        )

        # Get results
        results = await page.inner_text("#results")
        end_time = time.time()

        print(f"{option_name} completed in {(end_time - start_time):.2f}s")

        if "SUCCESS" in results:
            # Extract timing info
            lines = results.split("\n")
            for line in lines:
                if "Total time:" in line:
                    print(f"  {line.strip()}")
                elif "Test query result:" in line:
                    print(f"  {line.strip()}")
            print("  Status: ✅ SUCCESS")
        else:
            print("  Status: ❌ FAILED")
            # Print error details
            error_lines = [line for line in results.split("\n") if "FAILED" in line or "error" in line.lower()]
            for line in error_lines[:3]:  # First 3 error lines
                print(f"  Error: {line.strip()}")

    except Exception as e:
        print(f"{option_name} test failed with exception: {e}")


async def start_local_server():
    """Start local HTTP server"""
    import subprocess

    # Start server in background
    process = subprocess.Popen(["python", "-m", "http.server", "8080"], cwd="d:/mypython/micropython-stubs/tools/board_compare")

    return process


if __name__ == "__main__":
    # Run the test directly
    asyncio.run(test_database_optimization_with_playwright())
