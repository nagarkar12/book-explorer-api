from . import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    author = db.Column(db.String(120), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(300))
    genre = db.Column(db.String(100))
