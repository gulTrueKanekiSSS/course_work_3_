from unittest.mock import MagicMock

import pytest

from app.dao.model.user import User
from app.dao.user import UserDao
from app.services.user import UserService


@pytest.fixture
def user_dao():
    user_dao = UserDao(None)

    roma_boronov_csgo = User(id=1, username='Roma')
    pasha_top_programmer = User(id=2, username='Pasha')
    dima = User(id=3, username='Dima')

    user_dao.get_one = MagicMock(return_value=roma_boronov_csgo)
    user_dao.get_all = MagicMock(return_value=[roma_boronov_csgo, pasha_top_programmer, dima])
    user_dao.create = MagicMock(return_value=User(id=3))
    user_dao.get_by_username = MagicMock(return_value=pasha_top_programmer)
    user_dao.delete = MagicMock()
    user_dao.update = MagicMock()
    return user_dao


class TestUserService:
    @pytest.fixture(autouse=True)
    def user_service(self, user_dao):
        self.user_service = UserService(dao=user_dao)

    def test_get_one(self):
        user = self.user_service.get_one(1)

        assert user is not None
        assert user.id is not None

    def test_get_all(self):
        users = self.user_service.get_all()

        assert len(users) > 0

    def test_create(self):
        user_d = {
            "username": 'who',
            "password": 'test',
            "role": 'admin'
        }
        user = self.user_service.create(user_d)

        assert user.id is not None

    def test_delete(self):
        self.user_service.delete(1)

    def test_update(self):
        user_d = {
            "id": 2,
            "username": "RoRo"
        }
        self.user_service.update(user_d)
