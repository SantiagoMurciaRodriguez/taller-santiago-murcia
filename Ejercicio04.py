class CuentaBancaria:
    def __init__(self):
        self._saldo = 0  # Atributo protegido (con un guión bajo al principio)

    def depositar(self, cantidad):
        """Deposita una cantidad en la cuenta."""
        if cantidad > 0:
            self._saldo += cantidad
            print(f"Se depositaron ${cantidad}. Saldo actual: ${self._saldo}")
        else:
            print("La cantidad debe ser mayor que cero.")

    def retirar(self, cantidad):
        """Retira una cantidad de la cuenta."""
        if 0 < cantidad <= self._saldo:
            self._saldo -= cantidad
            print(f"Se retiraron ${cantidad}. Saldo actual: ${self._saldo}")
        else:
            print("Fondos insuficientes o cantidad inválida.")

    def consultar_saldo(self):
        """Consulta el saldo actual."""
        print(f"Saldo actual: ${self._saldo}")

# Ejemplo de uso
mi_cuenta = CuentaBancaria()
mi_cuenta.depositar(1000)
mi_cuenta.retirar(300)
mi_cuenta.consultar_saldo()

class Coche:
    def __init__(self):
        self._velocidad = 0  # Atributo protegido (con un guión bajo al principio)

    def acelerar(self):
        """Aumenta la velocidad del coche."""
        self._velocidad += 1

    def frenar(self):
        """Reduce la velocidad del coche."""
        if self._velocidad > 0:
            self._velocidad -= 1
        else:
            print("El coche ya está detenido.")

    def obtener_velocidad(self):
        """Consulta la velocidad actual del coche."""
        return self._velocidad

# Ejemplo de uso
mi_coche = Coche()
mi_coche.acelerar()
mi_coche.acelerar()
mi_coche.frenar()
print(f"Velocidad actual del coche: {mi_coche.obtener_velocidad()}")
