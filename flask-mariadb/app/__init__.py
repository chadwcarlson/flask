import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config.Database import DbConfig
from flask_caching import Cache

config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_TYPE": "RedisCache",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300,
    # "CACHE_KEY_PREFIX": 300,
    # "CACHE_OPTIONS": 300,
    "CACHE_REDIS_HOST": os.getenv("CACHE_HOST_REDIS"),
    "CACHE_REDIS_PORT": os.getenv("CACHE_PORT_REDIS"),
    "CACHE_REDIS_PASSWORD": None,
    "CACHE_REDIS_DB": None,
    "CACHE_REDIS_URL": os.getenv("CACHE_LOCATION_REDIS"),
}

# The app.
app = Flask(__name__)

# Database.
app.config["SQLALCHEMY_DATABASE_URI"] = DbConfig().getUri()
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# Caching.
app.config.from_mapping(config)
cache = Cache(app)

from app.model import CoursesModel, CollegerModel, TakeCourseModel

migrate = Migrate(app, db)

from app.controller.Main import *
from app.controller.CollegerController import *
from app.controller.CoursesController import *
from app.controller.TakeCourseController import *
