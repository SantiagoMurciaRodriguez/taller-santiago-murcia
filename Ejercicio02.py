class Persona:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos

    def mostrar_datos(self):
        print(f"Nombre completo: {self.nombre} {self.apellidos}")

class Empleado(Persona):
    def __init__(self, nombre, apellidos, salario, puesto):
        # Llamamos al constructor de la clase base (Persona)
        super().__init__(nombre, apellidos)
        self.salario = salario
        self.puesto = puesto

    def mostrar_datos(self):
        # Llamamos al método de la clase base para mostrar el nombre completo
        super().mostrar_datos()
        print(f"Salario: ${self.salario}")
        print(f"Puesto de trabajo: {self.puesto}")

# Ejemplo de uso
empleado1 = Empleado(nombre="Juan", apellidos="Pérez", salario=50000, puesto="Analista")
empleado1.mostrar_datos()


class Persona:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos

    def mostrar_datos(self):
        print(f"Nombre completo: {self.nombre} {self.apellidos}")

class Estudiante(Persona):
    def __init__(self, nombre, apellidos, grado, escuela):
        # Llamamos al constructor de la clase base (Persona)
        super().__init__(nombre, apellidos)
        self.grado = grado
        self.escuela = escuela

    def mostrar_datos(self):
        # Llamamos al método de la clase base para mostrar el nombre completo
        super().mostrar_datos()
        print(f"Grado: {self.grado}")
        print(f"Escuela: {self.escuela}")

# Ejemplo de uso
estudiante1 = Estudiante(nombre="María", apellidos="González", grado="10°", escuela="Colegio XYZ")
estudiante1.mostrar_datos()