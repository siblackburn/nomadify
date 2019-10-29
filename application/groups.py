from flask import Blueprint, jsonify, request, render_template

from . import db
from .models import User, GroupDescription, group_membership_table


GroupsApi = Blueprint('groups', __name__)


@GroupsApi.route('/', methods=['POST']) # can create more than one method here (e.g. POST, GET etc)
def create_groups():

    try:
        request_data = request.get_json()
        user_ids = request_data.get("user_ids")
        new_group_name = request_data.get("group_name")

        new_group = GroupDescription.create_group(request.json)
        for user_id in user_ids:
            user = User.query.filter(User.user_id == user_id).first()
            new_group.users.append(user)

    except KeyError as e:
        return jsonify(f'Missing key: {e.args[0]}'), 400

    db.session.add(new_group)
    db.session.commit()



    return jsonify(), 200

'''
Need to add functionality to the function above
 user = Users.query...
    group = Groups.query.get(group_id)
    group.users.append(user)

'''

