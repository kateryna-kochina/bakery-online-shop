from flask import Blueprint, redirect, render_template, request, url_for

from ..database import db


cart_bp = Blueprint('cart', __name__, template_folder='templates')


@cart_bp.route('/cart')
def view_cart():
    return render_template('cart/cart.html')

# @cart_bp.route('/add_to_cart')
# def add_to_cart():
#     pass

# @cart_bp.route('/quick_add')
# def quick_add():
#     pass

# @cart_bp.route('/remove_from_cart')
# def remove_from_cart():
#     pass

# @cart_bp.route('/view_cart')
# def view_cart():
#     pass



# @app.route('/quick-add/<id>')
# def quick_add(id):
#     if 'cart' not in session:
#         session['cart'] = []

#     session['cart'].append({'id': id, 'quantity': 1})
#     session.modified = True

#     return redirect(url_for('index'))