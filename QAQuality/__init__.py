from flask import Flask
from flask_wtf.csrf import CSRFProtect


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'testonly'
    csrf_protect = CSRFProtect()
    csrf_protect.init_app(app)

    from .analysis import analysis as analysis_blueprint
    from .auth import auth as auth_blueprint
    from .main import main as main_blueprint
    from .tester import tester as tester_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(analysis_blueprint, url_prefix='/analysis')
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(tester_blueprint, url_prefix='/tester')

    return app
