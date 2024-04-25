import io
import logging
import sqlite3

from .hashing import Hashing

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def to_blob_format(file):
    file_object = open(file, "rb")
    binary_file = file_object.read()
    return binary_file


def from_blob_format(binary_file):
    file_stream = io.BytesIO(binary_file)
    file = file_stream.read()
    return file


class DB:
    """
    Origin database class
    """
    def __init__(self, database_name: str, database_path: str):
        self.database_name = database_name
        self.database_path = database_path

        self.connection: sqlite3.Connection = sqlite3.connect(self.database_path)
        self.connection.row_factory = sqlite3.Row
        self.cursor: sqlite3.Cursor = self.connection.cursor()
        self.hasher: Hashing = Hashing()

    def commit_changes(self):
        self.connection.commit()
        logger.info(f'Изменения в {self.database_name} сохранены')

    def close_connection(self):
        self.commit_changes()
        self.connection.close()
        logger.info(f'Соединение c {self.database_name} закрыто')

    def get_data(self, query: str, params: tuple):
        if self.cursor is not None and self.connection is not None:
            sql_data: sqlite3.Cursor = self.cursor.execute(query, params)
            fetch_sql_data = sql_data.fetchall()
            return fetch_sql_data

    @staticmethod
    def to_blob_format(file):
        file_object = open(file, "rb")
        binary_file = file_object.read()
        return binary_file

    @staticmethod
    def from_blob_format(binary_file):
        file_stream = io.BytesIO(binary_file)

        return file_stream


class UserDB(DB):
    def __init__(self, database_name: str, database_path: str):
        super().__init__(database_name, database_path)

    def add_user(self, username: str, email: str, password: str):
        query = f"""INSERT INTO Users (username, email, password) VALUES (?, ?, ?)"""
        self.cursor.execute(query, (username, email, password))
        logger.info(f'Success added user {username} to database {self.database_name}')

    def get_user_data(self, email: str, *args):
        if not args:
            query = f"""SELECT * FROM Users WHERE email = ?"""
            user_data = self.get_data(query, (email,))
            logger.info(f'data from user {email} collected')
        else:
            query = f"""SELECT {args[0]} FROM Users WHERE email = ?"""
            user_data = self.get_data(query, (email,))
            logger.info(f'data {args} from user {email} collected')

        return user_data

    def change_data(self, email: str, column_name: str, new_data: str | bytes):
        if column_name == 'password':
            new_data = self.hasher.hash_data(new_data)

        query = f"""UPDATE Users SET {column_name} = ? WHERE Users.email = ?"""
        self.cursor.execute(query, (new_data, email,))
        logger.info(f'{column_name} changed')

    def delete_user(self, email: str):
        query = f"""DELETE FROM Users WHERE email = ?"""
        self.cursor.execute(query, (email,))
        logger.info(f'user {email} was deleted')


class MusicDB(DB):
    """
    Подвязать музыку по айдишнику в плйлист
    """
    def __init__(self, database_name: str, database_path: str):
        super().__init__(database_name, database_path)

    def add_song(self, song_name: str, artist: str, song_genre: str, song_file: str | bytes, song_link: str,
                 song_icon_file: str | bytes):
        query = f"""INSERT INTO Music (name, artist, genre, song, song_link, song_image) VALUES (?, ?, ?, ?, ?, ?)"""
        self.cursor.execute(query, (song_name, artist, song_genre, song_file, song_link, song_icon_file))
        logger.info(f'Succec added song {song_name} to database {self.database_name}')

    def get_song_data(self):
        pass

    def change_song_data(self):
        pass

    def delete_music(self):
        pass
