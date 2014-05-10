from flask import Flask, render_template

from mario.models.user import User
from mario.libs.extension import db, login_manager


__all__ = ['create_app']

BLUEPRINTS = []


def create_app():
    app = Flask(__name__)

    configure_app(app)
    configure_blueprints(app, blueprints=BLUEPRINTS)
    configure_extensions(app)
    configure_error_handlers(app)

    return app


def configure_app(app):
    app.config.from_pyfile('config.py', silent=True)


def configure_blueprints(app, blueprints):
    for blueprint in blueprints:
        app.register_blueprint(blueprint)


def configure_extensions(app):
    # flask-sqlalchemy
    db.init_app(app)

    # flask-login
    # TODO
    login_manager.login_view = ''
    login_manager.refresh_view = ''
    @login_manager.user_loader
    def load_user(id_):
        return User.get(id_)
    login_manager.setup_app(app)


def configure_error_handlers(app):

    @app.errorhandler(403)
    def forbidden_page(error):
        return render_template("errors/403.html"), 403

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("errors/404.html"), 404

    @app.errorhandler(500)
    def server_error_page(error):
        return render_template("errors/500.html"), 500
