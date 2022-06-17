
"""Manejo de excepciones"""

"""Manejo del type para saber qué tipo de error ha ocurrido"""

try:
    val1 = 2 + "Hola Pythonistas"
except Exception as ex:
    print("Ha ocurrido una excepcion: ", type(ex))

