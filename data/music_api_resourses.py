from flask import abort, jsonify
from flask_restful import Resource

from . import db_session
from .music_api import MusicSQLA as music
from .music_api_parser import *


class musicResource(Resource):
    def get(self, music_id):
        abort_if_musics_not_found(music_id)

        session = db_session.create_session()
        musics = session.query(music).get(music_id)

        return jsonify(
            {
                'musics.html': musics.to_dict(
                    only=("id", "name", "artist", "song", "song_link", "song_image")
                )
            }
        )

    def delete(self, music_id):
        abort_if_musics_not_found(music_id)

        session = db_session.create_session()
        musics = session.query(music).get(music_id)

        session.delete(musics)
        session.commit()

        return jsonify(
            {
                'success': 'OK'
            }
        )

    def put(self, music_id):
        args = parser.parse_args()

        abort_if_musics_not_found(music_id)

        session = db_session.create_session()
        musics = session.query(music).get(music_id)

        musics.name = args['name']
        musics.email = args['email']
        musics.artist = args['artist']
        musics.song = args['song']
        musics.song_link = args['song_link']
        musics.song_image = args['song_image']

        session.commit()
        return jsonify(
            {
                'success': 'OK'
            }
        )


class musicListResource(Resource):
    def get(self):
        session = db_session.create_session()
        musics = session.query(music).all()
        return jsonify(
            {'websites.html':
                [
                    item.to_dict(
                        only=("id", "name", "artist", "song", "song_link", "song_image"))
                    for item in musics
                ]
            }
        )

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        musics = music()

        musics.id = args['id']
        musics.name = args['name']
        musics.email = args['email']
        musics.artist = args['artist']
        musics.song = args['song']
        musics.song_link = args['song_link']
        musics.song_image = args['song_image']

        session.add(musics)
        session.commit()
        return jsonify(
            {
                'id': musics.id
            }
        )


def abort_if_musics_not_found(music_id):
    session = db_session.create_session()
    musics = session.query(music).get(music_id)
    if not musics:
        abort(404, message=f"musics {music_id} not found")
