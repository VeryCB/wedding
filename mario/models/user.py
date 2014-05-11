import hashlib

from enum import Enum

from mario.libs.extension import db, UserMixin
from mario.utils import get_current_time
from mario.models.base import EntityModel
from mario.models.consts import RESERVED_USER_NAMES


class Role(Enum):

    normal = 1
    admin = 2


class Status(Enum):

    normal = 1
    nonactivated = 2
    banned = 3


class User(db.Model, UserMixin, EntityModel):

    key_fields = ['id', 'name', 'phone']

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    uid = db.Column(db.String(20), unique=True)
    phone = db.Column(db.Integer, unique=True)
    email = db.Column(db.String(100), unique=True)
    role = db.Column(db.Integer, nullable=False, default=Role.normal.value)
    status = db.Column(db.Integer, nullable=False, default=Status.nonactivated.value)
    create_time = db.Column(
            db.DateTime, default=get_current_time, nullable=False)
    update_time = db.Column(
            db.DateTime, default=get_current_time, nullable=False)

    __table_args__ = {'mysql_engine': 'InnoDB'}

    @property
    def password(self):
        return UserPassword.get_latest_password(self.id)

    @password.setter
    def password(self, password):
        UserPassword.add(self.id, password)

    @classmethod
    def get(cls, user_id):
        return cls.query.get(user_id)

    @classmethod
    def _check_fields(self, **kwargs):
        name = kwargs.get('name')
        uid = kwargs.get('uid')

        if uid and not uid[0].isalpha():
            raise ValueError('uid:%s should start with alphabet' % uid)

        if name and name.lower() in RESERVED_USER_NAMES:
            raise ValueError('name:%s is reserved' % name)

    def update(self, **kwargs):
        self._check_fields(**kwargs)

        self.query.filter_by(id=self.id).update(kwargs)
        db.session.commit()

    @classmethod
    def add(cls, **kwargs):
        cls._check_fields(**kwargs)

        instance = cls(**kwargs)
        db.session.add(instance)
        db.session.commit()
        return instance

    def is_active(self):
        return self.status == Status.normal.value


class UserPassword(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False, index=True)
    password = db.Column(db.String(80), nullable=False)
    create_time = db.Column(
            db.DateTime, default=get_current_time, nullable=False)

    __table_args__ = {'mysql_engine': 'InnoDB'}

    @classmethod
    def add(cls, user_id, password):
        password = cls.encrypt(password)
        item = cls(user_id=user_id, password=password)
        db.session.add(item)
        db.session.commit()

    @classmethod
    def get_latest_password(cls, user_id):
        query = cls.query.filter_by(user_id=user_id).order_by(cls.id.desc())
        instance = query.first()

        if instance:
            return instance.password

    @classmethod
    def encrypt(cls, password):
        return hashlib.md5(password).hexdigest()

    @classmethod
    def validate(cls, user_id, password):
        user_password = cls.get_latest_password(user_id)
        return user_password == cls.encrypt(password)
