class Cliente:
    def __init__(self, nombre: str, edad: int, correo: str, activo: bool):
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
        self.activo = activo

    def __str__(self):
        return (
            f"Cliente: {self.nombre} | "
            f"Edad: {self.edad} | "
            f"Correo: {self.correo} | "
            f"Activo: {self.activo}"
        )