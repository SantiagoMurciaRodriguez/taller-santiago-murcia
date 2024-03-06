class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print(f"Hola, soy {self.nombre}. ¡Un placer conocerte!")

class Empleado(Persona):
    def __init__(self, nombre, salario, puesto):
        super().__init__(nombre)
        self.salario = salario
        self.puesto = puesto

    def saludar(self):
        print(f"Hola, soy {self.nombre}, un {self.puesto}. Mi salario es ${self.salario}.")

class Estudiante(Persona):
    def __init__(self, nombre, grado, escuela):
        super().__init__(nombre)
        self.grado = grado
        self.escuela = escuela

    def saludar(self):
        print(f"Hola, soy {self.nombre}, un estudiante de {self.grado} en {self.escuela}.")

# Ejemplo de uso
persona1 = Persona(nombre="Juan")
empleado1 = Empleado(nombre="María", salario=50000, puesto="Analista")
estudiante1 = Estudiante(nombre="Carlos", grado="10°", escuela="Colegio XYZ")

persona1.saludar()
empleado1.saludar()
estudiante1.saludar()

from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    @abstractmethod
    def calcularArea(self):
        """Método abstracto para calcular el área."""
        pass

    @abstractmethod
    def calcularPerimetro(self):
        """Método abstracto para calcular el perímetro."""
        pass

class Rectangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        """Calcula el área del rectángulo."""
        return self.base * self.altura

    def calcularPerimetro(self):
        """Calcula el perímetro del rectángulo."""
        return 2 * (self.base + self.altura)

# Ejemplo de uso
rectangulo1 = Rectangulo(base=5, altura=3)
print(f"Área del rectángulo: {rectangulo1.calcularArea()}")
print(f"Perímetro del rectángulo: {rectangulo1.calcularPerimetro()}")
