from dataclasses import dataclass


@dataclass
class Usuario:
    identificacion: str
    nombre: str
    correo: str

    def __str__(self) -> str:
        return (
            f"ID: {self.identificacion} | "
            f"Nombre: {self.nombre} | "
            f"Correo: {self.correo}"
        )