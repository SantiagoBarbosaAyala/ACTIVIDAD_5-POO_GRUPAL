import tkinter as tk

label_error = None 
def calcular_division():
   
    if label_error: 
        label_error.config(text="", fg="black")
    try:
        numerador = float(entry_numerador.get())
        denominador = float(entry_denominador.get())

        if denominador == 0:
            entry_resultado.config(state="normal")
            entry_resultado.delete(0, tk.END)
            entry_resultado.insert(0, "Infinity")
            entry_resultado.config(state="readonly")
            if label_error:
                label_error.config(text="Error: No se puede dividir entre cero.", fg="red")
            
        else:
            resultado = numerador / denominador
            entry_resultado.config(state="normal")
            entry_resultado.delete(0, tk.END)
            entry_resultado.insert(0, str(resultado))
            entry_resultado.config(state="readonly")

    except ValueError:
        if label_error:
            label_error.config(text="Error de entrada: Ingrese números válidos en ambos campos.", fg="red")
        entry_resultado.config(state="normal")
        entry_resultado.delete(0, tk.END)
        entry_resultado.config(state="readonly")
    except Exception as e:
        if label_error:
            label_error.config(text=f"Ocurrió un error inesperado: {e}", fg="red")
        entry_resultado.config(state="normal")
        entry_resultado.delete(0, tk.END)
        entry_resultado.config(state="readonly")

def borrar_campos():
    entry_resultado.config(state="normal")
    entry_numerador.delete(0, tk.END)
    entry_denominador.delete(0, tk.END)
    entry_resultado.delete(0, tk.END)
    entry_resultado.config(state="readonly")
    if label_error:
        label_error.config(text="", fg="black")
#Ventana
ventana = tk.Tk()
ventana.title("Calculadora de división")
ventana.geometry("400x250")

label_numerador = tk.Label(ventana, text="Numerador")
label_numerador.grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_numerador = tk.Entry(ventana, width=30)
entry_numerador.grid(row=0, column=1, padx=10, pady=10)

label_denominador = tk.Label(ventana, text="Denominador")
label_denominador.grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_denominador = tk.Entry(ventana, width=30)
entry_denominador.grid(row=1, column=1, padx=10, pady=10)

label_resultado = tk.Label(ventana, text="Resultado")
label_resultado.grid(row=2, column=0, padx=10, pady=10, sticky="w")
entry_resultado = tk.Entry(ventana, width=30, state="readonly")
entry_resultado.grid(row=2, column=1, padx=10, pady=10)

# botones
boton_calcular = tk.Button(ventana, text="Calcular", command=calcular_division,
                            bg="green", fg="white", width=8, height=2)
boton_calcular.grid(row=3, column=0, padx=10, pady=20, sticky="e")

boton_borrar = tk.Button(ventana, text="Borrar", command=borrar_campos,
                         bg="red", fg="white", width=8, height=2)
boton_borrar.grid(row=3, column=1, padx=10, pady=20, sticky="w")


label_error = tk.Label(ventana, text="", fg="red")
label_error.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="w")


ventana.mainloop()