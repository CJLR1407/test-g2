
"""Uso de la libreria fechas y tiempos"""
"""Comparacion de fechas"""

import datetime

fecha1 = datetime.datetime(2014, 3, 13) #Tipos de dato datetime
fecha2 = datetime.datetime(2014, 4, 15) #Tipos de dato datetime

if fecha1 == fecha2:
    print("Nacieron el mismo dia")
elif fecha1 < fecha2:
    print("El niño 1 es mayor que el niño 2")
else:
    print("El niño 2 es mayor que el niño 1")
