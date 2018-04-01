from flask import render_template
from . import analysis
from .form import AppNameForm


@analysis.route('/', methods=['GET', 'POST'])
def index():
    form = AppNameForm()
    if form.validate_on_submit():
        app_name = form.app_name.data
        return 'hi {}'.format(app_name)
    return render_template('analysis/index.html', form=form)
