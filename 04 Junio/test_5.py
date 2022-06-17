
"""
3. Pedir numero al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de
sus digitos. Al finalizar, mostrar la sumatoria de todos los numeros ingresados y la suma
de sus digitos. Reutilizar la misma funcion realiza en el ejercicio 2.
"""

def sumarDigitos(numero):
    suma = 0
    while numero != 0:
        digito = numero % 10
        suma = suma + digito
        numero = int(numero / 10)
    return suma

sumatoria = 0

num = int(input("Ingrese numero a procesar: "))

while num != 0:
    print("La suma es: ", sumarDigitos(num))
    sumatoria = sumatoria + num
    num = int(input("Ingrese numero a procesar: "))

print("Sumatoria final es: ", sumatoria)
print("Suma de digitos es: ", sumarDigitos(sumatoria))

