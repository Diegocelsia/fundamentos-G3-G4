#Operadores aritmeticos (+, -, *, /, %, **)

a = 10
b = 5

suma = a + b
#print(suma)

resta = a - b
#print(resta)

multiplicacion = a * b
#print(multiplicacion)

division = a / b
#print(division)

resto = a % b
#print(resto)

potencia = a ** b
#print(potencia)


#Operadores comparativos
#Estas operaciones arrojan Verdadero o Falso

a = 10
b = 5

igual = (a == b)
#print(igual)

desigualda = (a != b)
#print(desigualda)

mayor_que = (a > b)
#print(mayor_que)


menor_que = (a < b)
#print(menor_que)


#Operadores logicos

# Tabla de verdad del operador 'and' (y lógico):


"""
Operando A | Operando B | A and B
-----------------------------------
    True   |    True    |  True
    True   |   False    |  False
    False  |    True    |  False
    False  |   False    |  False
"""


# Tabla de verdad del operador 'or' (o lógico):
"""
Operando A | Operando B | A or B
----------------------------------
    True   |    True    |  True
    True   |   False    |  True
    False  |    True    |  True
    False  |   False    |  False
"""

# Tabla de verdad del operador 'not' (negación):
"""
Operando |  not Operando
-------------------------
    True  |     False
    False |     True
"""


variable = 11


if  variable <= 9 and variable >= 1:
    print(f"El numero {variable} menor a 9")
elif variable >= 10:
    print(f"Numero {variable}, es mayor o igual a 10")
else:
    print(f"el numero ingresado es menor a cero o es cero")



