from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
from flask_caching import Cache
from flask_restful import Resource, Api

app = Flask(__name__)

app.config.from_object(Config)

bootstrap = Bootstrap(app=app)
cache = Cache(app=app, config={'CACHE_TYPE': app.config['CACHE_TYPE']})

from app.main import bp as main_bp
from app.errors import bp as errors_bp
from app.libraries import bp as libraries_bp

app.register_blueprint(main_bp)
app.register_blueprint(errors_bp)
app.register_blueprint(libraries_bp)