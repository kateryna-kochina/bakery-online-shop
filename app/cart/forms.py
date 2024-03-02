from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, HiddenField
from wtforms.validators import DataRequired, NumberRange


class UpdateQuantity(FlaskForm):
    quantity = IntegerField('Quantity', validators=[DataRequired(), NumberRange(min=1)])
    add_button = SubmitField('Add', id='selected_option')
    subtract_button = SubmitField('Subtract')
