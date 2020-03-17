from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column

db = SQLAlchemy()


class Observation(db.Model):
    id = Column(db.Integer, primary_key=True, autoincrement=True)

    sync_time = Column(db.DateTime, default=datetime.utcnow)

    tested = Column(db.Integer)
    positive = Column(db.Integer)
    negative = Column(db.Integer)

    def __init__(self, **kwargs):
        super(Observation, self).__init__(**kwargs)

    def __repr__(self):
        return f'<Observation {self.id},' \
               f' tested={self.tested},' \
               f' positive={self.positive},' \
               f' negative={self.negative}' \
               f' sync_time={self.sync_time}>'
