# File Name: routes/auth.py
# Version: 1.1
# Last Updated: 01-Apr-2025
# Description: Defines Flask routes for authentication-related features in MrClean, including User Login and User Log Out.

from flask import render_template, request, redirect, url_for, flash, session
from flask_login import login_user, current_user, logout_user, login_required
from app import db
from models.users import mc_users
from models.roles import mc_user_roles, mc_roles
from models.features import mc_role_features, mc_features
from app import authorize_feature

# FR# 2.1: Set current_page
def login():
    # FR# 2.1: Set current_page
    current_page = '/login'

    # Redirect if already logged in
    if current_user.is_authenticated:
        return redirect(url_for('ui.home'))

    # FR# 2.3: Display form
    alert_message = session.pop('alert_message', None)  # Retrieve alert if passed
    if request.method == 'GET':
        return render_template('login.html', alert_message=alert_message)

    # FR# 2.4 & 2.5: Validate inputs
    email = request.form.get('email')
    password = request.form.get('password')

    if not email or not email.strip() or '@' not in email or '.' not in email:
        flash("Please enter a valid email address")
        return render_template('login.html', alert_message=alert_message)

    if not password or not password.strip():
        flash("Please enter a password")
        return render_template('login.html', alert_message=alert_message)

    # FR# 2.6: Query mc_users
    user = db.session.query(mc_users).filter_by(email=email).first()

    # FR# 2.7: Verify password
    if not user or not user.check_password(password):
        # FR# 2.13: Invalid email or password
        flash("Invalid email or password")
        return render_template('login.html', alert_message=alert_message)

    # FR# 2.8: Check is_active
    if not user.is_active:
        flash("Your login is no longer active. Please contact your administrator")
        return render_template('login.html', alert_message=alert_message)

    # FR# 2.9: Check force_reset
    if user.force_reset:
        session['alert_message'] = "Please reset your password to continue"
        session['email'] = user.email  # Store email for /reset
        return redirect(url_for('password.reset'))

    # FR# 2.10: Set session, update last_login_ts, set roles
    login_user(user)
    user.last_login_ts = db.func.current_timestamp()
    db.session.commit()
    session['ROLE'] = [r.role.role_name for r in user.roles]

    # FR# 2.11: Update left panel menu
    public_features = db.session.query(mc_features).join(mc_role_features).join(mc_roles).filter(mc_roles.role_name == 'PUBLIC', mc_features.is_active == True).all()
    user_features = db.session.query(mc_features).join(mc_role_features).join(mc_roles).filter(mc_roles.role_name.in_(session['ROLE']), mc_features.is_active == True).all()
    menu_features = list(set(public_features + user_features))
    session['menu_features'] = [{'feature_name': f.feature_name, 'feature_link': f.feature_link} for f in menu_features]

    # FR# 2.12: Redirect to requested URL or home
    next_page = request.args.get('next') or url_for('ui.home')
    return redirect(next_page)

# FR# 9.1: Set current_page
def logout():
    # FR# 9.1: Set current_page
    current_page = '/logout'

    # FR# 9.3: Clear user session
    logout_user()

    # FR# 9.4: Clear role and menu session
    session.pop('ROLE', None)
    session.pop('menu_features', None)

    # FR# 9.5: Clear workflow session
    session.pop('feature_in_progress', None)

    # FR# 9.6: Redirect to login with alert
    session['alert_message'] = "You have been logged out successfully"
    return redirect(url_for('login'))