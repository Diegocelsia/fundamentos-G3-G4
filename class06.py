numeros = range (1, 51)
#30
for numero in numeros:
    if numero % 3 == 0 and numero % 5 == 0:
        print("FizzBuzz")
    elif numero % 3 == 0:
        print("Fizz")
    elif numero % 5 == 0:
        print("Buzz")
    else:
        print(numero)




personas = [
    {"nombre": "Ana", "edad": 10},#0
    {"nombre": "Luis", "edad": 16},#1
    {"nombre": "Carlos", "edad": 25},#2
    {"nombre": "María", "edad": 70},#3
    {"nombre": "Marta", "edad": 50},#4
    {"nombre": "José", "edad": 13},#5
    {"nombre": "Lucía", "edad": 64},#6
    {"nombre": "Miguel", "edad": 65}#7
]

for persona in personas:
    nombre = persona["nombre"]
    edad = persona["edad"]


    if edad < 13:
        clasificacion = "Niño"
    elif 13 <= edad <= 17:
        clasificacion = "Adolescente"
    elif 18 <= edad <= 64:
        clasificacion = "Adulto"
    else:
        clasificacion = "Anciano"

    print(f"{nombre} es {clasificacion}")


