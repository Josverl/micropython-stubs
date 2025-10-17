#!/usr/bin/env python3
"""
Test script for the board comparison tool.
Validates that the tool can scan stubs, build database, and export JSON.
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from .build_database import DatabaseBuilder
from .models import Class, Method, Module, Parameter
from .scan_stubs import StubScanner


def test_models():
    """Test Pydantic models."""
    print("Testing Pydantic models...")
    
    # Create a parameter
    param = Parameter(name="x", type_hint="int", default_value="0", is_optional=True)
    assert param.name == "x"
    
    # Create a method
    method = Method(name="test_func", parameters=[param], return_type="None")
    assert method.name == "test_func"
    assert len(method.parameters) == 1
    
    # Create a class
    cls = Class(name="TestClass", methods=[method])
    assert cls.name == "TestClass"
    assert len(cls.methods) == 1
    
    # Create a module
    module = Module(name="test_module", classes=[cls], functions=[method])
    assert module.name == "test_module"
    assert len(module.classes) == 1
    assert len(module.functions) == 1
    
    print("✓ Models work correctly")


def test_stub_scanner():
    """Test stub scanner."""
    print("\nTesting stub scanner...")
    
    # Find a test stub directory
    repo_root = Path(__file__).parent.parent.parent
    stub_dir = repo_root / "publish" / "micropython-v1_26_0-esp32-esp32_generic-stubs"
    
    if not stub_dir.exists():
        print(f"⚠ Warning: Test stub directory not found at {stub_dir}")
        return
    
    scanner = StubScanner(stub_dir)
    modules = scanner.scan_all_modules()
    
    assert len(modules) > 0, "Should find at least one module"
    
    # Check that we found some expected modules
    module_names = {m.name for m in modules}
    expected_modules = {"machine", "time", "math", "gc"}
    found = expected_modules & module_names
    
    assert len(found) > 0, f"Should find some common modules, found: {found}"
    
    # Find the machine module and check it has classes
    machine_module = next((m for m in modules if m.name == "machine"), None)
    if machine_module:
        assert len(machine_module.classes) > 0, "machine module should have classes"
        print(f"✓ Found {len(modules)} modules, machine has {len(machine_module.classes)} classes")
    else:
        print("⚠ Warning: machine module not found")
    
    print("✓ Stub scanner works correctly")


def test_database_builder():
    """Test database builder."""
    print("\nTesting database builder...")
    
    import os
    import tempfile
    
    # Create temporary database
    with tempfile.NamedTemporaryFile(suffix=".db", delete=False) as f:
        db_path = Path(f.name)
    
    try:
        builder = DatabaseBuilder(db_path)
        builder.connect()
        builder.create_schema()
        
        # Add a test board
        test_board = {
            "version": "v1.26.0",
            "port": "test",
            "board": "test_board",
            "modules": [
                {
                    "name": "test_module",
                    "classes": [
                        {
                            "name": "TestClass",
                            "base_classes": [],
                            "methods": [
                                {
                                    "name": "test_method",
                                    "parameters": [
                                        {"name": "self"},
                                        {"name": "x", "type_hint": "int"}
                                    ],
                                    "return_type": "None"
                                }
                            ],
                            "attributes": ["TEST_CONST"]
                        }
                    ],
                    "functions": [
                        {
                            "name": "test_func",
                            "parameters": [],
                            "return_type": "int"
                        }
                    ],
                    "constants": ["CONST1", "CONST2"]
                }
            ]
        }
        
        board_id = builder.add_board(test_board)
        assert board_id > 0, "Should get a valid board ID"
        
        # Export to JSON
        with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as f:
            json_path = Path(f.name)
        
        try:
            builder.export_to_json(json_path)
            
            # Verify JSON was created
            assert json_path.exists(), "JSON file should be created"
            
            # Read and verify JSON
            import json
            with open(json_path) as f:
                data = json.load(f)
            
            assert "version" in data
            assert "boards" in data
            assert len(data["boards"]) == 1
            assert data["boards"][0]["port"] == "test"
            
            print("✓ Database builder works correctly")
            
        finally:
            if json_path.exists():
                os.unlink(json_path)
        
        builder.close()
        
    finally:
        if db_path.exists():
            os.unlink(db_path)


def main():
    """Run all tests."""
    print("=" * 60)
    print("Board Comparison Tool - Test Suite")
    print("=" * 60)
    
    try:
        test_models()
        test_stub_scanner()
        test_database_builder()
        
        print("\n" + "=" * 60)
        print("✓ All tests passed!")
        print("=" * 60)
        return 0
        
    except AssertionError as e:
        print(f"\n✗ Test failed: {e}")
        return 1
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
