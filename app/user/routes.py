from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user
from sqlalchemy.exc import IntegrityError

from ..database import db
from .forms import LoginForm, RegisterForm
from .models import User


user_bp = Blueprint('user', __name__, template_folder='templates')


@user_bp.route('/user/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Logged in successfully!', 'success')

            return redirect(url_for('general.home'))

        else:
            flash('Invalid username or password', 'error')

    return render_template('user/login.html', form=form)


@user_bp.route('/user/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully!', 'success')

    return redirect(url_for('general.home'))


@user_bp.route('/user/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,
                    email_address=form.email.data)
        user.set_password(form.password.data)
        
        try:
            db.session.add(user)
            db.session.commit()
            flash('Registered successfully! You can now login.', 'success')
            login_user(user)  # Automatically login the user after registration

            return redirect(url_for('general.home'))
        
        except IntegrityError:
            db.session.rollback()  # Rollback the transaction
            flash('Username already exists. Please choose a different username.', 'error')

    return render_template('user/register.html', form=form)
