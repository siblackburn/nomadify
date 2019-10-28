from flask import Blueprint, jsonify, request, render_template
import json

from . import db
from .models import Users, Messages, GroupDescription, group_membership_table
from sqlalchemy import DateTime, desc


ChatsApi = Blueprint('chats', __name__)

'''
The route for create message is different to get message, because it's a specific user sending it. Therefore user is no
longer a query parameter
'''
#/api/chats/<group_id>/messages?user_id=<user_id>&limit=10
@ChatsApi.route('/<group_id>/messages', methods=['POST'])
def post_message(group_id):
    try:
        user_id = request.args['user_id']
        request_data = request.get_json()
        message_content = request_data.get("message_content", " ")
        new_message = Messages(group_id=group_id, message_content=message_content, user_id=user_id)
    except KeyError as e:
        return jsonify(f'Missing key: {e.args[0]}'), 400

    db.session.add(new_message)
    db.session.commit()
    return jsonify(), 200


# http://0.0.0.0:5000/api/chats/2/messages?user_id=9&
'''
# this defines the api route that flask will try to parse. so when the user passes
#1 into the space where <group_id> is, flask knows that group_id = 1. we then define the second part of the url as messages. Everything after the
#? is the query parameters. So in this case, we're accessing group chat 1, and we're querying them for user_id=2
'''
@ChatsApi.route('/<int:group_id>/messages', methods=['GET'])
def get_messages(group_id):
    # user_id = request.args['user_id'] #returns the user_id, just so we can use the user_id in this function
    # user = Users.query.filter(Users.user_id == user_id).first()
    '''
    #The above two lines aren't needed for the below query because all the group messages are relevant to all users
    #however in the future we may want to put a forbidden message here. e.g. if the user accessing is doesn't have a user id already in the group, don't let them
    #access the messages!!
    '''
    group_messages = Messages.query.filter(Messages.group_id == group_id).all()
    new_list = [Messages.return_message(message) for message in group_messages]
    return jsonify(new_list), 200


'''
Method for getting a list of chats for a particular user
/api/chats?user_id=<user_id>
'''
@ChatsApi.route('/<user_id>', methods=['GET'])
def get_users_groups(user_id):
    group_chats = GroupDescription.query.join(Users.groups).filter(Users.user_id == user_id).all()
    list_of_chats = [GroupDescription.return_groups(g) for g in group_chats]
    return jsonify(list_of_chats), 200
