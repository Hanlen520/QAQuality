from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField
from wtforms.validators import DataRequired
import os


device_list = [each.strip().split('\t') for each in os.popen('adb devices').readlines()[1:-1]]
device_list = ('{} ({})'.format(each[0], each[1]) for each in device_list)

widget_dict = dict()
widget_dict['selector'] = SelectField('Device ID', choices=[(i, i) for i in device_list], validators=[DataRequired()])
widget_dict['commit'] = SubmitField('Next')
DeviceForm = type('DeviceForm', (FlaskForm,), widget_dict)