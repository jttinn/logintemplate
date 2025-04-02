# File Name: models/features.py
# Version: 1.0
# Last Updated: 01-Apr-2025
# Description: SQLAlchemy models for feature-related database tables in MrClean.

from app import db
from models.users import mc_users
from models.roles import mc_roles

class mc_features(db.Model):
    __tablename__ = 'mc_features'
    feature_id = db.Column(db.Integer, primary_key=True)
    feature_name = db.Column(db.String(50), unique=True, nullable=False)
    feature_desc = db.Column(db.String(255), nullable=False)
    is_active = db.Column(db.Boolean, default=True, nullable=False)
    feature_link = db.Column(db.String(50), unique=True, nullable=False)
    feature_added_by = db.Column(db.Integer, db.ForeignKey('mc_users.user_id'))
    feature_added_ts = db.Column(db.DateTime, default=db.func.current_timestamp())
    feature_updated_by = db.Column(db.Integer, db.ForeignKey('mc_users.user_id'))
    feature_updated_ts = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

class mc_role_features(db.Model):
    __tablename__ = 'mc_role_features'
    role_id = db.Column(db.Integer, db.ForeignKey('mc_roles.role_id'), primary_key=True)
    feature_id = db.Column(db.Integer, db.ForeignKey('mc_features.feature_id'), primary_key=True)
    role = db.relationship('mc_roles', backref=db.backref('features', cascade='all, delete-orphan'))
    feature = db.relationship('mc_features', backref=db.backref('roles', cascade='all, delete-orphan'))