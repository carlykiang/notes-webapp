
from os import path
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from sqlalchemy.sql import func

db = SQLAlchemy()
DB_NAME= "database.db"

class Setting(db.Model):
    #define all of the columns you want in the table
    id = db.Column(db.Integer, primary_key = True)
    color = db.Column(db.String(10000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class Note(db.Model):
    #define all of the columns you want in the table
    id = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    #must pass a valid id of an existing user
    #user comes from the name of the table you are getting the foreign id from
    #id is the name of the column you want to take it from
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    #define all of the columns you want in the table
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150), unique = True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')
    settings = db.relationship('Setting')

