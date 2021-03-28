from flask import Blueprint, render_template, request
from models.cupcake import Cupcake as Cake
from forms.cupcake_forms import NewCupcakeForm

main = Blueprint('main_routes', __name__)


@main.route('')
def show_home_page():
    """Show a welcome page"""
    form = NewCupcakeForm()
    return render_template('home.html', form=form)
