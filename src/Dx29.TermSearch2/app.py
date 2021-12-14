import os
import settings

from flask import Flask, Blueprint

from WebAPI import API, endpoints

app = Flask(__name__)

def initialize_app(flask_app):
    blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
    API.init_app(blueprint)
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP
    flask_app.register_blueprint(blueprint)

def main(debug=False):
    initialize_app(app)
    app.run(host='0.0.0.0', port=8080, debug=debug)

if __name__ == '__main__':
    main(False)
