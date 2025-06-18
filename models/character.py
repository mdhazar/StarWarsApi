from mongoengine import Document, StringField
from marshmallow import Schema, fields, validate


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
