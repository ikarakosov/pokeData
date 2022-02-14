import requests
import json


pokemonNamesDict=[]
apiAdr="https://pokeapi.co/api/v2"
pokemonAdr="pokemon"
pokeLim=1
r = requests.get(apiAdr+"/"+pokemonAdr+"?limit="+str(pokeLim))
jr = r.json()

for i in jr['results']:
    pokemonNamesDict.append(i['name'])


for i in pokemonNamesDict:
    r = requests.get(apiAdr+"/"+pokemonAdr+"/"+i)
    jr = r.json()
    print(jr)