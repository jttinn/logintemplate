# File Name: app/__init__.py
# Version: 1.5
# Last Updated: 01-Apr-2025
# Description: Initializes the Flask application for MrClean, including the authorization decorator.

from flask import Flask, session, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from functools import wraps
from config import Config
from models.users import mc_users
from models import mc_temp_codes  # Not yet defined, placeholder for future use

app = Flask(__name__, static_folder='static', template_folder='templates')
app.config.from_object(Config)

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'routes.login'

@login_manager.user_loader
def load_user(user_id):
    return mc_users.query.get(int(user_id))

# Feature #1: Authorize and Authenticate Users (FR# 1.1-1.11)
def authorize_feature(current_feature_name):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            # FR# 1.1: Receive current_feature_name
            feature_name = current_feature_name

            # FR# 1.2 & 1.3: Set or fetch session['feature_in_progress']
            from models.features import mc_features
            feature = db.session.query(mc_features).filter_by(feature_name=feature_name, is_active=True).first()
            if not feature:
                flash("That feature is not available. Please contact the Administrator.")
                return redirect(url_for('routes.home'))

            # Check if this is a workflow-start page
            if feature.feature_link == request.path:
                session['feature_in_progress'] = feature_name
            # For mid-process pages, fetch from session
            else:
                session_feature = session.get('feature_in_progress')
                if not session_feature:
                    flash("That feature is not available. Please contact the Administrator.")
                    return redirect(url_for('routes.home'))
                feature_name = session_feature  # Use session value for mid-process pages

            # FR# 1.4 & 1.5: Fetch roles
            from flask_login import current_user
            from models.roles import mc_user_roles, mc_roles
            roles = session.get('ROLE', ['PUBLIC']) if not current_user.is_authenticated else [r.role.role_name for r in db.session.query(mc_user_roles).filter_by(user_id=current_user.user_id).all()] or ['PUBLIC']

            # FR# 1.6 & 1.7: Query mc_features and mc_role_features
            from models.features import mc_role_features
            access = db.session.query(mc_features, mc_role_features).join(mc_role_features, mc_features.feature_id == mc_role_features.feature_id).join(mc_roles, mc_role_features.role_id == mc_roles.role_id).filter(mc_features.feature_name == feature_name, mc_features.is_active == True, mc_roles.role_name.in_(roles)).first()
            if not access:
                flash("You do not have access to that feature")
                return redirect(url_for('routes.home'))

            # FR# 1.8 & 1.9: Workflow context check
            if request.path == access.mc_features.feature_link:
                # FR# 1.8: Workflow-start page, proceed
                return f(*args, **kwargs)
            else:
                # FR# 1.9: Mid-process page, check workflow context
                if session.get('feature_in_progress') != feature_name:
                    flash(f"Please start {feature_name} from the beginning")
                    return redirect(access.mc_features.feature_link)
                # Check supporting data (e.g., mc_temp_codes for /verify, /change_password)
                if feature_name in ['User_Registration', 'Password_Reset']:
                    email = session.get('email') or (current_user.email if current_user.is_authenticated else None)
                    if not email or not db.session.query(mc_temp_codes).filter_by(email=email).first():
                        flash(f"Please start {feature_name} from the beginning")
                        return redirect(access.mc_features.feature_link)

            # FR# 1.10: Session cleanup on menu navigation (handled in routes if needed)
            # FR# 1.11: Implicitly satisfied by decorator

            return f(*args, **kwargs)
        return decorated_function
    return decorator

# Import routes after app setup to avoid circular imports
from routes import *