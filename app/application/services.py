from ..domain.repository import UserSettingsRepository
from ..domain.models import Settings, session_scope
from ..infrastructure.communication.socket_client import SocketClient

class UserService:

    def __init__(self, repository: UserSettingsRepository):
        self.repository = repository
        self.socket_client = SocketClient()  

    def update_settings(self, name, value):
        with session_scope.session_scope() as session:
            property_ = session.query(session_scope.Settings).first()
            setattr(property_, name, value)
        if name == "cascade_time":
            value /= 60
        if name != "mode_switch_timestamp":
            self.socket_client.send({
                "event": "misc",
                "message": {name: value}
            })


    def get_settings(self, user_id: int) -> UserSettingsRepository:
        return self.repository.get(user_id)

    def list_users(self) -> list[UserSettingsRepository]:
        return self.repository.list()
