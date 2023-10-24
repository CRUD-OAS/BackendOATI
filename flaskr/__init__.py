import os

from flask import Flask
from flask_cors import CORS

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    # enable CORS
    CORS(app, resources={r'/*': {'origins': '*'}})

    from . import db
    db.init_app(app)
    from . import candidatos
    app.register_blueprint(candidatos.bp)
    from . import partidos
    app.register_blueprint(partidos.bp)
    from . import votos
    app.register_blueprint(votos.bp)
    return app