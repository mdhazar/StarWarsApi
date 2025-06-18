from app import CharacterModel, CharacterSchema


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
]
for character in characters:
    errors = CharacterSchema().validate(character)
    if errors:
        print(f"Validation error for {character['name']}: {errors}")
        continue
    if not CharacterModel.objects(name=character["name"]):
        CharacterModel(**character).save()

print("Dummy users inserted.")
