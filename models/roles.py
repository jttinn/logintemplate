# File Name: models/roles.py
# Version: 1.0
# Last Updated: 01-Apr-2025
# Description: SQLAlchemy models for role-related database tables in MrClean.

from app import db
from models.users import mc_users  # Import mc_users for foreign keys

class mc_roles(db.Model):
    __tablename__ = 'mc_roles'
    role_id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(50), unique=True, nullable=False)
    role_desc = db.Column(db.String(255), nullable=False)
    is_active = db.Column(db.Boolean, default=True, nullable=False)
    role_added_by = db.Column(db.Integer, db.ForeignKey('mc_users.user_id'))
    role_added_ts = db.Column(db.DateTime, default=db.func.current_timestamp())
    role_updated_by = db.Column(db.Integer, db.ForeignKey('mc_users.user_id'))
    role_updated_ts = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

class mc_user_roles(db.Model):
    __tablename__ = 'mc_user_roles'
    user_id = db.Column(db.Integer, db.ForeignKey('mc_users.user_id'), primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey('mc_roles.role_id'), primary_key=True)
    user = db.relationship('mc_users', backref=db.backref('roles', cascade='all, delete-orphan'))
    role = db.relationship('mc_roles', backref=db.backref('users', cascade='all, delete-orphan'))