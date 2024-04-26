from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import PasswordField, SubmitField, EmailField, BooleanField, StringField
from wtforms.validators import DataRequired, InputRequired, Length, EqualTo, Email


# from .validators import email_db_validator


class LoginForm(FlaskForm):
    email = EmailField(
        label='email',
        validators=[
            DataRequired(),
            Email()
        ]
    )
    password = PasswordField(
        label='password',
        validators=[
            InputRequired(),
        ]
    )
    submit = SubmitField('Войти')


class RegisterForm(FlaskForm):
    username = StringField(
        label='Логин',
        validators=[DataRequired()]
    )
    user_mail = EmailField(
        label='Электронная почта',
        validators=[DataRequired()]
    )
    password = PasswordField(
        'Пароль',
        [
            InputRequired(),
            EqualTo('confirm_password', message='Пароли должны совпадать'),
            Length(min=6, max=35)
        ]
    )
    confirm_password = PasswordField(
        label='Повторите пароль'
    )
    creator = BooleanField(
        label='Я музыкант',
        validators=[DataRequired()]
    )
    submit = SubmitField('Зарегестрироваться')


class LoadFileForm(FlaskForm):
    song_name = StringField(
        label='song_name',
        validators=[DataRequired()]
    )
    artist = StringField(
        label='artist',
        validators=[DataRequired()]
    )
    song_file = FileField(
        label='song_file',
        validators=[FileRequired()]
    )
    song_link = StringField(
        label='song_link',
        validators=[DataRequired()]
    )
    song_image = FileField(
        label='song_image',
        validators=[FileRequired()]
    )
    submit = SubmitField('Загрузить говно!')
