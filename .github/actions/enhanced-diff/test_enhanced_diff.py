#!/usr/bin/env python3
"""
Test script for the enhanced diff checker.
This script simulates different scenarios to verify the enhanced diff logic works correctly.
"""

import os
import sys
import tempfile
import subprocess
from pathlib import Path

# Add the action directory to the path so we can import our script
action_dir = Path(__file__).parent.parent / "enhanced-diff"
sys.path.insert(0, str(action_dir))

from check_changes import categorize_files, get_changed_files


def test_categorize_files():
    """Test the file categorization logic."""
    print("Testing file categorization...")
    
    # Test case 1: Mixed files
    files = ["stub.py", "config.json", "module.pyi", "data.json", "README.md"]
    json_files, non_json_files = categorize_files(files)
    
    expected_json = ["config.json", "data.json"]
    expected_non_json = ["stub.py", "module.pyi", "README.md"]
    
    assert json_files == expected_json, f"Expected {expected_json}, got {json_files}"
    assert non_json_files == expected_non_json, f"Expected {expected_non_json}, got {non_json_files}"
    print("✓ Mixed files test passed")
    
    # Test case 2: Only JSON files
    files = ["config.json", "package.json"]
    json_files, non_json_files = categorize_files(files)
    
    assert json_files == ["config.json", "package.json"]
    assert non_json_files == []
    print("✓ JSON-only files test passed")
    
    # Test case 3: Only non-JSON files
    files = ["main.py", "utils.py", "README.md"]
    json_files, non_json_files = categorize_files(files)
    
    assert json_files == []
    assert non_json_files == ["main.py", "utils.py", "README.md"]
    print("✓ Non-JSON-only files test passed")
    
    # Test case 4: Empty list
    files = []
    json_files, non_json_files = categorize_files(files)
    
    assert json_files == []
    assert non_json_files == []
    print("✓ Empty files test passed")
    
    # Test case 5: Case insensitive JSON detection
    files = ["CONFIG.JSON", "data.Json", "mixed.JSON"]
    json_files, non_json_files = categorize_files(files)
    
    assert json_files == ["CONFIG.JSON", "data.Json", "mixed.JSON"]
    assert non_json_files == []
    print("✓ Case insensitive JSON test passed")


def simulate_git_status_scenarios():
    """Simulate different git status scenarios to show decision logic."""
    print("\nSimulating different change scenarios...")
    
    scenarios = [
        {
            "name": "Only JSON files changed",
            "files": ["config.json", "package.json"],
            "should_commit": False
        },
        {
            "name": "Only non-JSON files changed",
            "files": ["main.py", "README.md"],
            "should_commit": True
        },
        {
            "name": "Mixed files changed",
            "files": ["main.py", "config.json", "utils.py"],
            "should_commit": True
        },
        {
            "name": "No files changed",
            "files": [],
            "should_commit": False
        }
    ]
    
    for scenario in scenarios:
        print(f"\nScenario: {scenario['name']}")
        files = scenario['files']
        json_files, non_json_files = categorize_files(files)
        
        should_commit = len(non_json_files) > 0
        
        print(f"  Files: {files}")
        print(f"  JSON files: {json_files}")
        print(f"  Non-JSON files: {non_json_files}")
        print(f"  Should commit: {should_commit}")
        
        assert should_commit == scenario['should_commit'], \
            f"Expected should_commit={scenario['should_commit']}, got {should_commit}"
        print("  ✓ Decision logic correct")


if __name__ == "__main__":
    print("Running enhanced diff checker tests...\n")
    
    try:
        test_categorize_files()
        simulate_git_status_scenarios()
        print("\n🎉 All tests passed!")
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n💥 Unexpected error: {e}")
        sys.exit(1)