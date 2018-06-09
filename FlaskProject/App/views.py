
from flask import Blueprint
from App.models import Animal

blue =Blueprint("first_blue", __name__, url_prefix='/blue/')

def init_blue(app):
    app.register_blueprint(blueprint=blue)


@blue.route('/index/')
def index():
    return 'Flask Index'