"""13) Desenvolva um programa em Python que cadastre alunos
utilizando um dicionário. O sistema deve permitir inserir
nome e nota de vários alunos, armazenando os dados no formato chave-valor.
Ao final, o programa deve exibir todos os alunos cadastrados
e calcular a média das notas. """




alunos = {}
global num_alunos
nota_turma = 0.0
global media
while True:
    nome = input("Digite o nome do aluno (ou 'sair' para encerrar):")
    nome=nome.title()
        
    if nome.lower() == 'sair':
        break
    if nome.lower() =='media':
        num_alunos=len(alunos)
        for nome, nota in alunos.items():
            nota_turma += nota
            
            
        media = nota_turma/num_alunos
        print(f"A turma tem {num_alunos} alunos e a média da turma é {media:.1f}.")
        break
    nota = float(input(f"Digite a nota de {nome}:"))
    alunos[nome] = nota

    print("Digite 'media' para acessar a média da turma")
    print("\n==Lista de alunos e notas==")

    for nome, nota in alunos.items():
        print(f"{nome}:{nota:.2f}")

        

        
