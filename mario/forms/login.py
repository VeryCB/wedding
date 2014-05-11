# coding: utf-8

from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, validators

from mario.models.user import User, UserPassword


class LoginForm(Form):

    email = TextField(u'邮箱', [
        validators.Required(u'不填邮箱可不能登录哦~'),
        validators.Email(u'Oops, 看起来你填的并不是合法的电子邮箱地址呢~'),
    ])
    password = PasswordField(u'密码', [
        validators.required(u'大概没有人会设一个空密码吧~'),
    ])

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.user = None

    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False

        email = self.email.data.encode('utf-8')
        password = self.password.data.encode('utf-8')

        user = User.query.filter_by(email=email).first()

        if not user:
            self.email.errors.append(u'这个邮箱还没有被注册哦~')
            return False

        if not UserPassword.validate(user.id, password):
            self.password.errors.append(u'密码没有输对呢~再试试看？')
            return False

        self.user = user
        return True
