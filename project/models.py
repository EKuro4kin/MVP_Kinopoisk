from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from marshmallow import Schema, fields

from project.setup.db import models


# Создаю модель жанр, для создании таблицы жанры
class Genre(models.Base):
    __tablename__ = 'genres'

    name = Column(String(100), unique=True, nullable=False)


# Модель режисера, для создании таблицы режисеры
class Director(models.Base):
    __tablename__ = 'directors'

    name = Column(String(100), unique=True, nullable=False)

# Модель фильмов, для создании таблицы с фильмами
class Movie(models.Base):
    __tablename__ = 'movies'

    title = Column(String(255))
    description = Column(String(255))
    trailer = Column(String(255))
    year = Column(Integer)
    rating = Column(Float)
    genre_id = Column(Integer, ForeignKey(Genre.id))
    genre = relationship("Genre")
    director_id = Column(Integer, ForeignKey(Director.id))
    director = relationship("Director")

# Модель пользователя, для создании таблицы с пользователями
class User(models.Base):
    __tablename__ = 'users'

    email = Column(String(255), nullable=False)
    password_hash = Column(String(255), nullable=False)
    name = Column(String(255))
    surname = Column(String(255))
    favourite_genre = Column(ForeignKey(Genre.id))
    genre = relationship("Genre")


# классы СХЕМЫ для сериализации НИЖЕ (4) через marshmallow, который не использовался в данном проекте
# оставлю тут, если время будит, попробую реализовать через marshmallow

# class GenreSchema(Schema):
#     id = fields.Int()
#     name = fields.Str()
#
#
# class DirectorSchema(Schema):
#     id = fields.Int()
#     name = fields.Str()
#
#
# class MovieSchema(Schema):
#     id = fields.Int()
#     title = fields.Str()
#     description = fields.Str()
#     trailer = fields.Str()
#     year = fields.Int()
#     rating = fields.Float()
#
#
# class UserSchema(Schema):
#     id = fields.Int()
#     title = fields.Str()
#     email = fields.Str()
#     password_hash = fields.Str()
#     name = fields.Str()
#     surname = fields.Str()
