"""
2. Usando el concepto de herencia y encapsulación (para saldo) para crear el siguiente programa:
Reglas:
- Agregar un atributo saldo a la clase persona.
- Crear un método transferencia(self, persona2, monto)
- El saldo deberá representar el dinero que tiene la otra persona
- El método transferencia hace que la Persona que llame al método pueda transferir la cantidad monto al objeto Persona2
- Comprobar si no se tiene dinero suficiente no se ejecuta la acción e imprimir “Saldo insuficiente”
"""

class Persona:
    saldo = 100

    def transferencia(self, persona2, monto):
        self.persona2 = Persona()
        self.monto = monto

        if self.monto > self.saldo:
            print("Saldo insuficiente para esta transferencia")
        else:
            self.saldo = self.saldo - self.monto
            persona2.saldo = persona2.saldo + self.monto


persona1 = Persona()
persona2 = Persona()
print("Soy persona 1 y mi saldo es: ", persona1.saldo)
print("Soy persona 2 y mi saldo es: ", persona2.saldo)
persona1.transferencia(persona2, 50)
print("Persona 1 hizo una transferencia de 20 a persona 2 y ahora tienen\n")
print("Soy persona 1 y mi saldo es: ", persona1.saldo)
print("Soy persona 2 y mi saldo es: ", persona2.saldo)

