from flask import Blueprint, current_app as app
from flask_login import login_required, current_user

from models.user import User

from . import create_response_body


bp = Blueprint('users', __name__, url_prefix='/api/users')


@bp.route('')
@login_required
def list_users():
    users = []
    for user in User.query:
        # convert to dict
        u = user.to_dict()
        # hide the password field
        u.pop(User.password.key)
        users.append(u)
    return create_response_body(users)
