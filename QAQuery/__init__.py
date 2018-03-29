from flask import Flask


def create_app():
    app = Flask(__name__)

    from .analysis import analysis as analysis_blueprint
    from .auth import auth as auth_blueprint
    from .main import main as main_blueprint
    from .tester import tester as tester_blueprint

    app.register_blueprint(analysis_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)
    app.register_blueprint(tester_blueprint)

    return app
