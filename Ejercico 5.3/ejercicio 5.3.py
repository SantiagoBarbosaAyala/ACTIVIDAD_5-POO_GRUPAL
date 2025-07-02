import tkinter as tk
from tkinter import messagebox
import math

def calcular():
    try:
        valor = float(entrada_valor.get())
        resultado_log = ""
        resultado_raiz = ""

        if valor <= 0:
            raise ArithmeticError

        resultado_log = f"{math.log(valor):.4f}"
        resultado_raiz = f"{math.sqrt(valor):.4f}"

        salida_logaritmo.config(state='normal')
        salida_raiz.config(state='normal')

        salida_logaritmo.delete(0, tk.END)
        salida_logaritmo.insert(0, resultado_log)

        salida_raiz.delete(0, tk.END)
        salida_raiz.insert(0, resultado_raiz)

        salida_logaritmo.config(state='readonly')
        salida_raiz.config(state='readonly')

    except ValueError:
        messagebox.showerror("Error", "El valor debe ser numérico.")
    except ArithmeticError:
        messagebox.showerror("Error", "El valor debe ser un número positivo.")

def borrar():
    entrada_valor.delete(0, tk.END)
    salida_logaritmo.config(state='normal')
    salida_raiz.config(state='normal')
    salida_logaritmo.delete(0, tk.END)
    salida_raiz.delete(0, tk.END)
    salida_logaritmo.config(state='readonly')
    salida_raiz.config(state='readonly')

# Ventana principal
ventana = tk.Tk()
ventana.title("cálculos Numéricos")
ventana.geometry("380x200")

# Etiquetas y campos
tk.Label(ventana, text="Valor numérico:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entrada_valor = tk.Entry(ventana, width=25)
entrada_valor.grid(row=0, column=1, padx=10, pady=5)

tk.Label(ventana, text="Logaritmo neperiano:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
salida_logaritmo = tk.Entry(ventana, width=25, state='readonly')
salida_logaritmo.grid(row=1, column=1, padx=10, pady=5)

tk.Label(ventana, text="Raíz cuadrada:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
salida_raiz = tk.Entry(ventana, width=25, state='readonly')
salida_raiz.grid(row=2, column=1, padx=10, pady=5)

# Botones
btn_calcular = tk.Button(ventana, text="Calcular", command=calcular, bg='green', fg='white', width=10)
btn_calcular.grid(row=3, column=0, pady=15)

btn_borrar = tk.Button(ventana, text="Borrar", command=borrar, bg='red', fg='white', width=10)
btn_borrar.grid(row=3, column=1, pady=15)

ventana.mainloop()
