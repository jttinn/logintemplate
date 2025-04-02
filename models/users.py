# File Name: models/users.py
# Version: 1.0
# Last Updated: 01-Apr-2025
# Description: SQLAlchemy models for user-related database tables in MrClean.

from flask_login import UserMixin
from werkzeug.security import check_password_hash
from app import db

class mc_users(UserMixin, db.Model):
    __tablename__ = 'mc_users'
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    user_given_name = db.Column(db.String(50), nullable=False)
    password_hash = db.Column(db.String(128))
    is_active = db.Column(db.Boolean, default=True, nullable=False)
    force_reset = db.Column(db.Boolean, default=False, nullable=False)
    user_created_by = db.Column(db.Integer, db.ForeignKey('mc_users.user_id'))
    user_created_ts = db.Column(db.DateTime, default=db.func.current_timestamp())
    user_updated_by = db.Column(db.Integer, db.ForeignKey('mc_users.user_id'))
    user_updated_ts = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    last_login_ts = db.Column(db.DateTime)

    def get_id(self):
        return str(self.user_id)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)