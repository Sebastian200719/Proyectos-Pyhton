import tkinter as tk
from tkinter import ttk, messagebox


class MainView:

    def __init__(self, root, restaurante_servicio):
        self.root = root
        self.servicio = restaurante_servicio

        self.root.title("Restaurante App")
        self.root.geometry("900x600")

        self.crear_interfaz()

    def crear_interfaz(self):

        titulo = ttk.Label(
            self.root,
            text="Sistema de Restaurante",
            font=("Arial", 20, "bold")
        )
        titulo.pack(pady=20)

        frame_ventas = ttk.LabelFrame(
            self.root,
            text="Registrar Venta"
        )
        frame_ventas.pack(
            padx=20,
            pady=10,
            fill="x"
        )

        ttk.Label(
            frame_ventas,
            text="Usuario:"
        ).grid(row=0, column=0, padx=10, pady=10)

        self.combo_usuario = ttk.Combobox(
            frame_ventas,
            state="readonly",
            width=30
        )
        self.combo_usuario.grid(
            row=0,
            column=1,
            padx=10,
            pady=10
        )

        ttk.Label(
            frame_ventas,
            text="Producto:"
        ).grid(row=1, column=0, padx=10, pady=10)

        self.combo_producto = ttk.Combobox(
            frame_ventas,
            state="readonly",
            width=30
        )
        self.combo_producto.grid(
            row=1,
            column=1,
            padx=10,
            pady=10
        )

        # AQUÍ SE APLICA command=
        boton_venta = ttk.Button(
            frame_ventas,
            text="Registrar venta",
            command=self.registrar_venta
        )
        boton_venta.grid(
            row=2,
            column=0,
            columnspan=2,
            pady=15
        )

        # Tabla de ventas
        frame_tabla = ttk.LabelFrame(
            self.root,
            text="Ventas registradas"
        )
        frame_tabla.pack(
            padx=20,
            pady=10,
            fill="both",
            expand=True
        )

        self.tabla_ventas = ttk.Treeview(
            frame_tabla,
            columns=("usuario", "producto", "fecha"),
            show="headings"
        )

        self.tabla_ventas.heading(
            "usuario",
            text="Usuario"
        )

        self.tabla_ventas.heading(
            "producto",
            text="Producto"
        )

        self.tabla_ventas.heading(
            "fecha",
            text="Fecha"
        )

        self.tabla_ventas.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

    def registrar_venta(self):
        usuario = self.combo_usuario.get()
        producto = self.combo_producto.get()

        correcto, mensaje = self.servicio.registrar_venta(
            usuario,
            producto
        )

        if correcto:
            messagebox.showinfo(
                "Venta",
                mensaje
            )

            self.actualizar_tabla_ventas()

        else:
            messagebox.showwarning(
                "Venta",
                mensaje
            )

    def actualizar_tabla_ventas(self):

        for item in self.tabla_ventas.get_children():
            self.tabla_ventas.delete(item)

        ventas = self.servicio.obtener_ventas()

        for venta in ventas:
            self.tabla_ventas.insert(
                "",
                "end",
                values=(
                    venta.usuario,
                    venta.producto,
                    venta.fecha
                )
            )