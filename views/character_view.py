from flask import request
from flask_restx import Namespace, Resource, fields
from controllers.character_controller import CharacterController


api = Namespace("characters", description="Star Wars Characters operations")


character_model = api.model(
    "Character",
    {
        "id": fields.String(readonly=True, description="Unique character identifier"),
        "name": fields.String(
            required=True, description="Character name", example="Luke Skywalker"
        ),
        "affiliation": fields.String(
            required=True, description="Character affiliation", example="Rebel Alliance"
        ),
        "homeworld": fields.String(
            required=True, description="Character homeworld", example="Tatooine"
        ),
        "species": fields.String(
            required=True, description="Character species", example="Human"
        ),
        "image": fields.String(
            description="Character image URL", example="https://example.com/luke.jpg"
        ),
    },
)

character_input = api.model(
    "CharacterInput",
    {
        "name": fields.String(
            required=True, description="Character name", example="Luke Skywalker"
        ),
        "affiliation": fields.String(
            required=True, description="Character affiliation", example="Rebel Alliance"
        ),
        "homeworld": fields.String(
            required=True, description="Character homeworld", example="Tatooine"
        ),
        "species": fields.String(
            required=True, description="Character species", example="Human"
        ),
        "image": fields.String(
            description="Character image URL", example="https://example.com/luke.jpg"
        ),
    },
)

error_model = api.model(
    "Error",
    {
        "message": fields.String(description="Error message"),
        "errors": fields.Raw(description="Detailed error information"),
    },
)

names_model = api.model(
    "CharacterNames",
    {"names": fields.List(fields.String, description="List of character names")},
)

affiliations_model = api.model(
    "CharacterAffiliations",
    {"affiliations": fields.Raw(description="Characters grouped by affiliation")},
)

species_model = api.model(
    "CharacterSpecies",
    {"species": fields.Raw(description="Characters grouped by species")},
)

homeworld_model = api.model(
    "CharacterHomeworlds",
    {"homeworld": fields.Raw(description="Characters grouped by homeworld")},
)


@api.route("/")
class CharacterList(Resource):
    @api.doc("list_characters")
    @api.marshal_list_with(character_model)
    @api.response(200, "Success")
    def get(self):
        """Fetch all characters"""
        return CharacterController.get_all_characters()

    @api.doc("create_character")
    @api.expect(character_input)
    @api.marshal_with(character_model, code=201)
    @api.response(201, "Character created successfully")
    @api.response(400, "Validation error", error_model)
    def post(self):
        """Create a new character"""
        return CharacterController.create_character(request.get_json())

    @api.doc("delete_all_characters")
    @api.response(200, "All characters deleted successfully")
    @api.response(500, "Server error", error_model)
    def delete(self):
        """Delete all characters (use with caution!)"""
        return CharacterController.delete_all_characters()


@api.route("/names")
class CharacterNames(Resource):
    @api.doc("get_character_names")
    @api.marshal_with(names_model)
    @api.response(200, "Success")
    def get(self):
        """Get list of all character names"""
        return CharacterController.get_character_names()


@api.route("/affiliations")
class CharacterAffiliations(Resource):
    @api.doc("get_character_affiliations")
    @api.marshal_with(affiliations_model)
    @api.response(200, "Success")
    def get(self):
        """Get characters grouped by affiliation"""
        return CharacterController.get_character_affiliations()


@api.route("/species")
class CharacterSpecies(Resource):
    @api.doc("get_character_species")
    @api.marshal_with(species_model)
    @api.response(200, "Success")
    def get(self):
        """Get characters grouped by species"""
        return CharacterController.get_character_species()


@api.route("/homeworld")
class CharacterHomeworlds(Resource):
    @api.doc("get_character_homeworlds")
    @api.marshal_with(homeworld_model)
    @api.response(200, "Success")
    def get(self):
        """Get characters grouped by homeworld"""
        return CharacterController.get_character_homeworlds()


@api.route("/<string:name>")
class CharacterByName(Resource):
    @api.doc("get_character_by_name")
    @api.marshal_with(character_model)
    @api.response(200, "Success")
    @api.response(404, "Character not found", error_model)
    def get(self, name):
        """Fetch a character by name"""
        return CharacterController.get_character_by_name(name)

    @api.doc("update_character_by_name")
    @api.expect(character_input)
    @api.marshal_with(character_model)
    @api.response(200, "Character updated successfully")
    @api.response(400, "Validation error", error_model)
    @api.response(404, "Character not found", error_model)
    def patch(self, name):
        """Update a character by name"""
        return CharacterController.update_character_by_name(name, request.get_json())

    @api.doc("delete_character_by_name")
    @api.response(204, "Character deleted successfully")
    @api.response(404, "Character not found", error_model)
    def delete(self, name):
        """Delete a character by name"""
        return CharacterController.delete_character_by_name(name)


@api.route("/id/<string:id>")
class CharacterById(Resource):
    @api.doc("get_character_by_id")
    @api.marshal_with(character_model)
    @api.response(200, "Success")
    @api.response(404, "Character not found", error_model)
    def get(self, id):
        """Fetch a character by ID"""
        return CharacterController.get_character_by_id(id)

    @api.doc("update_character_by_id")
    @api.expect(character_input)
    @api.marshal_with(character_model)
    @api.response(200, "Character updated successfully")
    @api.response(400, "Validation error", error_model)
    @api.response(404, "Character not found", error_model)
    def patch(self, id):
        """Update a character by ID"""
        return CharacterController.update_character_by_id(id, request.get_json())

    @api.doc("delete_character_by_id")
    @api.response(204, "Character deleted successfully")
    @api.response(404, "Character not found", error_model)
    def delete(self, id):
        """Delete a character by ID"""
        return CharacterController.delete_character_by_id(id)
