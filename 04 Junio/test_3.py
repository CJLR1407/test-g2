
"""
1. Pedir a un usuario ingresar su direccion email. Imprimir un mensaje indicando si la direccion es valido o no,
valiendose de una funcion para decidirlo. Una direccion se considerará valido si contiene el simbolo "@".
"""

def validar(email):
    caracterPedido = "@"
    emailValido = False
    for caracter in email:
        if caracter == caracterPedido:
            return True
    return False

emailUsuario = input("Ingrese tu email: ")

if validar(emailUsuario):
    print("Email valido")
else:
    print("Email invalido")





