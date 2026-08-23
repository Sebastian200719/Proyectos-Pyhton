from dataclasses import dataclass


@dataclass
class Producto:
    nombre: str
    precio: float
    categoria: str

    def __post_init__(self) -> None:
        self.nombre = self.nombre.strip()
        self.categoria = self.categoria.strip()

        if not self.nombre:
            raise ValueError("El nombre del producto no puede estar vacío.")

        if self.precio <= 0:
            raise ValueError("El precio debe ser mayor que 0.")

        if not self.categoria:
            raise ValueError("La categoría no puede estar vacía.")

    def to_dict(self) -> dict:
        return {
            "nombre": self.nombre,
            "precio": self.precio,
            "categoria": self.categoria
        }

    @classmethod
    def from_dict(cls, datos: dict) -> "Producto":
        return cls(
            nombre=datos["nombre"],
            precio=float(datos["precio"]),
            categoria=datos["categoria"]
        )

    def __str__(self) -> str:
        return (
            f"Nombre: {self.nombre} | "
            f"Precio: ${self.precio:.2f} | "
            f"Categoría: {self.categoria}"
        )