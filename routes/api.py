from flask import Blueprint, jsonify, request
from models.cupcake import Cupcake as Cake

api = Blueprint('api_routes', __name__)


@api.route('')
def show_home_page():
    """Show a welcome page"""
    return "hello"


@api.route('/cupcakes')
def show_all_cupcakes():
    """Shows all the cupcakes in the DB"""
    cakes = Cake.get_all()
    json_cakes = jsonify(cupcakes=[cake.serialize() for cake in cakes])
    return json_cakes


@api.route('/cupcakes/<int:cake_id>')
def show_a_cupcake(cake_id):
    """Shows a cupcake from the DB"""
    cake = Cake.get(cake_id)
    return jsonify(cupcake=cake.serialize())


@api.route('/cupcakes', methods=["POST"])
def create_a_cupcake():
    """Create a cupcake in the DB returns 404 and the sent in cake on failiure"""
    json = request.json
    new_cake = Cake()
    if new_cake.from_serial(json):
        return (jsonify(cupcake=new_cake.serialize()), 201)
    else:
        return (json, 404)


@api.route('/cupcakes/<int:cake_id>', methods=["PATCH"])
def update_a_cupcake(cake_id):
    """Updates a cupcake in the DB"""
    cake = Cake.get(cake_id)
    json = request.json
    if json:
        if cake.update_from_serial(json):
            cake.update_db()
            return jsonify(cupcake=cake.serialize())
        else:
            return (jsonify(message="Could not Update", data=json), 404)
    else:
        return (jsonify(message="bad Input"), 404)
