print("")
print("guzman jared 1188")
print("")
#abrimos clase llamada cuenta
class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        self.titular = titular
        self.cantidad = cantidad

    # Métodos para mostrar los datos de la cuenta
    def mostrar(self):
        print(f"Titular: {self.titular}")
        print(f"Cantidad en cuenta: {self.cantidad:.2f}")
    
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad
    
    def retirar(self, cantidad):
        if cantidad > 0:
            self.cantidad -= cantidad

# Crear una cuenta con un titular y un saldo inicial
cuenta1 = Cuenta("guzman", 5000.0)

# Mostrar los datos de la cuenta
cuenta1.mostrar()

# Ingresar dinero en la cuenta
cuenta1.ingresar(100.0)
print("Después de ingresar 100.0:")
cuenta1.mostrar()

# Retirar dinero de la cuenta
cuenta1.retirar(200.0)
print("Después de retirar 200.0:")
cuenta1.mostrar()

# ingresar una cantidad negativa
cuenta1.ingresar(-100)
print("Intentando ingresar una cantidad negativa:")
cuenta1.mostrar()

# retirar una cantidad negativa
cuenta1.retirar(-50)
print("Intentando retirar una cantidad negativa:")
cuenta1.mostrar()