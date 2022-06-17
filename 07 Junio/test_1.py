
"""POO en Python"""
"""Clases y Atributos"""

class Carro:
    """Atributos"""
    ruedas = 4
    """Constructor: Valores que va a tener por defecto mi clase cuando se le instancia a una variable"""
    def __init__(self, color, aceleracion):
        self.color = color
        self.aceleracion = aceleracion
        self.velocidad = 0

        """Metodos: Son las funciones de la clase"""
    def acelera(self):
        self.velocidad = self.velocidad + self.aceleracion

    def frena(self):
        velocidad = self.velocidad - self.aceleracion
        if velocidad < 0:
            velocidad = 0
        self.velocidad = velocidad

"""Instanciamos nuestra clase"""

carro1 = Carro("Rojo", 20)
print("El color de mi primer carro es: ", carro1.color)
print("La aceleracion de mi primer carro es: ", carro1.aceleracion)
print("La cantidad total de ruedas de mi primer carro es: ", carro1.ruedas)


carro2 = Carro("Blanco", 30)
"""Se le asignará un atributo de dato a la instancia de nuestro segundo carro"""

carro2.marchas = 1000

print("El numero de marchas de mi carro es: ", carro2.marchas)

"""No es posible llamar a un atributo de dato que se le ha asignado a otra instancia de la clase"""
print("La numero de marchas de mi primer carro es: ", carro1.marchas)

