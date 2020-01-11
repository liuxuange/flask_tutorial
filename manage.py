from pathlib import Path
import hashlib

import click
import flask_migrate

from app import app, db
from models.user import User


def init_db():
    user = User(name='admin',
                password=hashlib.sha1(b'userpassword').hexdigest())
    db.session.add(user)
    db.session.commit()


@click.group()
def cli():
    pass


@cli.command()
def init():
    with app.app_context():
        path = Path() / 'migrations'
        if path.exists():
            return

        path.mkdir()
        flask_migrate.init()
        flask_migrate.migrate()
        flask_migrate.upgrade()
        init_db()
    print('Init finished.')


@cli.command()
def upgrade():
    with app.app_context():
        path = Path() / 'migrations'
        if not path.exists():
            return

        flask_migrate.migrate()
        flask_migrate.upgrade()
    print('Init finished.')


if __name__ == '__main__':
    cli()
