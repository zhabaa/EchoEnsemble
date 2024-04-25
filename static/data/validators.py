# from wtforms import Form, StringField, validators, EmailField
# from __database import UserDB

from flask_wtf import FlaskForm
from wtforms import StringField, validators


def email_db_validator(form, field):
    if field.data == 'admin':
        print(f'field: {field.data}')
        raise validators.ValidationError(f'{form.data}, {field}')



# class MyForm(FlaskForm):
#     my_field = StringField('My Field', validators=[validators.InputRequired(), email_db_validator])
