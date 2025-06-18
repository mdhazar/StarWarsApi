from models.character import CharacterModel, CharacterSchema


characters = [
    {
        "id": "6852c2017e3ec8f15995f01c",
        "name": "Palpatine",
        "affiliation": "Galactic Empire",
        "homeworld": "Naboo",
        "species": "Human",
        "image": "https://static.wikia.nocookie.net/starwars/images/d/d8/Emperor_Sidious.png",
    },
    {
        "id": "6852c2017e3ec8f15995f01d",
        "name": "Darth Vader",
        "affiliation": "Galactic Empire",
        "homeworld": "Tatooine",
        "species": "Human (Cyborg)",
        "image": "https://static.wikia.nocookie.net/starwars/images/9/94/Vaderrotj.jpg",
    },
    {
        "id": "6852c2017e3ec8f15995f01e",
        "name": "Grand Moff Tarkin",
        "affiliation": "Galactic Empire",
        "homeworld": "Eriadu",
        "species": "Human",
        "image": "https://static.wikia.nocookie.net/starwars/images/c/c1/Tarkininfobox.jpg",
    },
    {
        "id": "6852c2017e3ec8f15995f01f",
        "name": "Orson Callan Krennic",
        "affiliation": "Galactic Empire",
        "homeworld": "Lexrul",
        "species": "Human",
        "image": "https://static.wikia.nocookie.net/starwars/images/0/05/OrsonKrennic-SWI171.png",
    },
    {
        "id": "6852c2017e3ec8f15995f020",
        "name": "Firmus Piett",
        "affiliation": "Galactic Empire",
        "homeworld": "Axxila",
        "species": "Human",
        "image": "https://static.wikia.nocookie.net/starwars/images/1/13/FirusPiett-CGSWG.png/revision/latest?cb=20241127051016",
    },
    {
        "id": "6852c2017e3ec8f15995f021",
        "name": "Leia Organa",
        "affiliation": "New Republic",
        "homeworld": "Alderaan",
        "species": "Human",
        "image": "https://static.wikia.nocookie.net/starwars/images/9/9b/Princessleiaheadwithgun.jpg/revision/latest?cb=20240522043127",
    },
    {
        "id": "6852c2017e3ec8f15995f022",
        "name": "Mon Mothma",
        "affiliation": "New Republic",
        "homeworld": "Chandrila",
        "species": "Human",
        "image": "https://static.wikia.nocookie.net/starwars/images/2/22/Mon_Mothma_Ahsoka_poster.png/revision/latest?cb=20230904071259",
    },
    {
        "id": "6852c2017e3ec8f15995f023",
        "name": "Gial Ackbar",
        "affiliation": "New Republic",
        "homeworld": "Mon Cala",
        "species": "Mon Calamari",
        "image": "https://static.wikia.nocookie.net/starwars/images/2/29/Admiral_Ackbar_RH.png/revision/latest?cb=20221224032123",
    },
    {
        "id": "6852c2017e3ec8f15995f024",
        "name": "Wedge Antilles",
        "affiliation": "New Republic",
        "homeworld": "Corellia",
        "species": "Human",
        "image": "https://static.wikia.nocookie.net/starwars/images/7/7e/WedgesEntireHead-ROTJ.png",
    },
    {
        "id": "6852c2017e3ec8f15995f025",
        "name": "Hera Syndulla",
        "affiliation": "New Republic",
        "homeworld": "Ryloth",
        "species": "Twi'lek",
        "image": "https://static.wikia.nocookie.net/starwars/images/4/46/Hera_Syndulla-AG.png",
    },
    {
        "id": "68531674aa03eb8c43d54627",
        "name": "Boba Fett",
        "affiliation": "Galactic Empire",
        "homeworld": "Kamino",
        "species": "Human",
        "image": "https://vignette.wikia.nocookie.net/starwars/images/7/79/Boba_Fett_HS_Fathead.png",
    },
    {
        "id": "685320346a096adcc211cdf7",
        "name": "Jango Fett",
        "affiliation": "Galactic Empire",
        "homeworld": "Concord Dawn",
        "species": "Human",
        "image": "https://vignette.wikia.nocookie.net/starwars/images/5/56/JangoInfobox.png",
    },
    {
        "id": "68532282e49ac91d0c0afc69",
        "name": "Padme Amidala",
        "affiliation": "New Republic",
        "homeworld": "Naboo",
        "species": "Human",
        "image": "https://static.wikia.nocookie.net/starwars/images/8/8a/Padme32BBY.png",
    },
    {
        "id": "685322b6e49ac91d0c0afc6a",
        "name": "Luke Skywalker",
        "affiliation": "New Republic",
        "homeworld": "Tatooine",
        "species": "Human",
        "image": "https://vignette.wikia.nocookie.net/starwars/images/2/20/LukeTLJ.jpg",
    },
    {
        "id": "685322dce49ac91d0c0afc6b",
        "name": "C-3po",
        "affiliation": "New Republic",
        "homeworld": "Tatooine",
        "species": "Droid",
        "image": "https://vignette.wikia.nocookie.net/starwars/images/3/3f/C-3PO_TLJ_Card_Trader_Award_Card.png",
    },
    {
        "id": "685322f9e49ac91d0c0afc6c",
        "name": "R2-d2",
        "affiliation": "New Republic",
        "homeworld": "Naboo",
        "species": "Droid",
        "image": "https://vignette.wikia.nocookie.net/starwars/images/e/eb/ArtooTFA2-Fathead.png",
    },
    {
        "id": "6853266ae49ac91d0c0afc6d",
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
