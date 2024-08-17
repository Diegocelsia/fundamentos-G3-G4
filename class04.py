"""numero = float(input("Ingrese un numero: "))

if numero > 0:
    print("Su numero es positivo")
elif numero == 0:
    print("Su numero es cero")
else:
    print("Su numero es negativo")"""

"""_________"""








while True:

    print("CALCULADORA DE AREA")
    print("1. CIRCULO")
    print("2. CUADRADO")
    print("3. RECTANGULO")
    print("4. TRIANGULO")
    print("5. SALIR")

    opcion = int(input("Escoja la opcion: "))

    if opcion == 1:
        radio = float(input("Ingrese el radio del circulo: "))
        areacir = 3.1416 * radio * radio 
        print(f"El area del Circulo es {areacir}.")

    elif opcion == 2:
        lado = float(input("Ingrese el lado del cuadrado: "))
        areacua = lado * lado
        print(f"El area del Cuadrado es {areacua}.")

    elif opcion == 3:
        base = float(input("Ingrese la base del rectangulo: "))
        altu = float(input("Ingrese la altura del rectangulo: "))
        arearec = base * altu
        print(f"El area del Rectangulo es {arearec}.")

    elif opcion == 4:
        base = float(input("Ingrese la base del triangulo: "))
        altu = float(input("Ingrese la altura del triangulo: "))
        areatri = (base * altu) / 2
        print(f"El area del Triangulo es {areatri}.")

    elif opcion == 5:
        print("Saliendo del menú")
        break

    else:
        print("Escoja correctamente su opcion")
