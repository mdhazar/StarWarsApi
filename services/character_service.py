import string


class CharacterService:
    @staticmethod
    def capitalize_fields(data):
        for field in ["name", "affiliation", "homeworld", "species"]:
            if field in data and isinstance(data[field], str):
                data[field] = string.capwords(data[field])
        return data
