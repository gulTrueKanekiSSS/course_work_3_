from unittest.mock import MagicMock

import pytest

from app.dao.model.director import Director
from app.dao.director import DirectorDAO
from app.services.director import DirectorService

@pytest.fixture()
def director_dao():

    director_dao = DirectorDAO(None)

    harry = Director(id=1, name="Harry")
    ronald = Director(id=2, name="Ronald")
    hermiona = Director(id=3, name="hermiona")

    director_dao.get_one = MagicMock(return_value=harry)
    director_dao.get_all = MagicMock(return_value=[harry, hermiona, ronald])
    director_dao.create = MagicMock(return_value=Director(id=1))
    director_dao.update = MagicMock()
    director_dao.delete = MagicMock()

    return director_dao

class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)
    def test_get_one(self):
        user = self.director_service.get_one(1)

        assert user is not None
        assert user.id is not None

    def test_get_all(self):
        users = self.director_service.get_all()

        assert len(users) > 0

    def test_create(self):
        director_d = {
            "name": "Drako"
        }
        director = self.director_service.create(director_d)

        assert director.id is not None

    def test_update(self):
        user_d = {
            "id": 1,
            "name": "Goil"
        }
        self.director_service.update(user_d)

    def test_delete(self):
        self.director_service.delete(3)




