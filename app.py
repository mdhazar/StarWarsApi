from flask import Flask
from flask_restful import Api
from mongoengine import connect
from config import Config
from views.character_view import (
    CharacterList,
    CharacterCreate,
    CharacterGetByName,
    CharacterUpdateByName,
    CharacterDeleteByName,
    CharacterGetById,
    CharacterUpdateById,
    CharacterDeleteById,
    CharacterCollectionName,
    CharacterCollectionAffiliation,
    CharacterCollectionSpecies,
    CharacterCollectionHomeworld,
    CharacterDeleteAll,
)
from views.home_view import home_bp

app = Flask(__name__)
app.config.from_object(Config)


connect(
    db=app.config["MONGODB_SETTINGS"]["db"],
    host=app.config["MONGODB_SETTINGS"]["host"],
    port=app.config["MONGODB_SETTINGS"]["port"],
)

api = Api(app)

api.add_resource(CharacterGetByName, "/api/characters/<string:name>")
api.add_resource(CharacterUpdateByName, "/api/characters/<string:name>")
api.add_resource(CharacterDeleteByName, "/api/characters/<string:name>")
api.add_resource(CharacterGetById, "/api/characters/id/<string:id>")
api.add_resource(CharacterUpdateById, "/api/characters/id/<string:id>")
api.add_resource(CharacterDeleteById, "/api/characters/id/<string:id>")
api.add_resource(CharacterList, "/api/characters")
api.add_resource(CharacterCreate, "/api/characters")
api.add_resource(CharacterCollectionName, "/api/characters/names")
api.add_resource(CharacterCollectionAffiliation, "/api/characters/affiliations")
api.add_resource(CharacterCollectionSpecies, "/api/characters/species")
api.add_resource(CharacterCollectionHomeworld, "/api/characters/homeworld")
api.add_resource(CharacterDeleteAll, "/api/characters")

app.register_blueprint(home_bp)

if __name__ == "__main__":
    app.run(debug=True)
