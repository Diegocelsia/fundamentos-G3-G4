"""numero = range(15) #[0, 1, 2, 3, 4] # Valor del elemento
                #   0, 1, 2, 3, 4 Ubicacion del elemento

for a in numero:
    print(a, "Hola")"""


"""tabla = range(11)  #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                    #0, 1, 2, 3, 4
for a in tabla:
    print( a * 11 )
    #print(a, "x 11 =", a * 11)
"""

"""numeros = range(1, 13)

for i in numeros:
    for j in numeros:
        print(i * j)
    print()
"""

tabla = int(input("Ingrese un numero: "))
rango = range(1, 13) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
for a in rango:
    print(tabla, "*", a,"=" ,tabla*a)


