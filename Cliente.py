class Cliente:
    def __init__(self, nombre, apellido, genero, ocupacion):
        # Se corrigen los atributos para que tomen los valores pasados como parámetro
        self.nombre = nombre  # Usa el setter para la validación inicial
        self.apellido = apellido
        self.genero = genero
        self.ocupacion = ocupacion

    @staticmethod
    def _validar_cadena(value, attr_name):
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"El {attr_name} no puede estar vacío y debe ser una cadena.")
        return value

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = self._validar_cadena(value, "nombre")

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, value):
        self._apellido = self._validar_cadena(value, "apellido")

    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, value):
        self._genero = self._validar_cadena(value, "género")

    @property
    def ocupacion(self):
        return self._ocupacion

    @ocupacion.setter
    def ocupacion(self, value):
        self._ocupacion = self._validar_cadena(value, "ocupación")

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} {self.apellido}."

    def __str__(self):
        return (f"Detalles del Cliente: {self.nombre} {self.apellido} | "
                f"Género: {self.genero} | Ocupación: {self.ocupacion}")


# Demostración de la clase Cliente con los cambios:
print("Demostración de la clase Cliente:")

# Crear un objeto Cliente
cliente1 = Cliente("Ana", "García", "Femenino", "Ingeniera")
print(f"Cliente 1: {cliente1}")

# Acceder a los atributos usando los getters
print(f"Nombre de Cliente 1: {cliente1.nombre}")
print(f"Ocupación de Cliente 1: {cliente1.ocupacion}")

# Modificar un atributo usando el setter
cliente1.ocupacion = "Científica de Datos"
print(f"Cliente 1 después de cambiar ocupación: {cliente1}")

# Usar el nuevo método saludar
print(f"Saludo de Cliente 1: {cliente1.saludar()}")

# Intentar asignar un valor inválido (esto generará un error)
try:
    cliente1.nombre = ""
except ValueError as e:
    print(f"Error al intentar cambiar el nombre a un valor vacío: {e}")

try:
    cliente2 = Cliente("", "Pérez", "Masculino", "Desarrollador")
except ValueError as e:
    print(f"Error al crear Cliente 2 con nombre vacío: {e}")
