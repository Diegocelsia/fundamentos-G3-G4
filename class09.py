#Listas

OJOOOOO ESTO YA LO HICE CON LOS DE LOS SABADOS



#Manera de declarar una #lista
#lista = [25, 26, 27, 28, 29]


#De esta manera accedemos a un elemento de una lista
#print(lista[4])
#print(lista[-2])


#De esta manera agregamos un elemento a nuestra lista
#lista.append(8)
#print(lista)

# de esta manera reemplazamos nuesto valor de un elemento
#lista[1] = 3
#print(lista)



"""

numero = int(input("Ingrese un numero: "))

if numero in lista:
    elemento = lista.index(numero)
    lista[elemento] = 6
print(lista)"""


#Manera de eliminar un elemento

"""del lista[0]
print(lista)
"""

"""lista = [25, 26, 27, 28, 29]

numero = int(input("Ingrese un numero: "))
print(lista)

for i in range(len(lista)):
    if numero == lista[i]:
        del lista[i]
        break

print(lista)"""

#Manera de sumar elementos de nuestra lita
lista = [25, 26, 27, 28, 29]
#print(sum(lista))





#Tuplas

frutas = ("Manzana", "Pera", "Chontaduro", "Kiwi")

print(frutas[1])
print(frutas[-2])

lista_frutas = list(frutas)
print(frutas)
print(lista_frutas)
print(tuple(lista_frutas))


#Diciionarios

contacto = {"Diego": "12345678", #0
            "Tomas": "15567343", #1
            "Juana": "13245796"} #2

print(contacto["Juana"])

contacto["Ana"] = "124565432"
print(contacto)

del contacto["Diego"]
print(contacto)


for nombre, telefono in contacto.items():
    print(nombre, telefono)

