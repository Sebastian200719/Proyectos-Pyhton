class Producto:
    def __init__(self, nombre, precio, tipo):
        # Atributos del producto
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo  # Ejemplo: comida, bebida, postre

    def __str__(self):
        # Representación en texto del objeto
        return f"Producto: {self.nombre} | Tipo: {self.tipo} | Precio: ${self.precio:.2f}"