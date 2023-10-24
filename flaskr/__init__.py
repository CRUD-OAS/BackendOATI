import os

from flask import Flask
from flask_cors import CORS


def create_app(app):
    # create and configure the app
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
app = Flask(__name__)
app = create_app(app)