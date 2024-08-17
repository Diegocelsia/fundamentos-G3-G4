class Curso:
    def __init__(self, nombre_curso):
        self.nombre_curso = nombre_curso
        self.estudiantes = []
        self.notas = {}

    def agregar_estudiante(self, nombre_estudiante):
        if nombre_estudiante not in self.estudiantes:
            self.estudiantes.append(nombre_estudiante)
            self.notas[nombre_estudiante] = []
            print(f"El estudiante {nombre_estudiante} ha sido agregado al curso {self.nombre_curso}.")
        else:
            print(f"El estudiante {nombre_estudiante} ya está en el curso.")

    def asignar_nota(self, nombre_estudiante, nota):
        if nombre_estudiante in self.estudiantes:
            self.notas[nombre_estudiante].append(nota)
            print(f"La nota {nota} fue asignada al estudiante {nombre_estudiante}.")
        else:
            print("El estudiante no está en el curso")

    def promedio_estudiante(self, nombre_estudiante):
        if nombre_estudiante in self.estudiantes:
            notas = self.notas[nombre_estudiante]
            if notas:
                promedio = sum(notas) / len(notas)
                return promedio
            else:
                print(f"El estudiante {nombre_estudiante} no tiene notas asignadas.")
                return None
        else:
            print(f"El estudiante {nombre_estudiante} no está en el curso.")
            return None

    def lista_estudiantes(self):
        for estudiante in self.estudiantes:
            promedio = self.promedio_estudiante(estudiante)
            notas = self.notas[estudiante]
            print(f"Estudiante: {estudiante}, Notas: {notas}, Promedio: {promedio:.2f}")


# Ejemplo de uso
curso = Curso("Matemáticas")

# Agregar estudiantes
curso.agregar_estudiante("Juan")
curso.agregar_estudiante("Pablo")

# Asignar notas
curso.asignar_nota("Juan", 80)
curso.asignar_nota("Juan", 50)
curso.asignar_nota("Pablo", 90)
curso.asignar_nota("Pablo", 10)

# Calcular promedios
print(f"Promedio de Juan = {curso.promedio_estudiante('Juan'):.2f}")

# Listar estudiantes
curso.lista_estudiantes()






# Paso 1: Crear la clase `Curso`
# Esta clase representará un curso con estudiantes y notas.

class Curso:
    # El método __init__ es el constructor de la clase y se ejecuta cuando se crea una instancia de `Curso`.
    def __init__(self, nombre_curso):
        # Almacena el nombre del curso.
        self.nombre_curso = nombre_curso
        # Lista vacía para almacenar los nombres de los estudiantes.
        self.estudiantes = []
        # Diccionario vacío para asociar cada estudiante con sus notas.
        self.notas = {}

    # Paso 2: Crear un método para agregar estudiantes.
    # Este método agrega un estudiante al curso si no está ya en la lista de estudiantes.
    def agregar_estudiante(self, nombre_estudiante):
        # Verifica si el estudiante ya está en la lista.
        if nombre_estudiante not in self.estudiantes:
            # Si no está, lo agrega a la lista.
            self.estudiantes.append(nombre_estudiante)
            # Inicializa una lista vacía de notas para el nuevo estudiante.
            self.notas[nombre_estudiante] = []
            print(f"El estudiante {nombre_estudiante} ha sido agregado al curso {self.nombre_curso}.")
        else:
            print(f"El estudiante {nombre_estudiante} ya está en el curso.")

    # Paso 3: Crear un método para asignar notas a los estudiantes.
    # Este método asigna una nota a un estudiante específico.
    def asignar_nota(self, nombre_estudiante, nota):
        # Verifica si el estudiante está en la lista.
        if nombre_estudiante in self.estudiantes:
            # Si está, agrega la nota a la lista de notas del estudiante.
            self.notas[nombre_estudiante].append(nota)
            print(f"La nota {nota} fue asignada al estudiante {nombre_estudiante}.")
        else:
            print("El estudiante no está en el curso.")

    # Paso 4: Crear un método para calcular el promedio de un estudiante.
    # Este método calcula el promedio de las notas de un estudiante específico.
    def promedio_estudiante(self, nombre_estudiante):
        # Verifica si el estudiante está en la lista.
        if nombre_estudiante in self.estudiantes:
            # Obtiene la lista de notas del estudiante.
            notas = self.notas[nombre_estudiante]
            # Verifica si el estudiante tiene notas.
            if notas:
                # Calcula el promedio de las notas.
                promedio = sum(notas) / len(notas)
                return promedio
            else:
                # Si no tiene notas, devuelve None.
                print(f"El estudiante {nombre_estudiante} no tiene notas asignadas.")
                return None
        else:
            print(f"El estudiante {nombre_estudiante} no está en el curso.")
            return None

    # Paso 5: Crear un método para listar todos los estudiantes con sus notas y promedios.
    # Este método imprime la información de todos los estudiantes del curso.
    def lista_estudiantes(self):
        for estudiante in self.estudiantes:
            promedio = self.promedio_estudiante(estudiante)
            notas = self.notas[estudiante]
            # Imprime el nombre del estudiante, sus notas y su promedio.
            if promedio is not None:
                print(f"Estudiante: {estudiante}, Notas: {notas}, Promedio: {promedio:.2f}")
            else:
                print(f"Estudiante: {estudiante}, Notas: {notas}, Promedio: No disponible")

# Paso 6: Ejemplo de uso
# 6.1 Crear una instancia de `Curso`
curso = Curso("Matemáticas")

# 6.2 Agregar estudiantes
curso.agregar_estudiante("Juan")
curso.agregar_estudiante("Pablo")

# 6.3 Asignar notas
curso.asignar_nota("Juan", 80)
curso.asignar_nota("Juan", 50)
curso.asignar_nota("Pablo", 90)
curso.asignar_nota("Pablo", 10)

# 6.4 Mostrar promedios
print(f"Promedio de Juan = {curso.promedio_estudiante('Juan'):.2f}")
print(f"Promedio de Pablo = {curso.promedio_estudiante('Pablo'):.2f}")

# 6.5 Listar estudiantes
curso.lista_estudiantes()
