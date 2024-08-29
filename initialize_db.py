import sqlite3
from datetime import datetime

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('python_intern.db')
cursor = conn.cursor()

# Create the users table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    join_date TEXT NOT NULL
)
''')

# Create the transactions table
cursor.execute('''
CREATE TABLE IF NOT EXISTS transactions (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    amount REAL NOT NULL,
    transaction_date TEXT NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(user_id)
)
''')

# Sample users
users = [
    ('Alice', 'alice@example.com', '2023-01-01'),
    ('Bob', 'bob@example.com', '2023-02-15'),
    ('Charlie', 'charlie@example.com', '2023-03-10')
]

# Insert users
cursor.executemany('''
INSERT INTO users (name, email, join_date) VALUES (?, ?, ?)
''', users)

# Sample transactions
transactions = [
    (1, 150.75, '2023-03-01'),
    (2, 200.50, '2023-03-15'),
    (1, 75.00, '2023-03-20'),
    (3, 165.00, '2023-03-20'),
    (3, 75.00, '2023-03-20'),
]

# Insert transactions
cursor.executemany('''
INSERT INTO transactions (user_id, amount, transaction_date) VALUES (?, ?, ?)
''', transactions)

# Commit the changes and close the connection
print("DB has initialized!")
conn.commit()
conn.close()
