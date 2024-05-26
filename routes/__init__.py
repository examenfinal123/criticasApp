from flask import Blueprint

bp = Blueprint('main', __name__)

from . import auth, usuario_routes, sitio_routes, critica_routes
