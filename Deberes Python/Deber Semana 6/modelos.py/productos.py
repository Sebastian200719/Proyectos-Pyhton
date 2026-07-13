class Producto:
    def __init__(self, nombre, categoria, precio, disponible=True):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.disponible = disponible

    # Nombre
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if valor.strip() == "":
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = valor

    # Categoría
    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, valor):
        if valor.strip() == "":
            raise ValueError("La categoría no puede estar vacía.")
        self._categoria = valor

    # Precio
    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        if valor <= 0:
            raise ValueError("El precio debe ser mayor que cero.")
        self._precio = valor

    def mostrar_informacion(self):
        estado = "Disponible" if self.disponible else "No disponible"
        return (f"Nombre: {self.nombre} | "
                f"Categoría: {self.categoria} | "
                f"Precio: ${self.precio:.2f} | "
                f"{estado}")