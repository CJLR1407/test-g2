"""
3. Teniendo presente el uso y concepto de diccionarios en Python, realizar un programa con los siguientes requerimientos
Reglas:
- Crear una diccionario con los keys de nombre, apellidos, edad y dni.
- Pedir por consola los valores para estos keys.
- Convertir el diccionario a una lista y mostrar en pantalla el tipo de dato.
- Agregar un key adicional con el nombre de “profesion”
- Eliminar el key dni y mostrar el nuevo diccionario.
"""

nombreUsuario = input("¿cuál es tu nombre?: \n")
apellidoUsuario = input("¿cuál es tu apellido?: \n")
edadUsuario = int(input("¿cuál es tu edad?: \n"))
dniUsuario = input("¿cuál es tu DNI?: \n")

varDiccionario = {'Nombre': nombreUsuario, 'Apellido': apellidoUsuario, 'Edad': edadUsuario, 'DNI': dniUsuario }

miLista = list(varDiccionario.values())
print("Mi diccionario convertido a lista es: ",miLista)
print("El tipo de dato de mi lista es: ", type(miLista))

print("se agregó mi profesion")
varDiccionario['profesion']="Ingeniero de Sistemas"
print(varDiccionario)

#borrar el key dni
del varDiccionario["DNI"]
print("Se borro dni")
print("Mi diccionario final es: ", varDiccionario)







