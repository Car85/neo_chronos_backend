from ..domain.repository import SettingsRepository
from ..domain.models import Settings

class SettingsService:

    def __init__(self, settings_repository: SettingsRepository):
        self.settings_repository = settings_repository

    def get_settings(self) -> Settings:
        return self.settings_repository.get()

    def update_settings(self, settings: Settings) -> None:
        self.settings_repository.update(settings)
