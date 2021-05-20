from flask import render_template
from flask import current_app as app
from flask import Blueprint

routes = Blueprint('public', __name__, template_folder='templates')


@routes.route('/')
def home():
    """Landing page."""
    return render_template(
        'index.html',
    )