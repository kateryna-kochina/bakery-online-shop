from flask import Blueprint, render_template
from .models import Product

from ..database import db


products_bp = Blueprint('products', __name__, template_folder='templates')


# @products_bp.route('/products')
# def show_products():
#     return render_template('products/products.html')


# @products_bp.route('/products/product')
# def product():
#     return render_template('products/products.html')


@products_bp.route('/products')
def show_products():
    result = db.session.execute(db.select(Product))
    all_products = result.scalars()
    
    return render_template('products/products.html', products=all_products)
