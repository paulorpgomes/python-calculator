import math
from tkinter import messagebox
from tkinter import *

def calcular():
    operacao = operacao_var.get()
    num1_str = num1_entry.get().strip()
    num2_str = num2_entry.get().strip()

    if num1_str == '':
        messagebox.showerror("Erro", "O campo de número 1 está vazio!")
        return

    if not num1_str.isdigit():
        messagebox.showerror("Erro", "O campo de número 1 contém caracteres inválidos!")
        return

    num1 = float(num1_str)

    if operacao != "Raiz" and num2_str == '':
        messagebox.showerror("Erro", "O campo de número 2 está vazio!")
        return

    if num2_str != '':
        if not num2_str.isdigit():
            messagebox.showerror("Erro", "O campo de número 2 contém caracteres inválidos!")
            return
        num2 = float(num2_str)

    if operacao == "Soma":
        resultado = num1 + num2
    elif operacao == "Subtração":
        resultado = num1 - num2
    elif operacao == "Multiplicação":
        resultado = num1 * num2
    elif operacao == "Exponenciação":
        resultado = num1 ** num2
    elif operacao == "Raiz":
        resultado = math.sqrt(num1)
    elif operacao == "Divisão":
        if num2 == 0:
            messagebox.showerror("Erro", "Divisão por zero não é permitida!")
            return
        resultado = num1 / num2
    else:
        messagebox.showerror("Erro", "Operação inválida!")
        return

    resultado_label.config(text="Resultado: " + str(resultado))

def encerrar():
    window.destroy()

def atualizar_cores():
    cor_fundo = "#26242f" if switch_value else "white"
    cor_texto = "white" if switch_value else "black"

    window.config(bg=cor_fundo)

    for widget in window.winfo_children():
        if isinstance(widget, (Button, Label, Entry, OptionMenu)):
            widget.config(bg=cor_fundo, fg=cor_texto)

# Declaracao da Interface e seu tamanho
window = Tk()
window.title("Calculadora")
window.geometry("300x270")
window.config(bg="white")

light=PhotoImage(file="light.png")
light = light.subsample(3, 3)
dark=PhotoImage(file="dark.png")
dark = dark.subsample(3, 3)
switch_value = True

def toggle():
    global switch_value
    if switch_value:
        switch.config(image=dark, bg="#26242f",
                      activebackground="#26242f")
    else:
        switch.config(image=light, bg="white",
                      activebackground="white")

    switch_value = not switch_value
    atualizar_cores()

switch = Button(window, image=light,
                bd=0, bg="white",
                activebackground="white",
                command=toggle)
switch.pack(padx=0, pady=0)

texto_orientacao = Label(window, text="Bem-vindo à calculadora!", bg="white")  # Definir cor de fundo como branco
texto_orientacao.pack(anchor="n")  # Centralizar texto no topo

operacao_var = StringVar()
num1_var = StringVar()
num2_var = StringVar()

num1_label = Label(window, text="Número 1:", bg="white")  # Definir cor de fundo como branco
num1_label.pack()
num1_entry = Entry(window, textvariable=num1_var)
num1_entry.pack()

num2_label = Label(window, text="Número 2:", bg="white")  # Definir cor de fundo como branco
num2_label.pack()
num2_entry = Entry(window, textvariable=num2_var)
num2_entry.pack()

operacao_label = Label(window, text="Escolha a Operação abaixo:", bg="white")  # Definir cor de fundo como branco
operacao_label.pack()
operacao_optionmenu = OptionMenu(window, operacao_var, "Soma", "Subtração", "Multiplicação", "Divisão", "Exponenciação", "Raiz")
operacao_optionmenu.config(bg="white")  # Definir cor de fundo do OptionMenu como branco
operacao_optionmenu.pack()

calcular_button = Button(window, text="Calcular", command=calcular, bg="white")  # Definir cor de fundo como branco
calcular_button.pack()

resultado_label = Label(window, text="", bg="white")  # Definir cor de fundo como branco
resultado_label.pack()

encerrar_button = Button(window, text="Encerrar", command=encerrar, bg="white")  # Definir cor de fundo como branco
encerrar_button.pack()


atualizar_cores()
window.mainloop()
