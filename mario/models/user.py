from mario.libs.extension import db, UserMixin
from mario.models.base import EntityModel


class User(db.Model, UserMixin, EntityModel):

    key_fields = ['id', 'name', 'display_name']

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20, collation='utf8_bin'),
                     nullable=False, unique=True)
    display_name = db.Column(db.String(20, collation='utf8_bin'))
    count = db.Column(db.Integer)

    __table_args__ = {'mysql_engine': 'InnoDB'}

    @classmethod
    def get(cls, user_id):
        return cls.query.get(user_id)

    @classmethod
    def add(cls, **kwargs):
        instance = cls(**kwargs)
        db.session.add(instance)
        db.session.commit()
        return instance
