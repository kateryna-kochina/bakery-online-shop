from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, HiddenField
from wtforms.validators import DataRequired, NumberRange


class ChoiceForm(FlaskForm):
    selected_choice = HiddenField('Selected Choice', id='selected_choice')
    quantity = IntegerField('Quantity', validators=[DataRequired(), NumberRange(min=1)])
    add_to_cart_btn = SubmitField('Add to Cart')
