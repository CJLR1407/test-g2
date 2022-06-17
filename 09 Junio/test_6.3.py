
"""Uso de la libreria fechas y tiempos"""
"""Conversion total del tiempo"""

from datetime import  datetime

"""Uso del timestamp"""
timeNow = datetime.strptime("2022/02/01 18:40:10", "%Y/%m/%d %H:%M:%S").timestamp()

print("La conversion de nuestro valor en timenow es: ", timeNow)










