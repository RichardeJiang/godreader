from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize the app
app = Flask(__name__)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
# Load the views
from app import views, models

# Load the config file
app.config.from_object(Config)