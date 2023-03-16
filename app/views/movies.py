from flask import request
from flask_restx import Resource, Namespace

from app.container import movie_service
from app.dao.model.movie import Movie_scheme, Movie
from app.data_base import db
from decorator import auth_reguired

movies_ns = Namespace('movies')

movie_schema = Movie_scheme()
movies_schema = Movie_scheme(many=True)


@movies_ns.route('/')
class MoviesView(Resource):
    # @auth_reguired
    def get(self):
        director_id = request.args.get("director_id")
        genre_id = request.args.get("genre_id")
        movie_year = request.args.get("year")
        status = request.args.get('status')
        page = request.args.get('page')

        filters = {
            'director_id': director_id,
            'genre_id': genre_id,
            'year': movie_year,
            'status': status,
            'page': page
        }

        all_movies = movie_service.get_all(filters)

        return movies_schema.dump(all_movies)

        # @auth_reguired

    def post(self):
        req_json = request.json
        movie_service.create(req_json)

        return "", 201


@movies_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid: int):
        movie = movie_service.get_one(mid)
        return movie_schema.dump(movie)

    def put(self, mid):
        movie = request.json
        movie['id'] = mid
        movie_service.update(movie)
        return '', 204

    def patch(self, mid):
        movie = request.json
        movie['id'] = mid
        movie_service.update(movie)
        return '', 204

    def delete(self, mid):
        movie_service.delete(mid)
        return '', 204
