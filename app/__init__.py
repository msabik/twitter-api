from flask import Flask
from flask_restplus import Api
<<<<<<< HEAD
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
=======
from .db import tweet_repository
from .models import Tweet

tweet_repository.add(Tweet("a first tweet"))
tweet_repository.add(Tweet("a second tweet"))
>>>>>>> df1b6b8718bfc5762252663c6cefef16e49a6ef1


def create_app():
    app = Flask(__name__)

<<<<<<< HEAD
    from config import Config
    app.config.from_object(Config)
    db.init_app(app)

=======
>>>>>>> df1b6b8718bfc5762252663c6cefef16e49a6ef1
    @app.route('/hello')
    def hello():
        return "Goodbye World!"

    from .apis.tweets import api as tweets
    api = Api()
    api.add_namespace(tweets)
    api.init_app(app)

    app.config['ERROR_404_HELP'] = False
    return app
<<<<<<< HEAD

=======
>>>>>>> df1b6b8718bfc5762252663c6cefef16e49a6ef1
