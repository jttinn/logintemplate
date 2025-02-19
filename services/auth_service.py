# File Name: logintemplate\services\auth_service.py
# Version: 1.1
# Last Updated: 17-Feb-2025
# Description: Business logic for user authentication.

from logintemplate.models.user_model import User
from logintemplate import db
from werkzeug.security import generate_password_hash, check_password_hash

def register_user(username, email, password):
    password_hash = generate_password_hash(password)
    new_user = User(username=username, email=email, password_hash=password_hash)
    # Add user to the database
    pass

def login_user(email, password):
    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password_hash, password):
        # Handle login logic
        pass