# File Name: logintemplate\routes\profile_routes.py
# Version: 1.0
# Last Updated: 25-Nov-2024
# Description: Define routes for user profile management.

from flask import Blueprint, render_template
from flask_login import login_required, current_user

profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)