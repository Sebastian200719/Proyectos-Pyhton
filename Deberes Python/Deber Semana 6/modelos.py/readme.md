# Restaurante App

## Estudiante

Edy Nieves Otero

## Descripción

Este proyecto corresponde a la tarea de la Semana 7 de Programación Orientada a Objetos. El sistema permite registrar, listar y buscar productos y clientes mediante un menú interactivo desarrollado en Python.

## Estructura

```
restaurante_app/
│
├── modelos/
│   ├── producto.py
│   └── cliente.py
│
├── servicios/
│   └── restaurante.py
│
└── main.py
```

## Constructor

La clase Producto utiliza el constructor `__init__()` para crear objetos a partir de los datos ingresados por el usuario.

## Uso de @property y @setter

Se utilizan para controlar el acceso a los atributos del producto y validar que:

- El nombre no esté vacío.
- La categoría no esté vacía.
- El precio sea mayor que cero.

## Uso de @dataclass

La clase Cliente utiliza `@dataclass`, lo que facilita la creación automática del constructor y la representación de los objetos.

## Menú interactivo

El programa permite:

- Registrar productos.
- Listar productos.
- Buscar productos.
- Registrar clientes.
- Listar clientes.
- Buscar clientes.
- Salir del sistema.

## Reflexión

La Programación Orientada a Objetos permite organizar mejor el código mediante clases y objetos. El uso de constructores, propiedades y clases de datos mejora la seguridad, legibilidad y mantenimiento del programa. Además, crear objetos a partir de datos ingresados por el usuario hace que la aplicación sea más dinámica y cercana a un sistema real.