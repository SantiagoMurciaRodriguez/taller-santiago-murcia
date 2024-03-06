class Persona:
    def __init__(self, nombre, apellidos, sexo, edad, ciudad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.sexo = sexo
        self.edad = edad
        self.ciudad = ciudad

    def mostrar_datos(self):
        print(f"Nombre completo: {self.nombre} {self.apellidos}")
        print(f"Sexo: {self.sexo}")
        print(f"Edad: {self.edad} años")
        print(f"Ciudad: {self.ciudad}")

# Ejemplo de uso
persona1 = Persona(nombre="Juan", apellidos="Pérez", sexo="Masculino", edad=30, ciudad="Manizales")
persona1.mostrar_datos()


class Rectangulo:
    def __init__(self, longitud, ancho):
        self.longitud = longitud
        self.ancho = ancho

# Ejemplo de uso
rectangulo1 = Rectangulo(longitud=5, ancho=3)
print(f"Longitud del rectángulo: {rectangulo1.longitud}")
print(f"Ancho del rectángulo: {rectangulo1.ancho}")
