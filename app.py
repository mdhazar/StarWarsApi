from flask import Flask, request
from flask_restful import Resource, Api, abort
from mongoengine import Document, StringField, connect, DoesNotExist
from marshmallow import Schema, fields

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

    def __repr__(self):
        return f"Character(name={self.name}, affiliation={self.affiliation}, homeworld={self.homeworld}, species={self.species})"


class CharacterSchema(Schema):
    id = fields.String(dump_only=True)
    name = fields.String(required=True)
    affiliation = fields.String(required=True)
    homeworld = fields.String(required=True)
    species = fields.String(required=True)


character_schema = CharacterSchema()
characters_schema = CharacterSchema(many=True)


class CharacterCollection(Resource):
    def get(self):
        characters = CharacterModel.objects()
        return characters_schema.dump(characters), 200

    def post(self):
        json_data = request.get_json()
        errors = character_schema.validate(json_data)
        if errors:
            return errors, 400
        character = CharacterModel(**json_data)
        character.save()
        return character_schema.dump(character), 201


class CharacterCollectionName(Resource):
    def get(self):
        characters = CharacterModel.objects()
        return characters_schema.dump(characters), 200


class CharacterResourceName(Resource):
    def get(self, name):
        try:
            character = CharacterModel.objects.get(name=name)
        except DoesNotExist:
            abort(404, message="Character not found")
        return character_schema.dump(character), 200

    def patch(self, name):
        json_data = request.get_json()
        try:
            character = CharacterModel.objects.get(name=name)
        except DoesNotExist:
            abort(404, message="Character not found")
        if "name" in json_data:
            character.name = json_data["name"]
        if "affiliation" in json_data:
            character.affiliation = json_data["affiliation"]
        if "homeworld" in json_data:
            character.homeworld = json_data["homeworld"]
        if "species" in json_data:
            character.species = json_data["species"]
        character.save()
        return character_schema.dump(character), 200

    def delete(self, name):
        try:
            character = CharacterModel.objects.get(name=name)
        except DoesNotExist:
            abort(404, message="Character not found")
        character.delete()
        return "", 204


class CharacterResourceId(Resource):

    def get(self, id):
        try:
            character = CharacterModel.objects.get(id=id)
        except DoesNotExist:
            abort(404, message="Character not found")
        return character_schema.dump(character), 200

    def patch(self, id):
        json_data = request.get_json()
        try:
            character = CharacterModel.objects.get(id=id)
        except DoesNotExist:
            abort(404, message="Character not found")
        if "name" in json_data:
            character.name = json_data["name"]
        if "affiliation" in json_data:
            character.affiliation = json_data["affiliation"]
        if "homeworld" in json_data:
            character.homeworld = json_data["homeworld"]
        if "species" in json_data:
            character.species = json_data["species"]
        character.save()
        return character_schema.dump(character), 200

    def delete(self, id):
        try:
            character = CharacterModel.objects.get(id=id)
        except DoesNotExist:
            abort(404, message="Character not found")
        character.delete()
        return "", 204


api.add_resource(CharacterResourceName, "/api/characters/<string:name>")
api.add_resource(CharacterResourceId, "/api/characters/id/<string:id>")
api.add_resource(CharacterCollection, "/api/characters")
api.add_resource(CharacterCollectionName, "/api/characters/name")


@app.route("/")
def home():
    return "<h1>Star Wars REST API with MongoDB and Marshmallow</h1>"


if __name__ == "__main__":
    app.run(debug=True)
