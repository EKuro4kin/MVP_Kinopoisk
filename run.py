from project.config import DevelopmentConfig
from project.models import Genre
from project.models import Director
from project.models import Movie
from project.models import User
from project.server import create_app, db

app = create_app(DevelopmentConfig)


@app.shell_context_processor
def shell():
    return {
        "db": db,
        "Genre": Genre,
        "Director": Director,
        "Movie": Movie,
        "User": User,

    }


if __name__ == '__main__':
    app.run(port=25000)