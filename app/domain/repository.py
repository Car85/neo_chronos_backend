# app/domain/repository.py
from abc import ABC, abstractmethod
from ..domain.models import Settings

class SettingsRepository(ABC):

    @abstractmethod
    def add_settings(self, settings: Settings) -> None:
        pass

    @abstractmethod
    def update_settings(self, settings: Settings) -> None:
        pass

    @abstractmethod
    def get(self, id: int) -> Settings:
        pass

    @abstractmethod
    def list(self) -> list[Settings]:
        pass
