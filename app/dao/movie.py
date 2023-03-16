from flask import request
from sqlalchemy import desc

from app.dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_movie(self, mid):
        return self.session.query(Movie).get(mid)

    def get_all(self):
        return self.session.query(Movie).all()

    def create(self, data):
        movie = Movie(**data)

        self.session.add(movie)
        self.session.commit()

        return movie

    def get_by_did(self, did):
        movie = self.session.query(Movie).filter(Movie.director_id == did)
        return movie

    def get_by_gid(self, gid):
        movie = self.session.query(Movie).filter(Movie.genre_id == gid)
        return movie

    def get_by_year(self, year):
        movie = self.session.query(Movie).filter(Movie.year == year)
        return movie

    def delete_movie(self, mid):
        movie = self.get_movie(mid)
        self.session.delete(movie)
        self.session.commit()

    def update_movie(self, data):
        self.session.add(data)
        self.session.commit()

    def get_status(self):
        return self.session.query(Movie).order_by(desc(Movie.year))