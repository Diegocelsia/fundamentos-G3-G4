# Definir una clase llamada persona

class Persona:
    #Metodo __init__ es el contructor que se llama cuando creamos una instancia.
    def __init__(self, nombre, edad):
        #Atributo que almacena el nombre de la persona
        self.nombre = nombre
        #Atributo que almacena la edad de la persona
        self.edad = edad
    
    #definir un metodo llamado presentarser.
    def presentarse(self):
        print(f"Hola mi nombre es {self.nombre} y tengo {self.edad} años")


# Se crea una instancia para persona1
persona1 = Persona("Carlos", 30)
#Llamada del metodo "Presentarse" con los valores de la persona1
persona1.presentarse()

#Se crea segunda instancia para persona2
persona2 = Persona("Maria", 17)
#Llamada del metodo "Presentarse" con los valores de la persona2
persona2.presentarse()



class Coche:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
    
    def descripcion(self):
        print(f"Este coche es un {self.marca} {self.modelo} del año {self.anio}.")
    
    def es_antiguo(self):
        current_year = 2024  # Puedes usar el año actual si lo deseas
        return (current_year - self.anio) > 20

# Ejemplo de uso
coche1 = Coche("Toyota", "Corolla", 2000)
coche1.descripcion()  # Salida: Este coche es un Toyota Corolla del año 2000.
print(coche1.es_antiguo())  # Salida: True

