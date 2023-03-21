from marshmallow import fields, Schema

from app.dao.model.director import Director_scheme
from app.dao.model.genre import Genre_scheme
from app.data_base import db


class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=True)
    description = db.Column(db.String(255), nullable=True)
    trailer = db.Column(db.String(255), nullable=True)
    year = db.Column(db.Integer, nullable=True)
    rating = db.Column(db.Float, nullable=True)
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"), nullable=True)
    genre = db.relationship("Genre")
    director_id = db.Column(db.Integer, db.ForeignKey("director.id"), nullable=True)
    director = db.relationship("Director")

class Movie_scheme(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
    genre_id = fields.Int()
    genre = fields.Nested(Genre_scheme)
    director_id = fields.Int()
    director = fields.Nested(Director_scheme)