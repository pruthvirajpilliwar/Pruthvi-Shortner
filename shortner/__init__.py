from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    app.config["SECRET_KEY"] = "010baac4fabe349b7b5afa3e5ee31201495e9b5de231e22cc8066866b53fe175"

    db.init_app(app)
    from . import home, auth, links
    app.register_blueprint(home.bp)
    app.register_blueprint(auth.bp)
    app.register_blueprint(links.bp)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Please log in to access this page.'
    login_manager.login_message_category = 'warning'
    login_manager.init_app(app)

    from .models import User, Link
    with app.app_context():
        db.create_all()

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    return app
