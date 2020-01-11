from flask import Blueprint, current_app as app, jsonify
from flask_login import current_user, login_user, logout_user

from models.user import User


bp = Blueprint('sign', __name__, url_prefix='/api/sign')


@bp.route('/in')
def login():
    if current_user.get_id():
        return jsonify({'statusCode': 0, 'message': 'Already login.'})

    user = User.query.get(1)
    login_user(user)

    u = user.to_dict()
    u.pop(User.password.key)
    return jsonify({'statusCode': 0, 'user': u})


@bp.route('/out')
def logout():
    logout_user()
    return jsonify({'statusCode': 0, 'message': 'Logout successd.'})
