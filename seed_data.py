from app import create_app, db
from app.models import Book

app = create_app()

with app.app_context():
    books = [
        Book(title="Atomic Habits", author="James Clear", year=2018, description="A guide to building good habits and breaking bad ones.", genre="Self-help"),
        Book(title="The Alchemist", author="Paulo Coelho", year=1988, description="A novel about a boy’s journey in search of treasure.", genre="Fiction"),
        Book(title="Clean Code", author="Robert C. Martin", year=2008, description="A handbook of agile software craftsmanship.", genre="Programming"),
        Book(title="Deep Work", author="Cal Newport", year=2016, description="Strategies for focused success in a distracted world.", genre="Productivity"),
        Book(title="1984", author="George Orwell", year=1949, description="A dystopian novel about surveillance and control.", genre="Science Fiction")
    ]

    db.session.bulk_save_objects(books)
    db.session.commit()
    print("✅ Books added successfully!")
