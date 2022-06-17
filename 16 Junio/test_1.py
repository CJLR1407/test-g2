
"""Decoradores en Python"""

"""Creación de función decoradora"""

def funcionA(funcionB):
    """Funcion interna de la funcion decoradora"""
    def funcionC():
        print("Antes de ejecutar la funcion a decorar")
        funcionB()
        print("Después de ejecutar la función a decorar")

    return funcionC()

"""Funcion a decorar"""
#@funcionA
def saludar(nombre):
    return print("Hola {}".format(nombre))

saludo = input("Ingrese su nombre: ")
print(saludar(saludo))



