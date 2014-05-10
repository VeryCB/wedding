import os

from mario.utils import make_dir


HOST = '127.0.0.1'
PORT = 5000

DEBUG = False

SECRET_KEY = 'JIn398/3yX R~XHH!328jl]LW0X/,?2*(T'

make_dir('tmp')

INSTANCE_FOLDER_PATH = os.path.join('tmp', 'instance')
make_dir(INSTANCE_FOLDER_PATH)

LOG_FOLDER = os.path.join(INSTANCE_FOLDER_PATH, 'logs')
make_dir(LOG_FOLDER)

UPLOAD_FOLDER = os.path.join(INSTANCE_FOLDER_PATH, 'uploads')
make_dir(UPLOAD_FOLDER)

MAX_CONTENT_LENGTH = 16 * 1024 * 1024

PROJECT_URL = 'http://%s' % ':'.join([HOST, str(PORT)])

SQLALCHEMY_DATABASE_URI = 'mysql://username:password@server/db'


try:
    from mario.local_config import *
except ImportError:
    pass
