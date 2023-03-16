from flask_restx import Namespace, Resource
from app.container import user_service, user_dao
from app.dao.model.user import User_scheme
from flask import request

user_ns = Namespace("users")

user_schema = User_scheme()
users_schema = User_scheme(many=True)

@user_ns.route("/")
class UsersView(Resource):
    def get(self):
        users = user_service.get_all(), 200
        return users_schema.dumps(users)
    def post(self):
        req_data = request.json
        print(req_data)
        user_service.create(req_data)
        return "", 201



@user_ns.route("/<int:uid>")
class UserView(Resource):
    def get(self, uid: int):
        print(uid)
        user = user_dao.get_one(uid)
        return user_schema.dumps(user)

    def put(self):
        data = request.json
        user_service.update(data)
        return "", 204

    def patch(self, uid: int):
        data = request.json
        user_service.update_partial(data, uid)
        return "", 204

@user_ns.route("/password/<int:uid>")
class UserView(Resource):
    def put(self, uid):
        data = request.json
        user_service.update(data, uid)
