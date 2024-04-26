import sqlalchemy
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


class UserSQLA(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'Users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    username = sqlalchemy.Column(sqlalchemy.String)
    email = sqlalchemy.Column(sqlalchemy.String)
    icon = sqlalchemy.Column(sqlalchemy.BLOB)
    password = sqlalchemy.Column(sqlalchemy.String)
    isCreator = sqlalchemy.Column(sqlalchemy.BOOLEAN)
