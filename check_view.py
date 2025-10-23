import sqlite3

conn = sqlite3.connect('tools/board_compare/frontend/board_comparison.db')
cursor = conn.cursor()

# Get unique_class_attributes columns
cursor.execute("PRAGMA table_info(unique_class_attributes)")
columns = cursor.fetchall()
print("unique_class_attributes columns:")
for col in columns:
    print(f"  {col[1]} - {col[2]}")

conn.close()
