from flask import render_template, url_for, redirect
from . import get_latest
from .forms import DeviceForm


@get_latest.route('/')
def index():
    return render_template('get_latest/index.html')


@get_latest.route('/choose_device', methods=['GET', 'POST'])
def choose_device():
    form = DeviceForm()
    if form.validate_on_submit():
        return redirect(url_for('.start_install', device_id=form.selector.data))

    return render_template('get_latest/device.html', form=form)


@get_latest.route('/start_install/<device_id>')
def start_install(device_id):
    return device_id
