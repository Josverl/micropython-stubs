"""
Quick test to check for PyScript errors
"""

import asyncio

from playwright.async_api import async_playwright


async def test_errors():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, devtools=True)
        page = await browser.new_page()

        # Capture console messages
        console_logs = []
        page.on("console", lambda msg: console_logs.append(f"[{msg.type}] {msg.text}"))
        page.on("pageerror", lambda exc: console_logs.append(f"PAGE ERROR: {exc}"))

        # Start server
        import subprocess

        server = subprocess.Popen(["python", "-m", "http.server", "8080"], cwd="d:/mypython/micropython-stubs/tools/board_compare")

        try:
            await asyncio.sleep(2)
            await page.goto("http://localhost:8080/frontend/test-database-optimization.html")
            await page.wait_for_selector("text=Ready to test", timeout=15000)

            print("✅ Page loaded successfully")

            # Test Option 1 (should work)
            print("Testing Option 1...")
            await page.click('button:text("Option 1: JS Direct")')
            await asyncio.sleep(3)

            # Check for errors
            print("\n=== RECENT CONSOLE LOGS ===")
            error_found = False
            for log in console_logs[-15:]:  # Last 15 logs
                if "Traceback" in log or "ImportError" in log:
                    print(f"❌ ERROR: {log}")
                    error_found = True
                elif "Error" in log and "Failed to load resource" not in log:
                    print(f"⚠️  WARNING: {log}")
                elif "SUCCESS" in log or "Total time" in log:
                    print(f"✅ SUCCESS: {log}")

            if not error_found:
                print("✅ No Python/PyScript errors found!")
            else:
                print("❌ Found PyScript errors that need fixing")

        finally:
            await browser.close()
            server.terminate()


if __name__ == "__main__":
    asyncio.run(test_errors())
