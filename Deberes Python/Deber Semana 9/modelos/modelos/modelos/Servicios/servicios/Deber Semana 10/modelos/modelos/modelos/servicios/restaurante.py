from typing import List, Optional

from modelos.producto import Producto


class Restaurante:
    def __init__(self) -> None:
        self._productos: List[Producto] = []

    def registrar_producto(self, producto: Producto) -> bool:
        if self.buscar_producto(producto.nombre) is not None:
            return False

        self._productos.append(producto)
        return True

    def listar_productos(self) -> List[Producto]:
        return self._productos.copy()

    def buscar_producto(self, nombre: str) -> Optional[Producto]:
        nombre_busqueda = nombre.strip().lower()

        for producto in self._productos:
            if producto.nombre.lower() == nombre_busqueda:
                return producto

        return None

    def actualizar_producto(
        self,
        nombre_actual: str,
        nuevo_nombre: str,
        nuevo_precio: float,
        nueva_categoria: str
    ) -> bool:

        producto = self.buscar_producto(nombre_actual)

        if producto is None:
            return False

        producto_actualizado = Producto(
            nombre=nuevo_nombre,
            precio=nuevo_precio,
            categoria=nueva_categoria
        )

        if (
            nuevo_nombre.strip().lower() != nombre_actual.strip().lower()
            and self.buscar_producto(nuevo_nombre) is not None
        ):
            return False

        producto.nombre = producto_actualizado.nombre
        producto.precio = producto_actualizado.precio
        producto.categoria = producto_actualizado.categoria

        return True

    def eliminar_producto(self, nombre: str) -> bool:
        producto = self.buscar_producto(nombre)

        if producto is None:
            return False

        self._productos.remove(producto)
        return True

    def cargar_productos(self, productos: List[Producto]) -> None:
        self._productos = productos.copy()