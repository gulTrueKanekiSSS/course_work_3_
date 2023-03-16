from flask_restx import Namespace, Resource
from flask import request

from app.container import genre_dao
from app.dao.model.genre import Genre_scheme

from decorator import auth_reguired



genres_ns = Namespace('genres')

genre_scheme = Genre_scheme()
genres_scheme = Genre_scheme(many=True)

@genres_ns.route('/')
class GenresView(Resource):
    # @auth_reguired
    def get(self):
        genres = genre_dao.get_all()
        return genres_scheme.dump(genres), 200

    def post(self):
        req_json = request.json
        genre_dao.create(req_json)

        return "", 201
@genres_ns.route('/<int:gid>')
class GenreView(Resource):
    # @auth_reguired
    def get(self, gid :int):
        try:
            genre = genre_dao.get_one(gid)
            return genre_scheme.dump(genre)
        except Exception:
            return "", 404

    def put(self, gid: int):
        req_json = request.json
        req_json["id"] = gid
        genre_dao.update(req_json)

        return "", 204

    def delete(self, gid: int):
        genre_dao.delete(gid)

        return "", 204