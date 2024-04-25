from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    params = {
        'title': 'music-test',
        'filename': 'lastlove',
        'filepath': url_for('static', filename='music/lastlove.mp3'),
    }
    return render_template('music_test.html', **params)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
