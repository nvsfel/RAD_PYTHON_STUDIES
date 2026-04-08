"""13) Desenvolva um programa em Python que cadastre alunos
utilizando um dicionário. O sistema deve permitir inserir
nome e nota de vários alunos, armazenando os dados no formato chave-valor.
Ao final, o programa deve exibir todos os alunos cadastrados
e calcular a média das notas. """



alunos = {}

while True:
    nome = input("Digite o nome do aluno (ou 'sair' para encerrar):")
    nome=nome.title()
    global num_alunos
    global media
    if nome.lower() == 'sair':
        break
    if nome.lower() =='media':
        for nome in alunos.items():
            num_alunos+=1
            media = alunos[nota]/num_alunos
        print(f"A turma tem {n_alunos} e a média é {alunos[notas]}.")
        break
    nota = float(input(f"Digite a nota de {nome}:"))
    alunos[nome] = nota

    print("Digite 'media' para acessar a média da turma")
    print("\n==Lista de alunos e notas==")

    for nome, nota in alunos.items():
        print(f"{nome}:{nota:.1f}")

        
