from flask.ext.script import Manager

from mario.config import HOST, PORT
from mario.app import create_app
from mario.libs.extension import db
from mario.models.user import User


app = create_app()
manager = Manager(app)


@manager.command
def run():
    app.run(host=HOST, port=PORT)


@manager.shell
def make_shell_context():
    return {'app': app, 'db': db, 'User': User}


@manager.command
def init_db():
    db.drop_all()
    db.create_all()


@manager.command
def init_data():
    user = User.add(name='verycb', phone='12345', email='imcaibin@gmail.com')
    password = 'test'
    user.password = password
    print 'User %s is added, password is "%s"' % (User, password)


if __name__ == '__main__':
    manager.run()
