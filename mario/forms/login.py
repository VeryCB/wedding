# coding: utf-8

from flask.ext.wtf import Form
from wtforms import TextField, validators

from mario.models.user import User


class LoginForm(Form):

    name = TextField(u'姓名', [
        validators.Required(u'不告诉我你叫什么可不能随便看~'),
    ])

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.user = None

    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False

        name = self.name.data

        user = User.query.filter_by(name=name).first()

        if not user:
            self.name.errors.append(u'暂时还没有您的请帖呢~')
            return False

        self.user = user
        return True
