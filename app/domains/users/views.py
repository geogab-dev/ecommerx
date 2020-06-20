from flask import Blueprint, request, jsonify
from app.domains.users.actions import get_all_users, insert_user, get_user_by_id, update_user, delete_user


app_users = Blueprint('app.users', __name__)


@app_users.route('/users', methods=['GET'])
def get_users():
    return jsonify([user.serialize() for user in get_all_users()]), 200


@app_users.route('/users/<id>', methods=["GET"])
def get_by_id(id: str):
    user = get_user_by_id(id_user=id)
    return jsonify(user.serialize()), 200


@app_users.route('/users', methods=["POST"])
def post_user():
    payload = request.get_json()
    user = insert_user(payload)
    return jsonify(user.serialize()), 201


@app_users.route('/users/<id>', methods=["PUT"])
def update(id: str):
    payload = request.get_json()
    user = update_user(id_user=id, data=payload)
    return jsonify(user.serialize()), 200


@app_users.route('/users/<id>', methods=["DELETE"])
def delete(id: str):
    delete_user(id_user=id)
    return jsonify({"message": "user deleted"}), 200
