import os

# APP
DEBUG = True
SECRET_KEY = os.urandom(24)
# SQLAlchemy
SQLALCHEMY_DATABASE_URI = 'sqlite:///tutorial.db'
