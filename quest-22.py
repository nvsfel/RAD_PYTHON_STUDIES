def calcular_vm(distancia, tempo):
    #nome nos parâmetros não interfere na variável. pode ser qualquer nome.
    try:
        velocidade_media = (distancia/100)/(tempo/60)

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
        return

atletas = {}

while True:

    chave = input("Digite qualquer tecla para iniciar, ou 'sair' para fechar.\n").strip()
    if chave.lower=='sair':
        break
    
    
    raias = int(input("Quantos atletas serão avaliados?"))
    
    for corredores in range(raias):
        nome = input("Nome do atleta:").title()
        dist = float(input("Digite, em metros, a distância percorrida"))
        tempo = float(input("Digite, em minutos, o tempo percorrido"))
        
        vm_atleta, status = calcular_vm(dist, tempo)
        
        atletas[nome] = {
            "distancia" : dist,
            "tempo" : tempo,
            "velocidade" : vm_atleta,
            "status" : status
            }

   

    print(atletas)
    
