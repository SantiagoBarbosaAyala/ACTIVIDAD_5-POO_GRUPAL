import tkinter as tk

class Vendedor:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = 0  
    def imprimir(self):
        return (f"Nombre: {self.nombre}\n"
                f"Apellido: {self.apellidos}\n"
                f"Edad: {self.edad}")
    def verificar_edad(self, edad):
        if edad >= 0 and edad < 18:
            raise ValueError("El vendedor debe ser mayor de 18 años.")
        elif edad >= 18 and edad < 120:
            self.edad = edad
        else:
            raise ValueError("La edad no puede ser negativa ni mayor a 120.")

class VendedorApp:
    def __init__(self, master):
        self.master = master
        master.title("Registro de Vendedor")
        master.geometry("400x350") 

        self.label_nombre = tk.Label(master, text="Nombre")
        self.label_nombre.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.entry_nombre = tk.Entry(master, width=30)
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        self.label_apellido = tk.Label(master, text="Apellido")
        self.label_apellido.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry_apellido = tk.Entry(master, width=30)
        self.entry_apellido.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        self.label_edad = tk.Label(master, text="Edad      ")
        self.label_edad.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.entry_edad = tk.Entry(master, width=30)
        self.entry_edad.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        self.boton_mostrar = tk.Button(master, text="Mostrar", command=self.mostrar_datos,
                                       bg="lightblue", fg="black", width=10, height=2)
        self.boton_mostrar.grid(row=3, column=0, padx=10, pady=20, sticky="e")

        self.boton_borrar = tk.Button(master, text="Borrar", command=self.borrar_datos,
                                      bg="lightgray", fg="black", width=10, height=2)
        self.boton_borrar.grid(row=3, column=1, padx=10, pady=20, sticky="w")

        self.label_output = tk.Label(master, text="", justify=tk.LEFT, anchor="w", wraplength=400)
        self.label_output.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="nw")

    def mostrar_datos(self):
        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        edad_ini = self.entry_edad.get()

        self.label_output.config(text="") 
        try:
            edad = int(edad_ini) 
            vendedor = Vendedor(nombre, apellido)
            vendedor.verificar_edad(edad) 
            self.label_output.config(text=vendedor.imprimir())
        except ValueError as e:
            self.label_output.config(text=f"Error: {e}", fg="darkred")

    def borrar_datos(self):
        self.entry_nombre.delete(0, tk.END)
        self.entry_apellido.delete(0, tk.END)
        self.entry_edad.delete(0, tk.END)
        self.label_output.config(text="", fg="black") 

if __name__ == "__main__":
    root = tk.Tk()
    app = VendedorApp(root)
    root.mainloop()