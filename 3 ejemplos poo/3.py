print(" ")
print("guzman 1188")
print(" ")
class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, value):
        if not isinstance(value, str):
            raise ValueError("El nombre debe ser una cadena de texto.")
        self._nombre = value
    @property
    def edad(self):
        return self._edad
    @edad.setter
    def edad(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("La edad debe ser un entero positivo.")
        self._edad = value
    @property
    def dni(self):
        return self._dni
    @dni.setter
    def dni(self, value):
        if not isinstance(value, str) or len(value) != 9:
            raise ValueError("El DNI debe ser una cadena de 9 caracteres.")
        self._dni = value
    def mostrar(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.dni}"
    def esMayorDeEdad(self):
        return self.edad >= 18
class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        if not isinstance(titular, Persona):
            raise ValueError("El titular debe ser una instancia de la clase Persona.")
        self.titular = titular
        self._cantidad = float(cantidad)
    @property
    def cantidad(self):
        return self._cantidad
    def ingresar(self, cantidad):
        if cantidad > 0:
            self._cantidad += cantidad
    def retirar(self, cantidad):
        self._cantidad -= cantidad
    def mostrar(self):
        return f"Titular: {self.titular.mostrar()}, Cantidad: {self.cantidad:.2f}"
class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0.0, bonificacion=0.0):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion
    @property
    def bonificacion(self):
        return self._bonificacion
    @bonificacion.setter
    def bonificacion(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("La bonificación debe ser un número positivo.")
        self._bonificacion = value
    def esTitularValido(self):
        return self.titular.esMayorDeEdad() and self.titular.edad < 25
    def retirar(self, cantidad):
        if self.esTitularValido():
            super().retirar(cantidad)
        else:
            raise PermissionError("El titular no es válido para retirar dinero.")
    def mostrar(self):
        return (f"Cuenta Joven\nTitular: {self.titular.mostrar()}, "
                f"Cantidad: {self.cantidad:.2f}, Bonificación: {self.bonificacion}%")
try:
    persona1 = Persona("guzman jared", 19, "y8903484u")  # Titular válido
    cuenta_joven = CuentaJoven(persona1, 1500.0, 5.0)  
    print(cuenta_joven.mostrar())  # Mostrar datos iniciales
    cuenta_joven.ingresar(500)     # Ingresar 500
    cuenta_joven.retirar(300)      # Retirar 300
    print(cuenta_joven.mostrar())  # Mostrar datos actualizados
    persona2 = Persona("Carlos Sánchez", 30, "12345678C")  # Titular no válido
    cuenta_joven_no_valida = CuentaJoven(persona2, 2000.0, 3.0)
    cuenta_joven_no_valida.retirar(100)  # Esto generará un error
except Exception as e:
    print(f"Error: {e}")