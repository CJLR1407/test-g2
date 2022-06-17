
"""Manejo de archivos"""

tecnologiasBackend = ["\nPython", "\nJava"]

file = open("my_files/file3.txt", "a+")

file.writelines(tecnologiasBackend)

file = open("my_files/file3.txt", "r")

for newLine in file:
    if newLine.find("M"):
        print(newLine)
        print("Ha encontrado un varon")

"""Cerrar el archivo aperturado"""
file.close()



