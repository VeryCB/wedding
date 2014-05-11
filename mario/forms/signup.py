# coding: utf-8

from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, validators


class EmailSignupForm(Form):

    email = TextField(u'邮箱', [
        validators.Required(u'不填邮箱可不能注册哦~'),
        validators.Email(u'Oops, 看起来你填的并不是合法的电子邮箱地址呢~'),
    ])
    name = TextField(u'用户名', [
        validators.Required(u'不妨起一个有个性的名字吧！'),
    ])
    password = PasswordField(u'密码', [
        validators.required(u'没有密码的话，别人也可以登录你的账户哦~'),
    ])
