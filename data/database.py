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
    def __init__(self, database_name: str, database_path: str):
        self.database_name = database_name
        self.database_path = database_path

        try:
            self.connection: sqlite3.Connection = sqlite3.connect(self.database_path)
            self.cursor: sqlite3.Cursor = self.connection.cursor()

        except sqlite3.Error as ex:
            logger.critical(f'Ошибка {ex} при подключении к {self.database_name}')

        self.hasher: Hashing = Hashing()

    def commit_changes(self):
        self.connection.commit()
        logger.info(f'Изменения в {self.database_name} сохранены')

    def close_connection(self):
        self.commit_changes()
        self.connection.close()
        logger.info(f'Соединение c {self.database_name} закрыто')

    def get_data(self, query: str, params: tuple):
        try:
            if self.cursor is not None and self.connection is not None:
                sql_data: sqlite3.Cursor = self.cursor.execute(query, params)
                fetch_sql_data = sql_data.fetchall()
                return fetch_sql_data

        except sqlite3.Error as ex:
            logger.critical(f'Ошибка получения данных {ex}')
            return []

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
        try:
            query = f"""INSERT INTO Users (username, email, password) VALUES (?, ?, ?)"""
            self.cursor.execute(query, (username, email, password))
            logger.info(f'Пользователь {username} успешно добавлен в {self.database_name}')

        except sqlite3.Error as ex:
            logger.critical(f'Ошибка при добавлении пользователя {ex}')

    def get_user_data(self, email: str, *args):
        if not args:
            query = f"""SELECT * FROM Users WHERE email = ?"""
            user_data = self.get_data(query, (email,))
            logger.info(f'Данные пользователя с {email} собраны')
        else:
            query = f"""SELECT {args[0]} FROM Users WHERE email = ?"""
            user_data = self.get_data(query, (email,))
            logger.info(f'Данные пользователя {email} {args} собраны')

        return user_data

    def get_user(self, user_id: int):
        query = f"""SELECT * FROM Users WHERE id = ? LIMIT 1"""
        user = self.get_data(query, (user_id,))
        logger.info(f'Пользователь с id={user_id} получен')

        return user

    def change_data(self, email: str, column_name: str, new_data: str | bytes):
        try:
            if column_name == 'password':
                new_data = self.hasher.hash_data(new_data)

            query = f"""UPDATE Users SET {column_name} = ? WHERE Users.email = ?"""
            self.cursor.execute(query, (new_data, email,))
            logger.info(f'{column_name} изменено')

        except sqlite3.Error as ex:
            logger.critical(f'Ошибка при попытке обновления данных {ex}')

    def delete_user(self, email: str):
        try:
            query = f"""DELETE FROM Users WHERE email = ?"""
            self.cursor.execute(query, (email,))
            logger.info(f'user {email} was deleted')

        except sqlite3.Error as ex:
            logger.critical(f'Ошибка {ex} при удалении пользователя {email}')

    def check_password(self, email: str, password: str):
        user_password = self.get_user_data(email, ('password',))
        return self.hasher.hash_data(password) == user_password


class MusicDB(DB):
    def __init__(self, database_name: str, database_path: str):
        super().__init__(database_name, database_path)

    def add_song(self, song_name: str, artist: str, song_file: str | bytes, song_link: str, song_icon: str | bytes):
        try:
            query = f"""INSERT INTO Music (name, artist, song, song_link, song_image) VALUES (?, ?, ?, ?, ?)"""
            self.cursor.execute(query, (song_name, artist, song_file, song_link, song_icon))
            logger.info(f'Песня {song_name} успешно добавлена в {self.database_name}')

        except sqlite3.Error as ex:
            logger.critical(f'Ошибка {ex} при добавлении песни в {self.database_name}')

    def get_song_data(self, song_link: str, *args):
        if not args:
            query = f"""SELECT * FROM Music WHERE song_link = ?"""
            song_data = self.get_data(query, (song_link,))
            logger.info(f'Данные о {song_link} успешно собраны')
        else:
            query = f"""SELECT {args[0]} FROM Music WHERE song_link = ?"""
            song_data = self.get_data(query, (song_link,))
            logger.info(f'Данные {args} от песни {song_link} успешно собраны')

        return song_data

    def change_song_data(self, song_link: str, column_name: str, new_data: str | bytes):
        try:
            query = f"""UPDATE Music SET {column_name} = ? WHERE song_link = ?"""
            self.cursor.execute(query, (new_data, song_link,))
            logger.info(f'{column_name} изменено')

        except sqlite3.Error as ex:
            logger.critical(f'Ошибка {ex} при изменении {column_name}')

    def delete_music(self, song_link: str):
        try:
            query = f"""DELETE FROM Music WHERE song_link = ?"""
            self.cursor.execute(query, (song_link,))
            logger.info(f'Песня {song_link} успешно удалена')

        except sqlite3.Error as ex:
            logger.critical(f'Ошибка {ex} при удалении песни')
