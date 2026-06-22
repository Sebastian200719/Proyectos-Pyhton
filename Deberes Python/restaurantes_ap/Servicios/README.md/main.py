from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

# Crear el restaurante
restaurante = Restaurante("El Buen Sabor")

# Crear productos
p1 = Producto("Hamburguesa", 3.50, "Comida")
p2 = Producto("Pizza", 5.00, "Comida")
p3 = Producto("Coca Cola", 1.25, "Bebida")

# Crear clientes
c1 = Cliente("Juan Pérez", "0102030405")
c2 = Cliente("María López", "0908070605")

# Agregar productos al restaurante
restaurante.agregar_producto(p1)
restaurante.agregar_producto(p2)
restaurante.agregar_producto(p3)

# Agregar clientes al restaurante
restaurante.agregar_cliente(c1)
restaurante.agregar_cliente(c2)

# Mostrar información en consola
restaurante.listar_productos()
restaurante.listar_clientes()
