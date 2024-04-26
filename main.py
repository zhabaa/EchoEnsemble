import logging
from pprint import pprint

from flask import Flask, request, render_template, redirect, flash, session, url_for, abort
from flask_login import logout_user, LoginManager, login_user, login_required
from flask_restful import Api

from config import _USER_DATABASE_, _MUSIC_DATABASE_
from data import user_api_resourses, music_api_resourses
from data.database import UserDB, MusicDB
from data.user_login import UserLogin
from forms.load_fileForm import LoadFileForm
from forms.loginForm import LoginForm
from forms.registerForm import RegisterForm

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'qwerty'

login_manager = LoginManager()
login_manager.init_app(app)

user_db = None
music_db = None


def main():
    user_db.global_init("db/site_guessr.db")
    music_db.global_init("db/site_guessr.db")

    api.add_resource(user_api_resourses.UserListResource, '/api/users')
    api.add_resource(user_api_resourses.UserResource, '/api/user/<int:users_id>')

    api.add_resource(music_api_resourses.MusicListResource, '/api/music.html')
    api.add_resource(music_api_resourses.MusicResource, '/api/music/<int:music_id>')

    app.run(port=8088, host='127.0.0.1')


@app.before_request
def before_request():
    global user_db, music_db
    user_db = UserDB('users', _USER_DATABASE_)
    music_db = MusicDB('music', _MUSIC_DATABASE_)


@app.teardown_appcontext
def close_db(error):
    pass


@login_manager.user_loader
def load_user(user_id):
    logger.info('Load user')
    return UserLogin().fromDB(user_id, user_db)


# @app.route('/')
@app.route('/index')
@login_required
def index():
    return f"""<h1> Index page </h1>"""


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    params = {
        'title': 'EchoEnsamble Login',
        'style_css': url_for('static', filename='css/style_login.css'),
        'to_register': redirect(url_for('register')),
        # 'help': redirect(url_for('help'))
    }

    if request.method == 'POST':
        user = user_db.get_user_data(request.form.get('email'))

        print(user)

        if user and user_db.check_password(user['password'], request.form.get('password')):
            userlogin = UserLogin().create(user)
            login_user(userlogin)

            return redirect(url_for('index'))

    return render_template('login.html', form=form, **params)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    params = {
        'title': 'EchoEnsamble Register',
        'style_css': url_for('static', filename='css/style_register.css')
    }

    # + проверка в бд + созадть юзера

    if 'userAuth' in session:
        return redirect(url_for('account', username=session['userAuth']))

    elif request.method == 'POST' and ():
        session['userAuth'] = request.form['username']
        return redirect(url_for('account', username=session['userAuth']))

    return render_template('register.html', form=form, **params)


@app.route('/load_music', methods=['POST', 'GET'])
@login_required
def load_music():
    form = LoadFileForm()

    params = {
        'title': 'Загрузить Музыку',
        'script_js': url_for('static', filename='js/loadFile.js'),
        'loadfile_css': url_for('static', filename='css/style_loadfile.css'),
        'inputfile_css': url_for('static', filename='css/style_input_image.css')
    }

    # if 'userAuth' not in session:
    #     return redirect(url_for('login'))

    if request.method == 'POST':
        song_name = request.form['song_name']
        artist = request.form['artist']
        song_link = request.form['song_link']

        song_file = request.files['song_file']
        song_image = request.files['song_image']

        binary_image = form.song_image.raw_data

        pprint(form.data)

        pprint(binary_image)

        # print(song_name, artist, song_link, *form.song_image.raw_data)

        # with open('image.jpg', 'wb') as file:
        #     form.song_image.data.save(dst=file)
        # write_to_file(song_file, 'tmp.mp3')

        # return redirect(url_for('/'))

    return render_template('load_music.html', form=form, **params)


@app.route('/account/<username>')
@login_required
def account(username):
    if 'userAuth' not in session or session['userAuth'] != username:
        abort(401)

    return render_template('account.html', username=username)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Вы вышли из аккаунта', 'succec')
    return redirect(url_for('login'))


# Обработка не найденных страниц
@app.errorhandler(404)
def page_dont_find(error):
    return '<h1> This page is not allowed </h1>', 404


if __name__ == '__main__':
    main()
