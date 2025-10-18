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


# Create the 'orders' table
cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    product_name TEXT,
    quantity INTEGER,
    price DECIMAL(10,2),
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users (id)
)
""")

# Create the 'user_profiles' table
cursor.execute("""
CREATE TABLE IF NOT EXISTS user_profiles (
    id INTEGER PRIMARY KEY,
    user_id INTEGER UNIQUE,
    email TEXT UNIQUE,
    age INTEGER,
    city TEXT,
    registration_date DATE DEFAULT CURRENT_DATE,
    is_active BOOLEAN DEFAULT 1,
    FOREIGN KEY (user_id) REFERENCES users (id)
)
""")

# Insert sample orders
cursor.executemany("INSERT INTO orders (user_id, product_name, quantity, price) VALUES (?, ?, ?, ?)", [
    (1, "Laptop", 1, 999.99),
    (1, "Mouse", 2, 25.50),
    (2, "Keyboard", 1, 75.00),
    (3, "Monitor", 1, 299.99),
    (2, "Headphones", 1, 150.00)
])

# Insert sample user profiles
cursor.executemany("INSERT INTO user_profiles (user_id, email, age, city) VALUES (?, ?, ?, ?)", [
    (1, "alice@email.com", 28, "New York"),
    (2, "bob@email.com", 34, "Los Angeles"),
    (3, "charlie@email.com", 22, "Chicago")
])

# Commit and close
conn.commit()
conn.close()

print("Database 'data.sqlite' created with table 'users' and 3 entries.")

