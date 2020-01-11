# views/index.py

from flask import Blueprint, jsonify


bp = Blueprint('index', __name__)


@bp.route('/')
def index():
    return jsonify({'ok': True, 'message': 'Welcome.'})
