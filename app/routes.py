from flask import request, jsonify
from .models import Book
from . import db

def register_routes(app):
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

    @app.route('/seed', methods=['POST'])
    def seed_data():
        books = [
            {
                "title": "Atomic Habits",
                "author": "James Clear",
                "year": 2018,
                "description": "A guide to building good habits and breaking bad ones.",
                "genre": "Self-help"
            },
            {
                "title": "The Alchemist",
                "author": "Paulo Coelho",
                "year": 1988,
                "description": "A novel about a boy’s journey in search of treasure.",
                "genre": "Fiction"
            },
            {
                "title": "Clean Code",
                "author": "Robert C. Martin",
                "year": 2008,
                "description": "A handbook of agile software craftsmanship.",
                "genre": "Programming"
            },
            {
                "title": "Deep Work",
                "author": "Cal Newport",
                "year": 2016,
                "description": "Strategies for focused success in a distracted world.",
                "genre": "Productivity"
            },
            {
                "title": "1984",
                "author": "George Orwell",
                "year": 1949,
                "description": "A dystopian novel about surveillance and control.",
                "genre": "Science Fiction"
            }
        ]

        for data in books:
            book = Book(**data)
            db.session.add(book)
        db.session.commit()
        return jsonify({"message": "Sample books added!"})
