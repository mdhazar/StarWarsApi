from models.character_model import CharacterModel
from mongoengine import DoesNotExist


class CharacterRepository:
    @staticmethod
    def get_all():
        return CharacterModel.objects()

    @staticmethod
    def get_all_names():
        return CharacterModel.objects().only("name")

    @staticmethod
    def get_all_affiliations():
        return CharacterModel.objects().only("name", "affiliation")

    @staticmethod
    def get_all_species():
        return CharacterModel.objects().only("name", "species")

    @staticmethod
    def get_all_homeworlds():
        return CharacterModel.objects().only("name", "homeworld", "species")

    @staticmethod
    def create(data):
        character = CharacterModel(**data)
        character.save()
        return character

    @staticmethod
    def get_by_name(name):
        try:
            return CharacterModel.objects.get(name=name)
        except DoesNotExist:
            return None

    @staticmethod
    def get_by_id(id):
        try:
            return CharacterModel.objects.get(id=id)
        except DoesNotExist:
            return None

    @staticmethod
    def update(character, data):
        for field, value in data.items():
            setattr(character, field, value)
        character.save()
        return character

    @staticmethod
    def delete(character):
        character.delete()
