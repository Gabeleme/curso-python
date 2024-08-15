''' Crie um programa que leia nome e duas notas de varios alunos
e guarde tudo em uma lista composta. No final mostre um boletim
contendo a media de cada um e permita que o usuario possa
mostrar a nota de cada um dos alunos individualmente '''

# Lista para armazenar os dados dos alunos
alunos = []

# Loop para entrada dos dados dos alunos
while True:
    nome = input("Nome do aluno: ")
    nota1 = float(input(f"Nota 1 de {nome}: "))
    nota2 = float(input(f"Nota 2 de {nome}: "))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])
    
    continuar = input("Deseja adicionar outro aluno? (S/N): ").strip().upper()
    if continuar == 'N':
        break

# Exibir boletim com média dos alunos
print("\nBoletim:")
print(f"{'No.':<4} {'Nome':<10} {'Média':>8}")
print('-' * 26)
for i, aluno in enumerate(alunos):
    print(f"{i:<4} {aluno[0]:<10} {aluno[2]:>8.1f}")

# Permitir que o usuário visualize as notas de cada aluno individualmente
while True:
    opcao = int(input("\nMostrar notas de qual aluno? (999 para interromper): "))
    if opcao == 999:
        break
    if opcao < len(alunos):
        print(f"Notas de {alunos[opcao][0]} são {alunos[opcao][1]}")
    else:
        print("Aluno não encontrado.")
