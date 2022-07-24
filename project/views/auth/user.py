from flask import request
from flask_restx import Namespace, Resource

from project.container import user_service
from project.setup.api.models import user
from project.setup.api.parsers import page_parser


user_ns = Namespace('user')

@user_ns.route('/')
class UserView(Resource):
    @user_ns.marshal_with(user, as_list=True, code=200, description='OK')
    def get(self):
        """
        Получаем информацию о пользователе.
        """
        header = request.headers.environ.get('HTTP_AUTHORIZATION').replace('Bearer ', '')

        return user_service.get_user_by_token(refresh_token=header)


    def patch(self):
        """
        Обновляем данные в профиле пользователя.
        """
        data = request.json
        header = request.headers.environ.get('HTTP_AUTHORIZATION').replace('Bearer ', '')

        return user_service.update_user(data=data, refresh_token=header)

@user_ns.route('/password/')
class LoginView(Resource):
    @user_ns.response(404, 'Not Found')
    def put(self):
        """
        Обновляем пароль пользователя (смена пароля).
        """
        data = request.json
        header = request.headers.environ.get('HTTP_AUTHORIZATION').replace('Bearer ', '')

        return user_service.update_password(data=data, refresh_token=header)