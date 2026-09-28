class Venta:
    def __init__(self, usuario, producto, fecha):
        self.usuario = usuario
        self.producto = producto
        self.fecha = fecha

    def to_dict(self):
        return {
            "usuario": self.usuario,
            "producto": self.producto,
            "fecha": self.fecha
        }

    @staticmethod
    def from_dict(data):
        return Venta(
            data["usuario"],
            data["producto"],
            data["fecha"]
        )