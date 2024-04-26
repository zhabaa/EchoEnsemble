from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, EmailField
from wtforms.validators import DataRequired, InputRequired, EqualTo, Length


class RegisterForm(FlaskForm):
    username = StringField(
        label='Логин',
        validators=[
            DataRequired(message="Это поле обязательно к заполнению."),
            Length(min=4, max=18),
            InputRequired()
        ]
    )
    user_mail = EmailField(
        label='Электронная почта',
        validators=[DataRequired()]
    )
    password = PasswordField(
        label='Пароль',
        validators=[
            DataRequired(),
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
