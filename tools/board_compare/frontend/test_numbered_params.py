"""
Test numbered parameters in web frontend using Playwright.

This script tests that the web application (board-explorer-mpy.html) correctly:
1. Loads the comparison page
2. Selects two boards (ESP32 vs STM32, v1.26.0)
3. Performs comparison using database.py with numbered parameters
4. Verifies results are displayed without errors

Expected results should match compare_esp32_stm32.py output:
- ESP32: 70 modules, STM32: 47 modules
- Unique ESP32: 26, Unique STM32: 3, Common: 44
"""

import asyncio
import sys
from pathlib import Path

try:
    from playwright.async_api import async_playwright
    print("✅ Playwright imported successfully")
except ImportError:
    print("❌ ERROR: Playwright not available")
    print("   Install with: pip install playwright")
    print("   Then run: playwright install")
    sys.exit(1)


async def test_comparison():
    """Test board comparison with numbered parameters."""
    print("\n" + "=" * 80)
    print("Testing Board Comparison Web Frontend")
    print("=" * 80)
    
    async with async_playwright() as p:
        # Launch browser
        print("\n1. Launching browser...")
        browser = await p.chromium.launch(headless=False)  # Visible for debugging
        page = await browser.new_page()
        
        # Listen for console messages
        console_messages = []
        page.on("console", lambda msg: console_messages.append(f"[{msg.type}] {msg.text}"))
        
        # Listen for errors
        errors = []
        page.on("pageerror", lambda exc: errors.append(str(exc)))
        
        try:
            # Load page
            print("\n2. Loading board-explorer-mpy.html...")
            url = "http://localhost:8080/board-explorer-mpy.html?view=compare"
            await page.goto(url, wait_until="networkidle", timeout=30000)
            print("   ✅ Page loaded")
            
            # Wait for PyScript to initialize
            print("\n3. Waiting for PyScript initialization...")
            await page.wait_for_selector("#board1-version", state="visible", timeout=30000)
            print("   ✅ PyScript initialized")
            
            # Select Board 1 (ESP32 v1.26.0)
            print("\n4. Selecting Board 1 (ESP32 v1.26.0)...")
            await page.select_option("#board1-version", "v1.26.0")
            await asyncio.sleep(0.5)  # Wait for board list to update
            await page.select_option("#board1", "esp32/esp32_generic")
            print("   ✅ Board 1 selected")
            
            # Select Board 2 (STM32 v1.26.0)
            print("\n5. Selecting Board 2 (STM32 v1.26.0)...")
            await page.select_option("#board2-version", "v1.26.0")
            await asyncio.sleep(0.5)  # Wait for board list to update
            await page.select_option("#board2", "stm32/pybv11")
            print("   ✅ Board 2 selected")
            
            # Click compare button
            print("\n6. Clicking Compare button...")
            await page.click("#compare-btn")
            
            # Wait for results with explicit logging
            print("\n7. Waiting for comparison results...")
            try:
                # Wait for stats to appear (indicates comparison completed)
                await page.wait_for_selector("#compare-stats", state="visible", timeout=60000)
                print("   ✅ Comparison completed")
            except Exception as e:
                print(f"   ❌ Timeout waiting for results: {e}")
                print("\n   Recent console messages:")
                for msg in console_messages[-10:]:
                    print(f"      {msg}")
                raise
            
            # Extract statistics
            print("\n8. Extracting statistics...")
            
            # Level 1: Module comparison
            level1_unique1 = await page.text_content("[data-level1-unique1]")
            level1_unique2 = await page.text_content("[data-level1-unique2]")
            level1_common = await page.text_content("[data-level1-common]")
            
            print(f"\n   LEVEL 1 - Module Comparison:")
            print(f"      Unique ESP32: {level1_unique1}")
            print(f"      Unique STM32: {level1_unique2}")
            print(f"      Common: {level1_common}")
            
            # Level 2: Classes/Functions/Constants
            level2_classes1 = await page.text_content("[data-level2-classes1-unique]")
            level2_classes2 = await page.text_content("[data-level2-classes2-unique]")
            level2_functions1 = await page.text_content("[data-level2-functions1-unique]")
            level2_functions2 = await page.text_content("[data-level2-functions2-unique]")
            level2_constants1 = await page.text_content("[data-level2-constants1-unique]")
            level2_constants2 = await page.text_content("[data-level2-constants2-unique]")
            
            print(f"\n   LEVEL 2 - Classes/Functions/Constants:")
            print(f"      Classes:    ESP32={level2_classes1}, STM32={level2_classes2}")
            print(f"      Functions:  ESP32={level2_functions1}, STM32={level2_functions2}")
            print(f"      Constants:  ESP32={level2_constants1}, STM32={level2_constants2}")
            
            # Level 3: Methods/Attributes
            level3_methods1 = await page.text_content("[data-level3-methods1-unique]")
            level3_methods2 = await page.text_content("[data-level3-methods2-unique]")
            level3_methods_diff = await page.text_content("[data-level3-methods-different]")
            level3_attrs1 = await page.text_content("[data-level3-attributes1-unique]")
            level3_attrs2 = await page.text_content("[data-level3-attributes2-unique]")
            
            print(f"\n   LEVEL 3 - Methods/Attributes:")
            print(f"      Methods:    ESP32={level3_methods1}, STM32={level3_methods2}, Different={level3_methods_diff}")
            print(f"      Attributes: ESP32={level3_attrs1}, STM32={level3_attrs2}")
            
            # Validate against expected values (from compare_esp32_stm32.py)
            print("\n9. Validating results...")
            expected = {
                "level1_unique1": "26",
                "level1_unique2": "3",
                "level1_common": "44",
                "level2_classes1": "34",
                "level2_classes2": "24",
                "level2_functions1": "4",
                "level2_functions2": "4",
                "level2_constants1": "59",
                "level2_constants2": "3",
                "level3_methods1": "207",
                "level3_methods2": "291",
                "level3_methods_diff": "12",
                "level3_attrs1": "76",
                "level3_attrs2": "134"
            }
            
            actual = {
                "level1_unique1": level1_unique1,
                "level1_unique2": level1_unique2,
                "level1_common": level1_common,
                "level2_classes1": level2_classes1,
                "level2_classes2": level2_classes2,
                "level2_functions1": level2_functions1,
                "level2_functions2": level2_functions2,
                "level2_constants1": level2_constants1,
                "level2_constants2": level2_constants2,
                "level3_methods1": level3_methods1,
                "level3_methods2": level3_methods2,
                "level3_methods_diff": level3_methods_diff,
                "level3_attrs1": level3_attrs1,
                "level3_attrs2": level3_attrs2
            }
            
            all_match = True
            for key, expected_val in expected.items():
                actual_val = actual[key]
                if actual_val == expected_val:
                    print(f"   ✅ {key}: {actual_val}")
                else:
                    print(f"   ❌ {key}: expected {expected_val}, got {actual_val}")
                    all_match = False
            
            # Check for errors
            if errors:
                print(f"\n⚠️  JavaScript errors detected:")
                for error in errors:
                    print(f"   {error}")
                all_match = False
            
            # Final result
            print("\n" + "=" * 80)
            if all_match and not errors:
                print("✅ TEST PASSED: Numbered parameters work correctly in frontend")
                print("=" * 80)
                return 0
            else:
                print("❌ TEST FAILED: Results don't match expected values or errors occurred")
                print("=" * 80)
                return 1
                
        finally:
            # Close browser
            print("\n10. Closing browser...")
            await browser.close()


async def main():
    """Main entry point."""
    try:
        result = await test_comparison()
        return result
    except Exception as e:
        print(f"\n❌ TEST FAILED with exception: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    result = asyncio.run(main())
    sys.exit(result)
