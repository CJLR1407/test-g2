"""
1. Usando los tipos de datos y sus conversiones realizar lo siguiente.
Reglas:
- Pedir por consola nombre y edad.
- Edad tiene que ser tipo entero, para esto apoyarse de la conversión de datos
- Identificar los tipos ingresados.
- Pedir los nombre para dos personales y finalmente mostrar en pantalla la suma de ambos.

"""
#USUARIO 1
print("BIENVENIDO USUARIO1")
nombreUsuario1 = input("¿cuál es tu nombre?: \n")
edadUsuario1 = int(input("¿cuál es tu edad?: \n"))

print("El tipo de dato del nombre de usuario1 es: ", type(nombreUsuario1))
print("El tipo de dato de la edad del usuario1 es: ",type(edadUsuario1))

#USUARIO 2
print("BIENVENIDO USUARIO2")
nombreUsuario2 = input("¿cuál es tu nombre?: \n")
edadUsuario2 = int(input("¿cuál es tu edad?: \n"))

print("El tipo de dato del nombre de usuario2 es: ",type(nombreUsuario2))
print("El tipo de dato de la edad del usuario2 es: ",type(edadUsuario2))

#SUMA DE EDADES DE AMBOS
suma = edadUsuario1 + edadUsuario2
print("\nLa suma de edades del usuario1 y usuario2 es: ", suma)



print("Nuevo cambio")







