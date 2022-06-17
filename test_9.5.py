
"""Manejo de cadenas"""

cadena = "Conexion a base de datos con Python"

cadena2 = cadena.replace(cadena[0],"CCCCC")
print("Cadena con reemplazos tiene el siguiente valor: {}".format(cadena2))

"""Eliminando espacios en blanco de mi cadena"""

cadena3 = "       Conexion a base de datos con Python"
cadena4 = cadena3.lstrip()
print("Mi cadena con espacios eleiminados: {}".format(cadena4))



cadena5 = "                Conexion a base de datos con Python                 "
cadena6 = cadena5.rstrip()
print("Mi cadena con espacios eleiminados: {}".format(cadena6))



