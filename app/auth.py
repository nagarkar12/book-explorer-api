from flask import Blueprint, request, jsonify
from app.models import db, User
import jwt, datetime
from werkzeug.security import check_password_hash
from flask import current_app

auth_dp = Blueprint('auth', __name__)

@auth_dp.route('/register', methods = ['POST'])
def register():
    data = request.get_json()
    if User.query.filter_by(username = data['username']).first():
        return jsonify({'message': 'User already exists'}), 409
    user = User(username = data['username'])
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User registered successfull'})

@auth_dp.route('/login', methods = ['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username = data['username']).first()
    if user and user.check_password(data['password']):
        token = jwt.encode({
            'user_id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedate(hours = 1)
        },current_app.config['SECRET_KEY'], algorithm = 'HS256')
        return jsonify({'token': token})
    return jsonify({'message': 'Invalid credentials'}), 401