import tkinter as tk
from tkinter import filedialog, messagebox
import os

class LectorArchivos:
    def __init__(self, master):
        self.master = master
        master.title("Ejercicio 5.5")
        master.geometry("450x300") 
        master.resizable(False, False) 

        self.archivo_seleccionado_ruta = ""
        self.top_frame = tk.Frame(master)
        self.top_frame.pack(pady=10)

        self.pasos_label = tk.Label(self.top_frame, text="Busque el archivo y luego seleccione Leer archivo")
        self.pasos_label.pack()

        self.ruta_label = tk.Label(self.top_frame, text="Ningún archivo seleccionado", font=('Arial', 10), wraplength=450)
        self.ruta_label.pack(pady=5)

        self.seleccionar_btn = tk.Button(master, text="Seleccionar Archivo", command=self.seleccionar_archivo)
        self.seleccionar_btn.pack(pady=5)

        self.leer_btn = tk.Button(master, text="Leer Archivo", command=self.leer_archivo)
        self.leer_btn.pack(pady=5)

        self.estado_label = tk.Label(master, text="", fg="blue")
        self.estado_label.pack(pady=10)

        self.contenido_texto = tk.Text(master, height=5, width=50, state='disabled')
        self.contenido_texto.pack(pady=10)

    def seleccionar_archivo(self):
        ruta_archivo = filedialog.askopenfilename(
            title="Selecciona un archivo de texto",
            filetypes=[("Archivos de Texto", "*.txt"), ("Todos los Archivos", "*.*")])
        if ruta_archivo:
            self.archivo_seleccionado_ruta = ruta_archivo
            self.ruta_label.config(text=self.archivo_seleccionado_ruta)
            self.estado_label.config(text="Archivo listo para leer.")
            self.contenido_texto.config(state='normal')
            self.contenido_texto.delete(1.0, tk.END)
            self.contenido_texto.config(state='disabled')
        else:
            self.archivo_seleccionado_ruta = ""
            self.ruta_label.config(text="Ningún archivo seleccionado")
            messagebox.showwarning("Advertencia", "No se seleccionó ningún archivo")
            self.estado_label.config(text="")
            self.contenido_texto.config(state='normal')
            self.contenido_texto.delete(1.0, tk.END)
            self.contenido_texto.config(state='disabled')

    def leer_archivo(self):
        if not self.archivo_seleccionado_ruta:
            messagebox.showwarning("Advertencia", "Por favor, primero seleccione un archivo.")
            self.estado_label.config(text="No se ha seleccionado ningún archivo para leer.")
            return
        nombre_archivo = self.archivo_seleccionado_ruta
        contenido_leido = "" 
        try:
            with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
                contenido_leido = archivo.read()
                self.contenido_texto.config(state='normal')
                self.contenido_texto.delete(1.0, tk.END) 
                self.contenido_texto.insert(tk.END, contenido_leido) 
                self.contenido_texto.config(state='disabled') 
                self.estado_label.config(text="Se confirma que se leyó el archivo.", fg="green")
        except FileNotFoundError:
            self.estado_label.config(text="¡ERROR! No se pudo leer el archivo.", fg="red")
            messagebox.showerror("Error al Leer Archivo",
                                 f"¡ERROR! El archivo '{os.path.basename(nombre_archivo)}' no pudo ser encontrado.\n\n"
                                 "Mensaje de tu código: No se pudo leer el archivo.\n"
                                 "Por favor, verifica que el archivo exista en la ruta especificada.")
            self.contenido_texto.config(state='normal')
            self.contenido_texto.delete(1.0, tk.END)
            self.contenido_texto.insert(tk.END, "No se pudo leer el archivo.") 
            self.contenido_texto.config(state='disabled')
        except IOError as e:
            self.estado_label.config(text="¡ERROR! Problema de E/S al leer el archivo.", fg="red")
            messagebox.showerror("Error de E/S",
                                 f"Ocurrió un error de entrada/salida al leer el archivo '{os.path.basename(nombre_archivo)}':\n\n"
                                 f"Detalles del sistema: {e}\n\n"
                                 "Mensaje de tu código: No se pudo leer el archivo.")
            self.contenido_texto.config(state='normal')
            self.contenido_texto.delete(1.0, tk.END)
            self.contenido_texto.insert(tk.END, "No se pudo leer el archivo (Error de E/S).")
            self.contenido_texto.config(state='disabled')
        except Exception as e:
            self.estado_label.config(text="¡ERROR! Ocurrió un error inesperado.", fg="red")
            messagebox.showerror("Error Inesperado",
                                 f"Ocurrió un error inesperado al intentar leer el archivo:\n\n"
                                 f"Detalles: {type(e).__name__}: {e}\n\n"
                                 "Mensaje de tu código: No se pudo leer el archivo (Error inesperado).")
            self.contenido_texto.config(state='normal')
            self.contenido_texto.delete(1.0, tk.END)
            self.contenido_texto.insert(tk.END, "No se pudo leer el archivo (Error inesperado).")
            self.contenido_texto.config(state='disabled')

root = tk.Tk()
app = LectorArchivos(root)
root.mainloop()
