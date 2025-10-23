"""Test script to validate database views creation."""
import os
import sqlite3

# Add parent directory to path
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from build_database import DatabaseBuilder


def test_view_creation():
    """Test that all database views are created correctly."""
    # Create temporary database
    tf = tempfile.NamedTemporaryFile(delete=False, suffix='.db')
    tf.close()
    test_db_path = tf.name
    
    try:
        print("Creating test database...")
        builder = DatabaseBuilder(test_db_path)
        builder.connect()
        
        print("Creating schema...")
        builder.create_schema()
        
        print("Creating views...")
        builder.create_views()
        
        builder.close()
        
        # Verify views were created
        print("\nVerifying views...")
        conn = sqlite3.connect(test_db_path)
        cursor = conn.cursor()
        
        cursor.execute("SELECT name FROM sqlite_master WHERE type='view' ORDER BY name")
        views = [row[0] for row in cursor.fetchall()]
        
        expected_views = [
            'v_board_entities',
            'v_board_modules',
            'v_class_methods',
            'v_entity_hierarchy',
            'v_module_classes'
        ]
        
        print(f"Expected views: {expected_views}")
        print(f"Found views: {views}")
        
        missing_views = set(expected_views) - set(views)
        extra_views = set(views) - set(expected_views)
        
        if missing_views:
            print(f"\n❌ FAIL: Missing views: {missing_views}")
            return False
        
        if extra_views:
            print(f"\n⚠️  WARNING: Unexpected views: {extra_views}")
        
        print(f"\n✅ SUCCESS: All {len(expected_views)} views created correctly!")
        
        # Test that views can be queried (even if empty)
        print("\nTesting view queries...")
        for view_name in expected_views:
            try:
                cursor.execute(f"SELECT * FROM {view_name} LIMIT 1")
                print(f"  ✓ {view_name} is queryable")
            except Exception as e:
                print(f"  ✗ {view_name} query failed: {e}")
                return False
        
        conn.close()
        return True
        
    finally:
        # Cleanup
        if os.path.exists(test_db_path):
            os.unlink(test_db_path)
            print(f"\nTest database cleaned up: {test_db_path}")

if __name__ == "__main__":
    success = test_view_creation()
    sys.exit(0 if success else 1)
