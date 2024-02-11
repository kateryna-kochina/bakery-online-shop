from flask import Flask

from config import Config

from .database import db, setup_database
from .general.general import general_bp
from .products.products import products_bp


def create_app():
    app = Flask(__name__)

    try:
        app.config.from_object(Config)

        # Set up database
        app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
        db.init_app(app)
        setup_database(app)
        print('Database initialized successfully.')

        # Register blueprints
        app.register_blueprint(general_bp)
        app.register_blueprint(products_bp)
        print('Blueprints registered successfully.')

        return app

    except Exception as e:

        print(f'Error occurred during app initialization: {e}')

        return None
