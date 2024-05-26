from flask import Flask, request, jsonify
import sqlite3  # For SQLite
# import mysql.connector  # For MySQL

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('books.db')  # For SQLite
    conn.row_factory = sqlite3.Row
    
    # For MySQL
    # conn = mysql.connector.connect(user='username', password='password', host='localhost', database='books')
    return conn

@app.route('/books', methods=['GET'])
def get_books():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books')
    books = cursor.fetchall()
    conn.close()
    return jsonify([dict(row) for row in books])

@app.route('/create_books', methods=['POST'])
def add_book():
    new_book = request.get_json()
    title = new_book['title']
    author = new_book['author']
    price = new_book['price']
    category = new_book['category']
    description = new_book['description']
    date = new_book['date']
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO books (title, author, price,catergory,description,date) VALUES (?, ?, ?,?,?,?)', (title, author, price,category,description,date))
    conn.commit()
    conn.close()
    return jsonify(new_book), 201

@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    update_data = request.get_json()
    title = update_data['title']
    author = update_data['author']
    price = update_data['price']
    category = update_data['category']
    description = update_data['description']
    date = update_data['date']
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE books SET title = ?, author = ? WHERE id = ?, price = ?,category = ?,description = ?,date = ?', (title, author, id, price,category,description,date))
    conn.commit()
    conn.close()
    return jsonify(update_data)

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM books WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
