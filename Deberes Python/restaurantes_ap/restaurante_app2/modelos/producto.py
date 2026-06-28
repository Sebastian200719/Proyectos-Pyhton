class Producto:
    # Constructor de la clase Producto
    def __init__(self, nombre: str, precio: float, cantidad: int, disponible: bool):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.disponible = disponible

    # Devuelve la información del producto como texto
    def __str__(self):
        return (
            f"Producto: {self.nombre}\n"
            f"Precio: ${self.precio}\n"
            f"Cantidad: {self.cantidad}\n"
            f"Disponible: {self.disponible}"
        )