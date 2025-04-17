from flask import request, jsonify
from .models import Book
from . import db

def register_routes(app):
    @app.route("/books", methods=["GET"])
    def get_books():
        query = request.args.get('q', '')
        books = Book.query.filter(
            (Book.title.ilike(f"%{query}%")) |
            (Book.author.ilike(f"%{query}%"))
        ).all()
        return jsonify([{
            "id": b.id,
            "title": b.title,
            "author": b.author,
            "year": b.year,
            "description": b.description,
            "genre": b.genre
        } for b in books])

    @app.route("/books", methods=["POST"])
    def add_book():
        data = request.get_json()
        new_book = Book(**data)
        db.session.add(new_book)
        db.session.commit()
        return jsonify({"message": "Book added!"}), 201

    @app.route("/books/<int:book_id>", methods=["DELETE"])
    def delete_book(book_id):
        book = Book.query.get_or_404(book_id)
        db.session.delete(book)
        db.session.commit()
        return jsonify({"message": "Book deleted"})