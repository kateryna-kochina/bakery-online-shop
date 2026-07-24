import os

from dotenv import load_dotenv


load_dotenv()


class Config:

    # Flask configuration
    FLASK_APP = os.getenv('FLASK_APP')
    FLASK_ENV = os.getenv('FLASK_ENV')
    FLASK_DEBUG = os.getenv('FLASK_DEBUG')
    FLASK_RUN_HOST = os.getenv('FLASK_RUN_HOST')
    FLASK_RUN_PORT = os.getenv('FLASK_RUN_PORT')
    SECRET_KEY = os.getenv('SECRET_KEY') or os.getenv('FLASK_SECRET_KEY')

    # Database configuration
    SQLALCHEMY_DATABASE_URI = 'sqlite:///bakery.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
