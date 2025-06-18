import string
from flask import Flask, request
from flask_restful import Resource, Api, abort
from mongoengine import Document, StringField, connect, DoesNotExist, ValidationError
from marshmallow import Schema, fields, validate

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {
    "db": "starwarsapi",
    "host": "localhost",
    "port": 27017,
}
connect(
    db=app.config["MONGODB_SETTINGS"]["db"],
    host=app.config["MONGODB_SETTINGS"]["host"],
    port=app.config["MONGODB_SETTINGS"]["port"],
)
api = Api(app)


class CharacterModel(Document):
    name = StringField(required=True, unique=True, max_length=80)
    affiliation = StringField(required=True, max_length=80)
    homeworld = StringField(required=True, max_length=80)
    species = StringField(required=True, max_length=80)
    image = StringField(required=False, max_length=500)

    def __repr__(self):
        return f"Character(name={self.name})"


class CharacterSchema(Schema):
    id = fields.String(dump_only=True)
    name = fields.String(required=True, validate=validate.Length(max=80))
    affiliation = fields.String(required=True, validate=validate.Length(max=80))
    homeworld = fields.String(required=True, validate=validate.Length(max=80))
    species = fields.String(required=True, validate=validate.Length(max=80))
    image = fields.String(
        required=False, validate=validate.Length(max=500), allow_none=True
    )


character_schema = CharacterSchema()
characters_schema = CharacterSchema(many=True)


class CharacterList(Resource):
    def get(self):
        characters = CharacterModel.objects()
        return characters_schema.dump(characters), 200


class CharacterCollectionName(Resource):
    def get(self):
        characters = CharacterModel.objects().only("name")
        return {"names": [c.name for c in characters]}, 200


class CharacterCollectionAffiliation(Resource):
    def get(self):
        characters = CharacterModel.objects().only("name", "affiliation")
        affiliation_dict = {}
        for character in characters:
            if character.affiliation not in affiliation_dict:
                affiliation_dict[character.affiliation] = []
            affiliation_dict[character.affiliation].append(character.name)
        return {"affiliations": affiliation_dict}, 200


class CharacterCollectionSpecies(Resource):
    def get(self):
        characters = CharacterModel.objects().only("name", "species")
        species_dict = {}
        for character in characters:
            if character.species not in species_dict:
                species_dict[character.species] = []
            species_dict[character.species].append(character.name)
        return {"species": species_dict}, 200


class CharacterCollectionHomeworld(Resource):
    def get(self):
        characters = CharacterModel.objects().only("name", "homeworld", "species")
        homeworld_dict = {}
        for character in characters:
            if character.homeworld not in homeworld_dict:
                homeworld_dict[character.homeworld] = []
            homeworld_dict[character.homeworld].append(
                {"name": character.name, "species": character.species}
            )
        return {"homeworld": homeworld_dict}, 200


class CharacterCreate(Resource):
    def post(self):
        json_data = request.get_json()
        for field in ["name", "affiliation", "homeworld", "species"]:
            if field in json_data and isinstance(json_data[field], str):
                json_data[field] = string.capwords(json_data[field])
        errors = character_schema.validate(json_data)
        if errors:
            return {"message": "Validation failed", "errors": errors}, 400
        try:
            character = CharacterModel(**json_data)
            character.save()
            return character_schema.dump(character), 201
        except ValidationError as e:
            return {"message": "Validation failed", "errors": str(e)}, 400


class CharacterGetByName(Resource):
    def get(self, name):
        try:
            character = CharacterModel.objects.get(name=name)
            return character_schema.dump(character), 200
        except DoesNotExist:
            abort(404, message=f"Character with name '{name}' not found")


class CharacterUpdateByName(Resource):
    def patch(self, name):
        json_data = request.get_json()
        for field in ["name", "affiliation", "homeworld", "species"]:
            if field in json_data and isinstance(json_data[field], str):
                json_data[field] = string.capwords(json_data[field])
        errors = character_schema.validate(json_data, partial=True)
        if errors:
            return {"message": "Validation failed", "errors": errors}, 400
        try:
            character = CharacterModel.objects.get(name=name)
            for field, value in json_data.items():
                setattr(character, field, value)
            character.save()
            return character_schema.dump(character), 200
        except DoesNotExist:
            abort(404, message=f"Character with name '{name}' not found")
        except ValidationError as e:
            return {"message": "Validation failed", "errors": str(e)}, 400


class CharacterDeleteByName(Resource):
    def delete(self, name):
        try:
            character = CharacterModel.objects.get(name=name)
            character.delete()
            return "", 204
        except DoesNotExist:
            abort(404, message=f"Character with name '{name}' not found")


class CharacterGetById(Resource):
    def get(self, id):
        try:
            character = CharacterModel.objects.get(id=id)
            return character_schema.dump(character), 200
        except DoesNotExist:
            abort(404, message=f"Character with ID '{id}' not found")


class CharacterUpdateById(Resource):
    def patch(self, id):
        json_data = request.get_json()
        for field in ["name", "affiliation", "homeworld", "species"]:
            if field in json_data and isinstance(json_data[field], str):
                json_data[field] = string.capwords(json_data[field])
        errors = character_schema.validate(json_data, partial=True)
        if errors:
            return {"message": "Validation failed", "errors": errors}, 400
        try:
            character = CharacterModel.objects.get(id=id)
            for field, value in json_data.items():
                setattr(character, field, value)
            character.save()
            return character_schema.dump(character), 200
        except DoesNotExist:
            abort(404, message=f"Character with ID '{id}' not found")
        except ValidationError as e:
            return {"message": "Validation failed", "errors": str(e)}, 400


class CharacterDeleteById(Resource):
    def delete(self, id):
        try:
            character = CharacterModel.objects.get(id=id)
            character.delete()
            return "", 204
        except DoesNotExist:
            abort(404, message=f"Character with ID '{id}' not found")


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


@app.route("/")
def home():
    return "<h1>Star Wars REST API with MongoDB and Marshmallow</h1>"


if __name__ == "__main__":
    app.run(debug=True)
