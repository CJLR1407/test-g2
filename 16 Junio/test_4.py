
"""Decoradores en Python"""

import time

"""Creacion de funcion decoradora"""

def mesureTime(function):
    def wrapper(*args, **kwargs):
        start = time.time()

        result = function(*args, **kwargs)

        total = time.time() - start
        print("La demora de ejecución fue de: {}".format(total))

        return result
    return wrapper

@mesureTime
def suma(a, b, c, d):
    time.sleep(1) #Pausa la ejecucion del codigo por 1 segundo
    s = a + b + c + d
    return s

print(suma(20,40,60,100))

