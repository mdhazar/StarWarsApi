from models.character import CharacterModel, character_schema, characters_schema
from mongoengine import DoesNotExist, ValidationError
import string


class CharacterController:
    @staticmethod
    def get_all_characters():
        return characters_schema.dump(CharacterModel.objects()), 200

    @staticmethod
    def get_character_names():
        characters = CharacterModel.objects().only("name")
        return {"names": [c.name for c in characters]}, 200

    @staticmethod
    def get_character_affiliations():
        characters = CharacterModel.objects().only("name", "affiliation")
        affiliation_dict = {}
        for character in characters:
            if character.affiliation not in affiliation_dict:
                affiliation_dict[character.affiliation] = []
            affiliation_dict[character.affiliation].append(character.name)
        return {"affiliations": affiliation_dict}, 200

    @staticmethod
    def get_character_species():
        characters = CharacterModel.objects().only("name", "species")
        species_dict = {}
        for character in characters:
            if character.species not in species_dict:
                species_dict[character.species] = []
            species_dict[character.species].append(character.name)
        return {"species": species_dict}, 200

    @staticmethod
    def get_character_homeworlds():
        characters = CharacterModel.objects().only("name", "homeworld", "species")
        homeworld_dict = {}
        for character in characters:
            if character.homeworld not in homeworld_dict:
                homeworld_dict[character.homeworld] = []
            homeworld_dict[character.homeworld].append(
                {"name": character.name, "species": character.species}
            )
        return {"homeworld": homeworld_dict}, 200

    @staticmethod
    def create_character(data):
        for field in ["name", "affiliation", "homeworld", "species"]:
            if field in data and isinstance(data[field], str):
                data[field] = string.capwords(data[field])
        errors = character_schema.validate(data)
        if errors:
            return {"message": "Validation failed", "errors": errors}, 400
        try:
            CharacterModel(**data).save()
            return character_schema.dump(CharacterModel(**data)), 201
        except ValidationError as e:
            return {"message": "Validation failed", "errors": str(e)}, 400

    @staticmethod
    def get_character_by_name(name):
        try:
            return character_schema.dump(CharacterModel.objects.get(name=name)), 200
        except DoesNotExist:
            return {"message": f"Character with name '{name}' not found"}, 404

    @staticmethod
    def update_character_by_name(name, data):
        for field in ["name", "affiliation", "homeworld", "species"]:
            if field in data and isinstance(data[field], str):
                data[field] = string.capwords(data[field])
        errors = character_schema.validate(data, partial=True)
        if errors:
            return {"message": "Validation failed", "errors": errors}, 400
        try:
            character = CharacterModel.objects.get(name=name)
            for field, value in data.items():
                setattr(character, field, value)
            character.save()
            return character_schema.dump(character), 200
        except DoesNotExist:
            return {"message": f"Character with name '{name}' not found"}, 404
        except ValidationError as e:
            return {"message": "Validation failed", "errors": str(e)}, 400

    @staticmethod
    def update_character_by_id(id, data):
        for field in ["name", "affiliation", "homeworld", "species"]:
            if field in data and isinstance(data[field], str):
                data[field] = string.capwords(data[field])
        errors = character_schema.validate(data, partial=True)
        if errors:
            return {"message": "Validation failed", "errors": errors}, 400
        try:
            character = CharacterModel.objects.get(id=id)
            for field, value in data.items():
                setattr(character, field, value)
            character.save()
            return character_schema.dump(character), 200
        except DoesNotExist:
            return {"message": f"Character with ID '{id}' not found"}, 404
        except ValidationError as e:
            return {"message": "Validation failed", "errors": str(e)}, 400

    @staticmethod
    def delete_character_by_name(name):
        try:
            CharacterModel.objects.get(name=name).delete()
            return "", 204
        except DoesNotExist:
            return {"message": f"Character with name '{name}' not found"}, 404

    @staticmethod
    def get_character_by_id(id):
        try:
            return character_schema.dump(CharacterModel.objects.get(id=id)), 200
        except DoesNotExist:
            return {"message": f"Character with ID '{id}' not found"}, 404

    @staticmethod
    def delete_character_by_id(id):
        try:
            CharacterModel.objects.get(id=id).delete()
            return "", 204
        except DoesNotExist:
            return {"message": f"Character with ID '{id}' not found"}, 404

    @staticmethod
    def delete_all_characters():
        try:
            CharacterModel.objects.delete()
            return {"message": "All characters deleted successfully"}, 200
        except Exception as e:
            return {"message": "An error occurred", "error": str(e)}, 500
