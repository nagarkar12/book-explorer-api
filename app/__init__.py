from flask import request, jsonify
from .models import Book
from . import db
from flask import current_app as app
import jwt
from functools import wraps
from datetime import datetime

# Helper: Decorator to protect routes
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        # Get token from Authorization header
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1]  # Bearer <token>

        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            # Here you could verify user existence using data['user_id'], etc.
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired!'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token!'}), 401

        return f(*args, **kwargs)
    return decorated


@app.route('/')
def home():
    return jsonify({"message": "Welcome to Book Explorer API!"})


# Protected route: only accessible with valid JWT
@app.route('/books', methods=['POST'])
@token_required
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
        "genre": b.genre,
        "year": b.year
    } for b in books])
