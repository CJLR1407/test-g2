
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

carro1 = Carro("Axul", 15)

print("La velocidad inicial de mi carro 1 es: ", carro1.velocidad)
carro1.acelera()
carro1.acelera()
carro1.acelera()
print("La velocidad luego de acelerar de mi carro 1 es: ", carro1.velocidad)

carro1.frena()
carro1.frena()

print("La velocidad luego de frenar es: ", carro1.velocidad)




