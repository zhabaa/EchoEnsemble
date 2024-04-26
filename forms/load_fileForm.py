from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired


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
    submit = SubmitField('Загрузить трек!')
