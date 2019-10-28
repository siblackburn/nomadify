from flask import Blueprint, jsonify, request, render_template

from . import db
from .models import Users, GroupDescription


GroupsApi = Blueprint('groups', __name__)


@GroupsApi.route('/', methods=['POST']) # can create more than one method here (e.g. POST, GET etc)
def create_groups():

    try:
        new_groups = GroupDescription.create_group(request.json)
    except KeyError as e:
        return jsonify(f'Missing key: {e.args[0]}'), 400

    db.session.add(new_groups)
    db.session.commit()
    return jsonify(), 200

