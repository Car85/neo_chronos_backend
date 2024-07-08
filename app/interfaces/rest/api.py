from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO
from ...application.settings_service import SettingsService
from ...infrastructure.settings_repository import SQLiteSettingsRepository
from ...domain.models import Settings, session_scope

app = Flask(__name__)
CORS(app)
DB_PATH = "./chronos.db"
socketio = SocketIO(app)
settings_repository = SQLiteSettingsRepository(DB_PATH)
settings_service = SettingsService(settings_repository)

@app.route('/settings', methods=['GET'])
def get_settings():
    settings = settings_service.get_settings()
    return jsonify(settings.__dict__)


@app.route('/settings', methods=['POST'])
def add_settings():
    data = request.json
    settings = Settings(
        id=data['id'],
        setpoint_min=data['setpoint_min'],
        setpoint_max=data['setpoint_max'],
        setpoint_offset_summer=data['setpoint_offset_summer'],
        setpoint_offset_winter=data['setpoint_offset_winter'],
        tolerance=data['tolerance'],
        mode_change_delta_temp=data['mode_change_delta_temp'],
        cascade_time=data['cascade_time'],
        mode=data['mode'],
        mode_switch_timestamp=data['mode_switch_timestamp'],
        mode_switch_lockout_time=data['mode_switch_lockout_time']
    )
    settings_service.add_settings(settings)
    return '', 204


@app.route('/settings', methods=['PUT'])
def update_settings():
    data = request.json
    settings = Settings(
        id=data['id'],
        setpoint_min=data['setpoint_min'],
        setpoint_max=data['setpoint_max'],
        setpoint_offset_summer=data['setpoint_offset_summer'],
        setpoint_offset_winter=data['setpoint_offset_winter'],
        tolerance=data['tolerance'],
        mode_change_delta_temp=data['mode_change_delta_temp'],
        cascade_time=data['cascade_time'],
        mode=data['mode'],
        mode_switch_timestamp=data['mode_switch_timestamp'],
        mode_switch_lockout_time=data['mode_switch_lockout_time']
    )
    settings_service.update_settings(settings)
    return '', 204

@socketio.on('update_settings')
def handle_update_settings(data):
    with session_scope() as session:
        settings = session.query(Settings).first()
        for name, value in data.items():
            setattr(settings, name, value)
        session.commit()

if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=8000)
