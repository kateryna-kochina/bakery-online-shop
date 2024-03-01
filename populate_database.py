import csv

from app.cart.models import Cart, CartItem
from app.database import db
from app.products.models import Category, Option, Product


def populate_database():
    try:
        with db.session.begin_nested():

            # Create all tables
            db.create_all()

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
                    category_id = int(row['category_id'])
                    product = Product(
                        title=row['title'],
                        price=int(row['price']),
                        img_path=row['img_path'],
                        description=row['description'],
                        category_id=category_id
                    )
                    db.session.add(product)

            # Read options and category_option from CSV file
            with open('data/options.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    option = Option(
                        name=row['name'],
                        coefficient=float(row['coefficient'])
                    )
                    db.session.add(option)

            # Read category_option from CSV file
            with open('data/category_option.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    category_id = int(row['category_id'])
                    option_id = int(row['option_id'])

                    # Retrieve category and option objects
                    category = Category.query.get(category_id)
                    option = Option.query.get(option_id)

                    # Ensure both category and option exist before associating them
                    if category and option:
                        category.options.append(option)

            # Commit the changes
            db.session.commit()
            print('Database populated successfully.')

    except Exception as e:
        db.session.rollback()
        print('Error populating database:', e)


if __name__ == '__main__':
    populate_database()
