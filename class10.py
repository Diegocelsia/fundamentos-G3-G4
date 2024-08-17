#Clases

class Persona:
    def __init__(self, nombre, edad): #Metodo clase inicializador
        self.nombre = nombre
        self.edad = edad
    
    def saludar(self): #Metodo de la clase
        print(f"Hola mi nombre es {self.nombre} y tengo {self.edad} años")



#Creo mi Instancias
persona1 = Persona("Juan", 40)
persona2 =Persona("Carla", 18)


#Llamar metodo
#persona1.saludar()
#persona2.saludar()


#/////////////////////////////////////////////////77


"""class Calculadora:
    def suma(self, num1, num2):
        return num1 + num2
    
    def div(self, num1, num2):
        if num2 == 0:
            return "No se puede dividir en cero"
        else:
            return num1 / num2


numero1 = float(input("Ingrese el numero1: "))
numero2 = float(input("Ingrese el numero2: "))

calculadora = Calculadora()

print(calculadora.suma(numero1, numero2))"""


#////////////////////////////////////////////////////////////////



class Calsuladora:
    def __init__(self, numero):
        self.resultado= numero

    def suma(self, numero):
        self.resultado = self.resultado + numero

    def resta(self, numero):
        self.resultado = self.resultado - numero

    def mult(self, numero):
        self.resultado = self.resultado * numero

    def div(self, numero):
        self.resultado = self.resultado / numero
    
    def obt_Result(self):
        return self.resultado


calculo = Calsuladora(0)

calculo.suma(5)
calculo.resta(4)
calculo.mult(5)
calculo.div(2)

resultadoOpe = calculo.obt_Result()
print(resultadoOpe)