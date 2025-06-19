from flask import Flask
from flask_restful import Api
from mongoengine import connect
from config import Config
from views.home_view import home_bp
from utils.routes import register_resources

app = Flask(__name__)
app.config.from_object(Config)


connect(
    db=app.config["MONGODB_SETTINGS"]["db"],
    host=app.config["MONGODB_SETTINGS"]["host"],
    port=app.config["MONGODB_SETTINGS"]["port"],
)

api = Api(app)
register_resources(api)

app.register_blueprint(home_bp)

if __name__ == "__main__":
    app.run(debug=True)
