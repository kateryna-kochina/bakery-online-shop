import csv

from app.database import db
from app.products.models import Category, Choice, Product


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
                    category_id = int(row['category_id'])
                    product = Product(
                        title=row['title'],
                        price=int(row['price']),
                        img_path=row['img_path'],
                        description=row['description'],
                        category_id=category_id
                    )
                    db.session.add(product)

            # Read choices and category_choice from CSV file
            with open('data/choices.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    choice = Choice(
                        name=row['name'],
                        coefficient=float(row['coefficient'])
                    )
                    db.session.add(choice)

            # Read category_choice from CSV file
            with open('data/category_choice.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    category_id = int(row['category_id'])
                    choice_id = int(row['choice_id'])

                    # Retrieve category and choice objects
                    category = Category.query.get(category_id)
                    choice = Choice.query.get(choice_id)

                    # Ensure both category and choice exist before associating them
                    if category and choice:
                        category.choices.append(choice)

            # Commit the changes
            db.session.commit()
            print('Database populated successfully.')

    except Exception as e:
        db.session.rollback()
        print('Error populating database:', e)


if __name__ == '__main__':
    populate_database()
