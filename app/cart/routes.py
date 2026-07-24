from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from sqlalchemy.exc import SQLAlchemyError

from ..database import db
from ..pricing import calculate_unit_price
from ..products.models import Option, Product
from .forms import UpdateQuantity, RemoveCartItem
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
        remove_item_forms = []

        for item in user_cart.items:
            print(item.id)

            form = UpdateQuantity(prefix=str(item.id))
            form.cart_item_id.data = item.id
            forms.append(form)

            remove_item_form = RemoveCartItem(prefix=str(item.id))
            remove_item_form.cart_item_id.data = item.id
            remove_item_forms.append(remove_item_form)

            product = Product.query.get(item.product_id)
            option = Option.query.get(item.option_id)
            unit_price = calculate_unit_price(product, option)
            cart_items.append({
                'product_title': product.title,
                'product_img': product.img_path,
                'option_name': option.name,
                'coefficient': option.coefficient,
                'quantity': item.quantity,
                'price': '{:.2f}'.format(unit_price),
                'sum': '{:.2f}'.format(unit_price * item.quantity),
                'cart_item_id': item.id
            })

        if request.method == 'POST':
            quantity_updated = False

            # Check if any quantity update form was submitted
            for form in forms:
                if form.validate_on_submit():
                    item_id = form.cart_item_id.data
                    new_quantity = form.quantity.data
                    if user_cart.update_quantity(item_id, new_quantity):
                        try:
                            db.session.commit()
                            quantity_updated = True
                            flash('Quantity updated successfully!', 'success')
                        except SQLAlchemyError:
                            db.session.rollback()
                            flash('Unable to update the item quantity.', 'error')

            # Process removal forms only if no quantity update form was submitted
            if not quantity_updated:
                for remove_item_form in remove_item_forms:
                    if remove_item_form.validate_on_submit():
                        item_id = remove_item_form.cart_item_id.data
                        item_removed = user_cart.remove_from_cart(item_id)

                        if item_removed:
                            try:
                                db.session.commit()
                                flash('Item deleted successfully!', 'success')
                            except SQLAlchemyError:
                                db.session.rollback()
                                flash('Unable to remove the item.', 'error')
                        else:
                            flash('Item could not be found in your cart.', 'error')

            return redirect(url_for('cart.view_cart'))

        return render_template('cart/cart.html',
                               forms=forms,
                               remove_item_forms=remove_item_forms,
                               cart_items=cart_items)

    # If user's cart is empty, return an empty cart
    return render_template('cart/empty_cart.html')
