from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from ..database import db


class Cart(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    items = relationship('CartItem', backref='cart',
                         cascade='all, delete-orphan', lazy=True)

    def add_to_cart(self, product, selected_choice, quantity):
        # Logic to add the specified product to the cart
        item = CartItem(product_id=product.id, choice_id=selected_choice.id, quantity=quantity)
        self.items.append(item)
        db.session.commit()

    def remove_from_cart(self, item_id):
        # Logic to remove a product from the cart
        item = CartItem.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()

    def update_quantity(self, quantity):
        # Logic to update the quantity of a product in the cart
        pass


class CartItem(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    cart_id = Column(Integer, ForeignKey('cart.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('product.id'), nullable=False)
    choice_id = Column(Integer, ForeignKey('choice.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
