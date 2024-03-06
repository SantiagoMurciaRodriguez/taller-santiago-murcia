class Motor:
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia

class Coche:
    def __init__(self, marca, modelo, motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor

    def mostrar_info(self):
        print(f"Coche {self.marca} {self.modelo} con motor {self.motor.tipo} ({self.motor.potencia} CV)")

# Ejemplo de uso
motor_gasolina = Motor(tipo="Gasolina", potencia=150)
mi_coche = Coche(marca="Toyota", modelo="Corolla", motor=motor_gasolina)
mi_coche.mostrar_info()


class Departamento:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []  # Lista de empleados

    def agregar_empleado(self, empleado):
        """Agrega un empleado al departamento."""
        self.empleados.append(empleado)

    def mostrar_empleados(self):
        """Muestra los empleados del departamento."""
        print(f"Empleados del departamento {self.nombre}:")
        for empleado in self.empleados:
            print(f"- {empleado}")

# Ejemplo de uso
departamento_it = Departamento(nombre="Tecnología")
departamento_it.agregar_empleado("Juan Pérez")
departamento_it.agregar_empleado("María González")

departamento_it.mostrar_empleados()
