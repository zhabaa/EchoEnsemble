from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, EmailField
from wtforms.validators import DataRequired, InputRequired, EqualTo, Length


class RegisterForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    user_mail = EmailField('Электронная почта', validators=[DataRequired()])
    password = PasswordField(
        'Пароль',
        [
            InputRequired(),
            EqualTo('confirm_password', message='Пароли должны совпадать'),
            Length(min=6, max=35)
        ]
    )
    confirm_password = PasswordField('Повторите пароль')
    creator = BooleanField('Я музыкант', validators=[DataRequired()])
    submit = SubmitField('Зарегестрироваться')
