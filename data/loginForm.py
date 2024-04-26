from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, InputRequired, Length

from .validators import email_db_validator


class LoginForm(FlaskForm):
    email = EmailField(
        label='email',
        validators=[
            DataRequired(),
            email_db_validator
        ]
    )

    password = PasswordField(
        label='password',
        validators=[
            InputRequired(),

        ]
    )

    submit = SubmitField('Войти')
