"""file = open("file1.txt", "r")
print(file)
lineas = file.readlines()
print(lineas)
file.close()"""

"""with open("file2.txt", "r") as archivo:
    lineas = archivo.readlines()
    #print(lineas)

print(lineas)
for i in lineas:
    print(i.replace("\n", ""))"""



with open("file2.txt", "r") as i:
    contenido = i.read()
    lineas = contenido.split("\n")
    print(lineas)

"""
with open('file2.txt', 'r') as archivo:
    print(type(archivo.read()))

with open('file2.txt', 'rb') as archivo:
    print(type(archivo.read()))
"""

"""
#Metodos de la documentacion oficial python --Modos de acceso

'r' - modo lectura. Es el modo predeterminado. Solo te permite leer el archivo, no modificarlo.
Cuando usas este modo, el archivo debe existir.

'w' - modo escritura. Creará un archivo nuevo si no existe, de lo contrario borrará el archivo
y te permitirá escribir en él.

'a' - modo anexar. Escribirá datos al final del archivo. No borra el archivo, y el archivo debe
existir para usar este modo.

'rb' - modo lectura en binario. Es similar a 'r', excepto que la lectura se realiza en modo
binario. También es una opción predeterminada.

'r+' - modo lectura y escritura al mismo tiempo. Te permite leer y escribir en los archivos
al mismo tiempo sin tener que usar 'r' y 'w' por separado.

'rb+' - modo lectura y escritura en binario. Igual que 'r+', excepto que los datos están en
formato binario.

'wb' - modo escritura en binario. Igual que 'w', excepto que los datos están en formato binario.

'w+' - modo escritura y lectura. Exactamente igual que 'r+', pero si el archivo no existe, se
crea uno nuevo. De lo contrario, el archivo se sobrescribe.

'wb+' - modo escritura y lectura en binario. Igual que 'w+', pero los datos están en formato
binario.

'ab' - modo anexar en binario. Similar a 'a', excepto que los datos están en formato binario.

'a+' - modo anexar y lectura. Similar a 'w+' ya que creará un archivo nuevo si el archivo no
existe. De lo contrario, el puntero del archivo estará al final del archivo si ya existe.

'ab+' - modo anexar y lectura en binario. Igual que 'a+', excepto que los datos están en
formato binario.
"""

with open("file3.txt", "a") as archivo:
    archivo.write("Oscar\nAlejandra\nPedro123\n")