from wtforms import validators, Field


def email_db_validator(form, field):
    if field.data == 'admin':
        print(f'field: {field.data}')
        raise validators.ValidationError(f'{form.data}, {field}')


def password_validator(form, field: Field):
    password = field.data

    if not (6 < len(password) < 45):
        raise validators.ValidationError(f'Password lenght must be 6 <> 45')

    # if not
