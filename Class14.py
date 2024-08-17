"""entrada = "abcd"
salida = ""

for i in entrada:
    salida += i * 3
print(salida)
"""

#Herencia y poliforismo

"""class vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def arrancar(self):
        return f"{self.marca} {self.modelo} esta arrancando"



class Carro(vehiculo):
    def acelerar(self):
        return f"{self.marca} {self.modelo} esta acelerando"


class Motocicleta(vehiculo):
    def caballito(self):
        return f"{self.marca} {self.modelo} esta haciendo un caballito"


carro = Carro("Toyota", "TXL")
motocicleta = Motocicleta("Ducati", "1199")

#Hererar datos
print(carro.acelerar())
print(motocicleta.caballito())

print("----------------------")

#Poliformismo

print(motocicleta.arrancar())
print(carro.arrancar())"""


### Manejo de errores###

numero1 = 5
numero2 = 1

numero1 = "1"



#Excepccion Base
try:
    #intenta ejecutar
    print(numero1 + numero2)
except:
    #Se ejecuta si hay una excepcion:
    print("Se ha producido un error")



print("-----------------------------")

#Flujo completo de una exprecion:
try:
    #Intenta ejecutar 
    print( numero1 + numero2)
    print("No se procede ningun error")
except:
    #Se ejecuta si hay alguna excepcion
    print("Se ha producido un error")
else:
    # Opcional Se ejecuta si no se procduce ninguna excepcion
    print("No se presenta ningun error, se sigue ejecutando de manera normal")
finally:
    #Opcional Siempre se ejecuta hayan o no hayn excepciones
    print("La ejecucion continua")