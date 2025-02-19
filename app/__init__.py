# File Name: logintemplate\app\__init__.py
# Version: 1.8
# Last Updated: 17-Feb-2025
# Description: Initialize the Flask application and configure it.

from flask import Flask, render_template, jsonify
from config import SECRET_KEY, DB_USER, DB_PASSWORD, DB_HOST, DB_NAME, DEBUG_MODE
from ..db import db

app = Flask(__name__, static_folder='../static', template_folder='../templates')

# Configure the Flask app
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = DEBUG_MODE

# Initialize the database
db.init_app(app)

# Import and register blueprints
from routes.auth_routes import auth_bp
from routes.profile_routes import profile_bp
from routes.upload_csv_routes import upload_csv_bp

app.register_blueprint(auth_bp)
app.register_blueprint(profile_bp)
app.register_blueprint(upload_csv_bp)

# Create the database tables
with app.app_context():
    db.create_all()

# Route to print environment variables
@app.route('/env')
def print_env():
    env_vars = {
        "SECRET_KEY": SECRET_KEY,
        "DB_USER": DB_USER,
        "DB_PASSWORD": DB_PASSWORD,
        "DB_HOST": DB_HOST,
        "DB_NAME": DB_NAME,
        "DEBUG_MODE": DEBUG_MODE
    }
    return jsonify(env_vars)

# Define the root URL route
@app.route('/')
def index():
    return render_template('index.html')