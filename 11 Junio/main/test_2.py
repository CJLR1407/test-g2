
"""Manejo de archivos"""
"""Apertura y lectura de archivos"""

"""r: Abre el archivo en modo de lectura archivo"""
file = open("../my_files/file.txt", "r")

"""read(): Nos ayuda a leer el contenido de un archivo"""
print("Contenido de nuestro archivo: ", file.read())

# Siempre tenemos que cerrar el archivo que hemos abierto al inicio

file.close()



