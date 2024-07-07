import sqlite3
from ..domain.models import Settings
from ..domain.repository import UserRepository

class SQLiteUserRepository(UserRepository):

    def __init__(self, db_path):
        self.db_path = db_path
        self._create_table()

    def get_connection(self):
        return sqlite3.connect(self.db_path)

    def _create_table(self):
        connection = self.get_connection()
        with connection:
            connection.execute(
                'CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)'
            )

    def add(self, user: User):
        connection = self.get_connection()
        with connection:
            connection.execute(
                'INSERT INTO users (name, email) VALUES (?, ?)', (user.name, user.email)
            )

    def get(self, user_id: int) -> User:
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT id, name, email FROM users WHERE id = ?', (user_id,))
        row = cursor.fetchone()
        if row:
            return User(id=row[0], name=row[1], email=row[2])
        return None

    def list(self) -> list[User]:
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT id, name, email FROM users')
        rows = cursor.fetchall()
        return [User(id=row[0], name=row[1], email=row[2]) for row in rows]
