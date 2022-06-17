
"""POO en Python"""
"""Encapsulamiento"""

class A():

    def __int__(self):
        """Encapsulamiento"""
        self.contador = 0 #Definiendo sus atributos como privados

class B():

    def __int__(self):
        """Encapsulamiento"""
        self.contador = 0  # Definiendo sus atributos como privados

    def incrementa(self):
        """Encapsulamiento"""
        self.contador = self.__contador + 1

    def cuenta(self):
        return self.__contador

varA = A()
varA.incrementa()
varA.incrementa()
print(varA.cuenta())




