from marshmallow import fields, Schema

from app.data_base import db


class User(db.Model):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=True)
    username = db.Column(db.String)
    surname = db.Column(db.String)
    password = db.Column(db.String, nullable=True)
    favorite_genre = db.Column(db.String)


class User_scheme(Schema):
    id = fields.Int()
    email = fields.Str()
    username = fields.Str()
    surname = fields.Str()
    password = fields.Str()
    favorite_genre = fields.Str()




