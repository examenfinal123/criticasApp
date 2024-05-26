from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from config import Config
from flask_cors import CORS
from models import *

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
app.template_folder = "templates"

app.config.from_object(Config)

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

db.create_all