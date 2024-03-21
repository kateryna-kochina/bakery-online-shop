from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from ..database import db
from ..products.models import Option, Product
from .forms import UpdateQuantity
from .models import Cart, CartItem


cart_bp = Blueprint('cart', __name__, template_folder='templates')


@cart_bp.route('/cart', methods=['GET', 'POST'])
@login_required
def view_cart():
    # Retrieve the current user's cart
    user_cart = Cart.query.filter_by(user_id=current_user.id).first()

    if user_cart:
        cart_items = []
        forms = []

        for item in user_cart.items:
            print(item.id)

            form = UpdateQuantity(prefix=str(item.id))
            form.cart_item_id.data = item.id
            forms.append(form)

            product = Product.query.get(item.product_id)
            option = Option.query.get(item.option_id)
            cart_items.append({
                'product_title': product.title,
                'product_img': product.img_path,
                'option_name': option.name,
                'coefficient': option.coefficient,
                'quantity': item.quantity,
                'price': '{:.2f}'.format(product.price * option.coefficient),
                'sum': '{:.2f}'.format(product.price * option.coefficient * item.quantity),
                'cart_item_id': item.id
            })

        if request.method == 'POST':
            for form in forms:
                if form.validate_on_submit():
                    item_id = form.cart_item_id.data
                    new_quantity = form.quantity.data
                    
                    # # Update the quantity of the cart item
                    user_cart.update_quantity(item_id, new_quantity)

                    flash('Quantity updated successfully!', 'success')
                    
                    # if 'update_btn' in request.form:
                    #     new_quantity = form.quantity.data
                    #     user_cart.update_quantity(item_id, new_quantity)

                    #     flash('Quantity updated successfully!', 'success')

                    # elif 'remove_btn' in request.form:
                    #     user_cart.remove_from_cart(item_id)

                    #     flash('Item deleted successfully!', 'success')

                    return redirect(url_for('cart.view_cart'))

        return render_template('cart/cart.html',
                               forms=forms,
                               cart_items=cart_items)

    # If user's cart is empty, return an empty cart
    return render_template('cart/empty_cart.html')
