# Importar las clases necesarias
from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

# Crear un objeto de la clase Restaurante
restaurante = Restaurante()

# Crear dos productos
producto1 = Producto("Pizza", 12.50, 10, True)
producto2 = Producto("Hamburguesa", 8.99, 15, True)

# Crear dos clientes
cliente1 = Cliente("Juan Pérez", 20, "juan@gmail.com", True)
cliente2 = Cliente("María López", 25, "maria@gmail.com", True)

# Agregar los productos al restaurante
restaurante.agregar_producto(producto1)
restaurante.agregar_producto(producto2)

# Agregar los clientes al restaurante
restaurante.agregar_cliente(cliente1)
restaurante.agregar_cliente(cliente2)

# Mostrar la información registrada
restaurante.mostrar_productos()
restaurante.mostrar_clientes()