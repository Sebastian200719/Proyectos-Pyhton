from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.restaurante import Restaurante


restaurante = Restaurante()


def mostrar_menu() -> None:
    """Muestra el menú principal."""

    print("\n========================================")
    print("         SISTEMA DE RESTAURANTE")
    print("========================================")
    print("1. Registrar producto")
    print("2. Buscar producto")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Listar productos")
    print("----------------------------------------")
    print("6. Registrar usuario")
    print("7. Listar usuarios")
    print("----------------------------------------")
    print("8. Mostrar categorías")
    print("9. Salir")
    print("========================================")


def registrar_producto() -> None:
    """Solicita datos y registra un producto."""

    print("\n--- REGISTRAR PRODUCTO ---")

    codigo = input("Ingrese el código: ").strip()

    if not codigo:
        print("El código no puede estar vacío.")
        return

    if restaurante.buscar_producto(codigo) is not None:
        print("Error: ya existe un producto con ese código.")
        return

    nombre = input("Ingrese el nombre: ").strip()
    categoria = input("Ingrese la categoría: ").strip()

    if not nombre or not categoria:
        print("El nombre y la categoría son obligatorios.")
        return

    try:
        precio = float(input("Ingrese el precio: "))

        if precio < 0:
            print("El precio no puede ser negativo.")
            return

    except ValueError:
        print("Error: el precio debe ser un número.")
        return

    producto = Producto(
        codigo=codigo,
        nombre=nombre,
        categoria=categoria,
        precio=precio
    )

    if restaurante.registrar_producto(producto):
        print("Producto registrado correctamente.")
    else:
        print("No se pudo registrar el producto.")


def buscar_producto() -> None:
    """Busca un producto mediante su código."""

    print("\n--- BUSCAR PRODUCTO ---")

    codigo = input("Ingrese el código del producto: ").strip()

    producto = restaurante.buscar_producto(codigo)

    if producto is None:
        print("Producto no encontrado.")
    else:
        print("\nProducto encontrado:")
        print(producto)


def actualizar_producto() -> None:
    """Actualiza la información de un producto."""

    print("\n--- ACTUALIZAR PRODUCTO ---")

    codigo = input("Ingrese el código del producto: ").strip()

    producto = restaurante.buscar_producto(codigo)

    if producto is None:
        print("Producto no encontrado.")
        return

    print(f"Producto actual: {producto}")

    nombre = input("Nuevo nombre: ").strip()
    categoria = input("Nueva categoría: ").strip()

    if not nombre or not categoria:
        print("El nombre y la categoría son obligatorios.")
        return

    try:
        precio = float(input("Nuevo precio: "))

        if precio < 0:
            print("El precio no puede ser negativo.")
            return

    except ValueError:
        print("Error: el precio debe ser un número.")
        return

    actualizado = restaurante.actualizar_producto(
        codigo,
        nombre,
        categoria,
        precio
    )

    if actualizado:
        print("Producto actualizado correctamente.")
    else:
        print("No se pudo actualizar el producto.")


def eliminar_producto() -> None:
    """Elimina un producto mediante su código."""

    print("\n--- ELIMINAR PRODUCTO ---")

    codigo = input("Ingrese el código del producto: ").strip()

    producto = restaurante.buscar_producto(codigo)

    if producto is None:
        print("Producto no encontrado.")
        return

    print(f"\nProducto seleccionado: {producto}")

    confirmacion = input(
        "¿Está seguro de eliminarlo? (s/n): "
    ).strip().lower()

    if confirmacion == "s":
        if restaurante.eliminar_producto(codigo):
            print("Producto eliminado correctamente.")
        else:
            print("No se pudo eliminar el producto.")
    else:
        print("Operación cancelada.")


def listar_productos() -> None:
    """Muestra todos los productos registrados."""

    print("\n--- LISTA DE PRODUCTOS ---")

    productos = restaurante.listar_productos()

    if not productos:
        print("No existen productos registrados.")
        return

    for numero, producto in enumerate(productos, start=1):
        print(f"{numero}. {producto}")


def registrar_usuario() -> None:
    """Solicita datos y registra un usuario."""

    print("\n--- REGISTRAR USUARIO ---")

    identificacion = input("Ingrese la identificación: ").strip()

    if not identificacion:
        print("La identificación no puede estar vacía.")
        return

    for usuario in restaurante.listar_usuarios():
        if usuario.identificacion == identificacion:
            print("Error: ya existe un usuario con esa identificación.")
            return

    nombre = input("Ingrese el nombre: ").strip()
    correo = input("Ingrese el correo: ").strip()

    if not nombre or not correo:
        print("El nombre y el correo son obligatorios.")
        return

    usuario = Usuario(
        identificacion=identificacion,
        nombre=nombre,
        correo=correo
    )

    if restaurante.registrar_usuario(usuario):
        print("Usuario registrado correctamente.")
    else:
        print("No se pudo registrar el usuario.")


def listar_usuarios() -> None:
    """Muestra todos los usuarios registrados."""

    print("\n--- LISTA DE USUARIOS ---")

    usuarios = restaurante.listar_usuarios()

    if not usuarios:
        print("No existen usuarios registrados.")
        return

    for numero, usuario in enumerate(usuarios, start=1):
        print(f"{numero}. {usuario}")


def mostrar_categorias() -> None:
    """Muestra las categorías únicas de los productos."""

    print("\n--- CATEGORÍAS DE PRODUCTOS ---")

    categorias = restaurante.obtener_categorias()

    if not categorias:
        print("No existen categorías registradas.")
        return

    for categoria in sorted(categorias):
        print(f"- {categoria}")


def ejecutar_opcion(opcion: int) -> bool:
    """
    Ejecuta la función correspondiente a la opción seleccionada.

    Retorna False cuando el usuario selecciona salir.
    """

    funciones: dict[int, callable] = {
        1: registrar_producto,
        2: buscar_producto,
        3: actualizar_producto,
        4: eliminar_producto,
        5: listar_productos,
        6: registrar_usuario,
        7: listar_usuarios,
        8: mostrar_categorias
    }

    if opcion == 9:
        return False

    funcion = funciones.get(opcion)

    if funcion is None:
        print("Opción inválida. Seleccione una opción del 1 al 9.")
        return True

    funcion()
    return True


def main() -> None:
    """Función principal del programa."""

    print("\nBienvenido al Sistema de Restaurante")

    continuar = True

    while continuar:
        mostrar_menu()

        try:
            opcion = int(input("Seleccione una opción: "))
            continuar = ejecutar_opcion(opcion)

        except ValueError:
            print("Error: debe ingresar un número del menú.")

    print("\nGracias por utilizar el Sistema de Restaurante.")


if __name__ == "__main__":
    main()