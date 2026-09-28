from datetime import datetime
from modelos.venta import Venta


class RestauranteServicio:

    def __init__(self):
        self.ventas = []

    def registrar_venta(self, usuario, producto):
        if not usuario:
            return False, "Debe seleccionar un usuario."

        if not producto:
            return False, "Debe seleccionar un producto."

        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        venta = Venta(
            usuario=usuario,
            producto=producto,
            fecha=fecha
        )

        self.ventas.append(venta)

        return True, "Venta registrada correctamente."

    def obtener_ventas(self):
        return self.ventas