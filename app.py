# app.py
from flask import Flask, request, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

# Function to connect to the database
def get_db_connection():
    conn = sqlite3.connect('library.db')
    conn.row_factory = sqlite3.Row
    return conn

# Home route to display all books
@app.route('/')
def index():
    conn = get_db_connection()
    books = conn.execute('SELECT * FROM books').fetchall()
    conn.close()
    return render_template('index.html', books=books)

# Route to add a new book
@app.route('/add', methods=['POST'])
def add_book():
    title = request.form['title']
    author = request.form['author']
    genre = request.form['genre']
    year = request.form['year']

    conn = get_db_connection()
    conn.execute('INSERT INTO books (title, author, genre, year) VALUES (?, ?, ?, ?)',
                 (title, author, genre, year))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

# Route to delete a book
@app.route('/delete/<int:id>')
def delete_book(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM books WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)