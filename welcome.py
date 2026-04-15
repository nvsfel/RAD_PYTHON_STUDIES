
import tkinter as tk
from tkinter import messagebox


def boa_vinda(event=None):
    nome=nome_welcome.get()
    if nome == "":
        messagebox.showwarning("Aviso","Sem nome, não dá...")
        return
    messagebox.showinfo("Opa", f"Bem vindo, {nome.title()}!")


welcome = tk.Tk()
welcome.geometry("230x200")
welcome.title("Welcome!")
welcome.bind("<Return>", boa_vinda)
welcome.bind("<KP_Enter>", boa_vinda)

tk.Label(welcome, text="Qual o seu nome?").pack(pady=20)
nome_welcome = tk.Entry(welcome, justify="center")
nome_welcome.pack(pady=10)

tk.Button(welcome, text="Boas vindas", command = boa_vinda).pack(pady=10)
