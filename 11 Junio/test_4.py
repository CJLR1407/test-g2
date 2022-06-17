
"""Manejo de archivos"""

tecnologiasBackend = ["\nPython", "\nJava", "\nRuby", "\nNodeJS"]
tecnologiasFrontend = ["\nAngular", "\nJavascript", "\nReactJS", "\nBoostrap"]

"""Apertura de nuestro archivo"""

"""a+: Permite escribir varias lineas de codigo al abrir nuestro archivo"""
"""a+: Escribe lineas de texto sin borrar las lineas que ya estaban escritas previamente en el archivo"""
file = open("my_files/file2.txt", "a+")

"""writeLines: Permite escribir los datos de una lista """
file.writelines(tecnologiasBackend)

file.writelines(tecnologiasFrontend)

file = open("my_files/file2.txt", "r")

print("El contenido de nuestro file2 es: ", file.read())

"""Cierre del archivo"""
file.close()

