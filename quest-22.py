def calcular_vm():
    try:
        velocidade_media = (dist/100)/(tempo/60)

        if velocidade_media < 8:
            status = "Lento!"
        elif velocidade_media >8 <= velocidade_media <12:
            status = "Moderado..."
        elif velocidade_media >12<= velocidade_media <16:
            status = "Rápido!"
        else:
            status = "Elite."
    except ValueError:
        print("Insira valores válidos!")
        return

atletas = {}

while True:

    chave = input("Digite qualquer tecla para iniciar, ou 'sair' para fechar.\n").strip()
    if chave.lower=='sair':
        break
    
    
    raias = int(input("Quantos atletas serão avaliados?"))
    
    for corredores in range(raias):
        nome = input("Nome do atleta:")
        dist = input("Digite, em metros, a distância percorrida")
        atletas[nome] = dist
        tempo = input("Digite, em minutos, o tempo percorrido")
        atletas[nome] = tempo

    print(atletas)
    
