from flask import Blueprint, render_template, request
from .models import User

HelloApi = Blueprint('hello_api', __name__)


@HelloApi.route('/<user_id>')
def hello_user(user_id):
    user_id = request.args['user_id']
    username = User.query.filter(User.user_id == user_id).first()
    return render_template('hello.html', username=user_id)