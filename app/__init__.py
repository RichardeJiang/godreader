from flask import Flask
# from config import Config
from flask_sqlalchemy import SQLAlchemy


# Initialize the app
app = Flask(__name__, instance_relative_config=True)

# Load the views
from app import views

# Load the config file
app.config.from_object('config')