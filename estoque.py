estoque = {}

def adicionar_produto():
    produto = input("Nome do produto:").strip().title()
    quantidade = int(input("Quantidade inicial: "))
    estoque[produto] = quantidade
    print(f"{produto} adicionado com {quantidade} unidades.")


def ver_estoque():
    print("\nEstoque atual: ")
    if not estoque:
        print("Estoque vazio.")
    else:
        for produto, quantidade in estoque.items():
            print(f"{produto}: {quantidade} unidades")

def atualizar_quantidade():
    produto = input("Produto a atualizar:").strip().title()
    if produto in estoque:
        nova_qtd = int(input("Nova quantidade:"))
        estoque[produto] = nova_qtd
        print(f"Estoque de {produto} atualizado para {nova_qtd}.")
    else:
        print("Produto não encontrado.")


def verificar_disponibilidade():
    produto = input("produto a verificar: ").strip().title()
    if produto in estoque:
        if estoque[produto]>0:
            print(f"{produto} está disponível({estoque[produto]} unidades).")
        else:
            print(f"{produto} está esgotado.")
    else:
        print("Produto não encontrado.")

def menu():
    while True:
        print("\n===MENU===")
        print("1 - Adicionar produto")
        print("2 - Ver estoque")
        print("3 - Atualizar quantidade")
        print("4 - Verificar disponibiidade")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_produto()
        elif opcao =='2':
            ver_estoque()
        elif opcao =='3':
            atualizar_quantidade()
        elif opcao == '4':
            verificar_disponibilidade()
        elif opcao == '5':
            print("Encerrando o programa...")
            break
        else:
            print("Opcao inválida! Tente novamente.")

menu()

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

#estrutura da janela

prog = tk.Tk()
prog.title("ESTOQUE")
#proporções
prog.geometry("500X700+700+180")
prog.maxsize(600,1050)
prog.minsize(250,350)

prog.config(bg='#180000')
#prog.iconbitmap('//caminhoimg.ico')

titulo = ttk.Label(
    prog,
    text=" ESTOQUE ",
    font=("Arial", 15),
    foreground='white',
    background='#7d000',
    anchor="center",
    justify="center",
    borderwidth=3,
    relief="groove"
)
titulo.pack(ipadx=60,ipady=40)

prog.mainloop()


            































    

