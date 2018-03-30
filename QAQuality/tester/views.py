from flask import render_template
from . import tester


@tester.route('/')
def index():
    return render_template('tester/index.html')
