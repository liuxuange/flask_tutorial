from datetime import datetime

from sqlalchemy import Column, Integer, DateTime, inspect

from ext import db


class BaseModel(db.Model):
    # must define
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.now)

    def to_dict(self):
        """ Convert Model to Dict Object """
        return {
            c.key: getattr(self, c.key, None)
            for c in inspect(self).mapper.column_attrs
        }
