import tkinter as tk
from tkinter import messagebox

class Programador:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos

class EquipoMaraton:
    def __init__(self, nombre_equipo, universidad, lenguaje):
        self.nombre_equipo = nombre_equipo
        self.universidad = universidad
        self.lenguaje = lenguaje
        self.programadores = []

    def esta_lleno(self):
        return len(self.programadores) >= 3

    def añadir(self, programador):
        if self.esta_lleno():
            raise Exception("El equipo está completo. No se pudo agregar otro programador.")
        self.programadores.append(programador)

    @staticmethod
    def validar_campo(texto):
        if any(char.isdigit() for char in texto):
            raise Exception("El nombre o apellido no puede tener dígitos.")
        if len(texto) > 20:
            raise Exception("El texto no debe tener más de 20 caracteres.")

# Funciones para la interfaz
def agregar_integrante():
    try:
        nombre = entrada_nombre.get().strip()
        apellidos = entrada_apellidos.get().strip()
        EquipoMaraton.validar_campo(nombre)
        EquipoMaraton.validar_campo(apellidos)
        programador = Programador(nombre, apellidos)
        equipo.añadir(programador)
        lista_integrantes.insert(tk.END, f"{nombre} {apellidos}")
        entrada_nombre.delete(0, tk.END)
        entrada_apellidos.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def crear_equipo():
    global equipo
    nombre_eq = entrada_equipo.get().strip()
    universidad = entrada_universidad.get().strip()
    lenguaje = entrada_lenguaje.get().strip()
    if not nombre_eq or not universidad or not lenguaje:
        messagebox.showerror("Error", "Todos los campos del equipo son obligatorios.")
        return
    equipo = EquipoMaraton(nombre_eq, universidad, lenguaje)
    entrada_equipo.config(state='disabled')
    entrada_universidad.config(state='disabled')
    entrada_lenguaje.config(state='disabled')
    btn_crear.config(state='disabled')
    messagebox.showinfo("Éxito", "Equipo creado. Ahora ingresa los integrantes.")

# Interfaz Tkinter
ventana = tk.Tk()
ventana.title("Registro Equipo Maratón")
ventana.geometry("460x420")

# Datos del equipo
tk.Label(ventana, text="Nombre del equipo:").grid(row=0, column=0, padx=10, pady=5, sticky='e')
entrada_equipo = tk.Entry(ventana, width=30)
entrada_equipo.grid(row=0, column=1)

tk.Label(ventana, text="Universidad:").grid(row=1, column=0, padx=10, pady=5, sticky='e')
entrada_universidad = tk.Entry(ventana, width=30)
entrada_universidad.grid(row=1, column=1)

tk.Label(ventana, text="Lenguaje de programación:").grid(row=2, column=0, padx=10, pady=5, sticky='e')
entrada_lenguaje = tk.Entry(ventana, width=30)
entrada_lenguaje.grid(row=2, column=1)

btn_crear = tk.Button(ventana, text="Crear Equipo", command=crear_equipo, bg='green', fg='white')
btn_crear.grid(row=3, column=1, pady=10)

# Datos de integrantes
tk.Label(ventana, text="Nombre del integrante:").grid(row=4, column=0, padx=10, pady=5, sticky='e')
entrada_nombre = tk.Entry(ventana, width=30)
entrada_nombre.grid(row=4, column=1)

tk.Label(ventana, text="Apellidos del integrante:").grid(row=5, column=0, padx=10, pady=5, sticky='e')
entrada_apellidos = tk.Entry(ventana, width=30)
entrada_apellidos.grid(row=5, column=1)

btn_agregar = tk.Button(ventana, text="Agregar Integrante", command=agregar_integrante, bg='blue', fg='white')
btn_agregar.grid(row=6, column=1, pady=10)

# Lista de integrantes
tk.Label(ventana, text="Integrantes:").grid(row=7, column=0, padx=10, sticky='ne')
lista_integrantes = tk.Listbox(ventana, width=35, height=6)
lista_integrantes.grid(row=7, column=1, pady=10)

ventana.mainloop()
