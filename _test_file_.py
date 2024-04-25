import pprint

from static.data.database import UserDB
from config import _USER_DATABASE_

db = UserDB('users', _USER_DATABASE_)

data = db.get_data("""SELECT * FROM Users""", ())

print(data)

db.close_connection()
