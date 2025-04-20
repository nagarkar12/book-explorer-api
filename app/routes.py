from flask import Blueprint, request, jsonify
from .models import Book
from . import db

book_routes = Blueprint('book_routes', __name__)

@book_routes.route('/')
def home():
    return "📚 Welcome to Book Explorer API"

@book_routes.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books])

@book_routes.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    new_book = Book(title=data['title'], author=data['author'])
    db.session.add(new_book)
    db.session.commit()
    return jsonify(new_book.to_dict()), 201

@book_routes.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({"error": "Book not found"}), 404
    db.session.delete(book)
    db.session.commit()
    return jsonify({"message": "Book deleted"})

@book_routes.route('/books/search', methods=['GET'])
def search_books():
    query = request.args.get('q')
    if not query:
        return jsonify({"error": "Search query is missing"}), 400

    results = Book.query.filter(
        (Book.title.ilike(f"%{query}%")) |
        (Book.author.ilike(f"%{query}%"))
    ).all()

    return jsonify([book.to_dict() for book in results])
