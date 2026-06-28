from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:
    # Constructor de la clase Restaurante
    def __init__(self):
        # Lista para almacenar los productos
        self.productos: list[Producto] = []

        # Lista para almacenar los clientes
        self.clientes: list[Cliente] = []

    # Agrega un producto a la lista
    def agregar_producto(self, producto: Producto):
        self.productos.append(producto)

    # Agrega un cliente a la lista
    def agregar_cliente(self, cliente: Cliente):
        self.clientes.append(cliente)

    # Muestra todos los productos
    def mostrar_productos(self):
        print("===== PRODUCTOS =====")
        for producto in self.productos:
            print(producto)
            print("--------------------")

    # Muestra todos los clientes
    def mostrar_clientes(self):
        print("\n===== CLIENTES =====")
        for cliente in self.clientes:
            print(cliente)
            print("--------------------")