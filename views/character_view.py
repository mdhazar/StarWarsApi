from flask_restful import Resource
from controllers.character_controller import CharacterController
from flask import request


class CharacterList(Resource):
    def get(self):
        return CharacterController.get_all_characters()


class CharacterCollectionName(Resource):
    def get(self):
        return CharacterController.get_character_names()


class CharacterCollectionAffiliation(Resource):
    def get(self):
        return CharacterController.get_character_affiliations()


class CharacterCollectionSpecies(Resource):
    def get(self):
        return CharacterController.get_character_species()


class CharacterCollectionHomeworld(Resource):
    def get(self):
        return CharacterController.get_character_homeworlds()


class CharacterCreate(Resource):
    def post(self):
        return CharacterController.create_character(request.get_json())


class CharacterGetByName(Resource):
    def get(self, name):
        return CharacterController.get_character_by_name(name)


class CharacterUpdateByName(Resource):
    def patch(self, name):
        return CharacterController.update_character_by_name(name, request.get_json())


class CharacterDeleteByName(Resource):
    def delete(self, name):
        return CharacterController.delete_character_by_name(name)


class CharacterGetById(Resource):
    def get(self, id):
        return CharacterController.get_character_by_id(id)


class CharacterUpdateById(Resource):
    def patch(self, id):
        return CharacterController.update_character_by_id(id, request.get_json())


class CharacterDeleteById(Resource):
    def delete(self, id):
        return CharacterController.delete_character_by_id(id)


class CharacterDeleteAll(Resource):
    def delete(self):
        return CharacterController.delete_all_characters()
