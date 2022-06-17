
"""Manejo de archivos"""

def fileManipulation(dir, mode):


    try:
        file = open(dir, mode)
        print(file.read())
        file.close()
        return file
    except OSError as err: #Tipo de error de apertura de archivo
        print("Error de lectura \n{}".format(err))


fileWrite = "my_files/file2.txt"

print("Lectura de un archivo")
fileManipulation(fileWrite, "r")

fileWrite2 = "my_files/append.txt"
fileManipulation(fileWrite2, "r")



