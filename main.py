import requests
import json

counter=1
pokemonNamesList=[]
pokemonDict={}
apiAdr="https://pokeapi.co/api/v2"
pokemonAdr="pokemon"
pokeLim=25
r = requests.get(apiAdr+"/"+pokemonAdr+"?limit="+str(pokeLim))
jr = r.json()

for i in jr['results']:
    pokemonNamesList.append(i['name'])

#print(pokemonNamesDict)

for i in pokemonNamesList:
    r = requests.get(apiAdr+"/"+pokemonAdr+"/"+i)
    #jr = r.json().keys()
    jr = r.json()
    pokemonDict[i] = [jr.get('id'), jr.get('height'), jr.get('is_default')]

print('Who is the highest?')
for name in pokemonNamesList:
    print(str(counter)+')'+ ' ' +name)
    counter += 1

#input()

# print(pokemonDict.items())
    