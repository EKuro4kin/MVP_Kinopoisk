from typing import Optional, List

from project.dao import UsersDAO
from project.exceptions import ItemNotFound
from project.models import User
from project.tools.security import generate_tokens, approve_refresh_token, get_data_from_token, generate_password_hash

#Сервис с логикой для работы с базой данных модели User
class UsersService:
    def __init__(self, dao: UsersDAO) -> None:
        self.dao = dao

    def get_item(self, pk: int) -> User:
        if user := self.dao.get_by_id(pk):
            return user
        raise ItemNotFound(f'Genre with pk={pk} not exists.')

    def get_all(self, page: Optional[int] = None) -> List[User]:
        return self.dao.get_all(page=page)

# метод, создаёт пользователя (записывая логин и пароль в базу данных(таблицу))
    def create_user(self, login, password):
        self.dao.create(login, password)

# метод, возвращает пользователя по переданному логину (проверяет логин и возвращает пользователя с таким логином)
    def get_user_by_login(self, login):
        return self.dao.get_user_by_login(login)

# метод, возвращает токены пользователя (пользователя которого ввели емеил и пароль)
    def check(self, login, password):
        user = self.get_user_by_login(login)
        return generate_tokens(email=user.email, password=password, password_hash=user.password_hash)

# метод, возвращает обновленные токены пользователя, по переданному refresh_token
    def update_token(self, refresh_token):
        return approve_refresh_token(refresh_token)

# метод, возвращает емеил пользователя по переданному refresh_token
    def get_user_by_token(self, refresh_token):
        data = get_data_from_token(refresh_token)

        if data:
            return self.get_user_by_login(data.get('email'))

# метод, возвращает обновленные данные конкретного пользователя (пользователь находится по refresh_token)
    def update_user(self, data: dict, refresh_token):
        user = self.get_user_by_token(refresh_token)
        if user:
            self.dao.update(login=user.email, data=data)
            return self.get_user_by_token(refresh_token)

# метод, возвращает обновленный пароль определённого пользователя (смена пароля)
    def update_password(self, data, refresh_token):
        user = self.get_user_by_token(refresh_token)
        if user:
            self.dao.update(login=user.email, data={"password": generate_password_hash(data.get('password_2'))})
            return self.check(login=user.email, password=data.get('password_2'))
