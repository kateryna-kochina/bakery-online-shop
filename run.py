from app.app import *


if __name__ == '__main__':
    app = create_app()
    setup_database(app)
    app.run()
