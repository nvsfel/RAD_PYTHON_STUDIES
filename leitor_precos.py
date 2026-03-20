import tkinter as tk
from tkinter import messagebox
def calcular_desconto():
    try:
        preco_original = float(entry_preco.get())
        if preco_original <0:
            preco_original=preco_original*-1
            #VERIFICAÇÃO PARA EVITAR ENTRADA NEGATIVA
        desconto = float(entry_desconto.get())
        if desconto <0:
            desconto=desconto*-1
            #VERIFICAÇÃO PARA EVITAR ENTRADA NEGATIVA
        
        desc = ((preco_original * desconto)/100)
        novo_preco = preco_original - desc

        if desconto <= 20:
            promo = "Promoção comum"
        elif 20 < desconto <= 49:
            promo = "Boa promoção!"
        else:
            promo = "SUPER PROMOÇÃO!!!"
        
        messagebox.showinfo("LEITOR",f"Novo preço é: ${novo_preco:.2f}:\n\n{promo}")

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




