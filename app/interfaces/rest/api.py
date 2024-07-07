from flask import Flask, request, jsonify
from ...application.services import UserSettingsRepository
from ...infrastructure.sqlite_repository import SQLiteUserRepository

app = Flask(__name__)
user_service = UserSettingsRepository(SQLiteUserRepository('chronos.db'))

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user_service.create_user(data['name'], data['email'])
    return jsonify({'message': 'User created'}), 201

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_service.get_user(user_id)
    return jsonify(user.__dict__)

@app.route('/users', methods=['GET'])
def list_users():
    users = user_service.list_users()
    return jsonify([user.__dict__ for user in users])
