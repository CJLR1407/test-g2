
import requests

"""Lectura de un API el cual nos va a traer un JSON"""

res = requests.get("http://pokeapi.co/api/v2/pokemon/charizard")

print(res.status_code)
print(res.headers)
#json = res.json()
print(res.json())