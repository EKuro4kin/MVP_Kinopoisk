from typing import Optional, List

from project.dao import MoviesDAO
from project.exceptions import ItemNotFound
from project.models import Movie

#Сервис с логикой для работы с базой данных модели Movie
class MoviesService:
    def __init__(self, dao: MoviesDAO) -> None:
        self.dao = dao

    def get_item(self, pk: int) -> Movie:
        if movie := self.dao.get_by_id(pk):
            return movie
        raise ItemNotFound(f'Movie with pk={pk} not exists.')

    def get_all(self, filter=None, page: Optional[int] = None) -> List[Movie]:
        return self.dao.get_all_order_by(page=page, filter=filter)
