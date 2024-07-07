from ..domain.models import Settings
from ..infrastructure.communication.socket_client import SocketClient


class SettingsService:

    def __init__(self, settings_repository: Settings):
        self.settings_repository = settings_repository
        self.socket_client = SocketClient()  


    def get_settings(self) -> Settings:
        return self.settings_repository.get()

    def update_settings(self, settings: Settings) -> None:
        self.settings_repository.update(settings)

