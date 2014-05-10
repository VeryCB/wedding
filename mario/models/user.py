import hashlib

from enum import Enum

from mario.libs.extension import db, UserMixin
from mario.utils import get_current_time
from .base import EntityModel


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
    phone = db.Column(db.Integer, nullable=False, unique=True)
    email = db.Column(db.String(100), unique=True)
    role = db.Column(db.Integer, nullable=False, default=Role.normal)
    status = db.Column(db.Integer, nullable=False, default=Status.nonactivated)
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
    def get_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def get_by_phone(cls, phone):
        return cls.query.filter_by(phone=phone).first()

    def update(self, **kwargs):
        self.query.filter_by(id=self.id).update(kwargs)
        db.session.commit()

    @classmethod
    def add(cls, **kwargs):
        instance = cls(**kwargs)
        db.session.add(instance)
        db.session.commit()
        return instance


class UserPassword(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
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
        return query.first()

    @classmethod
    def encrypt(cls, password):
        return hashlib.md5(password).hexdigest()

    @classmethod
    def validate(cls, user_id, password):
        user_password = cls.get_latest_password(user_id)
        return user_password == cls.encrypt(password)
