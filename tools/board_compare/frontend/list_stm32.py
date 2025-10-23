import sqlite3

conn = sqlite3.connect('board_comparison.db')
cursor = conn.cursor()
cursor.execute("SELECT DISTINCT board FROM boards WHERE version='v1.26.0' AND port='stm32' ORDER BY board")
for row in cursor.fetchall():
    print(row[0])
