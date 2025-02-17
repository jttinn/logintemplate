# File Name: logintemplate\models\profile_model.py
# Version: 1.0
# Last Updated: 25-Nov-2024
# Description: Define the Profile model.

from app import db

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bio = db.Column(db.Text, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)