import pymongo,json
import requests


########################################################################
#    CONFIG MONGODB
########################################################################
client = pymongo.MongoClient("mongodb://root:1234@localhost:27018/")

# Check the connection
try:
    client.server_info()
    print("Connected to MongoDB")
except pymongo.errors.ServerSelectionTimeoutError as err:
    print(f"Unable to connect to MongoDB: {err}")

db = client["JDG"]
collection = db["pokemon"]

########################################################################
#    RECUPERATION DES POKEMONS ET STOCKAGE DANS MONGODB
########################################################################

pokemon= requests.get("https://pokebuildapi.fr/api/v1/pokemon")
pokemon = pokemon.json()
collection.insert_many(pokemon)

########################################################################
#    AJOUT D UN POKEMON
########################################################################

new={ "id": 899, "pokedexId": 899, "name": "Darty Papa",
 "image": "https://tenor.com/fr/view/kassos-darty-papa-gif-5752923", 
 "videoYoutube": "https://www.youtube.com/watch?v=Gt5-xU1-Ows", 
 "slug": "Darty Papa", "stats": { "HP": 100000000, "attack": 100000000, 
 "defense": 2, "special\_attack": 100000000, "special\_defense": 2, "speed": 1 }
}
collection.insert_one(new)

########################################################################
#    RECUPERATION DE LA BASE DE DONNES EN FICHIER JSON
########################################################################

docs = list(collection.find({}, {"_id": False}))
with open("database.json", "w") as file:
    json.dump(docs, file)


