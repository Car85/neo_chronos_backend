from ..domain.repository import UserSettingsRepository
from ..domain.models import Settings, session_scope
from ..infrastructure.communication.socket_client import SocketClient

class UserService:

    def __init__(self, repository: UserSettingsRepository):
        self.repository = repository
        self.socket_client = SocketClient()  

    