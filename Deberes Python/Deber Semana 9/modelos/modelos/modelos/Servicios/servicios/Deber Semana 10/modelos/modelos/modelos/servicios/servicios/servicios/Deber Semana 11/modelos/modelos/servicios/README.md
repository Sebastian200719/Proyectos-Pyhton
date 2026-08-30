# restaurante_app - Semana 11

## Estudiante

Edy Nieves

## Descripción

Restaurante App es una aplicación desarrollada en Python utilizando Programación Orientada a Objetos. En la Semana 11 se amplió el proyecto para trabajar con colecciones de objetos, relaciones entre usuarios y productos, control de stock y persistencia mediante archivos JSON.

## Estructura

```text
restaurante_app/
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
├── main.py
└── README.md
```

## Componentes

### Producto

Representa los productos del restaurante y contiene código, nombre, precio y stock disponible.

### Usuario

Representa a las personas registradas que pueden realizar compras.

### Venta

Representa la relación entre un usuario y un producto. Contiene la identificación del usuario, código del producto y cantidad vendida.

### Restaurante

Administra las colecciones de productos, usuarios y ventas. También contiene las reglas de negocio para realizar ventas y consultar las ventas de un usuario.

### ArchivoServicio

Se encarga de guardar y recuperar productos, usuarios y ventas mediante archivos JSON.

### main.py

Es el punto de entrada del programa y permite al usuario interactuar mediante un menú por consola.

## Control de stock

Antes de realizar una venta se verifica que el producto exista, que el usuario esté registrado, que la cantidad sea mayor que cero y que exista suficiente stock.

Cuando la venta es válida, el stock del producto disminuye.

No se permite que el stock tenga valores negativos.

## Relación Usuario - Producto - Venta

Una venta relaciona un usuario registrado con un producto existente.

El proceso es:

1. Se identifica al usuario.
2. Se busca el producto.
3. Se valida la cantidad.
4. Se verifica el stock.
5. Se crea una Venta.
6. Se agrega la venta a la colección.
7. Se disminuye el stock.
8. Se guardan los cambios en los archivos JSON.

## Persistencia

El sistema utiliza tres archivos:

* `productos.json`: almacena productos y su stock actualizado.
* `usuarios.json`: almacena usuarios registrados.
* `ventas.json`: almacena las ventas realizadas.

Se utilizan `json.dump()`, `json.load()`, `with open()` y codificación UTF-8.

## Excepciones controladas

El programa controla:

* `FileNotFoundError`
* `json.JSONDecodeError`
* `PermissionError`
* `KeyError`
* `ValueError`

Los archivos que todavía no existen permiten iniciar el programa con colecciones vacías.

## Ejecución

Para ejecutar el programa se utiliza:

```bash
python main.py
```

## Pruebas realizadas

Se realizaron las siguientes pruebas:

1. Registrar un usuario.
2. Registrar un producto con stock.
3. Realizar una venta válida.
4. Comprobar que el stock disminuya.
5. Comprobar que la venta se almacene en `ventas.json`.
6. Consultar las ventas de un usuario.
7. Cerrar y volver a ejecutar el programa.
8. Comprobar la recuperación de productos, usuarios y ventas.
9. Intentar vender una cantidad superior al stock disponible.
10. Comprobar que la venta sea rechazada y que el stock no se modifique.

## Conclusión

La mejora de la Semana 11 permite trabajar con colecciones de objetos y establecer una relación entre usuarios, productos y ventas. Además, el sistema conserva la información mediante archivos JSON, permitiendo recuperar los datos después de cerrar y ejecutar nuevamente la aplicación.
