from flask import request, jsonify
from .models import Book
from . import db
from flask import current_app as app

@app.route('/')
def home():
    return jsonify({"message": "Welcome to Book Explorer API!"})

@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    new_book = Book(**data)
    db.session.add(new_book)
    db.session.commit()
    return jsonify({"message": "Book added!"}), 201

@app.route("/books", methods=["GET"])
def get_books():
    books = Book.query.all()
    return jsonify([{
        "id": b.id,
        "title": b.title,
        "author": b.author,
        "year": b.year,
        "description": b.description,
        "genre": b.genre
    } for b in books])


