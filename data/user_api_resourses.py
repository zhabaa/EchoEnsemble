from flask import abort, jsonify
from flask_restful import Resource

from . import db_session
from .user_api import UserSQLA as user
from .user_api_parser import *


class userResource(Resource):
    def get(self, user_id):
        abort_if_users_not_found(user_id)
        session = db_session.create_session()
        users = session.query(user).get(user_id)
        return jsonify(
            {
                'users.html': users.to_dict(
                    only=("id", "username", "email", "icon", "password", "isCreator")
                )
            }
        )

    def delete(self, user_id):
        abort_if_users_not_found(user_id)
        session = db_session.create_session()
        users = session.query(user).get(user_id)
        session.delete(users)
        session.commit()
        return jsonify(
            {
                'success': 'OK'
            }
        )

    def put(self, user_id):
        args = parser.parse_args()
        abort_if_users_not_found(user_id)
        session = db_session.create_session()
        users = session.query(user).get(user_id)

        users.username = args['username']
        users.email = args['email']
        users.icon = args['icon']
        users.password = args['password']
        users.email = args['email']
        users.isCreator = args['isCreator']

        session.commit()
        return jsonify(
            {
                'success': 'OK'
            }
        )


class userListResource(Resource):
    def get(self):
        session = db_session.create_session()
        users = session.query(user).all()
        return jsonify({'websites.html': [
            item.to_dict(
                only=("id", "username", "email", "icon", "password", "isCreator")) for
            item in users]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        users = user()

        users.id = args['id']
        users.username = args['username']
        users.email = args['email']
        users.icon = args['icon']
        users.password = args['password']
        users.email = args['email']
        users.isCreator = args['isCreator']

        session.add(users)
        session.commit()
        return jsonify(
            {
                'id': users.id
            }
        )


def abort_if_users_not_found(user_id):
    session = db_session.create_session()
    users = session.query(user).get(user_id)
    if not users:
        abort(404, message=f"users {user_id} not found")
