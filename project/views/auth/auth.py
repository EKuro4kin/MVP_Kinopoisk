from flask import request
from flask_restx import Namespace, Resource

from project.container import user_service
from project.setup.api.models import user
from project.setup.api.parsers import page_parser


auth_ns = Namespace('auth')

#вьюшка регистрирует пользователя по емейлу и паролю
@auth_ns.route('/register/')
class RegisterView(Resource):
    @auth_ns.marshal_with(user, as_list=True, code=200, description='OK')
    def post(self):
        data = request.json
        if data.get('email') and data.get('password'):
            return user_service.create_user(data.get('email'), data.get('password')), 201
        else:
            return "Чего то не хватает", 401

#вьюшка авторизовывает пользователя по емейлу и паролю
@auth_ns.route('/login/')
class LoginView(Resource):
    @auth_ns.response(404, 'Not Found')

    def post(self):
        data = request.json
        if data.get('email') and data.get('password'):
            return user_service.check(data.get('email'), data.get('password')), 201
        else:
            return "Чего то не хватает", 401

    @auth_ns.response(404, 'Not Found')
    def put(self):
        """
        Обновляет токены пользователя.
        """
        data = request.json
        if data.get('access_token') and data.get('refresh_token'):
            return user_service.update_token(data.get('refresh_token')), 201
        else:
            return "Чего то не хватает", 401