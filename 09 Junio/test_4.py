
"""Herencia"""
"""Herencia Multiple"""

class A:
    def inprimirA(self):
        print("a")
class B:
    def imprimirB(self):
        print("b")

"""Aplicando herencia multiple"""
class C(A,B):
    def imprimirC(self):
        print("c")

varC = C()
varC.inprimirA()
varC.imprimirB()
varC.imprimirC()



