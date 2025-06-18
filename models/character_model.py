from mongoengine import Document, StringField


class CharacterModel(Document):
    name = StringField(required=True, unique=True, max_length=80)
    affiliation = StringField(required=True, max_length=80)
    homeworld = StringField(required=True, max_length=80)
    species = StringField(required=True, max_length=80)
    image = StringField(required=False, max_length=500)

    def __repr__(self):
        return f"Character(name={self.name})"
