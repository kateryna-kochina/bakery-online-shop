from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, HiddenField
from wtforms.validators import DataRequired, NumberRange


class AddToCart(FlaskForm):
    selected_option = HiddenField('Selected Option', id='selected_option')
    quantity = IntegerField('Quantity', validators=[DataRequired(), NumberRange(min=1)])
    add_to_cart_btn = SubmitField('Add to Cart')
