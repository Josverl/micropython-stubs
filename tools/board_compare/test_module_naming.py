#!/usr/bin/env python3
"""
Test script to reproduce and verify module naming issues.

Issues to reproduce:
1. Backslashes in module names (should be dots)
2. Missing parent modules from __init__.pyi files
"""

import os
import shutil
import tempfile
from pathlib import Path

# Import the scanner
try:
    from .scan_stubs import StubScanner
except ImportError:
    from scan_stubs import StubScanner


def create_test_stubs():
    """Create a test stub directory structure to reproduce the issues."""
    test_dir = Path(tempfile.mkdtemp(prefix="test_stubs_"))
    
    # Create directory structure that reproduces the issues
    test_cases = [
        # Case 1: Package with __init__.pyi (should create 'rp2' module)
        ("rp2/__init__.pyi", '"""RP2 base module."""\n\nclass Pin:\n    def __init__(self): pass\n'),
        
        # Case 2: Module in package (should create 'rp2.asm_pio' module)
        ("rp2/asm_pio.pyi", '"""RP2 PIO assembly."""\n\ndef asm_pio(): pass\n'),
        
        # Case 3: Nested package structure
        ("umqtt/__init__.pyi", '"""MQTT base package."""\n'),
        ("umqtt/simple.pyi", '"""Simple MQTT client."""\n\nclass MQTTClient:\n    def __init__(self): pass\n'),
        
        # Case 4: Multi-level nesting
        ("GENERIC/__init__.pyi", '"""Generic modules."""\n'),
        ("GENERIC/tarfile/__init__.pyi", '"""Tarfile package."""\n'),
        ("GENERIC/tarfile/write.pyi", '"""Tarfile writer."""\n\ndef write(): pass\n'),
        
        # Case 5: Single module (control case)
        ("machine.pyi", '"""Machine module."""\n\nclass Pin:\n    def __init__(self): pass\n'),
    ]
    
    for rel_path, content in test_cases:
        file_path = test_dir / rel_path
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(content, encoding='utf-8')
        print(f"Created: {file_path}")
    
    return test_dir


def test_current_behavior(test_dir):
    """Test the current behavior to document the issues."""
    print(f"\n=== TESTING CURRENT BEHAVIOR ===")
    print(f"Test directory: {test_dir}")
    
    scanner = StubScanner(test_dir)
    modules = scanner.scan_all_modules()
    
    print(f"\nFound {len(modules)} modules:")
    module_names = []
    for module in modules:
        print(f"  - {module.name}")
        module_names.append(module.name)
    
    print("\n=== EXPECTED vs ACTUAL ===")
    expected = [
        "rp2",           # From rp2/__init__.pyi
        "rp2.asm_pio",   # From rp2/asm_pio.pyi
        "umqtt",         # From umqtt/__init__.pyi
        "umqtt.simple",  # From umqtt/simple.pyi
        "GENERIC",       # From GENERIC/__init__.pyi
        "GENERIC.tarfile",    # From GENERIC/tarfile/__init__.pyi
        "GENERIC.tarfile.write",  # From GENERIC/tarfile/write.pyi
        "machine",       # From machine.pyi
    ]
    
    print("Expected modules:")
    for exp in expected:
        print(f"  ✓ {exp}")
    
    print("\nActual modules:")
    for actual in sorted(module_names):
        if actual in expected:
            print(f"  ✓ {actual}")
        else:
            print(f"  ✗ {actual}")
    
    print("\nMissing modules:")
    missing = set(expected) - set(module_names)
    for miss in sorted(missing):
        print(f"  - {miss}")
    
    print("\nIncorrect modules (with backslashes):")
    incorrect = [name for name in module_names if '\\' in name or '/' in name]
    for inc in sorted(incorrect):
        print(f"  - {inc}")
    
    return module_names, expected


def main():
    """Main test function."""
    print("=== MODULE NAMING ISSUE REPRODUCTION TEST ===")
    
    # Create test directory structure
    test_dir = create_test_stubs()
    
    try:
        # Test current behavior
        actual_modules, expected_modules = test_current_behavior(test_dir)
        
        # Summary
        print(f"\n=== SUMMARY ===")
        print(f"Expected: {len(expected_modules)} modules")
        print(f"Actual: {len(actual_modules)} modules")
        
        missing = set(expected_modules) - set(actual_modules)
        incorrect = [name for name in actual_modules if '\\' in name or '/' in name]
        
        print(f"Missing: {len(missing)} modules")
        print(f"Incorrect (with path separators): {len(incorrect)} modules")
        
        if missing or incorrect:
            print("\n❌ ISSUES CONFIRMED:")
            if missing:
                print(f"  - Missing modules: {', '.join(sorted(missing))}")
            if incorrect:
                print(f"  - Incorrect names: {', '.join(sorted(incorrect))}")
        else:
            print("\n✅ NO ISSUES FOUND")
    
    finally:
        # Cleanup
        shutil.rmtree(test_dir)
        print(f"\nCleaned up test directory: {test_dir}")


if __name__ == "__main__":
    main()