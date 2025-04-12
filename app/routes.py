from flask import request, jsonify, send_from_directory
from .models import Book
from . import db
import os

def register_routes(app):
    @app.route('/')
    def serve_index():
        return send_from_directory('static', 'index.html')

    @app.route('/books', methods=['GET'])
    def get_books():
        try:
            books = Book.query.all()
            return jsonify([{
                "id": b.id,
                "title": b.title,
                "author": b.author,
                "year": b.year,
                "description": b.description,
                "genre": b.genre
            } for b in books])
        except Exception as e:
            return jsonify({"error": str(e)}), 500
