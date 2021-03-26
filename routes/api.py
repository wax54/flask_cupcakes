from flask import Blueprint, jsonify
from models.cupcake import Cupcake

api = Blueprint('api_routes', __name__)


@api.route('')
def show_home_page():
    """Show a welcome page"""
    return "hello"


@api.route('/cupcakes')
def show_all_cupcakes():
    """Shows all the cupcakes in the DB"""
    return jsonify([{'flavor': 'chocolate'}])
