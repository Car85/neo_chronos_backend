from flask import Flask, request
from flask_socketio import SocketIO, emit
from ../../domain.models import Settings, session_scope

app = Flask(__name__)
socketio = SocketIO(app)

@socketio.on('update_settings')
def handle_update_settings(data):
    with session_scope() as session:
        settings = session.query(Settings).first()
        for name, value in data.items():
            setattr(settings, name, value)
        session.commit()

if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=8000)
