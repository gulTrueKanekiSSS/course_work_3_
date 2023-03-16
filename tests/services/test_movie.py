from unittest.mock import MagicMock

import pytest

from app.dao.model.movie import Movie
from app.dao.movie import MovieDAO
from app.services.movie import MovieService

@pytest.mark.skip(reason='ok')
def movie_dao():
    movie_dao = MovieDAO(None)

    w = Movie(id=1, title='w', description='sss', trailer='www', year=2005, rating=2.7, genre_id=1, genre='drama', director_id=1, director='nc3onco')
    a = Movie(id=2, title='a', description='sss', trailer='www', year=2006, rating=2.8, genre_id=2, genre='triller', director_id=2, director='wcdc3')

    movie_dao.get_movie = MagicMock(return_value=w)
    movie_dao.get_all = MagicMock(return_value=[w,a])
    movie_dao.create = MagicMock(return_value=Movie(2))

class TestMovieService:
    @pytest.mark.skip(reason='init')
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    @pytest.mark.skip(reason='init')
    def test_get_movie(self):
        movie = self.movie_service.get_one()
        assert movie is not None
        assert movie.id is not None

    @pytest.mark.skip(reason='init')
    def test_get_all(self):
        movies = self.movie_service.get_all()

        assert len(movies) > 1

    @pytest.mark.skip(reason='init')
    def test_create(self):
        movie_d = {
            "title": "v3v3ev2v",
            "description": "ci3jvcivi",
            "trailer": "cwv3v3vvv3v3v",
            "year": 2000007,
            "rating": 2.8,
        }
        movie = self.movie_service.create(movie_d)

        assert movie.id is not None






