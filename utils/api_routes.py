from flask_restful import Api
import views.character_view as character_views


def register_api_routes(app):
    api = Api(app)

    api.add_resource(
        character_views.CharacterGetByName, "/api/characters/<string:name>"
    )
    api.add_resource(
        character_views.CharacterUpdateByName, "/api/characters/<string:name>"
    )
    api.add_resource(
        character_views.CharacterDeleteByName, "/api/characters/<string:name>"
    )

    api.add_resource(character_views.CharacterGetById, "/api/characters/id/<string:id>")
    api.add_resource(
        character_views.CharacterUpdateById, "/api/characters/id/<string:id>"
    )
    api.add_resource(
        character_views.CharacterDeleteById, "/api/characters/id/<string:id>"
    )

    api.add_resource(character_views.CharacterDeleteAll, "/api/characters")
    api.add_resource(character_views.CharacterList, "/api/characters")
    api.add_resource(character_views.CharacterCreate, "/api/characters")

    api.add_resource(character_views.CharacterCollectionName, "/api/characters/names")
    api.add_resource(
        character_views.CharacterCollectionAffiliation, "/api/characters/affiliations"
    )
    api.add_resource(
        character_views.CharacterCollectionSpecies, "/api/characters/species"
    )
    api.add_resource(
        character_views.CharacterCollectionHomeworld, "/api/characters/homeworld"
    )
