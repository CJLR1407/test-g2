
"""Manejo de excepciones"""

"""Manejo del error de división entre cero"""

try:
    #val1 = 5/0
    val2 = 2 + "Hola Pythonistas"
except ZeroDivisionError:
    print("No es posible dividir entre cero!!!")
except TypeError:
    print("Problema de tipos de datos!!!")



