from flask.ext.script import Manager, Shell

from mario.app import create_app
from mario.libs.extension import db
from mario.models.user import User


app = create_app()
manager = Manager(app)


@manager.command
def run():
    app.run()


@manager.shell
def make_shell_context():
    return {'app': app, 'db': db, 'User': User}


@manager.command
def initdb():
    db.drop_all()
    db.create_all()

    User.add(name='verycb', phone='12345', email='imcaibin@gmail.com')


manager.add_option('-c', '--config',
                   dest='config',
                   required=False,
                   help='config file')


if __name__ == '__main__':
    manager.run()
