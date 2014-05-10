import os
from datetime import datetime


def make_dir(dir_path):
    try:
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
    except Exception, e:
        raise e


def get_current_time():
    return datetime.now()
