from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager, UserMixin

__all__ = ['db', 'login_manager', 'UserMixin']


db = SQLAlchemy()
login_manager = LoginManager()
