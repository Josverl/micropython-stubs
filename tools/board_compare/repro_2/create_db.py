# create_db.py

import sqlite3

# Connect to (or create) the SQLite database
conn = sqlite3.connect("data.sqlite")
cursor = conn.cursor()

# Create the 'users' table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT
)
""")

# Insert sample users
cursor.executemany("INSERT INTO users (name) VALUES (?)", [
    ("Alice",),
    ("Bob",),
    ("Charlie",)
])

# Commit and close
conn.commit()
conn.close()

print("Database 'data.sqlite' created with table 'users' and 3 entries.")

