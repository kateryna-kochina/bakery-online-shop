from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user

from ..cart.models import Cart
from ..database import db
from .forms import AddToCart
from .models import Category, Option, Product


products_bp = Blueprint('products', __name__, template_folder='templates')


def add_to_cart(form, product):
    quantity = form.quantity.data
    selected_option_id = form.selected_option.data

    print(f'Quantity is: {quantity}')
    print(f'Selected_option id is: {selected_option_id}')

    # If selected_option is empty
    if not selected_option_id:
        # Query for a option where category_id = category_id of currently displayed product and option coefficient = 1.0
        default_option = db.session.query(Option).join(Category, Option.categories).filter(
            Category.id == product.category_id, Option.coefficient == 1.0).first()

        if default_option:
            # Assign the id of default option with coefficient = 1.0
            selected_option_id = default_option.id
            print(
                f'Option is not seleted, default_option id is: {selected_option_id}')

    # Check if the current user has a cart
    cart = Cart.query.filter_by(user_id=current_user.id).first()

    # If the user doesn't have a cart, create one
    if not cart:
        cart = Cart(user_id=current_user.id)
        db.session.add(cart)
        db.session.commit()

    # Add the selected product to the cart db table
    cart.add_to_cart(
        product_id=product.id,
        option_id=int(selected_option_id),
        quantity=quantity)

    print(
        f'{product.title} [id: {product.id}] added to cart with option [id: {selected_option_id}] in amount of {quantity}. ')

    return redirect(url_for('cart.view_cart'))


def get_options(category_id):
    category = db.session.query(Category).filter(
        Category.id == category_id).first()
    return category.options if category else []


def get_products_by_category(category=None):
    if category:
        # Retrieve products for the specified category
        products = db.session.query(Product).join(
            Category).filter(Category.name == category).all()
    else:
        # Retrieve all products
        products = db.session.query(Product).all()
    return products


def get_product_details(category, product_title):
    product_title = title_formatter(product_title)
    return db.session.query(Product).join(Category).filter(
        Category.name == category, Product.title == product_title).first()


def title_formatter(title):
    # Split the title into words
    words = title.split('-')

    # Capitalize each word
    capitalized_words = [word.capitalize() for word in words]

    # Join the capitalized words back into a sentence
    capitalized_title = ' '.join(capitalized_words)

    return capitalized_title


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
        products_by_category[category.name] = [{'title': product.title,
                                                'price': product.price,
                                                'img_path': product.img_path
                                                } for product in products]

    # Retrieve the active category from the request arguments
    active_category = request.args.get('category')

    if active_category:
        # Capitalize the active category for consistency
        active_category = active_category.capitalize()
        # Prepare data for the active category
        categories_data = [{
            'name': active_category,
            'products': products_by_category.get(active_category, [])
        }]
    else:
        # Prepare data for all categories
        categories_data = [{
            'name': category.name,
            'products': products_by_category[category.name]
        } for category in categories]

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
                            'title': product.title,
                            'price': product.price,
                            'img_path': product.img_path
                        } for product in products]}]

    # Render the template with the necessary data
    return render_template('products/products.html',
                           categories=categories,
                           categories_data=categories_data,
                           active_category=active_category)


@products_bp.route('/products/<active_category>/<product_title>', methods=['GET', 'POST'])
def show_product_details(active_category, product_title):
    form = AddToCart()

    # Retrieve product details by category and product name
    product = get_product_details(active_category, product_title)

    if product:

        # Get categories from db to display them for navigation
        categories = db.session.query(Category).all()

        # Retrieve available options by category
        options = get_options(product.category_id)

        if form.validate_on_submit():
            if current_user.is_authenticated:  # Check if user is logged in
                return add_to_cart(form, product)
            else:
                flash('Please log in to add items to your cart.', 'error')
                # Redirect to login page if not logged in
                return redirect(url_for('user.login'))
        else:
            return render_template('products/product.html',
                                   product=product,
                                   categories=categories,
                                   active_category=active_category,
                                   options=options,
                                   form=form)

    else:
        # If product not found, redirect to products page
        # TODO: notify user the selected product cannot be found
        return redirect(url_for('products.show_products'))


# @products_bp.route('/products/add', methods=['GET', 'POST'])
# def add_product():
#     pass


# @products_bp.route('/products/delete', methods=['GET', 'POST'])
# def delete_product():
#     pass


# @products_bp.route('/products/edit', methods=['GET', 'POST'])
# def edit_product():
#     pass
