from app import create_app, db
from app.models import Book

app = create_app()

with app.app_context():
    books = [
        Book(title="1984", author="George Orwell", year=1949, description="Dystopian future society.", genre="Fiction"),
        Book(title="To Kill a Mockingbird", author="Harper Lee", year=1960, description="Classic of racial injustice.", genre="Drama"),
        Book(title="The Great Gatsby", author="F. Scott Fitzgerald", year=1925, description="Jazz Age and the American dream.", genre="Classic")
    ]
    db.session.bulk_save_objects(books)
    db.session.commit()
    print(" Sample books inserted")
