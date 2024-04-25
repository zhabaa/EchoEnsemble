from flask import Flask, request, render_template, redirect, flash, session, url_for, abort

from static.data.loginForm import LoginForm
from static.data.registerForm import RegisterForm
from static.data.database import UserDB, MusicDB

from config import _USER_DATABASE_, _MUSIC_DATABASE_

import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
app.config['SECRET_KEY'] = "qwerty"


def main():
    user_db = UserDB('users', _USER_DATABASE_)
    music_db = MusicDB('music', _MUSIC_DATABASE_)

    app.run(host='127.0.0.1', port=8000, debug=True)


@app.route('/')
def index():
    return f"""<h1> Index page </h1>"""


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    # проверка в бд

    if 'userAuth' in session:
        return redirect(url_for('account', username=session['userAuth']))

    elif request.method == 'POST' and ():  # Проверка в бд
        session['userAuth'] = request.form['username']
        return redirect(url_for('account', username=session['userAuth']))

    return render_template('enter.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    params = {

    }

    # + проверка в бд + созадть юзера

    if 'userAuth' in session:
        return redirect(url_for('account', username=session['userAuth']))

    elif request.method == 'POST' and ():
        session['userAuth'] = request.form['username']
        return redirect(url_for('account', username=session['userAuth']))

    return render_template('register.html', form=form, **params)


@app.route('/account/<username>')
def account(username):
    if 'userAuth' not in session or session['userAuth'] != username:
        abort(401)

    return render_template('account.html', username=username)


# Обработка не найденных страниц
# @app.errorhandler(404)
# def page_dont_find():
#     return render_template('404page.html', ), 404


if __name__ == '__main__':
    main()
