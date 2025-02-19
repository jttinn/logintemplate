# File Name: logintemplate\models\user_model.py
# Version: 1.0
# Last Updated: 25-Nov-2024
# Description: Define the User model.

from logintemplate import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password_hash = db.Column(db.String(128), nullable=False)
    profiles = db.relationship('Profile', backref='user', lazy=True)