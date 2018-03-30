from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class AppNameForm(FlaskForm):
    app_name = StringField('App name', validators=[DataRequired()])
    submit = SubmitField('Commit')
