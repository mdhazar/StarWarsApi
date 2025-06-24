from flask import Flask
from flask_cors import CORS
from flask_restx import Api
from config import Config
from database import setup_database
import views.home_view as home_view
from views.character_view import api as characters_ns


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app, origins=app.config["CORS_ORIGINS"])

    setup_database(app)

    api = Api(
        app,
        version=app.config["API_VERSION"],
        title=app.config["API_TITLE"],
        description=app.config["API_DESCRIPTION"],
        doc="/docs/",
        prefix="/api",
    )

    api.add_namespace(characters_ns, path="/characters")

    app.register_blueprint(home_view.home_bp)

    return app
