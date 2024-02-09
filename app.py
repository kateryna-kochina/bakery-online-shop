from flask import Flask

from general.general import general_bp


def create_app():
    # Create Flask app
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(general_bp)

    return app


if __name__ == '__main__':
    # Run the app
    app = create_app()
    app.run()
