import json
from pathlib import Path
from typing import List

from modelos.producto import Producto


class ArchivoServicio:
    def __init__(self, ruta_archivo: str = "datos/productos.json") -> None:
        self.ruta_archivo = Path(ruta_archivo)

    def guardar_productos(self, productos: List[Producto]) -> bool:
        try:
            self.ruta_archivo.parent.mkdir(parents=True, exist_ok=True)

            datos = [producto.to_dict() for producto in productos]

            with open(
                self.ruta_archivo,
                "w",
                encoding="utf-8"
            ) as archivo:
                json.dump(
                    datos,
                    archivo,
                    ensure_ascii=False,
                    indent=4
                )

            return True

        except PermissionError:
            print("Error: no existen permisos para escribir el archivo.")
            return False

    def cargar_productos(self) -> List[Producto]:
        try:
            with open(
                self.ruta_archivo,
                "r",
                encoding="utf-8"
            ) as archivo:
                datos = json.load(archivo)

            if not isinstance(datos, list):
                raise ValueError(
                    "El archivo JSON debe contener una lista de productos."
                )

            productos: List[Producto] = []

            for registro in datos:
                try:
                    if not isinstance(registro, dict):
                        raise ValueError(
                            "El registro de producto no es válido."
                        )

                    producto = Producto.from_dict(registro)
                    productos.append(producto)

                except (KeyError, ValueError, TypeError) as error:
                    print(
                        f"Advertencia: se omitió un producto inválido: {error}"
                    )

            return productos

        except FileNotFoundError:
            print("Archivo productos.json no encontrado. Se iniciará vacío.")
            return []

        except json.JSONDecodeError:
            print("Error: productos.json contiene un JSON inválido.")
            return []

        except PermissionError:
            print("Error: no existen permisos para leer el archivo.")
            return []

        except ValueError as error:
            print(f"Error en la estructura del archivo: {error}")
            return []