from flask import Flask
from config import Config
from database import setup_database
from utils.api_routes import register_api_routes
import views.home_view as home_view


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    setup_database(app)

    register_api_routes(app)

    app.register_blueprint(home_view.home_bp)

    return app
