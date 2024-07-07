import unittest
from app.application.services import UserService
from app.domain.models import User
from app.infrastructure.sqlite_repository import SQLiteUserRepository

class TestUserService(unittest.TestCase):

    def setUp(self):
        self.repository = SQLiteUserRepository(':memory:')
        self.service = UserService(self.repository)

    def test_create_user(self):
        self.service.create_user('John Doe', 'john@example.com')
        users = self.service.list_users()
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].name, 'John Doe')

    def test_get_user(self):
        self.service.create_user('John Doe', 'john@example.com')
        user = self.service.get_user(1)
        self.assertEqual(user.name, 'John Doe')

if __name__ == '__main__':
    unittest.main()
