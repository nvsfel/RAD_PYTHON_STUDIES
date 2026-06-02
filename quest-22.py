def calcular_vm(distancia, tempo):
    #nome nos parâmetros não interfere na variável. pode ser qualquer nome.
    try:
        velocidade_media = (distancia/1000)/(tempo/60)

        if velocidade_media < 8:
            status = "Lento!"
        elif 8 <= velocidade_media <12:
            status = "Moderado..."
        elif 12 <= velocidade_media <16:
            status = "Rápido!"
        else:
            status = "Elite."
            
        return velocidade_media, status #retornar ambos valores
        
    except ValueError:
        print("Insira valores válidos!")
        return 0.0, "Erro nos dados!"

atletas = {}

while True:

    chave = input("Digite qualquer tecla para iniciar, ou 'sair' para fechar.\n").strip()
    if chave.lower()=='sair':
        break
    
    
    raias = int(input("Quantos atletas serão avaliados?"))
    
    for corredores in range(raias):
        nome = input("Nome do atleta:\n").title()
        dist = float(input("Digite, em metros, a distância percorrida:\n"))
        tempo = float(input("Digite, em minutos, o tempo percorrido:\n"))
        
        vm_atleta, status = calcular_vm(dist, tempo)

        
        atletas[nome] = {
            "distancia" : dist,
            "tempo" : tempo,
            "velocidade" : vm_atleta,
            "status" : status
            }
    for nome, dados in atletas.items():
        print("|=======================|")
        print(f"Atleta:{nome}\nDistância Percorrida:{dados['distancia']:.2f}\nTempo:{dados['tempo']:.2f}\nRitmo:{dados['velocidade']:.2f}km/h\nStatus:{dados['status']}")
        print("|=======================|")   

    
    
