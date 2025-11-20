#!/usr/bin/env python3
"""
Unit tests for module naming fixes in scan_stubs.py.

Tests ensure that:
1. Path separators (\\ and /) are properly converted to dots in module names
2. __init__.pyi files are processed correctly to create parent modules
3. Nested directory structures work correctly
"""

import os
import shutil
import tempfile
import unittest
from pathlib import Path

# Import the scanner
try:
    from .scan_stubs import StubScanner
except ImportError:
    from scan_stubs import StubScanner


class TestModuleNaming(unittest.TestCase):
    """Test cases for module naming functionality."""

    def setUp(self):
        """Set up a temporary test directory for each test."""
        self.test_dir = Path(tempfile.mkdtemp(prefix="test_module_naming_"))

    def tearDown(self):
        """Clean up the temporary test directory."""
        shutil.rmtree(self.test_dir)

    def _create_stub_file(self, rel_path: str, content: str = "# Test stub\n"):
        """Helper to create a stub file in the test directory."""
        file_path = self.test_dir / rel_path
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(content, encoding="utf-8")
        return file_path

    def _scan_modules(self):
        """Helper to scan modules and return their names."""
        scanner = StubScanner(self.test_dir)
        modules = scanner.scan_all_modules()
        return [module.name for module in modules]

    def test_single_module(self):
        """Test scanning a single .pyi file."""
        self._create_stub_file("machine.pyi", "class Pin: pass\n")

        module_names = self._scan_modules()
        self.assertEqual(module_names, ["machine"])

    def test_init_pyi_creates_parent_module(self):
        """Test that __init__.pyi creates a module with the parent directory name."""
        self._create_stub_file("rp2/__init__.pyi", "# RP2 base module\nclass Pin: pass\n")

        module_names = self._scan_modules()
        self.assertEqual(module_names, ["rp2"])

    def test_package_with_submodule(self):
        """Test scanning a package with both __init__.pyi and submodules."""
        self._create_stub_file("rp2/__init__.pyi", "class Pin: pass\n")
        self._create_stub_file("rp2/asm_pio.pyi", "def asm_pio(): pass\n")

        module_names = set(self._scan_modules())
        expected = {"rp2", "rp2.asm_pio"}
        self.assertEqual(module_names, expected)

    def test_nested_packages(self):
        """Test nested package structure."""
        self._create_stub_file("GENERIC/__init__.pyi", "# Generic package\n")
        self._create_stub_file("GENERIC/tarfile/__init__.pyi", "# Tarfile package\n")
        self._create_stub_file("GENERIC/tarfile/write.pyi", "def write(): pass\n")

        module_names = set(self._scan_modules())
        expected = {"GENERIC", "GENERIC.tarfile", "GENERIC.tarfile.write"}
        self.assertEqual(module_names, expected)

    def test_no_backslashes_in_module_names(self):
        """Test that module names never contain backslashes."""
        # Create various nested structures
        test_files = [
            "umqtt/__init__.pyi",
            "umqtt/simple.pyi",
            "umqtt/robust.pyi",
            "aioble/__init__.pyi",
            "aioble/client.pyi",
            "deep/nested/structure/__init__.pyi",
            "deep/nested/structure/module.pyi",
        ]

        for file_path in test_files:
            self._create_stub_file(file_path, "# Test module\n")

        module_names = self._scan_modules()

        # Check that no module names contain backslashes or forward slashes
        for name in module_names:
            self.assertNotIn("\\", name, f"Module name '{name}' contains backslash")
            self.assertNotIn("/", name, f"Module name '{name}' contains forward slash")

    def test_dots_in_nested_module_names(self):
        """Test that nested modules have proper dot notation."""
        self._create_stub_file("parent/__init__.pyi", "# Parent package\n")
        self._create_stub_file("parent/child/__init__.pyi", "# Child package\n")
        self._create_stub_file("parent/child/grandchild.pyi", "# Grandchild module\n")

        module_names = set(self._scan_modules())
        expected = {"parent", "parent.child", "parent.child.grandchild"}
        self.assertEqual(module_names, expected)

    def test_private_modules_skipped_except_init_and_builtins(self):
        """Test that private modules are skipped except __init__.pyi and __builtins__.pyi."""
        # Create various files starting with underscore
        test_files = [
            "__init__.pyi",  # Should be included
            "__builtins__.pyi",  # Should be included
            "_private.pyi",  # Should be skipped
            "_internal.pyi",  # Should be skipped
            "normal.pyi",  # Should be included
            "package/__init__.pyi",  # Should be included
            "package/_private.pyi",  # Should be skipped
        ]

        for file_path in test_files:
            self._create_stub_file(file_path, "# Test module\n")

        module_names = set(self._scan_modules())

        # Check what we expect to be included/excluded
        expected_included = {"__init__", "__builtins__", "normal", "package"}
        expected_excluded = {"_private", "_internal", "package._private"}

        # Verify included modules are present
        for expected in expected_included:
            self.assertIn(expected, module_names, f"Expected module '{expected}' not found")

        # Verify excluded modules are not present
        for excluded in expected_excluded:
            self.assertNotIn(excluded, module_names, f"Private module '{excluded}' should be excluded")

    def test_complex_real_world_structure(self):
        """Test a complex structure similar to real MicroPython stubs."""
        # Create a structure similar to what we see in the actual database
        files_and_expected = [
            ("rp2/__init__.pyi", "rp2"),
            ("rp2/asm_pio.pyi", "rp2.asm_pio"),
            ("umqtt/__init__.pyi", "umqtt"),
            ("umqtt/simple.pyi", "umqtt.simple"),
            ("umqtt/robust.pyi", "umqtt.robust"),
            ("aioble/__init__.pyi", "aioble"),
            ("aioble/central.pyi", "aioble.central"),
            ("aioble/client.pyi", "aioble.client"),
            ("GENERIC/__init__.pyi", "GENERIC"),
            ("GENERIC/base64.pyi", "GENERIC.base64"),
            ("GENERIC/tarfile/__init__.pyi", "GENERIC.tarfile"),
            ("GENERIC/tarfile/write.pyi", "GENERIC.tarfile.write"),
            ("machine.pyi", "machine"),
            ("micropython.pyi", "micropython"),
        ]

        # Create all the files
        for file_path, expected_name in files_and_expected:
            self._create_stub_file(file_path, f"# {expected_name} module\n")

        # Scan and verify
        module_names = set(self._scan_modules())
        expected_names = {expected for _, expected in files_and_expected}

        self.assertEqual(module_names, expected_names)

        # Verify no path separators in any module name
        for name in module_names:
            self.assertNotIn("\\", name, f"Module name '{name}' contains backslash")
            self.assertNotIn("/", name, f"Module name '{name}' contains forward slash")


if __name__ == "__main__":
    unittest.main()
