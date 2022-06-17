
"""Uso del for"""

ingenierias = ["Software", "Sistemas", "Industrial","Mecanica"]
i = 0

nombre = input("Ingrese su primer nombre: ")

#print("El tamaño de nuestra lista es: ", len(ingenierias))
print("El tamaño de nuestra lista es: {},programa creador por: {}".format(len(ingenierias),nombre))


for ingenieria in ingenierias:

    print("Ingenieria {}".format(ingenieria))
    i += 1
    print("Esta es la vuelta numero: {}".format(i))

print("Llegó el fin de nuestro for")



