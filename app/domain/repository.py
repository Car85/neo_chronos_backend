from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from .models import Settings

class UserSettingsRepository(ABC):


    def __init__(self, session: Session):
        self.session = session

    @abstractmethod
    def add(self, user: Settings):
        pass

    @abstractmethod
    def get(self, user_id: int) -> Settings:
        pass


    @abstractmethod
    def update(self, settings: Settings) -> None:
        pass

    @abstractmethod
    def list(self) -> list[Settings]:
        pass
