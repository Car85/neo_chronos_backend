# app/interfaces/rest/api.py 
from flask import Flask, request, jsonify
from flask_cors import CORS
from ...application.settings_service import SettingsService
from ...infrastructure.settings_repository import SQLiteSettingsRepository
from ...domain.models import Settings

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}}) 
DB_PATH = "./chronos.db"
settings_repository = SQLiteSettingsRepository(DB_PATH)
settings_service = SettingsService(settings_repository)


@app.route('/add_settings', methods=['POST'])
def add_settings():
    data = request.json
    settings = Settings(**data)
    settings_service.add_settings(settings)
    return jsonify({"message": "Settings added successfully"}), 201
    
@app.route('/settings/<int:id>', methods=['GET'])
def get_settings(id):
    settings = settings_service.get_settings_by_id(id)
    if settings:
        return jsonify(settings.to_dict()), 200
    else:
        return jsonify({"message": "Settings not found"}), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1983, debug=True)
