
"""Manejo de caracteres"""
"""Encontrar el indice inicial de una cadena dentro de una cadena mayor"""

nombre = input("Ingrese su nombre: ")
mensaje = "Bienvenido {}".format(nombre)

indice = mensaje.find(nombre)
print("El indice que empieza nuestra sub cadena en la cadena mayor es: ", indice)

mensaje2 = "{}{}{}".format(mensaje[0:indice], ": ", nombre)

print("{}".format(mensaje2))




