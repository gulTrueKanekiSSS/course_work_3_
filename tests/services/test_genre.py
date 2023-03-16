from unittest.mock import MagicMock

import pytest

from app.dao.model.genre import Genre
from app.dao.genre import GenreDAO
from app.services.genre import GenreService


@pytest.fixture
def genre_dao():
    genre_dao = GenreDAO(None)

    series = Genre(id=1, name='series')
    movies = Genre(id=2, name='movies')
    drama = Genre(id=3, name='drama')

    genre_dao.get_one = MagicMock(return_value=series)
    genre_dao.get_all = MagicMock(return_value=[series, movies, drama])
    genre_dao.create = MagicMock(return_value=Genre(id=3))
    genre_dao.delete = MagicMock()
    genre_dao.update = MagicMock()
    return genre_dao


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one(1)

        assert genre is not None
        assert genre.id is not None

    def test_get_all(self):
        genres = self.genre_service.get_all()

        assert len(genres) > 0

    def test_create(self):
        genre_d = {
            "name": "comedy"
        }
        genre = self.genre_service.create(genre_d)

        assert genre.id is not None

    def test_delete(self):
        self.genre_service.delete(1)

    def test_update(self):
        genre_d = {
            "id": 2,
            "name": "Triller"
        }
        self.genre_service.update(genre_d)