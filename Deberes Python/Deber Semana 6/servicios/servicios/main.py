from modelos.platillo import Platillo
from modelos.bebida import Bebida
from servicios.restaurante import Restaurante

# Crear restaurante
restaurante = Restaurante()

# Crear platillos
platillo1 = Platillo("Arroz con Pollo", 6.50, True, 650)
platillo2 = Platillo("Seco de Carne", 7.75, True, 850)

# Crear bebidas
bebida1 = Bebida("Jugo de Naranja", 2.50, True, 500)
bebida2 = Bebida("Gaseosa", 1.75, False, 600)

# Cambiar precio usando encapsulación
platillo1.cambiar_precio(7.00)

# Agregar productos
restaurante.agregar_producto(platillo1)
restaurante.agregar_producto(platillo2)
restaurante.agregar_producto(bebida1)
restaurante.agregar_producto(bebida2)

# Mostrar menú
restaurante.mostrar_productos()