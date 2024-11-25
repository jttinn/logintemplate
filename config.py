# config.py 
# Version:          1.0
# Version Date:     25-Nov-2024
# 

from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Application settings
SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")  # Fallback to a default if not found
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "ods")
DEBUG_MODE = os.getenv("DEBUG_MODE", "False").lower() == "true"

# Database connection string
SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
SQLALCHEMY_TRACK_MODIFICATIONS = False