# Restaurante App - Semana 10

## Información del estudiante

**Nombre:** Edy Nieves

## Descripción

Restaurante App es un sistema desarrollado en Python utilizando Programación Orientada a Objetos. El programa permite administrar productos de un restaurante mediante operaciones de registro, búsqueda, actualización, eliminación y listado.

En la Semana 10 se incorporó el manejo de archivos, excepciones y persistencia de productos utilizando un archivo JSON.

## Estructura del proyecto

```text
restaurante_app/
├── datos/
│   └── productos.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
├── main.py
└── README.md
```

## Componentes

### Producto

La clase `Producto` representa los productos del restaurante. Contiene el nombre, precio y categoría. También posee validaciones y métodos para convertir los objetos a diccionarios y reconstruirlos desde información JSON.

### Usuario

La clase `Usuario` representa a los usuarios del sistema. En esta semana sus datos permanecen solamente en memoria.

### Restaurante

El servicio `Restaurante` administra la colección de productos y realiza las operaciones de registrar, buscar, actualizar, eliminar y listar.

### ArchivoServicio

`ArchivoServicio` es responsable de leer y escribir el archivo `datos/productos.json`.

Utiliza:

* `with open()`
* `json.load()`
* `json.dump()`
* Codificación UTF-8

### main.py

Es el punto de entrada de la aplicación. Coordina el menú, recibe información mediante `input()`, carga los productos al iniciar y solicita guardar los cambios realizados.

## Persistencia JSON

Los productos se almacenan en:

```text
datos/productos.json
```

Antes de guardar, cada objeto `Producto` se convierte en un diccionario compatible con JSON.

Cuando la aplicación inicia, `ArchivoServicio` utiliza `json.load()` para recuperar los datos y posteriormente reconstruye cada registro como un objeto `Producto`.

De esta manera, los productos no se pierden cuando se cierra la aplicación.

## Flujo de carga

1. Se ejecuta `main.py`.
2. Se crea `ArchivoServicio`.
3. Se intenta leer `datos/productos.json`.
4. Se recuperan los datos mediante `json.load()`.
5. Se validan los registros.
6. Los registros válidos se convierten nuevamente en objetos `Producto`.
7. Los productos se entregan al servicio `Restaurante`.
8. El programa continúa funcionando normalmente.

## Flujo de guardado

Cuando se registra, actualiza o elimina un producto:

1. `Restaurante` modifica la colección.
2. `main.py` solicita guardar los productos.
3. Los objetos `Producto` se convierten en diccionarios.
4. `ArchivoServicio` utiliza `json.dump()`.
5. Se actualiza `datos/productos.json`.

## Manejo de excepciones

El programa controla diferentes situaciones:

* `FileNotFoundError`: permite iniciar el programa aunque todavía no exista `productos.json`.
* `json.JSONDecodeError`: controla archivos JSON con formato incorrecto.
* `PermissionError`: controla problemas de permisos de lectura o escritura.
* `KeyError`: controla registros que no contienen las claves esperadas.
* `ValueError`: controla datos inválidos, especialmente durante las validaciones de `Producto`.

## Ejecución

Para ejecutar el programa se debe abrir una terminal dentro de la carpeta del proyecto y ejecutar:

```bash
python main.py
```

También puede utilizarse:

```bash
python3 main.py
```

## Comprobación de persistencia

Para comprobar que la persistencia funciona:

1. Ejecutar `main.py`.
2. Registrar uno o más productos.
3. Revisar el archivo `datos/productos.json`.
4. Cerrar completamente el programa.
5. Ejecutar nuevamente `main.py`.
6. Seleccionar la opción de listar productos.
7. Comprobar que los productos registrados anteriormente continúan disponibles.
8. Actualizar o eliminar un producto.
9. Cerrar y ejecutar nuevamente el programa.
10. Comprobar que el cambio también se conservó.

## Conclusión

La Semana 10 permitió incorporar persistencia de datos mediante archivos JSON al proyecto `restaurante_app`. Los productos pueden guardarse, recuperarse y reconstruirse como objetos `Producto`, manteniendo la arquitectura modular y el funcionamiento del sistema.
