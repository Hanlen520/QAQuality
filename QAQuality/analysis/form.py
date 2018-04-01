from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class AppNameForm(FlaskForm):
    app_name = StringField('', validators=[DataRequired()], render_kw={
                    "placeholder": 'What\'s your app name?',
                    "value": ''
                })
    submit = SubmitField('Commit')
