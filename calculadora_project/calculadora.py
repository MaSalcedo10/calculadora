import tkinter as tk
from tkinter import messagebox


class Operaciones:

    @staticmethod
    def suma(a, b):
        return a + b

    @staticmethod
    def resta(a, b):
        return a - b

    @staticmethod
    def multiplicacion(a, b):
        return a * b

    @staticmethod
    def division(a, b):
        try:
            return a / b
        except ZeroDivisionError:
            messagebox.showerror("Error", "No se puede dividir entre cero.")
            return None


def calcular(operacion):
    try:
        a = float(entry1.get())
        b = float(entry2.get())
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese números válidos.")
        return

    if operacion == "suma":
        resultado = Operaciones.suma(a, b)
    elif operacion == "resta":
        resultado = Operaciones.resta(a, b)
    elif operacion == "multiplicacion":
        resultado = Operaciones.multiplicacion(a, b)
    elif operacion == "division":
        resultado = Operaciones.division(a, b)

    if resultado is not None:
        resultado_label.config(text=f"Resultado: {resultado}")

# Crear ventana principal


ventana = tk.Tk()
ventana.title("Calculadora con Tkinter")
ventana.geometry("300x300")
ventana.resizable(False, False)

# Entradas
tk.Label(ventana, text="Primer número:").pack()
entry1 = tk.Entry(ventana)
entry1.pack()

tk.Label(ventana, text="Segundo número:").pack()
entry2 = tk.Entry(ventana)
entry2.pack()

# Botones de operación
tk.Button(ventana, text="Sumar",
          command=lambda: calcular("suma")).pack(pady=5)
tk.Button(ventana, text="Restar",
          command=lambda: calcular("resta")).pack(pady=5)
tk.Button(ventana, text="Multiplicar",
          command=lambda: calcular("multiplicacion")).pack(pady=5)
tk.Button(ventana, text="Dividir",
          command=lambda: calcular("division")).pack(pady=5)

# Resultado
resultado_label = tk.Label(ventana, text="Resultado: ")
resultado_label.pack(pady=10)

# Ejecutar
ventana.mainloop()
