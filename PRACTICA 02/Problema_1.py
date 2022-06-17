"""
1. Escriba un programa donde tendrá los siguientes requisitos:
Reglas:
- Crear una clase llamada Persona donde sus atributos deben ser nombre, edad y de nacionalidad peruana (use el manejo de errores para el tipo de dato)
- Un método cumpleaños donde cada vez que invoque aumentará en un año la edad de la persona.
- Crear la instancia de la clase Persona y usar su método cumpleaños para incrementar su edad (mínimo 2 vez, mostrar por pantalla dicha edad actualizada).
- Crear una función que retorne solamente la fecha, hora y minuto que se ha registrado esta persona (Mostrar por pantalla)
"""
from datetime import date, datetime

class Persona:

    try:
        nombre = input("Ingrese su nombre: ")
        edad = int(input("Ingrese su edad: "))
        nacionalidad = "peruana"
    except TypeError:
        print("Problema de tipos de datos!!!")

    def cumpleanios(self):
        try:
            self.edad = self.edad + 1
        except TypeError:
            print("Problema de tipos de datos!!!")





def retornaHora(persona2):

    tiempo = datetime.now()
    """Uso del datetime para extraer la hora, el minuto y el segundo"""
    hora = tiempo.hour
    minuto = tiempo.minute
    segundo = tiempo.second

    print("La hora exacta son las: {} horas con {} minutos y {} segundos".format(hora, minuto, segundo))

persona1 = Persona()

print("Mi nombre es {} y tengo {} anios". format(persona1.nombre,persona1.edad))
persona1.cumpleanios()
persona1.cumpleanios()
print("\nMi edad luego de ejecutar 2 veces el método cumpleanios es {}".format(persona1.edad))
print("\nMi edad luego de ejecutar 2 veces el método cumpleanios es {}".format())



