"""
2. Usando el concepto y funciones de lista, realizar un programa con las siguiente características:
Reglas:
- Crear una lista con 10 valores random o alatorios
- Llenar otra lista con sus cubos.
- Llenar una lista nueva con sus cuadrados.
- Mostrar de manera inversa la suma de ambas listas.
"""
#lista con 10 numeros aleatorios
import random
listaNumeros = []

for indice in range(1,11):
    listaNumeros.append(random.randint(1,20))
print("\nMi lista inicial de 10 numeros aleatorios")
print(listaNumeros)

#nueva lista con los cubos de la lista inicial
listaCubos = []
for num in listaNumeros:
    listaCubos.append(num**3)
print("\nMi lista con los cubos de la lista inicial")
print(listaCubos)

#nueva lista con los cuadrados de la lista inicial
listaCuadrados = []
for num2 in listaNumeros:
    listaCuadrados.append(num2**2)
print("\nMi lista con los cuadrados de la lista inicial")
print(listaCuadrados)


#inversa de la suma de la lista de cuadrados y cubos

sumaLista =[0,0,0,0,0,0,0,0,0,0]
for i in range (0,10):
    sumaLista[i]  = listaCuadrados[i] + listaCubos[i]
print("\nMi lista con la suma de los cuadrados y cubos ")
print(sumaLista)


sumaLista.reverse()
print("Mi lista invertida es: ", sumaLista)
