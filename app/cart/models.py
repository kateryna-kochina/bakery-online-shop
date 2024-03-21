from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from ..database import db


class Cart(db.Model):
    __tablename__ = 'carts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    items = relationship('CartItem', backref='cart',
                         cascade='all, delete-orphan', lazy=True)

    def add_to_cart(self, product_id, option_id, quantity):
        item = CartItem(cart_id=self.id, product_id=product_id,
                        option_id=option_id, quantity=quantity)
        db.session.add(item)
        db.session.commit()

    def remove_from_cart(self, item_id):
        item = CartItem.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()

    def update_quantity(self, item_id, new_quantity):
        item = CartItem.query.filter_by(cart_id=self.id, id=item_id).first()
        if item:
            item.quantity = new_quantity
            db.session.commit()


class CartItem(db.Model):
    __tablename__ = 'cart_items'

    id = Column(Integer, primary_key=True, autoincrement=True)
    cart_id = Column(Integer, ForeignKey('carts.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    option_id = Column(Integer, ForeignKey('options.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
