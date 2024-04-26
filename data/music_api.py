import sqlalchemy
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


class MusicSQLA(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'Music'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    artist = sqlalchemy.Column(sqlalchemy.String)
    song = sqlalchemy.Column(sqlalchemy.BLOB)
    song_link = sqlalchemy.Column(sqlalchemy.String)
    song_image = sqlalchemy.Column(sqlalchemy.BLOB)
