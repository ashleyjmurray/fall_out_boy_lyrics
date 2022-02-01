from flask_wtf import FlaskForm
from wtforms import SubmitField


class CreateForm(FlaskForm):
    submit = SubmitField('Generate')
