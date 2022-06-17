
"""Uso de la libreria JSON para tratar tipos de datos JSON"""

import json

"""Creando nuestra variable con un tipo de Dato JSON"""
jsonData = '{"nombre": "Python", "tipo": "Backend", "paradigma": "POO"}'

"""Convertirlo a  un dato manejable para Python: loads()"""
jsonToPython = json.loads(jsonData)
print("Nuestro dato tipo JSON a dato para Python: ", jsonToPython)
print("El tipo de dato de nuestra variable es: ", type(jsonToPython))



