"""
Rango de IMC Clasificación
Menos de 18.5     --> Bajo peso
Entre 18.5 y 24.9 --> Peso normal
Entre 25 y 29.9	  --> Sobrepeso
30 o más	      --> Obesidad
"""

peso = float(input("Ingrese su peso en Kg: "))
altura = float(input("Ingrese su altura: "))

imc = peso / (altura*altura)


if imc < 18.5:
    clasificacion ="Bajo peso"
elif imc > 18.5 and imc < 24.9:
    clasificacion ="Peso normal"
elif imc > 25 and imc <= 29.9:
    clasificacion ="Sobre peso"
else:
    clasificacion ="Obesida"

print(f"Su IMC es: {imc:.4f}")
print(f"su calificacion es: {clasificacion}")



