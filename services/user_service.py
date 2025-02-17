# File Name: logintemplate\services\user_service.py
# Version: 1.0
# Last Updated: 25-Nov-2024
# Description: Logic for user management operations.

from models.user_model import User

def get_user_by_id(user_id):
    return User.query.get(user_id)