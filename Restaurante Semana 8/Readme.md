# Restaurante App

## Estudiante

Edy Nieves Otero

## Descripción

Aplicación desarrollada en Python utilizando Programación Orientada a Objetos y arquitectura modular para administrar productos, bebidas y clientes de un restaurante mediante un menú interactivo.

## Estructura

```
restaurante_app/
│
├── modelos/
│   ├── producto.py
│   ├── bebida.py
│   └── cliente.py
│
├── servicios/
│   └── restaurante.py
│
└── main.py
```

## Responsabilidad de cada clase

### Producto

Representa un producto general del restaurante.

### Bebida

Hereda de Producto e incorpora el atributo tamaño.

### Cliente

Representa la información de un cliente.

### Restaurante

Administra el registro y listado de productos y clientes, además de validar códigos e identificaciones repetidas.

### main.py

Controla el menú e interacción con el usuario.

## Relación entre Producto y Bebida

Bebida hereda de Producto porque toda bebida es un tipo de producto. Gracias a esta relación, ambos pueden almacenarse en una misma colección y utilizar el método mostrar_informacion() mediante polimorfismo.

## Principios SOLID

### SRP (Responsabilidad Única)

Cada clase tiene una única responsabilidad.

### OCP (Abierto/Cerrado)

La clase Bebida amplía el sistema sin modificar la lógica del servicio Restaurante.

### LSP (Sustitución de Liskov)

Los objetos Bebida pueden utilizarse como objetos Producto sin afectar el funcionamiento del sistema.

## Ejecución

1. Abrir la carpeta del proyecto.
2. Ejecutar:

```bash
python main.py
```

## Reflexión

La aplicación de los principios SOLID facilita la organización del código, mejora el mantenimiento del proyecto y permite agregar nuevas funcionalidades sin modificar la estructura principal del sistema.