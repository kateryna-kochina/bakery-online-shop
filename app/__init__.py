from flask import Flask

from config import Config
from populate_database import populate_database

from .cart.routes import cart_bp
from .database import db
from .general.routes import general_bp
from .login_manager import login_manager
from .products.routes import products_bp
from .user.routes import user_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    if not app.config['SECRET_KEY']:
        raise RuntimeError('SECRET_KEY must be configured before starting the app.')

    # Set up a login manager to handle user authentication
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'
    login_manager.login_message_category = 'error'

    # Set up database
    db.init_app(app)
    setup_database(app)

    # Register blueprints
    app.register_blueprint(general_bp)
    app.register_blueprint(products_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(cart_bp)

    return app


def setup_database(app):
    from .products.models import Category, Option, Product

    with app.app_context():
        db.create_all()

        if Category.query.count() == 0:
            populate_database()
