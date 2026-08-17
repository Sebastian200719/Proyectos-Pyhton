from dataclasses import dataclass


@dataclass
class Producto:
    codigo: str
    nombre: str
    categoria: str
    precio: float

    def __str__(self) -> str:
        return (
            f"Código: {self.codigo} | "
            f"Nombre: {self.nombre} | "
            f"Categoría: {self.categoria} | "
            f"Precio: ${self.precio:.2f}"
        )