"""
Comprehensive database optimization test with MicroPython query validation
Tests all options and verifies they return the expected count of 38 boards
"""

import asyncio
import subprocess
import time

from playwright.async_api import async_playwright


async def comprehensive_test():
    """Test all database loading options with query validation"""

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, devtools=True, slow_mo=500)
        page = await browser.new_page()

        # Start server
        server = subprocess.Popen(["python", "-m", "http.server", "8080"], cwd="d:/mypython/micropython-stubs/tools/board_compare")

        try:
            await asyncio.sleep(2)
            await page.goto("http://localhost:8080/frontend/test-database-optimization.html")
            await page.wait_for_selector("text=Ready to test", timeout=15000)

            print("🧪 COMPREHENSIVE DATABASE OPTIMIZATION TEST")
            print("=" * 60)
            print("Testing all options with MicroPython query: SELECT count(*) FROM boards")
            print("Expected result: 38 boards\n")

            # Test results storage
            test_results = {}

            # Test Option 1: JavaScript Direct
            print("📋 Testing Option 1: JavaScript Direct")
            result = await test_option(page, 1, "JavaScript Direct")
            test_results["Option 1"] = result

            await asyncio.sleep(2)

            # Test Option 3: Web Worker
            print("📋 Testing Option 3: Web Worker")
            result = await test_option(page, 3, "Web Worker")
            test_results["Option 3"] = result

            await asyncio.sleep(2)

            # Test Option 4: IndexedDB Cache (first run)
            print("📋 Testing Option 4: IndexedDB Cache (First Run)")
            result = await test_option(page, 4, "IndexedDB Cache")
            test_results["Option 4 (First)"] = result

            await asyncio.sleep(2)

            # Test Option 4: IndexedDB Cache (cached run)
            print("📋 Testing Option 4: IndexedDB Cache (Cached Run)")
            result = await test_option(page, 4, "IndexedDB Cache (Cached)")
            test_results["Option 4 (Cached)"] = result

            # Print summary
            print("\n" + "=" * 60)
            print("📊 TEST RESULTS SUMMARY")
            print("=" * 60)

            baseline_time = 41000  # 41 seconds baseline

            for option_name, result in test_results.items():
                if result["success"]:
                    improvement = baseline_time / result["load_time"] if result["load_time"] > 0 else 0
                    print(f"\n✅ {option_name}:")
                    print(f"   Load Time: {result['load_time']:.2f}ms")
                    print(f"   Query Validation: {'✅ PASSED' if result['query_valid'] else '❌ FAILED'}")
                    print(f"   Board Count: {result['board_count']} (Expected: 38)")
                    print(f"   Performance Improvement: {improvement:.1f}x faster")
                    print(f"   Time Saved: {baseline_time - result['load_time']:.0f}ms")
                else:
                    print(f"\n❌ {option_name}: FAILED")
                    print(f"   Error: {result['error']}")

            # Check if all tests passed
            all_passed = all(r["success"] and r["query_valid"] for r in test_results.values())

            print(f"\n{'🎉 ALL TESTS PASSED!' if all_passed else '⚠️  SOME TESTS FAILED'}")
            print("=" * 60)

        finally:
            await browser.close()
            server.terminate()


async def test_option(page, option_num, option_name):
    """Test a specific database loading option"""
    try:
        # Clear results
        await page.click('button:text("Clear Results")')
        await asyncio.sleep(0.5)

        # Record start time
        start_time = time.time()

        # Click option button
        button_text = f"Option {option_num}"
        await page.click(f'button:text("{button_text}")')

        # Wait for completion
        await page.wait_for_function(
            """
            document.getElementById('results').textContent.includes('SUCCESS') || 
            document.getElementById('results').textContent.includes('FAILED') ||
            document.getElementById('results').textContent.includes('VALIDATION')
            """,
            timeout=30000,
        )

        end_time = time.time()
        total_python_time = (end_time - start_time) * 1000

        # Get results text
        results_text = await page.inner_text("#results")

        # Parse results
        result = {"success": "SUCCESS" in results_text, "error": None, "load_time": 0, "query_valid": False, "board_count": 0}

        if result["success"]:
            # Extract load time
            for line in results_text.split("\n"):
                if "Total time:" in line:
                    try:
                        time_str = line.split(":")[1].strip().replace("ms", "")
                        result["load_time"] = float(time_str)
                    except Exception:
                        result["load_time"] = total_python_time

                # Extract board count and validation
                if "Query result:" in line and "boards found" in line:
                    try:
                        count_str = line.split("Query result:")[1].split("boards found")[0].strip()
                        result["board_count"] = int(count_str)
                    except Exception:
                        pass

                if "VALIDATION PASSED" in line:
                    result["query_valid"] = True
                elif "VALIDATION FAILED" in line:
                    result["query_valid"] = False
        else:
            # Extract error
            error_lines = [line for line in results_text.split("\n") if "FAILED" in line]
            result["error"] = error_lines[0] if error_lines else "Unknown error"

        # Print immediate results
        status = "✅ PASS" if result["success"] and result["query_valid"] else "❌ FAIL"
        print(f"   {status} - {result['load_time']:.2f}ms - {result['board_count']} boards")

        return result

    except Exception as e:
        print(f"   ❌ EXCEPTION: {str(e)}")
        return {"success": False, "error": str(e), "load_time": 0, "query_valid": False, "board_count": 0}


if __name__ == "__main__":
    asyncio.run(comprehensive_test())
