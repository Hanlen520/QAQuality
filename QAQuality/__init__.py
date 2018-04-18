from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_bootstrap import Bootstrap


def create_app():
    app = Flask(__name__)

    bootstrap = Bootstrap()
    bootstrap.init_app(app)

    app.config['SECRET_KEY'] = 'testonly'
    csrf_protect = CSRFProtect()
    csrf_protect.init_app(app)

    from .analysis import analysis as analysis_blueprint
    from .main import main as main_blueprint
    from .get_latest import get_latest as get_latest_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(analysis_blueprint, url_prefix='/analysis')
    app.register_blueprint(get_latest_blueprint, url_prefix='/get_latest')

    return app
