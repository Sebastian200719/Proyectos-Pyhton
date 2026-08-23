class Usuario:
    def __init__(self, nombre: str, correo: str) -> None:
        self.nombre = nombre
        self.correo = correo

    def __str__(self) -> str:
        return f"Usuario: {self.nombre} | Correo: {self.correo}"