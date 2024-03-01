from flask import (Blueprint, jsonify, redirect, render_template, request,
                   url_for)
from flask_login import current_user, login_required

from ..database import db
from ..products.models import Option, Product
from .models import Cart

cart_bp = Blueprint('cart', __name__, template_folder='templates')


@cart_bp.route('/cart')
@login_required
def view_cart():

    # Retrieve the current user's cart
    user_cart = Cart.query.filter_by(user_id=current_user.id).first()

    if user_cart:
        # Query cart items with additional information
        cart_items = []
        for item in user_cart.items:
            product = Product.query.get(item.product_id)
            option = Option.query.get(item.option_id)
            price = product.price * option.coefficient * item.quantity

            cart_items.append({
                'product_title': product.title,
                'product_img': product.img_path,
                'option_name': option.name,
                'coefficient': option.coefficient,
                'quantity': item.quantity,
                'price': price
            })

        # Return the list of cart items as JSON
        return render_template('cart/cart.html', cart_items=cart_items)
    
    else:
        # If the user does not have a cart yet, return an empty list
        return jsonify([])

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
