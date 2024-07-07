from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from .models import User

class UserSettingsRepository(ABC):


    def __init__(self, session: Session):
        self.session = session

    @abstractmethod
    def add(self, user: User):
        pass

    @abstractmethod
    def get(self, user_id: int) -> User:
        pass

    @abstractmethod
    def list(self) -> list[User]:
        pass
