#Condicional While

i = 1

while i <= 10:
    print(i)
    i = i + 1




numero = int(input("Introduce un numero (Y cero para terminar): "))
suma = 0

while numero != 0:
    suma = suma + numero
    numero = int(input("Introduce un numero (Y cero para terminar): "))

print("La suma es ", suma)


"""numero = int(input("Introduce un numero (y numero negativo para terminar): "))
suma = 0

while numero > 0:
    suma = suma + numero
    numero = int(input("Introduce un numero (y numero negativo para terminar): "))

print("La suma es ", suma)
"""

"""
numero = int(input("Introduce un numero (y un numero impar para terminar): "))
suma = 0

while numero % 2 == 0:
    suma = suma + numero
    numero = int(input("Introduce un numero (y un numero impar para terminar): "))
print("La suma es ", suma)
"""

#Funciones

"""def saludo():
    print("Hola")

saludo()



def suma(num1, num2):
    print(num1+num2)

suma(3,5)


def multiplicar(num3):
    return num3 * 100 

print(multiplicar(3))"""


def operaciones():
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Resto")
    print("6. Salir")


def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

operaciones()

opera1 = int(input("Por favor Ingrese una operacion, (1, 2, 3, 4, 4): "))
numero1 = int(input("Ingrese numero 1: "))
numero2 = int(input("Ingrese numero 2: "))


if opera1 == 1:
    print(suma(numero1, numero2))
elif opera1 == 2:
    print(resta(numero1, numero2))
