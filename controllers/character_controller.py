from models.character_schema import character_schema, characters_schema
from repositories.character_repository import CharacterRepository
from services.character_service import CharacterService
from mongoengine import ValidationError


class CharacterController:
    @staticmethod
    def get_all_characters():
        characters = CharacterRepository.get_all()
        return characters_schema.dump(characters), 200

    @staticmethod
    def get_character_names():
        characters = CharacterRepository.get_all_names()
        return {"names": [c.name for c in characters]}, 200

    @staticmethod
    def get_character_affiliations():
        characters = CharacterRepository.get_all_affiliations()
        affiliation_dict = {}
        for character in characters:
            if character.affiliation not in affiliation_dict:
                affiliation_dict[character.affiliation] = []
            affiliation_dict[character.affiliation].append(character.name)
        return {"affiliations": affiliation_dict}, 200

    @staticmethod
    def get_character_species():
        characters = CharacterRepository.get_all_species()
        species_dict = {}
        for character in characters:
            if character.species not in species_dict:
                species_dict[character.species] = []
            species_dict[character.species].append(character.name)
        return {"species": species_dict}, 200

    @staticmethod
    def get_character_homeworlds():
        characters = CharacterRepository.get_all_homeworlds()
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
        data = CharacterService.capitalize_fields(data)
        errors = character_schema.validate(data)
        if errors:
            return {"message": "Validation failed", "errors": errors}, 400
        try:
            character = CharacterRepository.create(data)
            return character_schema.dump(character), 201
        except ValidationError as e:
            return {"message": "Validation failed", "errors": str(e)}, 400

    @staticmethod
    def get_character_by_name(name):
        character = CharacterRepository.get_by_name(name)
        if character:
            return character_schema.dump(character), 200
        return {"message": f"Character with name '{name}' not found"}, 404

    @staticmethod
    def update_character_by_name(name, data):
        data = CharacterService.capitalize_fields(data)
        errors = character_schema.validate(data, partial=True)
        if errors:
            return {"message": "Validation failed", "errors": errors}, 400
        character = CharacterRepository.get_by_name(name)
        if not character:
            return {"message": f"Character with name '{name}' not found"}, 404
        try:
            updated_character = CharacterRepository.update(character, data)
            return character_schema.dump(updated_character), 200
        except ValidationError as e:
            return {"message": "Validation failed", "errors": str(e)}, 400

    @staticmethod
    def delete_character_by_name(name):
        character = CharacterRepository.get_by_name(name)
        if character:
            CharacterRepository.delete(character)
            return "", 204
        return {"message": f"Character with name '{name}' not found"}, 404

    @staticmethod
    def get_character_by_id(id):
        character = CharacterRepository.get_by_id(id)
        if character:
            return character_schema.dump(character), 200
        return {"message": f"Character with ID '{id}' not found"}, 404

    @staticmethod
    def update_character_by_id(id, data):
        data = CharacterService.capitalize_fields(data)
        errors = character_schema.validate(data, partial=True)
        if errors:
            return {"message": "Validation failed", "errors": errors}, 400
        character = CharacterRepository.get_by_id(id)
        if not character:
            return {"message": f"Character with ID '{id}' not found"}, 404
        try:
            updated_character = CharacterRepository.update(character, data)
            return character_schema.dump(updated_character), 200
        except ValidationError as e:
            return {"message": "Validation failed", "errors": str(e)}, 400

    @staticmethod
    def delete_character_by_id(id):
        character = CharacterRepository.get_by_id(id)
        if character:
            CharacterRepository.delete(character)
            return "", 204
        return {"message": f"Character with ID '{id}' not found"}, 404
