import tkinter as tk
from tkinter import ttk, messagebox
from modelos.visitante import Visitante

class AppTkinter:
    def __init__(self, root, servicio):
        self.root = root
        self.servicio = servicio
        self.root.title("Registro de Visitantes")

        # ===== FORMULARIO =====
        tk.Label(root, text="Cédula").grid(row=0, column=0)
        self.entry_cedula = tk.Entry(root)
        self.entry_cedula.grid(row=0, column=1)

        tk.Label(root, text="Nombre").grid(row=1, column=0)
        self.entry_nombre = tk.Entry(root)
        self.entry_nombre.grid(row=1, column=1)

        tk.Label(root, text="Motivo").grid(row=2, column=0)
        self.entry_motivo = tk.Entry(root)
        self.entry_motivo.grid(row=2, column=1)

        # ===== BOTONES =====
        tk.Button(root, text="Registrar", command=self.registrar).grid(row=3, column=0)
        tk.Button(root, text="Eliminar", command=self.eliminar).grid(row=3, column=1)
        tk.Button(root, text="Limpiar", command=self.limpiar).grid(row=3, column=2)

        # ===== TABLA =====
        self.tree = ttk.Treeview(root, columns=("cedula", "nombre", "motivo"), show="headings")
        self.tree.heading("cedula", text="Cédula")
        self.tree.heading("nombre", text="Nombre")
        self.tree.heading("motivo", text="Motivo")
        self.tree.grid(row=4, column=0, columnspan=3)

        self.actualizar_tabla()

    def registrar(self):
        cedula = self.entry_cedula.get()
        nombre = self.entry_nombre.get()
        motivo = self.entry_motivo.get()

        if not cedula or not nombre or not motivo:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        visitante = Visitante(cedula, nombre, motivo)

        if self.servicio.registrar(visitante):
            messagebox.showinfo("Éxito", "Visitante registrado")
            self.actualizar_tabla()
            self.limpiar()
        else:
            messagebox.showerror("Error", "La cédula ya existe")

    def eliminar(self):
        seleccionado = self.tree.selection()

        if not seleccionado:
            messagebox.showerror("Error", "Seleccione un registro")
            return

        # Confirmación (extra para el 10)
        confirmar = messagebox.askyesno("Confirmar", "¿Eliminar registro?")
        if not confirmar:
            return

        item_id = seleccionado[0]
        valores = self.tree.item(item_id, "values")
        cedula = valores[0]

        if self.servicio.eliminar(cedula):
            messagebox.showinfo("Éxito", "Eliminado correctamente")
            self.actualizar_tabla()
        else:
            messagebox.showerror("Error", "No se pudo eliminar")

    def limpiar(self):
        self.entry_cedula.delete(0, tk.END)
        self.entry_nombre.delete(0, tk.END)
        self.entry_motivo.delete(0, tk.END)

    def actualizar_tabla(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        for v in self.servicio.obtener_todos():
            self.tree.insert("", tk.END, values=(v.cedula, v.nombre, v.motivo))