from typing import Optional, Callable

from modelos.producto import Producto
from modelos.usuario import Usuario


class Restaurante:
    def __init__(self) -> None:
        # LISTAS:
        # Se utilizan para almacenar las colecciones dinámicas.
        self.productos: list[Producto] = []
        self.usuarios: list[Usuario] = []

        # TUPLA:
        # Contiene información estable del sistema.
        self.opciones_menu: tuple[str, ...] = (
            "Registrar producto",
            "Buscar producto",
            "Actualizar producto",
            "Eliminar producto",
            "Listar productos",
            "Registrar usuario",
            "Listar usuarios",
            "Mostrar categorías",
            "Salir"
        )

        # DICCIONARIO:
        # Relación clave -> descripción de la opción.
        self.menu_descripciones: dict[int, str] = {
            1: "Registrar producto",
            2: "Buscar producto",
            3: "Actualizar producto",
            4: "Eliminar producto",
            5: "Listar productos",
            6: "Registrar usuario",
            7: "Listar usuarios",
            8: "Mostrar categorías",
            9: "Salir"
        }

    # ==========================================================
    # PRODUCTOS
    # ==========================================================

    def registrar_producto(self, producto: Producto) -> bool:
        """Registra un producto evitando códigos duplicados."""

        if self.buscar_producto(producto.codigo) is not None:
            return False

        self.productos.append(producto)
        return True

    def buscar_producto(self, codigo: str) -> Optional[Producto]:
        """Busca un producto por su código."""

        for producto in self.productos:
            if producto.codigo == codigo:
                return producto

        return None

    def actualizar_producto(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float
    ) -> bool:
        """Actualiza los datos de un producto."""

        producto = self.buscar_producto(codigo)

        if producto is None:
            return False

        producto.nombre = nombre
        producto.categoria = categoria
        producto.precio = precio

        return True

    def eliminar_producto(self, codigo: str) -> bool:
        """Elimina un producto mediante su código."""

        producto = self.buscar_producto(codigo)

        if producto is None:
            return False

        self.productos.remove(producto)
        return True

    def listar_productos(self) -> list[Producto]:
        """Devuelve la lista de productos."""

        return self.productos.copy()

    # ==========================================================
    # USUARIOS
    # ==========================================================

    def registrar_usuario(self, usuario: Usuario) -> bool:
        """Registra un usuario evitando identificaciones duplicadas."""

        for usuario_registrado in self.usuarios:
            if usuario_registrado.identificacion == usuario.identificacion:
                return False

        self.usuarios.append(usuario)
        return True

    def listar_usuarios(self) -> list[Usuario]:
        """Devuelve la lista de usuarios."""

        return self.usuarios.copy()

    # ==========================================================
    # CONJUNTO
    # ==========================================================

    def obtener_categorias(self) -> set[str]:
        """
        Obtiene las categorías de los productos sin duplicados.
        Se utiliza un conjunto (set).
        """

        return {producto.categoria for producto in self.productos}

    # ==========================================================
    # DICCIONARIO
    # ==========================================================

    def obtener_menu(self) -> dict[int, str]:
        """Devuelve el diccionario de opciones del menú."""

        return self.menu_descripciones.copy()