from flask import Flask

from config import Config
from populate_database import populate_database

from .database import db
from .general.routes import general_bp
from .products.routes import products_bp


def create_app():
    app = Flask(__name__)

    try:
        app.config.from_object(Config)

        # Set secret key
        app.secret_key = app.config['FLASK_SECRET_KEY']

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


def setup_database(app):
    from .products.models import Category, Product

    with app.app_context():
        try:
            db.create_all()
            print('Database tables created successfully.')

            if Category.query.count() == 0:
                populate_database()
                db.session.commit()
                print('Database populated with data.')
            else:
                print('Database already populated.')

        except Exception as e:
            db.session.rollback()
            print('Error setting up database:', e)
