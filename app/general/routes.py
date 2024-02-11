from flask import Blueprint, render_template


general_bp = Blueprint('general', __name__, template_folder='templates')


@general_bp.route('/')
def home():
    return render_template('general/home.html')


@general_bp.route('/about')
def about():
    return render_template('general/about.html')
