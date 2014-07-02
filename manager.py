# coding:utf-8

from flask.ext.script import Manager

from mario.config import HOST, PORT, DEBUG
from mario.app import create_app
from mario.libs.extension import db
from mario.models.user import User


app = create_app()
manager = Manager(app)


@manager.command
def run():
    app.run(host=HOST, port=PORT, debug=DEBUG)


@manager.shell
def make_shell_context():
    return {'app': app, 'db': db, 'User': User}


@manager.command
def init_db():
    db.drop_all()
    db.create_all()


@manager.command
def init_data():
    user = User.add(name=u'喜碧', display_name='CB')
    print 'User {0} is added'.format(user)


if __name__ == '__main__':
    manager.run()
