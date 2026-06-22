class Restaurante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []
        self.clientes = []

    # agregar producto
    def agregar_producto(self, producto):
        self.productos.append(producto)

    # agregar cliente
    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    # mostrar productos
    def listar_productos(self):
        print("\n--- PRODUCTOS DEL RESTAURANTE ---")
        for p in self.productos:
            print(p)

    # mostrar clientes
    def listar_clientes(self):
        print("\n--- CLIENTES REGISTRADOS ---")
        for c in self.clientes:
            print(c)