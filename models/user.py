from sqlalchemy import Column, String
from flask_login import UserMixin

from .base import BaseModel


class User(BaseModel, UserMixin):
    __tablename__ = 'User'

    name = Column(String(20), nullable=False, unique=True)
    password = Column(String(100), nullable=False)

    def get_id(self):
        return self.id
