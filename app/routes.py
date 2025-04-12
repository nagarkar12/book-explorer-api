from flask import render_template, request, jsonify
from .models import Book
from . import db

def register_routes(app):
    @app.route('/')
    def home():
        return render_template("index.html")

    @app.route('/books', methods=['GET'])
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

    @app.route('/books', methods=['POST'])
    def add_book():
        data = request.get_json()
        new_book = Book(**data)
        db.session.add(new_book)
        db.session.commit()
        return jsonify({"message": "Book added!"}), 201
