from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flask_login import UserMixin
from sqlalchemy.sql import func
from .models import DB_NAME
from .models import db

# create a database object
#db = SQLAlchemy()
#DB_NAME= "database.db"



def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hdiwuediwc'
    app.config['SQLALCHEMY_DATABASE_URI']=f'sqlite:///{DB_NAME}'
    db.init_app(app)

    

    from .views import views
    from .auth import auth


    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # import models file
    from . import models
    from .models import User, Note
    with app.app_context():
        db.create_all()
    

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    # telling flask how we load a user, by default looks for primary key
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
