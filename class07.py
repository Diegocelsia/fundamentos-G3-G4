"""Problemas


1. Crea una variable llamada num_estudiantes.
Pide al usuario que ingrese el número de estudiantes y almacena el valor en num_estudiantes.
Iterar sobre cada estudiante:

2. Utiliza un bucle for que se ejecute una vez por cada estudiante.
Dentro del bucle, imprime el número del estudiante actual (usa i+1 para que empiece desde 1).
Inicializar el total de notas:

3. Dentro del bucle para cada estudiante, crea una variable llamada total_notas y inicialízala en 0.0.
Solicitar las notas de los exámenes:

4. Utiliza un bucle for dentro del bucle anterior para pedir las cuatro notas del estudiante.
Pide al usuario que ingrese la nota del examen y almacena el valor en una variable llamada nota.
Suma la nota ingresada al total_notas.
Calcular el promedio:

5. Después de salir del bucle de las notas, calcula el promedio dividiendo total_notas entre 4.
Almacena el promedio en una variable llamada promedio.
Determinar si el estudiante pasó o perdió:

6.Utiliza una estructura if-else para determinar si el estudiante pasó o perdió la materia según el promedio.
Si el promedio es mayor o igual a 3.0, el estudiante pasó. De lo contrario, perdió.
Imprimir el resultado final:

7. Imprime el resultado final para cada estudiante, indicando si pasó o perdió la materia y mostrando su promedio."""


num_estudiantes = int(input("Ingrese el numero de estudiantes: "))


for i in range(num_estudiantes):
    print(f"\nEstudianteb {i + 1}")

    total_notas = 0.0

    for j in range(4):
        nota = float(input(f"Ingrese la nota del examen {j+1} (de 0.0 a 5.0): "))
        total_notas = total_notas + nota

    promedio = total_notas/4


    if promedio >= 3.0:
        resultado = "Paso"
    else:
        resultado = "Perdio"

    print(f"El estudiante {i+1} {resultado} la materia con un promedio de {promedio:.2f}")

"""
#Manipulacion de cadenas (Strings)

#Obteber la longitud de una cadena 
cadena = "Hola,hdvsavs nvkljbasvfj.bs lkvnlñksav.absvjbasñldkvnñklvlgiuds"
longitud = len(cadena)
print(longitud)

# Convierto mi cadena de texto en Mayus
cadena = "Hola"
mayusc = cadena.upper()
print(mayusc)


# De esta manera se convierte de Mayus a mins
cadena2 = "HOLA"
minusculas = cadena2.lower()
print(minusculas)

#Manera de dividir text
cadena = "Hola Mundo"
cadenaDiv = cadena.split()
print(cadenaDiv)

#De esta manera elimino espacios
cadena = "      Hola      "
limpia = cadena.strip()
print(limpia)


#de esta manera reemplazo una cadena de texto
nueva_cadena = "Hola mundo"
reempla = nueva_cadena.replace("mundo", "Encap24")
print(reempla)



#Operaciones con Listas

lista = [8, 7, 9]
        #0  1  2
        #-3 -2 -1

#Obtener la longitud de la lista
longitud_Lista = len(lista)
print(longitud_Lista)


#Añadir un elemento al final
lista.append(8)
print(lista)


#Insertar en un valor espesifico
lista.insert(1, 4)
print(lista)

#Remover un elemento
lista.remove(9)
print(lista)

#Metodo para devolver el ultimo elemento de la lista
ultimo_element = lista.pop()
print(ultimo_element)
print(lista)

#   Odenar la lista

lista = [3, 2, 1]
lista.sort()
print(lista)

#Invertir un elemento
lista = [ 3, 4, 5, 6]
lista.reverse()
print(lista)


#Sumar valores de una lista
total = sum([ 3, 4, 5, 6])
print(total)
"""
