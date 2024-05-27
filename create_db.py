import sqlite3
# Connect to the database (creates the database file if it doesn't exist)
conn = sqlite3.connect('Book.db')

# Create a cursor object
c = conn.cursor()

# Insert sample data
books = [
    ('OOP', 'B Chandra', 'Description 1', 4.5, 'Academics'),
    ('BatMan Comics', 'Neal Adams', 'Description 2', 3.8, 'Comics'),
    ('Art Matters', 'Artews Didi', 'Description 3', 3.5, 'Classic'),
    ('Atomic Habits', 'James Clear', 'Description 3', 4.0, 'Selfhelp'),
    ('Beauty and the beast', 'Charmes lamb', 'Description 3', 3.0, 'Classic'),
    ('Discrete Mathematics', 'Edward A', 'Description 3', 4.6, 'Academics'),
    ('Money and Wealth', 'Raid Ernest', 'Description', 4.8, 'Money'),
    ('Think Python', 'Joe Aqwe', 'Description 3', 5.0, 'Academics'),
    ('Intelligent Investor', 'Benjamin Graham', 'Description 3', 3.0, 'Money'),
    ('Power of Zero', 'David McKnight', 'Description 3', 2.5, 'Selfhelp'),
]
c.executemany('''
INSERT INTO books (title, author, description, rating, genre)
VALUES ( ?, ?, ?, ?, ?)
''', books)

# Commit changes and close the connection
conn.commit()
conn.close()

print("Database and table created successfully.")
   