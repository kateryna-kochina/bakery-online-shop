from flask import Flask

from general.general import general_bp


app = Flask(__name__)


app.register_blueprint(general_bp)


if __name__ == '__main__':
    app.run(debug=True)
