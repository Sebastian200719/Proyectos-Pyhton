# Restaurante App

## Nombre del estudiante

Escriba aquí su nombre completo.

## Descripción

Este proyecto fue desarrollado en Python aplicando los principios de la Programación Orientada a Objetos.

El sistema administra productos de un restaurante mediante una estructura modular.

## Estructura

```
restaurante_app/
│
├── modelos/
│   ├── producto.py
│   ├── platillo.py
│   └── bebida.py
│
├── servicios/
│   └── restaurante.py
│
└── main.py
```

## Herencia

La clase Producto es la clase padre.

Las clases Platillo y Bebida heredan sus atributos y métodos mediante el uso de super().

## Encapsulación

El atributo precio fue encapsulado utilizando __precio.

Su acceso se realiza mediante:

- obtener_precio()
- cambiar_precio()

## Polimorfismo

Las clases Platillo y Bebida sobrescriben el método mostrar_informacion(), mostrando información diferente para cada tipo de producto.

## Reflexión

La Programación Orientada a Objetos facilita la reutilización del código, mejora la organización del proyecto y permite desarrollar aplicaciones más fáciles de mantener y ampliar.