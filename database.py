import sqlite3
from pprint import pprint


def connect(database_name, response):
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()
    data = cursor.execute(response).fetchall()
    connection.close()

    return data


# pprint(connect('music.db', 'SELECT * FROM Music'))


def transform_data(data: list[tuple]):
    songs = list()

    for song in data:
        songs.append(
            {
                'id': song[0],
                'name': song[1],
                'artist': song[2],
                'genre': song[3],
                'link': song[4]
            }
        )

    return songs


# data = connect('music.db', 'SELECT * FROM Music')
# data1 = transform_data(data)
# pprint(data1)

