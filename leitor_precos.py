import tkinter as tk
from tkinter import messagebox
def calcular_desconto():
    try:
        preco_original = float(entry_preco.get())
        desconto = float(entry_desconto.get())
        desc = ((preco_original * desconto)/100)
        novo_preco = preco_original - desc

        if desc <= 20:
            promo = "Promoção comum"
        elif 20 < desc <= 49:
            promo = "Boa promoção!"
        else:
            promo = "SUPER PROMOÇÃO!!!"
        
        messagebox.showinfo("Resultado",f"Novo preço é: ${novo_preco:.2f}:\n\n{promo}")

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos.")

janela = tk.Tk()
janela.title("LEITOR DE PREÇOS")
#nome
label_nome = tk.Label(janela, text="NOME:")
label_nome.grid(row = 0, column=0, padx=10, pady=10)
entry_nome = tk.Entry(janela)
entry_nome.grid(row = 0, column=1, padx=10, pady=10)
#preco
label_preco = tk.Label(janela, text="PREÇO ($) :")
label_preco.grid(row = 1, column=0, padx=10, pady=10)
entry_preco = tk.Entry(janela)
entry_preco.grid(row = 1, column=1, padx=10, pady=10)
#desconto
label_desconto = tk.Label(janela, text="DESCONTO (%):")
label_desconto.grid(row = 2, column=0, padx=10, pady=10)
entry_desconto = tk.Entry(janela)
entry_desconto.grid(row = 2, column=1, padx=10, pady=10)
#botao
botao_calcular = tk.Button(janela, text="CALCULAR NOVO PREÇO", command=calcular_desconto)
botao_calcular.grid(row = 3, column=0, columnspan=2, pady = 20)
janela.mainloop()


#com base no código acima, de forma estruturada, simule um programa com TKINTER com as seguintes funcionalidades:
#1 - um campo para digitar o nome de um produto
#2 - um campo para digitar o preço original
#3 - um campo para digitar o percentual do desconto;
#4 - ao clicar em 'CALCULAR DESCONTO', abrir uma caixa de mensagem exibindo o nome do produto e o preço
#e uma mensagem mostrando se o desconto for até 20: "promocao comum", entre 21 e 49 "boa promoção", acima de 50 "super promocao!";



