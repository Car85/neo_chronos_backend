from ..domain.models import Settings
from ..domain.repository import SettingsRepository


class SettingsService:

    def __init__(self, settings_repository: SettingsRepository):
        self.settings_repository = settings_repository


    def get_settings_by_id(self, id: int) -> Settings:
        return self.settings_repository.get(id)

    def update_settings(self, settings: Settings) -> None:
        self.settings_repository.update(settings)

    def add_settings(self, settings: Settings) -> None:
        self.settings_repository.add_settings(settings)

