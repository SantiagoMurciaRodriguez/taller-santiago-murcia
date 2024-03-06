class Persona:
    # Variable de clase para contar el número total de personas
    contador = 0

    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos
        # Incrementamos el contador cada vez que se crea una instancia de Persona
        Persona.contador += 1

    def mostrar_datos(self):
        print(f"Nombre completo: {self.nombre} {self.apellidos}")

# Ejemplo de uso
persona1 = Persona(nombre="Juan", apellidos="Pérez")
persona2 = Persona(nombre="María", apellidos="González")

print(f"Total de personas creadas: {Persona.contador}")


class Empleado:
    # Lista para almacenar los salarios de todos los empleados
    salarios_empleados = []

    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
        # Agregamos el salario a la lista de salarios_empleados
        Empleado.salarios_empleados.append(salario)

    @staticmethod
    def salario_promedio():
        """Calcula el salario promedio de todos los empleados."""
        if Empleado.salarios_empleados:
            total_salarios = sum(Empleado.salarios_empleados)
            num_empleados = len(Empleado.salarios_empleados)
            return total_salarios / num_empleados
        else:
            return 0

# Ejemplo de uso
empleado1 = Empleado(nombre="Juan", salario=50000)
empleado2 = Empleado(nombre="María", salario=60000)

print(f"Salario promedio de los empleados: ${Empleado.salario_promedio()}")
