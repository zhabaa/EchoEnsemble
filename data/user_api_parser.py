from flask_restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument('id', required=True, type=int)
parser.add_argument('username', required=True, type=str)
parser.add_argument('email', required=True, type=str)
parser.add_argument('icon', required=True, type=bytes)
parser.add_argument('isCreater', required=True, type=bool)
