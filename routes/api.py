from flask import Blueprint, jsonify, request
from models.cupcake import Cupcake as Cake
from forms.cupcake_forms import NewCupcakeForm

api = Blueprint('api_routes', __name__)


@api.route('/cupcakes')
def show_all_cupcakes():
    """Returns all the cupcakes in the DB"""
    search = request.args.get('term')

    cakes = Cake.search_by_flavor(search) if search else Cake.get_all()

    json_cakes = jsonify(cupcakes=[cake.serialize() for cake in cakes])
    return json_cakes


@api.route('/cupcakes/<int:cake_id>')
def show_a_cupcake(cake_id):
    """returns a specific cupcake from the DB"""
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
        return (json, 400)


@api.route('/cupcakes/<int:cake_id>', methods=["PATCH"])
def update_a_cupcake(cake_id):
    """updates a cupcake in the DB"""
    cake = Cake.get(cake_id)
    json = request.json
    if json:
        if cake.update_from_serial(json):
            cake.update_db()
            return jsonify(cupcake=cake.serialize())
        else:
            return (jsonify(message="Could not Update", data=json), 400)
    else:
        return (jsonify(message="Bad Input"), 400)


@api.route('/cupcakes/<int:cake_id>', methods=["DELETE"])
def delete_a_cupcake(cake_id):
    """Deletes the cupcake in the DB"""
    # throws a 404 if no cake_id
    cake = Cake.get(cake_id)
    serial_cake = cake.serialize()
    # deletes the cake and updates the DB
    cake.delete()

    return jsonify(message="Deleted", deleted_cupcake=serial_cake)
