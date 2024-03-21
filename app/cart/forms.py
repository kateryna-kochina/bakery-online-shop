from flask_wtf import FlaskForm
from wtforms import HiddenField, IntegerField, SubmitField
from wtforms.validators import DataRequired, InputRequired, NumberRange


class UpdateQuantity(FlaskForm):
    cart_item_id = HiddenField(
        'Cart Item ID', id='cart_item', name='cart_item', validators=[DataRequired()])
    quantity = IntegerField(
        'Quantity', validators=[DataRequired(), NumberRange(min=1), InputRequired()])
    update_btn = SubmitField('Update Quantity')
    

class RemoveCartItem(FlaskForm):
    cart_item_id = HiddenField(
        'Cart Item ID', id='cart_item', name='cart_item', validators=[DataRequired()])
    remove_btn = SubmitField('Remove Item From Cart')
