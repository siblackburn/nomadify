from flask import Blueprint, jsonify, request, render_template

from . import db
from .models import Users


NewUsersApi = Blueprint('new_users', __name__)


@NewUsersApi.route('/', methods=['POST']) # can create more than one method here (e.g. POST, GET etc)
def create_user():

    try:
        new_user = Users.create_user(request.json)
    except KeyError as e:
        return jsonify(f'Missing key: {e.args[0]}'), 400

    db.session.add(new_user)
    db.session.commit()
    return jsonify(), 200


@NewUsersApi.route('/<username>', methods=['GET'])
def get_user(username):
    username = Users.query.filter(Users.username == username).first()
    if username is None:
        return 'user not found', 404
    return jsonify(username.retrieve_users()), 200
