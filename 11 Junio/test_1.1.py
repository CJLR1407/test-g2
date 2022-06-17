
import json

"""Uso de libreria JSON"""
"""Conversion inversa de tipo de dato Python a JSON"""

pythonDict = {"name": "Harry", "edad": 27, "dni": "12345678"}

"""Conversion de tipo de dato JSON: """

dictToJson = json.dumps(pythonDict)
print("El dato convertido a JSON es el siguiente: ", dictToJson)
print("El tipo de dato convertido es de tipo: ", type(dictToJson))

