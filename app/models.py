from . import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    published_year = db.Column(db.Integer)
    genre = db.Column(db.String(50))
    isbn = db.Column(db.String(20))

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "description": self.description,
            "published_year": self.published_year,
            "genre": self.genre,
            "isbn": self.isbn
        }
