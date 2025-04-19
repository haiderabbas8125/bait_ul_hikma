import sqlite3

# Connect to the database (or create it)
conn = sqlite3.connect('library.db')

# Create a cursor
cursor = conn.cursor()

# Create a table for books
cursor.execute('''
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    genre TEXT,
    year INTEGER
)
''')

# Commit changes and close the connection
conn.commit()
conn.close()

print("Database and table created successfully.")