import requests
import json

#takes a string
def request(request):
    response = requests.get("https://pokeapi.co/api/v2/pokemon/"+request)
    return response.text