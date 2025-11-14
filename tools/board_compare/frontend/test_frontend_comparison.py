"""
Simplified test to verify numbered parameters work in the frontend.
Uses Playwright with explicit console logging to prove success/failure.
"""

import asyncio
import sys
from pathlib import Path

try:
    from playwright.async_api import async_playwright
except ImportError:
    print("❌ ERROR: Playwright not installed")
    sys.exit(1)


async def test_frontend():
    """Test that comparison works with numbered parameters."""
    print("\n" + "=" * 80)
    print("FRONTEND NUMBERED PARAMETERS TEST")
    print("=" * 80)
    
    console_logs = []
    js_errors = []
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        
        # Capture console and errors
        page.on("console", lambda msg: console_logs.append(f"[{msg.type}] {msg.text}"))
        page.on("pageerror", lambda exc: js_errors.append(str(exc)))
        
        try:
            # Load page
            print("\n1. Loading http://localhost:8080/board-explorer-mpy.html?view=compare")
            await page.goto("http://localhost:8080/board-explorer-mpy.html?view=compare", 
                          wait_until="domcontentloaded", timeout=60000)
            print("   ✅ Page loaded")
            
            # Wait for database to load (check console for "Database ready!")
            print("\n2. Waiting for database initialization (up to 90s)...")
            max_wait = 90
            db_ready = False
            for i in range(max_wait):
                await asyncio.sleep(1)
                if any("Database ready!" in log for log in console_logs):
                    db_ready = True
                    print(f"   ✅ Database loaded in ~{i+1}s")
                    break
            
            if not db_ready:
                print("   ❌ TIMEOUT: Database did not load")
                print("\n   Last 20 console messages:")
                for log in console_logs[-20:]:
                    print(f"      {log}")
                return False
            
            # Wait for compare UI to be visible
            await page.wait_for_selector("#board1-version", state="visible", timeout=10000)
            print("   ✅ Compare UI ready")
            
            # Fill in board selections
            print("\n3. Selecting boards...")
            
            # Board 1: ESP32 v1.26.0
            await page.fill("#board1-version", "v1.26.0")
            await asyncio.sleep(0.2)
            await page.fill("#board1", "esp32_generic")
            await asyncio.sleep(0.2)
            
            # Board 2: STM32 v1.26.0
            await page.fill("#board2-version", "v1.26.0")
            await asyncio.sleep(0.2)
            await page.fill("#board2", "stm32")  # Just "stm32", not "stm32_generic"
            await asyncio.sleep(0.2)
            
            print("   ✅ Boards selected: esp32_generic vs stm32 (v1.26.0)")
            
            # Click compare button (correct ID)
            print("\n4. Clicking Compare button...")
            await page.click("#compare-boards-btn")  # Correct button ID
            
            # Wait for comparison to complete (look for statistics)
            print("\n5. Waiting for comparison results (max 30s)...")
            try:
                await page.wait_for_selector("#compare-stats", state="visible", timeout=30000)
                print("   ✅ Results appeared")
                
                # Extra wait to ensure stats are populated
                await asyncio.sleep(1)
                
            except Exception as e:
                print(f"   ❌ TIMEOUT: Results did not appear within 30s")
                print(f"\n   Last 20 console messages:")
                for log in console_logs[-20:]:
                    print(f"      {log}")
                print(f"\n   JavaScript errors: {len(js_errors)}")
                for err in js_errors:
                    print(f"      {err}")
                return False
            
            # Extract and verify statistics
            print("\n6. Verifying statistics...")
            
            # Check if elements exist and have content
            level1_unique1_elem = await page.query_selector("[data-level1-unique1]")
            if not level1_unique1_elem:
                print("   ❌ FAILED: Statistics elements not found")
                return False
            
            level1_unique1 = await level1_unique1_elem.text_content()
            level1_unique2 = await page.text_content("[data-level1-unique2]")
            level1_common = await page.text_content("[data-level1-common]")
            
            level2_classes1 = await page.text_content("[data-level2-classes1-unique]")
            level2_classes2 = await page.text_content("[data-level2-classes2-unique]")
            
            level3_methods1 = await page.text_content("[data-level3-methods1-unique]")
            level3_methods2 = await page.text_content("[data-level3-methods2-unique]")
            
            print(f"\n   Results extracted:")
            print(f"      Level 1: Unique ESP32={level1_unique1}, Unique STM32={level1_unique2}, Common={level1_common}")
            print(f"      Level 2: Classes ESP32={level2_classes1}, Classes STM32={level2_classes2}")
            print(f"      Level 3: Methods ESP32={level3_methods1}, Methods STM32={level3_methods2}")
            
            # Validate against expected values (from MCP testing)
            expected = {
                "level1_unique1": "26",
                "level1_unique2": "3",
                "level1_common": "44",
                "level2_classes1": "34",
                "level2_classes2": "24",
                "level3_methods1": "207",
                "level3_methods2": "291",
            }
            
            actual = {
                "level1_unique1": level1_unique1.strip(),
                "level1_unique2": level1_unique2.strip(),
                "level1_common": level1_common.strip(),
                "level2_classes1": level2_classes1.strip(),
                "level2_classes2": level2_classes2.strip(),
                "level3_methods1": level3_methods1.strip(),
                "level3_methods2": level3_methods2.strip(),
            }
            
            print(f"\n7. Validating results...")
            all_correct = True
            for key, expected_val in expected.items():
                actual_val = actual[key]
                match = "✅" if actual_val == expected_val else "❌"
                print(f"   {match} {key}: expected={expected_val}, actual={actual_val}")
                if actual_val != expected_val:
                    all_correct = False
            
            # Check for JS errors
            if js_errors:
                print(f"\n   ❌ JavaScript errors detected ({len(js_errors)}):")
                for err in js_errors[:5]:  # Show first 5
                    print(f"      {err}")
                all_correct = False
            else:
                print(f"\n   ✅ No JavaScript errors")
            
            return all_correct
            
        except Exception as e:
            print(f"\n❌ TEST EXCEPTION: {e}")
            print(f"\nRecent console logs:")
            for log in console_logs[-10:]:
                print(f"   {log}")
            return False
            
        finally:
            await browser.close()


async def main():
    """Main entry point."""
    print("\nStarting frontend test...")
    print("Requires: HTTP server running on port 8080")
    
    success = await test_frontend()
    
    print("\n" + "=" * 80)
    if success:
        print("✅✅✅ TEST PASSED: Numbered parameters work correctly!")
        print("=" * 80)
        return 0
    else:
        print("❌❌❌ TEST FAILED: See errors above")
        print("=" * 80)
        return 1


if __name__ == "__main__":
    result = asyncio.run(main())
    sys.exit(result)
