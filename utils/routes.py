from views.character_view import *


def register_resources(api):
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
