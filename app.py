from flask import Flask, render_template, Response
from database import transform_data, connect


class App:
    def __init__(self):
        self.app = Flask(__name__)
        response = 'SELECT * FROM Music'

        self.stream = transform_data(connect('music.db', response))

    def start_app(self):
        @self.app.route('/')
        def index():
            general_data = {
                'title': 'Music Player'
            }

            return render_template('simple.html', entries=self.stream, **general_data)

        @self.app.route('/<int:stream_id>')
        def stream_mp3(stream_id):

            def generate():
                count = 1
                song = None
                data = self.stream

                for item in data:
                    if item['id'] == stream_id:
                        song = 'static/music/' + item['link'] + '.mp3'
                        print(song)

                try:
                    with open(song, 'rb') as fwav:
                        data = fwav.read(1024)

                        while data:
                            yield data
                            data = fwav.read(1024)
                            count += 1

                except Exception as ex:
                    print(f'Error: {ex}')

            return Response(generate(), mimetype='audio/mp3')

        self.app.run(host='127.0.0.1', port=1488, debug=True)


if __name__ == '__main__':
    a = App()
    a.start_app()
