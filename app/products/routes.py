from flask import Blueprint, redirect, render_template, request, url_for

from ..database import db
from .models import Category, Product


products_bp = Blueprint('products', __name__, template_folder='templates')


def get_products_by_category(category=None):
    if category:
        # Retrieve products for the specified category
        products = db.session.query(Product).join(
            Category).filter(Category.name == category).all()
    else:
        # Retrieve all products
        products = db.session.query(Product).all()
    return products


@products_bp.route('/products')
def show_products():
    # Retrieve all categories from the database
    categories = db.session.query(Category).all()

    # Initialize a dictionary to store products categorized by their respective categories
    products_by_category = {}

    # Loop through each category to gather its associated products
    for category in categories:
        # Query products associated with the current category
        products = get_products_by_category(category.name)
        # Store products in the dictionary with the category name as the key
        products_by_category[category.name] = [{'id': product.id,
                                                'title': product.title,
                                                'price': product.price,
                                                'img_path': product.img_path
                                                } for product in products]

    # Retrieve the active category from the request arguments
    active_category = request.args.get('category')

    if active_category:
        # Capitalize the active category for consistency
        active_category = active_category.capitalize()
        # Prepare data for the active category
        categories_data = [{'name': active_category,
                            'products': products_by_category.get(active_category, [])}]
    else:
        # Prepare data for all categories
        categories_data = [
            {'name': category.name,
             'products': products_by_category[category.name]} for category in categories]

    # Render the template with the necessary data
    return render_template('products/products.html',
                           categories=categories,
                           categories_data=categories_data,
                           active_category=active_category)


@products_bp.route('/products/<active_category>')
def show_products_by_category(active_category):
    # Retrieve all categories from the database
    categories = db.session.query(Category).all()

    # Retrieve products for the requested category
    products = get_products_by_category(active_category)

    # Prepare data for the requested category
    categories_data = [{'name': active_category,
                        'products': [{
                            'id': product.id,
                            'title': product.title,
                            'price': product.price,
                            'img_path': product.img_path
                        } for product in products]}]

    # Render the template with the necessary data
    return render_template('products/products.html',
                           categories=categories,
                           categories_data=categories_data,
                           active_category=active_category)


def capitalize_title(title):
    # Split the sentence into words
    words = title.split('-')

    # Capitalize each word
    capitalized_words = [word.capitalize() for word in words]

    # Join the capitalized words back into a sentence
    capitalized_title = ' '.join(capitalized_words)

    return capitalized_title


@products_bp.route('/products/<category>/<product_title>')
def show_product_details(category, product_title):
    # Convert title to same format as it is in db
    product_title = capitalize_title(product_title)

    print(category)

    print(product_title)

    # Retrieve product details by category and product name
    product = db.session.query(Product).join(Category).filter(
        Category.name == category, Product.title == product_title).first()

    if product:
        # Render the template with the product details
        return render_template('products/product.html', product=product)
    else:
        # If product not found, redirect to products page
        return redirect(url_for('products.show_products'))
