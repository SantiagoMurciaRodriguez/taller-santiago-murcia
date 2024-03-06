class Persona:
    def __init__(self, Nombre, Edad, Genero):
        self.identidad = f"La persona se llama {Nombre} y tiene {Edad} y es de genero {Genero}"

pedrito = Persona("Santiago", 19, "Hombre")
print(pedrito.identidad)

class Rectangulo:
    def __init__(self, longitud, ancho):
        self.longitud = longitud
        self.ancho = ancho

    def calcular_area(self):
        """Calcula el área del rectángulo."""
        return self.longitud * self.ancho

    def calcular_perimetro(self):
        """Calcula el perímetro del rectángulo."""
        return 2 * (self.longitud + self.ancho)

# Ejemplo de uso
rectangulo1 = Rectangulo(longitud=5, ancho=3)
print(f"Área del rectángulo: {rectangulo1.calcular_area()}")
print(f"Perímetro del rectángulo: {rectangulo1.calcular_perimetro()}")



