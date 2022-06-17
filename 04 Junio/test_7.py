
"""
5. Solicitar al usuario un numero entero y luego un digito. Informar la cantidad de ocurrencias
del digito en el numero (en ultimo lugar del numero), utilizando una funcion que calcule la frecuencia.
"""

def frecuencia(numero, digito):
    cantidad = 0
    while numero != 0:
        ultimoDigito = numero % 10
        if ultimoDigito == digito:
            cantidad = cantidad + 1
        numero = int(numero / 10)
    return cantidad

num = int(input("Ingrese un numero: "))
dig = int(input("Ingrese digito a encontrar en el numero: "))
print("La cantidad de veces que hay el digito {} en el numero {} es: {}".format(dig,num,frecuencia(num,dig)))




