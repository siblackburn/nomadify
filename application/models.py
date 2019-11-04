from . import db
from datetime import datetime
from sqlalchemy import Table, Integer, String, ForeignKey, Column, ForeignKeyConstraint


group_membership_table = Table('group_membership', db.Model.metadata,
    db.Column('group_id', db.Integer, db.ForeignKey('group_description.group_id', ondelete='CASCADE')),
    db.Column('user_id', db.Integer, db.ForeignKey('users.user_id', ondelete='CASCADE')))


class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer,
                   primary_key=True, autoincrement=True, nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(150), unique=False, nullable=False)
    location = db.Column(db.String(50), unique=False, nullable=True)
    profile_picture = db.Column(db.String(50), unique=False, nullable=True)
    signup_date = db.Column(db.DateTime, unique=False, nullable=False, default=datetime.utcnow)
    groups = db.relationship('GroupDescription', secondary=group_membership_table, back_populates="users")

    @staticmethod
    def create_user(dict):
        return User(username=dict['username'], email=dict['email'], password_hash=dict['password_hash'], location=dict['location'])

    def retrieve_users(self):
        return {
           'user_id': self.user_id,
           'username': self.username,
           'email': self.email,
           'password_hash': self.password_hash,
           'location': self.location,
           'profile_picture': self.profile_picture
       }


class GroupDescription(db.Model):
    __tablename__ = 'group_description'
    group_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    group_name = db.Column(db.String(50), nullable=True, unique=False)                  #if group has no name, return user name instead
    users = db.relationship('User', secondary=group_membership_table, back_populates="groups")

    @staticmethod
    def create_group(dict):
        return GroupDescription(group_name=dict['group_name'])

    def return_groups(self):
        return {
            'group_id': self.group_id,
           'group_name': self.group_name,
       }



class Messages(db.Model):
    __tablename__ = 'messages'
    message_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id',
                        ondelete="SET NULL"))  # need to check on delete syntax
    group_id = db.Column(db.Integer, db.ForeignKey('group_description.group_id',
                        ondelete="SET NULL"))
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    message_content = db.Column(db.String(500), nullable=True, unique=False)
    document_link = db.Column(db.String(150), nullable=True)
    message_sentiment = db.Column(db.String(100), nullable=True)

    user = db.relationship('User', foreign_keys=user_id)

    # @staticmethod
    # def create_message(dict, user_id, group_id):
    #     return Messages(message_content=dict['message_content'])

    def return_message(self):
        return {
            'message_id': self.message_id,
            'timestamp': self.timestamp,
            'message_content': self.message_content,
            'document_link': self.document_link,
            'message_sentiment': self.message_sentiment,
            'user': self.user.retrieve_users()
       }


