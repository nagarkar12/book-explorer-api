# Book Explorer API

A simple API built with Flask that allows users to manage a book collection. This includes adding, viewing, and searching books. It also includes JWT-based authentication for user registration and login.

## Live API
Hosted on [Render](https://book-explorer-api.onrender.com/)

## Features

- Add new books
- View all books
- Search books by title
- Update or delete books
- JWT-based user registration and login
- Simple frontend with HTML/CSS/JavaScript

## Technologies Used

- Python
- Flask
- SQLite
- SQLAlchemy
- JWT (Flask-JWT-Extended)
- HTML/CSS/JavaScript

##  Project Structure
book_explorer_api/ ├── backend/ │ ├── app/ │ │ ├── init.py │ │ ├── models.py │ │ ├── routes.py │ ├── instance/ │ │ └── book.db │ ├── run.py │ ├── requirements.txt │ └── Procfile ├── frontend/ │ ├── index.html │ ├── style.css │ └── script.js └── README.md


## API Endpoints

| Method | Endpoint        | Description              |
|--------|------------------|--------------------------|
| POST   | `/register`      | Register a new user      |
| POST   | `/login`         | Login and get token      |
| POST   | `/books`         | Add a new book (auth)    |
| GET    | `/books`         | Get all books (auth)     |

> Use `Authorization: Bearer <JWT_TOKEN>` for protected routes

## How to Run Locally

```bash
# Clone the repository
git clone https://github.com/your-username/book_explorer_api.git

# Navigate to backend folder
cd book_explorer_api/backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python run.py
