from flask_restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument('id', required=True, type=int)
parser.add_argument('username', required=True, type=str)
parser.add_argument('artist', required=True, type=str)
parser.add_argument('song', required=True, type=bytes)
parser.add_argument('song_link', required=True, type=str)
parser.add_argument('song_image', required=True, type=bytes)
