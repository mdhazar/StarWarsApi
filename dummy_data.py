from models.character_model import CharacterModel
from models.character_schema import CharacterSchema
from mongoengine import connect
from config import Config

connect(
    db=Config.MONGODB_SETTINGS["db"],
    host=Config.MONGODB_SETTINGS["host"],
    port=Config.MONGODB_SETTINGS["port"],
)


characters = [
    {
        "name": "Palpatine",
        "affiliation": "Galactic Empire",
        "homeworld": "Naboo",
        "species": "Human",
        "image": "https://static.wikia.nocookie.net/starwars/images/d/d8/Emperor_Sidious.png",
    },
    {
        "name": "Darth Vader",
        "affiliation": "Galactic Empire",
        "homeworld": "Tatooine",
        "species": "Human (Cyborg)",
        "image": "https://static.wikia.nocookie.net/starwars/images/9/94/Vaderrotj.jpg",
    },
    {
        "name": "Grand Moff Tarkin",
        "affiliation": "Galactic Empire",
        "homeworld": "Eriadu",
        "species": "Human",
        "image": "https://static.wikia.nocookie.net/starwars/images/c/c1/Tarkininfobox.jpg",
    },
    {
        "name": "Orson Callan Krennic",
        "affiliation": "Galactic Empire",
        "homeworld": "Lexrul",
        "species": "Human",
        "image": "https://static.wikia.nocookie.net/starwars/images/0/05/OrsonKrennic-SWI171.png",
    },
    {
        "name": "Firmus Piett",
        "affiliation": "Galactic Empire",
        "homeworld": "Axxila",
        "species": "Human",
        "image": "https://static.wikia.nocookie.net/starwars/images/1/13/FirusPiett-CGSWG.png/revision/latest?cb=20241127051016",
    },
    {
        "name": "Leia Organa",
        "affiliation": "New Republic",
        "homeworld": "Alderaan",
        "species": "Human",
        "image": "https://static.wikia.nocookie.net/starwars/images/9/9b/Princessleiaheadwithgun.jpg/revision/latest?cb=20240522043127",
    },
    {
        "name": "Mon Mothma",
        "affiliation": "New Republic",
        "homeworld": "Chandrila",
        "species": "Human",
        "image": "https://static.wikia.nocookie.net/starwars/images/2/22/Mon_Mothma_Ahsoka_poster.png/revision/latest?cb=20230904071259",
    },
    {
        "name": "Gial Ackbar",
        "affiliation": "New Republic",
        "homeworld": "Mon Cala",
        "species": "Mon Calamari",
        "image": "https://static.wikia.nocookie.net/starwars/images/2/29/Admiral_Ackbar_RH.png/revision/latest?cb=20221224032123",
    },
    {
        "name": "Wedge Antilles",
        "affiliation": "New Republic",
        "homeworld": "Corellia",
        "species": "Human",
        "image": "https://static.wikia.nocookie.net/starwars/images/7/7e/WedgesEntireHead-ROTJ.png",
    },
    {
        "name": "Hera Syndulla",
        "affiliation": "New Republic",
        "homeworld": "Ryloth",
        "species": "Twi'lek",
        "image": "https://static.wikia.nocookie.net/starwars/images/4/46/Hera_Syndulla-AG.png",
    },
    {
        "name": "Boba Fett",
        "affiliation": "Galactic Empire",
        "homeworld": "Kamino",
        "species": "Human",
        "image": "https://vignette.wikia.nocookie.net/starwars/images/7/79/Boba_Fett_HS_Fathead.png",
    },
    {
        "name": "Jango Fett",
        "affiliation": "Galactic Empire",
        "homeworld": "Concord Dawn",
        "species": "Human",
        "image": "https://vignette.wikia.nocookie.net/starwars/images/5/56/JangoInfobox.png",
    },
    {
        "name": "Padme Amidala",
        "affiliation": "New Republic",
        "homeworld": "Naboo",
        "species": "Human",
        "image": "https://static.wikia.nocookie.net/starwars/images/8/8a/Padme32BBY.png",
    },
    {
        "name": "Luke Skywalker",
        "affiliation": "New Republic",
        "homeworld": "Tatooine",
        "species": "Human",
        "image": "https://vignette.wikia.nocookie.net/starwars/images/2/20/LukeTLJ.jpg",
    },
    {
        "name": "C-3po",
        "affiliation": "New Republic",
        "homeworld": "Tatooine",
        "species": "Droid",
        "image": "https://vignette.wikia.nocookie.net/starwars/images/3/3f/C-3PO_TLJ_Card_Trader_Award_Card.png",
    },
    {
        "name": "R2-d2",
        "affiliation": "New Republic",
        "homeworld": "Naboo",
        "species": "Droid",
        "image": "https://vignette.wikia.nocookie.net/starwars/images/e/eb/ArtooTFA2-Fathead.png",
    },
    {
        "name": "Jar Jar Binks",
        "affiliation": "New Republic",
        "homeworld": "Naboo",
        "species": "Gungan",
        "image": "https://vignette.wikia.nocookie.net/starwars/images/d/d2/Jar_Jar_aotc.jpg",
    },
]
for character in characters:
    errors = CharacterSchema().validate(character)
    if errors:
        print(f"Validation error for {character['name']}: {errors}")
        continue
    if not CharacterModel.objects(name=character["name"]):
        CharacterModel(**character).save()

print("Dummy users inserted.")
