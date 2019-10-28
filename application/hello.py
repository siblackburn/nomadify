from flask import Blueprint, render_template

HelloApi = Blueprint('hello_api', __name__)


@HelloApi.route('/<name>')
def hello_user(name):
    return render_template('hello.html', user=name)