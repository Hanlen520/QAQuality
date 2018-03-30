from flask import render_template
from . import analysis


@analysis.route('/')
def index():
    return render_template('analysis/index.html')
