"""class Car:
    def __init__(self, marca, modelo, velocidad_max, precio):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_max = velocidad_max
        self.precio = precio
    
    def acelerar(self):
        self.velocidad_max += 10
        print(f"Velocidad aumentada a {self.velocidad_max}")

carro = Car("Mazda", "Cx30", 150, 130000000) 
carro.acelerar()

"""


letras = "zsfhgiflvsvgbildjfbisjabcde"

def ordenar(x):
    lista= []
    for elemento in x:
        lista.append(elemento)
    lista.sort()
    print(''.join(lista))

ordenar(letras)
