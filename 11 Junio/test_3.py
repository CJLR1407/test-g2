
"""Manejo de archivos"""

"""w: Abre el archivo para poder escribir sobre el"""
file = open("my_files/file.txt", "w")

file.write("\nLenguaje multiplataforma: Python")
file.write("\nEstá basado en POO")
file.write("\nBasado en diferentes paradigmas de programación")

file = open("my_files/file.txt", "r")

print("Nuestro file tiene el siguiente contenido: ", file.read())

"""Cierre del archivo"""
file.close()
