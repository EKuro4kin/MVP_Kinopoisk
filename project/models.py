from sqlalchemy import Column, String, relationship, Integer, Float, ForeignKey

from project.setup.db import models


class Genre(models.Base):
    __tablename__ = 'genres'

    name = Column(String(100), unique=True, nullable=False)

class Director(models.Base):
    __tablename__ = 'directors'

    name = Column(String(100), unique=True, nullable=False)

class Movie(models.Base):
    __tablename__ = 'movies'

    title = Column(String(255))
    description = Column(String(255))
    trailer = Column(String(255))
    year = Column(Integer)
    rating = Column(Float)
    genre_id = Column(Integer, ForeignKey("genre.id"))
    genre = relationship("Genre")
    director_id = Column(Integer, ForeignKey("director.id"))
    director = relationship("Director")

class User(models.Base):
    __tablename__ = 'users'

    title = Column(String(255))
    email = Column(String(255))
    password_hash = Column(String(255))
    name = Column(String(255))
    surname = Column(String(255))
    favorite_genre = Column(ForeignKey("genres.id"))
