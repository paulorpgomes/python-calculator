import tkinter as tk
from tkinter import messagebox

def calcular():
    operacao = operacao_var.get()
    num1 = float(num1_entry.get())
    num2 = float(num2_entry.get())

    if operacao == "Soma":
        resultado = num1 + num2
    elif operacao == "Subtração":
        resultado = num1 - num2
    elif operacao == "Multiplicação":
        resultado = num1 * num2
    elif operacao == "Divisão":
        if num2 == 0:
            messagebox.showerror("Erro", "Divisão por zero não é permitida!")
            return
        resultado = num1 / num2
    elif operacao == "Exponenciação":
        resultado = num1 ** num2
    elif operacao == "Raiz":
        resultado = num1 ** (1/num2)
    else:
        messagebox.showerror("Erro", "Operação inválida!")
        return

    resultado_label.config(text="Resultado: " + str(resultado))

def encerrar():
    window.destroy()

def modo_escuro():
    window.config(bg="black")
    num1_label.config(fg="white", bg="black")
    num2_label.config(fg="white", bg="black")
    operacao_label.config(fg="white", bg="black")
    calcular_button.config(fg="white", bg="black", activebackground="black")
    resultado_label.config(fg="white", bg="black")
    encerrar_button.config(fg="white", bg="black", activebackground="black")
    
window = tk.Tk()
window.title("Calculadora")
window.geometry("300x250")

operacao_var = tk.StringVar()
num1_var = tk.StringVar()
num2_var = tk.StringVar()

num1_label = tk.Label(window, text="Número 1:")
num1_label.pack()
num1_entry = tk.Entry(window, textvariable=num1_var)
num1_entry.pack()

num2_label = tk.Label(window, text="Número 2:")
num2_label.pack()
num2_entry = tk.Entry(window, textvariable=num2_var)
num2_entry.pack()

operacao_label = tk.Label(window, text="Operação:")
operacao_label.pack()
operacao_optionmenu = tk.OptionMenu(window, operacao_var, "Soma", "Subtração", "Multiplicação", "Divisão", "Exponenciação", "Raiz")
operacao_optionmenu.pack()

calcular_button = tk.Button(window, text="Calcular", command=calcular)
calcular_button.pack()

resultado_label = tk.Label(window, text="")
resultado_label.pack()

encerrar_button = tk.Button(window, text="Encerrar", command=encerrar)
encerrar_button.pack()

modo_escuro_button = tk.Button(window, text="Modo Escuro", command=modo_escuro)
modo_escuro_button.pack()

window.mainloop()
