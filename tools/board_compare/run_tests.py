#!/usr/bin/env python3
"""
Test runner for board comparison tool.
Runs both the simple test suite (test_tool.py) and pytest-based tests.
"""

import sys
import subprocess
from pathlib import Path


def run_simple_tests():
    """Run the simple test suite."""
    print("=" * 70)
    print("Running Simple Test Suite (test_tool.py)")
    print("=" * 70)

    result = subprocess.run([sys.executable, "test_tool.py"], cwd=Path(__file__).parent)
    return result.returncode


def run_pytest_tests():
    """Run pytest-based tests."""
    print("\n" + "=" * 70)
    print("Running Pytest Test Suite")
    print("=" * 70)

    try:
        result = subprocess.run([sys.executable, "-m", "pytest", "-v"], cwd=Path(__file__).parent)
        return result.returncode
    except Exception as e:
        print(f"Error running pytest: {e}")
        print("Pytest may not be installed. Run: pip install pytest")
        return 1


def main():
    """Run all tests."""
    print("\n" + "🔬" * 35)
    print("Board Comparison Tool - Complete Test Suite")
    print("🔬" * 35 + "\n")

    # Run simple tests first
    simple_result = run_simple_tests()

    # Run pytest tests
    pytest_result = run_pytest_tests()

    # Summary
    print("\n" + "=" * 70)
    print("Test Summary")
    print("=" * 70)
    print(f"Simple tests: {'✓ PASSED' if simple_result == 0 else '✗ FAILED'}")
    print(f"Pytest tests: {'✓ PASSED' if pytest_result == 0 else '✗ FAILED'}")
    print("=" * 70)

    # Exit with error if any tests failed
    return max(simple_result, pytest_result)


if __name__ == "__main__":
    sys.exit(main())
