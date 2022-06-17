
"""
4. Requerir al usuario que ingrese un numero entero e informar si es primo o no,
utilizando una funcion booleana que lo decida.
"""

def primo(numero):
    for i in range(2,numero):
        if numero % i == 0:
            return False
    return True

num = int(input("Ingrese numero a evaluar: "))

if primo(num):
    print("El numero {} es primo".format(num))
else:
    print("El numero {} no es primo".format(num))



