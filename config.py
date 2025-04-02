# File Name: config.py
# Version: 1.1
# Last Updated: 01-Apr-2025
# Description: Configuration settings for the MrClean Flask application.

from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Application settings
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")  # Fallback to our default
SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI", "mysql+pymysql://odsdev:xyzzy7@localhost/ods")
SQLALCHEMY_TRACK_MODIFICATIONS = False
DEBUG_MODE = os.getenv("DEBUG_MODE", "False").lower() == "true"