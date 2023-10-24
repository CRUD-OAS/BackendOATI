import os

from flask import Flask
from flask_cors import CORS


def create_app():
    # create and configure the app
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    # enable CORS
    CORS(app, resources={r'/*': {'origins': '*'}})

    from flaskr import db
    db.init_app(app)
    from flaskr import candidatos
    app.register_blueprint(candidatos.bp)
    from flaskr import partidos
    app.register_blueprint(partidos.bp)
    from flaskr import votos
    app.register_blueprint(votos.bp)
    return app
