from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import Config
from app.general.general import general_bp


def create_app():
    # Create Flask app
    app = Flask(__name__)

    # Set up database
    app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
    db = SQLAlchemy(app)

    # Register blueprints
    app.register_blueprint(general_bp)

    return app
