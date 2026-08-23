from modelos.producto import Producto
from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante import Restaurante


def mostrar_menu() -> None:
    print("\n" + "=" * 45)
    print("       RESTAURANTE APP")
    print("=" * 45)
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Salir")
    print("=" * 45)


def registrar_producto(
    restaurante: Restaurante,
    archivo_servicio: ArchivoServicio
) -> None:

    print("\n--- REGISTRAR PRODUCTO ---")

    nombre = input("Nombre: ")
    categoria = input("Categoría: ")

    try:
        precio = float(input("Precio: "))

        producto = Producto(
            nombre=nombre,
            precio=precio,
            categoria=categoria
        )

        if restaurante.registrar_producto(producto):
            archivo_servicio.guardar_productos(
                restaurante.listar_productos()
            )
            print("Producto registrado correctamente.")
        else:
            print("Ya existe un producto con ese nombre.")

    except ValueError as error:
        print(f"Error: {error}")


def listar_productos(restaurante: Restaurante) -> None:
    print("\n--- LISTA DE PRODUCTOS ---")

    productos = restaurante.listar_productos()

    if not productos:
        print("No existen productos registrados.")
        return

    for numero, producto in enumerate(productos, start=1):
        print(f"{numero}. {producto}")


def buscar_producto(restaurante: Restaurante) -> None:
    print("\n--- BUSCAR PRODUCTO ---")

    nombre = input("Ingrese el nombre del producto: ")

    producto = restaurante.buscar_producto(nombre)

    if producto is None:
        print("Producto no encontrado.")
    else:
        print("Producto encontrado:")
        print(producto)


def actualizar_producto(
    restaurante: Restaurante,
    archivo_servicio: ArchivoServicio
) -> None:

    print("\n--- ACTUALIZAR PRODUCTO ---")

    nombre_actual = input("Nombre del producto a actualizar: ")

    producto = restaurante.buscar_producto(nombre_actual)

    if producto is None:
        print("Producto no encontrado.")
        return

    print(f"Producto actual: {producto}")

    nuevo_nombre = input(
        f"Nuevo nombre [{producto.nombre}]: "
    ).strip()

    nuevo_precio_texto = input(
        f"Nuevo precio [{producto.precio}]: "
    ).strip()

    nueva_categoria = input(
        f"Nueva categoría [{producto.categoria}]: "
    ).strip()

    if not nuevo_nombre:
        nuevo_nombre = producto.nombre

    if not nueva_categoria:
        nueva_categoria = producto.categoria

    try:
        if nuevo_precio_texto:
            nuevo_precio = float(nuevo_precio_texto)
        else:
            nuevo_precio = producto.precio

        actualizado = restaurante.actualizar_producto(
            nombre_actual,
            nuevo_nombre,
            nuevo_precio,
            nueva_categoria
        )

        if actualizado:
            archivo_servicio.guardar_productos(
                restaurante.listar_productos()
            )
            print("Producto actualizado correctamente.")
        else:
            print(
                "No se pudo actualizar. "
                "Puede que el nuevo nombre ya exista."
            )

    except ValueError as error:
        print(f"Error: {error}")


def eliminar_producto(
    restaurante: Restaurante,
    archivo_servicio: ArchivoServicio
) -> None:

    print("\n--- ELIMINAR PRODUCTO ---")

    nombre = input("Nombre del producto a eliminar: ")

    producto = restaurante.buscar_producto(nombre)

    if producto is None:
        print("Producto no encontrado.")
        return

    print(f"Producto encontrado: {producto}")

    confirmacion = input(
        "¿Está seguro de eliminarlo? (s/n): "
    ).strip().lower()

    if confirmacion != "s":
        print("Operación cancelada.")
        return

    if restaurante.eliminar_producto(nombre):
        archivo_servicio.guardar_productos(
            restaurante.listar_productos()
        )
        print("Producto eliminado correctamente.")
    else:
        print("No se pudo eliminar el producto.")


def main() -> None:
    restaurante = Restaurante()
    archivo_servicio = ArchivoServicio()

    productos_guardados = archivo_servicio.cargar_productos()
    restaurante.cargar_productos(productos_guardados)

    print(
        f"\nSe cargaron {len(productos_guardados)} "
        "producto(s) desde productos.json."
    )

    while True:
        mostrar_menu()

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_producto(restaurante, archivo_servicio)

        elif opcion == "2":
            listar_productos(restaurante)

        elif opcion == "3":
            buscar_producto(restaurante)

        elif opcion == "4":
            actualizar_producto(restaurante, archivo_servicio)

        elif opcion == "5":
            eliminar_producto(restaurante, archivo_servicio)

        elif opcion == "6":
            print("Programa finalizado.")
            break

        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()