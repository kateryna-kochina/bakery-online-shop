from flask import Blueprint, render_template


products_bp = Blueprint('products', __name__, template_folder='templates')


@products_bp.route('/products')
def show_products():
    return render_template('products/products.html')


# @products_bp.route('/products/product')
# def product():
#     return render_template('products/products.html')
