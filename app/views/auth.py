from flask import request
from flask_restx import Namespace, Resource
from app.container import auth_service, user_service


auth_ns = Namespace("auth")


@auth_ns.route('/login/')
class AuthsViews(Resource):
    def post(self):
        data = request.json
        if None in [data.get("email", None), data.get("password", None)]:
            return "", 404
        tokens = auth_service.generate_token(data.get("email", None), data.get("password", None))

        return tokens, 201
    def put(self):
        data = request.json

        refresh_token = data.get('refresh_token', None)
        if refresh_token is None:
            return '', 401
        tokens = auth_service.approve_refr_token(refresh_token)

        return tokens, 201
@auth_ns.route('/register/')
class AuthView(Resource):
    def post(self):
        data = request.json
        if None in [data.get("email"), data.get("password")]:
            return "", 404
        print(data)
        user_service.create(data)
        return "", 201

