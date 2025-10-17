#!/usr/bin/env python3
"""Quick script to check database schema"""

import sqlite3

def main():
    conn = sqlite3.connect('frontend/board_comparison.db')
    cursor = conn.cursor()
    
    print("=== TABLES AND VIEWS ===")
    cursor.execute("SELECT type, name FROM sqlite_master WHERE type IN ('table', 'view') ORDER BY type, name")
    for row in cursor.fetchall():
        print(f"{row[0]}: {row[1]}")
    
    print("\n=== SAMPLE FROM boards ===")
    cursor.execute("SELECT * FROM boards LIMIT 3")
    for row in cursor.fetchall():
        print(row)
    
    print("\n=== SAMPLE FROM unique_modules ===")
    cursor.execute("SELECT * FROM unique_modules LIMIT 3")
    for row in cursor.fetchall():
        print(row)
    
    print("\n=== VIEW DEFINITION ===")
    cursor.execute("SELECT sql FROM sqlite_master WHERE name = 'methods_with_board_support'")
    result = cursor.fetchone()
    if result:
        print(result[0])
    
    print("\n=== NORMALIZATION CHECK ===")
    cursor.execute("SELECT COUNT(*) FROM unique_methods WHERE name = 'const'")
    print(f"Unique const methods: {cursor.fetchone()[0]}")
    
    cursor.execute("SELECT supported_boards FROM methods_with_board_support WHERE name = 'const' LIMIT 1")
    result = cursor.fetchone()
    if result:
        boards = result[0].split('; ')
        print(f"Board support for const(): {len(boards)} boards")
        print(f"First few boards: {boards[:3]}")
    
    print("\n=== VERSION CHECK ===")
    cursor.execute("SELECT DISTINCT version FROM boards")
    versions = cursor.fetchall()
    print(f"Versions in database: {[v[0] for v in versions]}")
    
    cursor.execute("SELECT version, port, board FROM boards LIMIT 5")
    sample_boards = cursor.fetchall()
    print("Sample board entries:")
    for board in sample_boards:
        print(f"  {board[1]}-{board[2]} (v{board[0]})")
    
    conn.close()

if __name__ == '__main__':
    main()