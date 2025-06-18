from marshmallow import Schema, fields, validate


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
