'''
DO NOT USE FOR NOW. Get users.py working first
'''

# from flask import Blueprint, jsonify, request, render_template
# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField, BooleanField, SubmitField
# from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
#
# from app.application import models
# from app.application import db
#
# new_user_api = Blueprint('new_user_api', __name__)
#
# '''
# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins
# '''
# class RegistrationForm(FlaskForm):
#     username = StringField('username', validators=[DataRequired()])
#     email = StringField('email', validators=[DataRequired(), Email()])
#     password = PasswordField('password', validators=[DataRequired()])
#     password2 = PasswordField(
#         'Repeat Password', validators=[DataRequired(), EqualTo('password')])
#     submit = SubmitField('Register')
#
#     def validate_username(self, username):
#         user = User.query.filter_by(username=username.data).first()
#         if user is not None:
#             raise ValidationError('Please use a different username.')
#
#     def validate_email(self, email):
#         user = User.query.filter_by(email=email.data).first()
#         if user is not None:
#             raise ValidationError('Please use a different email address.')