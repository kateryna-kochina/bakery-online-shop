from flask import request
from flask import Blueprint, render_template, request

from ..database import db
from .models import Category, Product

products_bp = Blueprint('products', __name__, template_folder='templates')


@products_bp.route('/products')
def show_products():
    # Retrieve all categories from the database
    categories = db.session.query(Category).all()
    # Initialize a dictionary to store products categorized by their respective categories
    products_by_category = {}

    # Loop through each category to gather its associated products
    for category in categories:
        # Query products associated with the current category
        products = db.session.query(Product).filter(
            Product.category_id == category.id).all()
        # Store products in the dictionary with the category name as the key
        products_by_category[category.name] = [
            {'title': product.title,
             'price': product.price,
             'img_path': product.img_path
             } for product in products]

    # Retrieve the active category from the request arguments
    active_category = request.args.get('category')

    # Check if the active category is present
    if active_category:
        # Convert the active category to lowercase for consistency
        active_category = active_category.capitalize()

        # Prepare data for all categories including the products for the active category
        categories_data = [{
            'name': active_category,
            'products': products_by_category.get(active_category, [])
        }]
    else:
        # If no active category is selected, return all products for all categories
        categories_data = [{
            'name': category.name,
            'products': products_by_category[category.name]
        } for category in categories]

    # Render the template with the necessary data
    return render_template('products/products.html', categories=categories, categories_data=categories_data, active_category=active_category)
