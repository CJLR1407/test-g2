
"""Manejo de excepciones"""

"""Manejo del error de división entre cero y tipo de datos"""
"""Multiples excepts en una sola linea"""

try:
    val1 = 5/0
    #val2 = 2 + "Hola Pythonistas"
except (ZeroDivisionError, TypeError):
    print("Excepcion división entre cero/TypeError")
