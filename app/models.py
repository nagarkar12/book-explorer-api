# models.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)  # Optional book summary
    published_year = db.Column(db.Integer)  # Year of publication
    genre = db.Column(db.String(50))  # Book genre like Fiction, History etc.
    isbn = db.Column(db.String(20))  # Optional, International Standard Book Number

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'description': self.description,
            'published_year': self.published_year,
            'genre': self.genre,
            'isbn': self.isbn
        }
