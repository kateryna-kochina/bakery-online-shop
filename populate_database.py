import csv

from app.database import db
from app.products.models import Category, Product


def populate_database():
    try:
        with db.session.begin_nested():

            # Read categories from CSV file
            with open('data/categories.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    category = Category(name=row['name'])
                    db.session.add(category)

            # Read products from CSV file
            with open('data/products.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    product = Product(
                        title=row['title'],
                        price=int(row['price']),
                        img_path=row['img_path'],
                        description=row['description'],
                        category_id=int(row['category_id'],
                        )
                    )
                    db.session.add(product)

            # Commit the changes
            db.session.commit()
            print('Database populated successfully.')

    except Exception as e:
        db.session.rollback()
        print('Error populating database:', e)
