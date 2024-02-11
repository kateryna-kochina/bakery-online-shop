from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def setup_database(app):
    
    from .models import Category, Product
    
    with app.app_context():
        try:
            db.create_all()
            db.session.commit()
            print('Database tables created successfully.')

        except Exception as e:
            db.session.rollback()
            print('Error creating database tables:', e)
