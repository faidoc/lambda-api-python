from importlib import import_module
from os import environ
from sys import exit

from flask import Flask
from flask import jsonify

from api.extensions import ma
from api.v1.blueprints import all_blueprints as all_blueprints_v1

app = Flask(__name__)

# Set environment
if environ.get('APP_ENV'):
    if environ.get('APP_ENV') == 'DEVELOPMENT':
        app.config.from_object('config.DevelopmentConfig')
    elif environ.get('APP_ENV') == 'PRODUCTION':
        app.config.from_object('config.ProductionConfig')
    elif environ.get('APP_ENV') == 'TESTING':
        app.config.from_object('config.TestingConfig')
else:
    print 'No APP_ENV variable found. Export one of the following: DEVELOPMENT, PRODUCTION, TESTING'
    exit(2)


@app.errorhandler(404)
def not_found(error):
    err = {'message': "Resource doesn't exist."}
    resp = jsonify(**err)
    resp.status_code = 404

    return resp


# Setup redirects and register blueprints.
for bp in all_blueprints_v1:
    import_module(bp.import_name)
    app.register_blueprint(bp)

# Initialize extensions
ma.init_app(app)

if __name__ == '__main__':
    app.run()
