from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS  # 👉 Add this line
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/book.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    
    CORS(app)  # 👉 Add this line to enable CORS

    from .routes import register_routes
    register_routes(app)

    return app
