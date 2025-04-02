# File Name: routes/__init__.py
# Version: 1.0
# Last Updated: 01-Apr-2025
# Description: Registers Flask routes for MrClean by importing route modules.

from app import app
from routes.auth import login, logout
from routes.ui import home

# Register routes
app.route('/')(home)
app.route('/login', methods=['GET', 'POST'])(authorize_feature('User_Login')(login))
app.route('/logout')(authorize_feature('User_Log_Out')(login_required(logout)))