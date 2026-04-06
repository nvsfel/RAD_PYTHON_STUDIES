import os

def criar_arquivo():
    
    conteudo = entry_conteudo.get()
    with open(nome, "w", encoding="utf-8") as f: f.write(conteudo)

    print("Arquivo criado com sucesso em:",os.path.abspath(nome))

def ler_arquivo():
    nome=input("Digite o nome do arquivo:")
    if os.path.exists(nome):
        with open(nome,"r", encoding="utf-8") as f:
            print("\nConteúdo do arquivo:\n")
            print(f.read())

    else:
        print("Arquivo não encontrado!")

def adicionar_conteudo():
    nome=input("Digite o nome do arquivo :")
    if os.path.exists(nome):
        novo = input("Digite o conteúdo a adicionar:")
        with open(nome, "a", encoding ="utf-8") as f:
            f.write("\n" + novo)
        print("Conteúdo adicionado!")

    else:
        print("Arquivo não encontrado!")

def excluir_arquivo():
    nome = input("Digite o nome do arquivo:")
    if os.path.exists(nome):
        os.remove(nome)
        print("Arquivo removido com sucesso!")
    else:
        print("Arquivo não encontrado!")

import tkinter as tk

def criar_arquivo_kamui():
    criar_kamui = tk.Toplevel()
    criar_kamui.title("Kamui: Criar Arquivo")
    tk.Label(criar_kamui, text="Digite o nome do arquivo(ex: teste.txt):").pack(pady=10)
    entry_conteudo = tk.Entry(criar_kamui)
    entry_conteudo.pack(pady=10)
    tk.Button(criar_kamui, text="Criar arquivo", command = criar_arquivo).pack(pady=10)

    
    
    

main_kamui = tk.Tk()
main_kamui.title("KAMUI")

tk.Label(main_kamui, text="GERENCIADOR DE ARQUIVOS").pack()

tk.Button(main_kamui, text="Criar arquivo", command = criar_arquivo_kamui).pack(pady=10)
tk.Button(main_kamui, text="Ler arquivo", command = ler_arquivo).pack(pady=10)
tk.Button(main_kamui, text="Adicionar conteúdo", command = adicionar_conteudo).pack(pady=10)
tk.Button(main_kamui, text="Excluir arquivo", command = excluir_arquivo).pack(pady=10)






"""def menu():
    while True:
        print("\n===GERENCIADOR DE ARQUIVOS---")
        print("1 - Criar arquivo")
        print("2 - Ler arquivo")
        print("3 - Adicionar conteúdo")
        print("4 - Excluir arquivo")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_arquivo()
        elif opcao == "2":
            ler_arquivo()
        elif opcao =="3":
            adicionar_conteudo()
        elif opcao =="4":
            excluir_arquivo()
        elif opcao =="0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida!")
menu()
"""
