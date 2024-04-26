from config import _MUSIC_DATABASE_
from data.binary import write_to_file
from data.database import MusicDB

db = MusicDB('music', _MUSIC_DATABASE_)

# data = db.add_song(
#     'Гроза',
#     'Сова',
#     convert_to_binary_data('static/music/Sova_-_Groza.mp3'),
#     'groza',
#     convert_to_binary_data('static/music/sova_image.jpg')
# )


data = db.get_song_data('groza')[0]
# data = ''.join(data

# with open('log.txt', 'w', encoding='utf-8') as output:
#     output.write(str(data))
print(len(data))
write_to_file(data[3], 'static/temp/out.mp3')

db.close_connection()
