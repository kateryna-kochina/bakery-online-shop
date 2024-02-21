from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Length, Email, ValidationError

from .models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

    def validate_username(self, field):
        user = User.query.filter_by(username=field.data).first()
        if not user:
            raise ValidationError('Invalid username.')

    def validate_password(self, field):
        user = User.query.filter_by(username=self.username.data).first()
        if user and not user.check_password(self.password.data):
            raise ValidationError('Invalid password.')


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[
                           DataRequired(), Length(min=4, max=50)])
    email = EmailField('Email', validators=[
                       DataRequired(Email), Length(min=4, max=50)])
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(min=4, max=50)])
    submit = SubmitField('Create account')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError(
                'Username already exists. Please choose a different username.')

    def validate_email(self, field):
        if User.query.filter_by(email_address=field.data).first():
            raise ValidationError(
                'Email address already exists. Please choose a different email address.')
